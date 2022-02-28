create database if not exists sqltrain ;
use sqltrain;
create table if not exists leftjoinedtable as select table1.id, table1.name,jointable.location,jointable.country from table1 left join jointable on table1.id = jointable.id;
create table if not exists innerjoinedtable as select table1.id, table1.name,jointable.location,jointable.country from table1 inner join jointable on table1.id = jointable.id;
create table if not exists rightjoinedtable as select table1.id, table1.name,jointable.location,jointable.country from table1 right join jointable on table1.id = jointable.id;
create table if not exists fulljoinedtable as select table1.id, table1.name,jointable.location,jointable.country from table1 cross join jointable on table1.id = jointable.id;