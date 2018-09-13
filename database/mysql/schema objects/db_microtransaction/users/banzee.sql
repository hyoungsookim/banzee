use mysql;

/* banzee is a user for API */
grant select, insert, update, delete, create temporary tables, execute on db_microtransaction.* to 'banzee'@'%';
flush privileges;

grant select, insert, update, delete, create temporary tables, execute on db_microtransaction.* to 'banzee'@'localhost';
flush privileges;
