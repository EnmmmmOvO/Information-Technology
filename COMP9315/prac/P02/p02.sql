drop type if exists SchemaTuple cascade;
create type SchemaTuple as ("table" text, "attributes" text);

create or replace function schema1() returns setof SchemaTuple as $$
declare
    rec record;
    detail record;
    result Schematuple;
    attr_list text[];
    pos integer;
begin
    for rec in
        select c.oid, c.relname
        from pg_class c join pg_namespace n on n.oid = c.relnamespace
        where n.nspname = 'public' and c.relkind = 'r'
    loop
        pos := 0;
        result."table" := rec.relname;

        for detail in
            select a.attname, t.typname, a.atttypmod
            from pg_attribute a join pg_type t on a.atttypid = t.oid
            where a.attrelid = rec.oid and a.attnum > 0
        loop
            if detail.typname = 'int4' then
                detail.typname := 'integer';
            else if detail.typname = 'float8' then
                detail.typname = 'float';
            end if;
                end if;

            if detail.atttypmod != -1 then
                detail.typname = detail.typname || '(' || detail.atttypmod || ')';
            end if;
            attr_list[pos] := detail.attname || ':' ||detail.typname;

            pos := pos + 1;
            end loop;

        result.attributes = array_to_string(attr_list, ', ');

        return next result;
        end loop;
end;
$$ language plpgsql;

select * from schema1();

