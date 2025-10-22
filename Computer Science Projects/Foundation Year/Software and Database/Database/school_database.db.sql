BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Teacher_Users" (
	"username"	TEXT NOT NULL UNIQUE,
	"password"	NUMERIC NOT NULL,
	"Teacher_ID"	INTEGER NOT NULL UNIQUE,
	"First_Name"	TEXT NOT NULL,
	"Last_Name"	TEXT NOT NULL,
	"Course"	TEXT NOT NULL,
	"Title"	TEXT NOT NULL,
	"Teacher_email"	NUMERIC NOT NULL UNIQUE,
	"Gender"	TEXT NOT NULL,
	"Pronouns"	TEXT NOT NULL,
	PRIMARY KEY("Teacher_ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Enrollment" (
	"UCAS_ID"	INTEGER NOT NULL UNIQUE,
	"First_Name"	TEXT NOT NULL,
	"Last_Name"	TEXT NOT NULL,
	"Course_ID"	INTEGER NOT NULL,
	"Age"	INTEGER NOT NULL,
	"Qualifications"	BLOB,
	PRIMARY KEY("UCAS_ID")
);
CREATE TABLE IF NOT EXISTS "Grades" (
	"Module1"	INTEGER DEFAULT 'N/A',
	"Module2"	INTEGER DEFAULT 'N/A',
	"Module3"	INTEGER DEFAULT 'N/A',
	"Module4"	INTEGER DEFAULT 'N/A',
	"OptionalModule1"	INTEGER DEFAULT 'N/A',
	"OptionalModule2"	INTEGER DEFAULT 'N/A',
	"OptionalModule3"	INTEGER DEFAULT 'N/A'
);
CREATE TABLE IF NOT EXISTS "Attendance" (
	"Module1"	INTEGER DEFAULT 'N/A',
	"Module2"	INTEGER DEFAULT 'N/A',
	"Module3"	INTEGER DEFAULT 'N/A',
	"Module4"	INTEGER DEFAULT 'N/A',
	"OptionalModule1"	INTEGER DEFAULT 'N/A',
	"OptionalModule2"	INTEGER DEFAULT 'N/A',
	"OptionalModule3"	INTEGER DEFAULT 'N/A'
);
CREATE TABLE IF NOT EXISTS "Student_Users" (
	"username"	TEXT NOT NULL UNIQUE,
	"password"	NUMERIC NOT NULL,
	"Student_ID"	INTEGER NOT NULL UNIQUE,
	"First_Name"	TEXT NOT NULL,
	"Last_Name"	TEXT NOT NULL,
	"Course_Name"	TEXT NOT NULL,
	"Student_Email"	NUMERIC NOT NULL UNIQUE,
	"Age"	INTEGER NOT NULL,
	"Gender"	TEXT NOT NULL,
	"Pronouns"	TEXT NOT NULL,
	"Enrollment_Date-Time"	BLOB NOT NULL,
	PRIMARY KEY("Student_ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Courses" (
	"Course_ID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL UNIQUE,
	"Duration"	NUMERIC NOT NULL,
	"Degree"	TEXT NOT NULL,
	"Study_Mode"	TEXT NOT NULL,
	"Foundation_Year"	NUMERIC NOT NULL DEFAULT 'N/A',
	"Placement_Year"	NUMERIC NOT NULL DEFAULT 'N/A',
	"Industrial_Year"	NUMERIC NOT NULL DEFAULT 'N/A',
	"UCAS_codes"	NUMERIC NOT NULL,
	PRIMARY KEY("Course_ID" AUTOINCREMENT)
);
INSERT INTO "Courses" VALUES (1,'Accountancy','3 years','Bsc','F-T/S','Available','N/A','N/A','N410');
INSERT INTO "Courses" VALUES (2,'Acting','3 years','Bsc','F-T/S','N/A','N/A','N/A','W411');
INSERT INTO "Courses" VALUES (3,'Adult Nursing','3 years','Bsc','F-T/O/B','N/A','N/A','N/A','B749');
INSERT INTO "Courses" VALUES (4,'Aerospace Engineering','3/4 years','BEng/MEng','F-T/S','N/A','N/A','N/A','H410/H411');
INSERT INTO "Courses" VALUES (5,'Architecture','3 years','BSc','F-T/S','N/A','N/A','N/A','K100');
INSERT INTO "Courses" VALUES (6,'Banking and Finance','3 years','BSc','F-T/S','Available','N/A','N/A','N310');
INSERT INTO "Courses" VALUES (7,'Business Economics','3 years','BSc','F-T/S','Available','N/A','N/A','L112');
COMMIT;
