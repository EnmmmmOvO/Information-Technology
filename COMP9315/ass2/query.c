// query.c ... query scan functions
// part of Multi-attribute Linear-hashed Files
// Manage creating and using Query objects
// Last modified by John Shepherd, July 2019

#include "defs.h"
#include "query.h"

#include <time.h>

#include "hash.h"
#include "reln.h"
#include "tuple.h"

// A suggestion ... you can change however you like

struct QueryRep {
	Reln    rel;       // need to remember Relation info
	Bits    known;     // the hash value from MAH
	Bits    unknown;   // the unknown bits from MAH
	PageID  curpage;   // current page in scan
	int     is_ovflow; // are we in the overflow pages?
	Offset  curtup;    // offset of current tuple within page
	Tuple   target;    // target tuple string
	int     index;     // number of tuples scanned
	PageID	record;    // record the normal page number during visiting overflow page
	//TODO
};

// take a query string (e.g. "1234,?,abc,?")
// set up a QueryRep object for the scan
PageID find_next_match_page(Bits known, Bits unknown, Reln r, Count start_page);

Query startQuery(Reln r, char *q)
{
	Query new = malloc(sizeof(struct QueryRep));
	assert(new != NULL);
	// TODO
	// Partial algorithm:
	// form known bits from known attributes
	// form unknown bits from '?' attributes
	// compute PageID of first page
	//   using known bits and first "unknown" value
	// set all values in QueryRep object

	new->rel = r;
	new->known = 0;
	new->unknown = 0;
	new->is_ovflow = FALSE;
	new->curpage = NO_PAGE;
	new->curtup = 0;
	new->index = -1;
	new->record = NO_PAGE;
	new->target = copyString(q);

	ChVecItem* cv = chvec(r);
	int unknown_part[nattrs(r)];
	Bits hash_val[nattrs(r)];

	char **tok = malloc(nattrs(r) * sizeof(char*));
	assert(tok != NULL);
	tupleVals(q, tok);

	for (int i = 0; i < nattrs(r); i++) {
		if (strcmp(tok[i], "?") == 0) {
			unknown_part[i] = 1;
		} else {
			unknown_part[i] = 0;
			hash_val[i] = hash_any((unsigned char *)tok[i], strlen(tok[i]));
		}
	}

	freeVals(tok, nattrs(r));

	for (int i = 0; i < MAXCHVEC; i++) {
		if (unknown_part[cv[i].att] == 0) {
			if (bitIsSet(hash_val[cv[i].att], cv[i].bit)) {
				new->known = setBit(new->known, i);
			}
		} else {
			new->unknown = setBit(new->unknown, i);
		}
	}

	return new;
}

// get next tuple during a scan

Tuple getNextTuple(Query q)
{
	// TODO
	// Partial algorithm:
	// if (more tuples in current page)
	//    get next matching tuple from current page
	// else if (current page has overflow)
	//    move to overflow page
	//    grab first matching tuple from page
	// else
	//    move to "next" bucket
	//    grab first matching tuple from data page
	// endif
	// if (current page has no matching tuples)
	//    go to next page (try again)
	// endif

	if (q->curpage == NO_PAGE) {
		q->curpage = find_next_match_page(q->known, q->unknown, q->rel, q->curpage);
	}

	while (TRUE) {
		FILE *f = q->is_ovflow ? ovflowFile(q->rel) : dataFile(q->rel);
		assert(f != NULL);
		Page p = getPage(f, q->curpage);
		assert(p != NULL);

		while (TRUE) {
			if (q->index != -1) {
				q->curtup += strlen(pageData(p) + q->curtup) + 1;
			}
			q->index += 1;
			Tuple t = pageData(p) + q->curtup;

			if (q->index >= pageNTuples(p)) break;
			if (tupleMatch(q->rel, t, q->target)) return t;
		}

		const Offset ov = pageOvflow(p);
		if (ov == NO_PAGE) {
			q->curpage = find_next_match_page(q->known, q->unknown, q->rel, q->is_ovflow ? q->record : q->curpage);
			if (q->curpage == -1) break;
			q->is_ovflow = FALSE;
			q->record = NO_PAGE;
		} else {
			if (!q->is_ovflow) q->record = q->curpage;
			q->is_ovflow = TRUE;
			q->curpage = ov;
		}

		q->curtup = 0;
		q->index = -1;
	}

	return NULL;
}

// clean up a QueryRep object and associated data

void closeQuery(Query q)
{
	free(q);
}

PageID find_next_match_page(Bits known, Bits unknown, Reln r, Count start_page) {
	Bits mask;

	for (int i = start_page + 1; i < npages(r); i++) {
		int valid = 1;
		Count current_depth = i < splitp(r) ? depth(r) + 1 : depth(r);
		mask = (1 << current_depth) - 1;

		Bits current_known = known & mask;
		Bits current_unknown = unknown & mask;

		for (int bit = 0; bit < current_depth; bit++) {
			if (bitIsSet(current_unknown, bit)) continue;
			if (bitIsSet(i, bit) != bitIsSet(current_known, bit)) {
				valid = 0;
				break;
			}
		}
		if (valid) return i;
	}
	return NO_PAGE;
}
