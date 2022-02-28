create database if not exists sqltrain ;
use sqltrain;
create table if not exists table1(id integer primary key,name varchar(25));
create table if not exists table2(id integer primary key,username varchar(25));
create table if not exists jointable(id integer, location varchar(30), country varchar(20));
insert into table1 values(12,"john");
insert into jointable values(12,"newjersy","canada");
insert into table1 values(22,"ponny");
insert into jointable values(22,"texas","USA");
insert into jointable values(22,"washing","USA");
insert into table1 values(32,"funny");
insert into jointable values(32,"soul","underworld");
insert into table1 values(42,"monster");
insert into jointable values(52,"bowl","worldless");
insert into table2(id,username) select id,name from table1;
select * from table2;



