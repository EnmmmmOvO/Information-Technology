-- Ex1, 10
select c.oid, c.relname
from pg_namespace n join pg_class c on c.relnamespace = n.oid
where n.nspname = 'public' and c.relkind = 'r';


-- Ex1, 11
create or replace function tablePath(tableName text) returns text as $$
declare
    r record;
    temp text;
    _did integer;
begin
    select c.oid, c.reltablespace into r
    from pg_class c
        join pg_namespace n on n.oid = c.relnamespace
    where relname = tableName and n.nspname = 'public' and c.relkind = 'r';

    if r isnull then
        return 'No such table: ' || tableName;
        end if;

    select oid into _did from pg_database where datname = current_database();

    if r.reltablespace = 0 then
        temp := 'PGDATA/base';
    else
        select t.spcname into temp from pg_tablespace t where r.reltablespace = t.oid;
        if temp isnull then
            temp := '???';
        end if;
    end if;
    return temp || '/' || _did || '/' || r.oid;
end;
$$ language plpgsql;


-- Ex1, 12
create or replace function tableSchemas() returns setof text as $$
declare
    _r record;
    _r2 record;
    _result text[];
begin
    for _r in
        select c.oid, c.relname
        from pg_class c join pg_namespace n on n.oid = c.relnamespace
        where n.nspname = 'public' and c.relkind = 'r'
    loop
        for _r2 in select attname from pg_attribute where attrelid = _r.oid and attnum > 0 loop
            _result := _result || _r2.attname;
        end loop;
        return next _r.relname || '(' || array_to_string(_result, ', ') || ')';
    end loop;
end;
$$ language plpgsql;


-- Ex1, 13
create or replace function tableSchemas() returns setof text as $$
declare
    _r record;
    _r2 record;
    _result text[];
begin
    for _r in
        select c.oid, c.relname
        from pg_class c join pg_namespace n on n.oid = c.relnamespace
        where n.nspname = 'public' and c.relkind = 'r'
    loop
        for _r2 in
            select a.attname, a.attlen, t.typname, a.atttypmod
            from pg_attribute a join pg_type t on t.oid = a.atttypid
            where attrelid = _r.oid and attnum > 0
        loop
            if _r2.attlen = -1 then
                _r2.typname := _r2.typname || '(' || _r2.atttypmod || ')';
            elsif _r2.typname = 'int4' then
                _r2.typname := 'integer';
                end if;
            _result := _result || (_r2.attname || ':' || _r2.typname);
        end loop;
        return next _r.relname || '(' || array_to_string(_result, ', ') || ')';
    end loop;
end;
$$ language plpgsql;
