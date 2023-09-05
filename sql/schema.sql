PRAGMA foreign_keys = ON;

-- Contains the information for current internships
CREATE TABLE jobs(
  jobid INTEGER PRIMARY KEY AUTOINCREMENT,
  salary INTEGER, 
  cname VARCHAR(50) NOT NULL,
  title VARCHAR(50) NOT NULL,
  jsubject VARCHAR(50) NOT NULL,
  jdesc VARCHAR(300) NOT NULL,
  loc VARCHAR(50) NOT NULL,
  jreq VARCHAR(100) NOT NULL,
  link VARCHAR(100) NOT NULL, 
  postdate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(cname, title)
);

--Contains the basic information for past internships
CREATE TABLE archive(
  jobid INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  cname VARCHAR(50) NOT NULL,
  salary INTEGER NOT NULL, 
  postdate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  closedate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--Contains an email list for users who sign up for updates 
CREATE TABLE subscribers(
  email VARCHAR(300) PRIMARY KEY,
  fullname VARCHAR(50) NOT NULL
);

--Contains reviews for internships
CREATE TABLE reviews(
  reviewid INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(50) NOT NULL DEFAULT 'Anonymous',
  jobid INTEGER NOT NULL,
  content VARCHAR(300) NOT NULL,
  user VARCHAR(50) NOT NULL,
  FOREIGN KEY(jobid) REFERENCES jobs(jobid) ON DELETE CASCADE,
  FOREIGN KEY(user) REFERENCES users(username) ON DELETE CASCADE
);

--Contains ratings (1 to 10, with 10 being the best) for internships
CREATE TABLE ratings(
  ratingid INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(50) NOT NULL DEFAULT 'Anonymous',
  jobid INTEGER NOT NULL,
  rating INTEGER NOT NULL,
  user VARCHAR(50) NOT NULL,
  CHECK (rating >= 1 AND rating <= 10),
  FOREIGN KEY(jobid) REFERENCES jobs(jobid) ON DELETE CASCADE,
  FOREIGN KEY(user) REFERENCES users(username) ON DELETE CASCADE
);

--User information used for login and access restrictions
CREATE TABLE users(
  username VARCHAR(50) PRIMARY KEY,
  password VARCHAR(256) NOT NULL,
  isadmin INTEGER NOT NULL DEFAULT 0
);