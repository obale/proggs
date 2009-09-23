/**
 * sqlite3 db/pm.db < install/create_pm.sql
 */

DROP TABLE message;
CREATE TABLE message (id INTEGER PRIMARY KEY, fromuser VARCHAR, touser VARCHAR, time VARCHAR, message VARCHAR);
