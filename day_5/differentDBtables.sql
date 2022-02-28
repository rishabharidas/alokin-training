-- insert data from one database's table to another DB's table (testing merge)
create database if not exists sqltrain2;
use sqltrain2;
create table if not exists table2(id integer primary key,username varchar(25));
insert into sqltrain2.table2(table2.id,table2.username) select table1.id,table1.name from sqltrain.table1;
select * from table2;