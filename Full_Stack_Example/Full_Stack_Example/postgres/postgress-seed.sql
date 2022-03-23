CREATE TABLE ApplicationSettings(app_key TEXT PRIMARY KEY, app_value TEXT);
CREATE TABLE Classes(ClassId SERIAL PRIMARY KEY, ClassName TEXT, ClassCode TEXT, Section TEXT, Semester TEXT, Teacher TEXT, SchoolId INT);
CREATE TABLE UserSchoolMapping(UniqueId SERIAL PRIMARY KEY, UserId INT, SchoolId INT);
CREATE TABLE UserClassMapping(UniqueId SERIAL PRIMARY KEY, UserId INT, SchoolId INT);
CREATE TABLE School(SchoolId SERIAL PRIMARY KEY, SchoolName TEXT, SchoolState TEXT, City TEXT, Picture TEXT);
CREATE TABLE Videos(VideoId SERIAL PRIMARY KEY, VideoSubject TEXT, Content TEXT, VideoDescription TEXT, UploadedBY INT, CreateDatetime TIMESTAMP, ClassId INT);
CREATE TABLE Users(UserId SERIAL PRIMARY KEY, Username TEXT, pwd TEXT, LastLogin TIMESTAMP);

INSERT INTO ApplicationSettings(app_key,app_value) VALUES ('ApplicationName', 'SSU Video Sharing');
INSERT INTO ApplicationSettings(app_key,app_value) VALUES ('ApplicationVersion', '1.0.0');

INSERT INTO Users(UserId, Username, pwd, LastLogin) VALUES (1, 'Username', 'password11', now());
INSERT INTO School(SchoolId, SchoolName, SchoolState, City, Picture) VALUES (1, 'Shawnee State University', 'Ohio', 'Portsmouth', 'Picture');