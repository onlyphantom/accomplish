-- sqlite3 accomplish.db < database/initial-data.sql

INSERT INTO projects (task_name, due_date, task_priority, scope, done)
VALUES ("Review Black Swan on Goodreads", "15/09/2018", 3, "personal", 1);

INSERT INTO projects (task_name, due_date, task_priority, scope, done)
VALUES ("Update Algoritma's Course Materials", "18/09/2018", 5, "work", 0);

INSERT INTO projects (task_name, due_date, task_priority, scope, done)
VALUES ("Conduct Quarterly Review with Team", "23/09/2018", 5, "work", 0);

INSERT INTO projects (task_name, due_date, task_priority, scope, done)
VALUES ("Pay Electricity Bills", "25/09/2018", 2, "personal", 0);

INSERT INTO projects (task_name, due_date, task_priority, scope, done)
VALUES ("Teach at Flask Internal Training", "29/09/2018", 4, "work", 0);