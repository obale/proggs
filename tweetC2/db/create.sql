/**
 * sqlite3 tweetC2.db < create.sql
 */
DROP TABLE handled_commands;

CREATE TABLE handled_commands ( id INTEGER PRIMARY KEY, username VARCHAR,  message VARCHAR, created_at VARCHAR);
