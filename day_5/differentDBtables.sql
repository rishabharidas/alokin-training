-- insert data from one databases table to another DB table

create database if not exists sqltrain2;
use sqltrain2;
create table if not exists table2(id integer primary key,username varchar(25));
insert into sqltrain2.table2(table2.id,table2.username) select table1.id,table1.name from sqltrain.table1;
select * from table2;
