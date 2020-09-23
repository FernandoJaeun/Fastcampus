BEGIN TRANSACTION;
CREATE TABLE users(    id INTEGER PRIMARY KEY,     username text,     email text,     phone text,     website text,    regdate text);
INSERT INTO "users" VALUES(1,'Kim','kim@naver.com','010-0000-0000','kim.com','2020-09-23 18:57:13');
INSERT INTO "users" VALUES(2,'Lee','leejaeyun95@naver.com','010-8589-2763','fercho@naver.com','2020-09-23 18:56:28');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','01012345566','Lee.com','2020-09-23 18:56:28');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','01012345566','Cho.com','2020-09-23 18:56:28');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@google.com','01012345566','Yoo.com','2020-09-23 18:56:28');
COMMIT;
