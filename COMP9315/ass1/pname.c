/*
 * src/tutorial/pname.c
 *
 ******************************************************************************
  Writen By: 	Jinghan Wang
       Date:	02/03/2024
        ZID:	z5286124
    Subject:    COMP9315, Database Systems Implementation
    Project:    Assignment 1
******************************************************************************/

#include "postgres.h"

#include "fmgr.h"
#include "regex.h"
#include "access/hash.h"

PG_MODULE_MAGIC;

/*****************************************************************************
 * Type PersonName
 *
 * Use a flexible array member to store the unknown length of the name
 *****************************************************************************/

typedef struct PersonName {
	int _placeholder;
    char pname[];
} PersonName;

/*****************************************************************************
 * Input/Output functions
 *
 * Include input and output functions
 *****************************************************************************/

PG_FUNCTION_INFO_V1(pname_in);

Datum pname_in(PG_FUNCTION_ARGS) {
	char *str, *src, *dst, *pos;
    PersonName *result;
    regex_t regex;
    int length;

    str = PG_GETARG_CSTRING(0);

    regcomp(&regex,
            "^[A-Z][A-Za-z'-]+( [A-Z][A-Za-z'-]+)*,[ ]?[A-Z][A-Za-z'-]+( [A-Z][A-Za-z'-]+)*$",
            REG_EXTENDED);

    if (regexec(&regex, str, 0, NULL, 0) != 0) {
        ereport(ERROR,
                (errcode(ERRCODE_INVALID_TEXT_REPRESENTATION),
                 errmsg("invalid input syntax for type %s: \"%s\"",
                        "PersonName", str)));
    }

    pos = strstr(str, ", ");
    if (pos != NULL) {
        length = strlen(str);
        result = (PersonName *) palloc(VARHDRSZ + length);
        SET_VARSIZE(result, VARHDRSZ + length);

        src = str, dst = result->pname;
        while (*src) {
            if (src == pos) {
                *dst++ = *src++;
                src++;
            } else {
                *dst++ = *src++;
            }
        }
        *dst = '\0';
    } else {
        length = strlen(str) + 1;
        result = (PersonName *) palloc(VARHDRSZ + length);
        SET_VARSIZE(result, VARHDRSZ + length);

        snprintf(result->pname, length, "%s", str);
    }

    PG_RETURN_POINTER(result);
}

PG_FUNCTION_INFO_V1(pname_out);

Datum pname_out(PG_FUNCTION_ARGS) {
    PersonName *pname = (PersonName *) PG_GETARG_POINTER(0);
    PG_RETURN_CSTRING(psprintf("%s", pname->pname));
}

/*****************************************************************************
 * Operator class for defining B-tree index
 *
 * Include comparison functions
 *****************************************************************************/

PG_FUNCTION_INFO_V1(pname_cmp);

Datum pname_cmp(PG_FUNCTION_ARGS) {
    PersonName *a = (PersonName *) PG_GETARG_POINTER(0);
    PersonName *b = (PersonName *) PG_GETARG_POINTER(1);

    PG_RETURN_INT32(strcmp(a->pname, b->pname));
}

PG_FUNCTION_INFO_V1(pname_eq);

Datum pname_eq(PG_FUNCTION_ARGS) {
    PersonName *a = (PersonName *) PG_GETARG_POINTER(0);
    PersonName *b = (PersonName *) PG_GETARG_POINTER(1);

    PG_RETURN_BOOL(strcmp(a->pname, b->pname) == 0);
}

PG_FUNCTION_INFO_V1(pname_ne);

Datum pname_ne(PG_FUNCTION_ARGS) {
    PersonName *a = (PersonName *) PG_GETARG_POINTER(0);
    PersonName *b = (PersonName *) PG_GETARG_POINTER(1);

    PG_RETURN_BOOL(strcmp(a->pname, b->pname) != 0);
}

PG_FUNCTION_INFO_V1(pname_lt);

