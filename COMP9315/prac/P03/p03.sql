-- Ex1

-- a. what is the largest staff/student id? (People.id)
select max(id) from people;

-- b. what is the earliest birthday of any person in the database? (People.birthday)
select min(birthday) from people;

-- c. what is the maximum mark available for any assessment item? (Items.maxmark)
select max(maxmark) from items;

-- d. what assessment items are in each course and how many marks does each have?
select c.code, i.name, i.maxmark
from courses c join items i on i.course = c.id;

-- e. how many students are enrolled in each course? (Courses.code,count(Enrolments.student))
select c.code, count(e)
from courses c join enrolments e on e.course = c.id
group by c.code
order by c.code;

-- f. check that each student's assessment marks add up to the final mark for each course
-- (Course.code,People.name,Enrolments.mark,sum(Assessment.marks))
select c.code, p.given || ' ' || p.family as name, e.mark, sum(a.mark)
from enrolments e
    join people p on e.student = p.id
    join courses c on c.id = e.course
    join items i on c.id = i.course
    join assessments a on a.student = p.id and a.item = i.id
group by p.given, p.family, c.code, e.mark
order by c.code, p.given, p.family;

-- Ex2
select oid, datname from pg_database;

select c.oid, c.relname, c.relpages
from pg_class c join pg_namespace n on n.oid = c.relnamespace
where n.nspname = 'public' and c.relkind = 'r';