PRAGMA foreign_keys = ON;


INSERT INTO jobs(salary, cname, title, jsubject, jdesc, loc, jreq, link, postdate)
VALUES
    (30, 'Aware', 'Software Engineering Intern', 'STEM', 'AI and ML', 'Columbus, Ohio', 'CS major', 'https://jobs.lever.co/Aware/59696e67-e50a-4f13-b845-1201164449fa/', '2023-03-02 12:15:00'),
    (80, 'Two Sigma', 'Quantitative Researcher Intern', 'STEM', 'programming and data analysis', 'New York, New York', 'STEM major', 'https://careers.twosigma.com/careers/JobDetail/New-York-New-York-United-States-Quantitative-Researcher-Internship/10972', '2023-01-02 07:13:00'),
    (14, 'City of Columbus', 'Airport-Summer Administrative Intern', 'non-STEM', 'customer service', 'Columbus, Indiana', 'valid driver''s license', 'https://cityofcolumbusin.munisselfservice.com/ess/employmentopportunities/default.aspx', '2023-03-10 09:33:00'),
    (20, 'Ascension', 'Nursing Intern - Medical Surgical Observational Unit', 'non-STEM', 'nursing', 'Novi, Michigan', 'enrolled in nursing program', 'https://www.linkedin.com/jobs/view/nursing-intern-medical-surgical-observational-unit-at-ascension-3510914865/', '2023-03-03 02:15:00'),
    (25, 'Vial', 'Software Engineer Intern', 'STEM', 'build products to power clinical trials', 'San Francisco, California', 'CS major', 'https://jobs.lever.co/Vial/c416c6df-63d7-47f8-b252-bfc159c2e2db', '2023-02-21 10:32:00');

INSERT INTO archive(title, cname, salary, postdate, closedate)
VALUES
    ('Software Engineer Intern', 'Google', 55, '2022-07-02 10:03:00', '2022-12-29 12:00:00'),
    ('Legal Intern', 'Harman International', 25, '2022-07-31 04:00:00', '2022-10-13 11:00:00'),
    ('PR Intern - Corporate', 'Current Global', 20, '2022-08-21 04:30:00', '2022-11-20 09:20:00'),
    ('Software Development Engineer Intern', 'Amazon', 50, '2022-07-04 12:43:00', '2022-12-22 11:12:00'),
    ('IT Intern', 'Belle Tire', 18, '2023-01-04 10:42:00', '2023-03-01 07:17:00');

INSERT INTO subscribers(email, fullname)
VALUES
    ('mattwang@umich.edu', 'Matthew Wang'),
    ('andli@umich.edu', 'Andrew Li'),
    ('bengoh@umich.edu', 'Benjamin Goh'),
    ('timchoi@umich.edu', 'Timothy Choi');

INSERT INTO users(username, password)
VALUES
    ("a", "123");

INSERT INTO reviews(jobid, content, user)
VALUES
    (1, 'The interview process consisted of 3 rounds', 'a'),
    (1, 'Make sure to review the interview tips from the company website, which are really helpful', 'a'),
    (3, 'The interview questions were extremely hard', 'a'),
    (5, 'I got ghosted', 'a'),
    (2, 'The interviewers asked a lot of behavioral questions', 'a');

INSERT INTO ratings(jobid, rating, user)
VALUES
    (1, 8, 'a'),
    (1, 6, 'a'),
    (2, 1, 'a'),
    (2, 9, 'a'),
    (5, 10, 'a'),
    (3, 2, 'a'),
    (3, 5, 'a'),
    (4, 7, 'a');

--Update user admin status here