Datum pname_lt(PG_FUNCTION_ARGS) {
    PersonName *a = (PersonName *) PG_GETARG_POINTER(0);
    PersonName *b = (PersonName *) PG_GETARG_POINTER(1);

    PG_RETURN_BOOL(strcmp(a->pname, b->pname) < 0);
}

PG_FUNCTION_INFO_V1(pname_le);

Datum pname_le(PG_FUNCTION_ARGS) {
    PersonName *a = (PersonName *) PG_GETARG_POINTER(0);
    PersonName *b = (PersonName *) PG_GETARG_POINTER(1);

    PG_RETURN_BOOL(strcmp(a->pname, b->pname) <= 0);
}

PG_FUNCTION_INFO_V1(pname_gt);

Datum pname_gt(PG_FUNCTION_ARGS) {
    PersonName *a = (PersonName *) PG_GETARG_POINTER(0);
    PersonName *b = (PersonName *) PG_GETARG_POINTER(1);

    PG_RETURN_BOOL(strcmp(a->pname, b->pname) > 0);
}

PG_FUNCTION_INFO_V1(pname_ge);

Datum pname_ge(PG_FUNCTION_ARGS) {
    PersonName *a = (PersonName *) PG_GETARG_POINTER(0);
    PersonName *b = (PersonName *) PG_GETARG_POINTER(1);

    PG_RETURN_BOOL(strcmp(a->pname, b->pname) >= 0);
}

/*****************************************************************************
 * Other functions
 *
 * Include family, given, show and hash functions
 *****************************************************************************/

PG_FUNCTION_INFO_V1(family);

Datum family(PG_FUNCTION_ARGS) {
    PersonName *pname = (PersonName *) PG_GETARG_POINTER(0);
    text *result;
    char *copy, *name;
    int length;

    copy = strdup(pname->pname);
    name = strtok(copy, ",");
    length = strlen(name);

    result = (text *) palloc(VARHDRSZ + length);
    SET_VARSIZE(result, VARHDRSZ + length);

    memcpy(VARDATA(result), name, length);

    free(copy);

    PG_RETURN_TEXT_P(result);
}

PG_FUNCTION_INFO_V1(given);

Datum given(PG_FUNCTION_ARGS) {
    PersonName *pname = (PersonName *) PG_GETARG_POINTER(0);
    text *result;
    char *copy, *name;
    int length;

    copy = strdup(pname->pname);
    strtok(copy, ",");
    name = strtok(NULL, ",");
    length = strlen(name);

    result = (text *) palloc(VARHDRSZ + length);

    SET_VARSIZE(result, VARHDRSZ + length);
    memcpy(VARDATA(result), name, length);

    free(copy);

    PG_RETURN_TEXT_P(result);
}

PG_FUNCTION_INFO_V1(show);

Datum show(PG_FUNCTION_ARGS) {
    PersonName *pname = (PersonName *) PG_GETARG_POINTER(0);
    text *result;
    char *copy, *family, *given, *result_str;
    int length;

    copy = strdup(pname->pname);
    family = strtok(copy, ",");
    given = strtok(NULL, ",");

    if (strstr(given, " ") != NULL) {
        given = strtok(given, " ");
    }

    result_str = psprintf("%s %s", given, family);

    length = strlen(result_str);
    result = (text *) palloc(VARHDRSZ + length);
    SET_VARSIZE(result, VARHDRSZ + length);
    memcpy(VARDATA(result), result_str, length);

    free(copy);

    PG_RETURN_TEXT_P(result);
}

PG_FUNCTION_INFO_V1(pname_hash);

Datum pname_hash(PG_FUNCTION_ARGS) {
    PersonName *pname = (PersonName *) PG_GETARG_POINTER(0);
    PG_RETURN_INT32(DatumGetUInt32(hash_any((unsigned char *) pname->pname, strlen(pname->pname))));
}
