-- sqlite3 accomplish.db < database/db-schema.sql

drop table if exists projects;
create table projects (
    id INTEGER PRIMARY KEY autoincrement,
    task_name TEXT NOT NULL,
    due_date TEXT NOT NULL,
    task_priority INTEGER NOT NULL, 
    scope TEXT NOT NULL,
    done INTEGER NOT NULL
);
