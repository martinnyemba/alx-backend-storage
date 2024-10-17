# 0x00. MySQL Advanced

## Back-end | SQL | MySQL

## Concepts

For this project, I will focus on the following concepts:

- Advanced SQL

## Resources

I will read or watch the following resources:

- MySQL cheatsheet
- MySQL Performance: How To Leverage MySQL Database Indexing
- Stored Procedure
- Triggers
- Views
- Functions and Operators- Trigger Syntax and Examples
- CREATE TABLE Statement
- CREATE PROCEDURE and CREATE FUNCTION Statements
- CREATE INDEX Statement
- CREATE VIEW Statement

## Learning Objectives

By the end of this project, I expect to be able to explain the following concepts:

### General

- How to create tables with constraints
- How to optimize queries by adding indexes
- What stored procedures and functions are and how to implement them in MySQL
- What views are and how to implement them in MySQL
- What triggers are and how to implement them in MySQL

## Requirements

### General

- All my files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
- All my files should end with a new line.
- All my SQL queries will have a comment just before (i.e., syntax above).
- All my files will start with a comment describing the task.
- All SQL keywords will be in uppercase (SELECT, WHERE…).
- A `README.md` file, at the root of the folder of the project, is mandatory.
- The length of my files will be tested using `wc`.

### More Info

**Comments for my SQL file:**

```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

**Using “container-on-demand” to run MySQL:**

- Ask for a container with Ubuntu 18.04 - Python 3.7.
- Connect via SSH or the WebTerminal.
- In the container, I will start MySQL before using it:

```bash
$ service mysql start
 * MySQL Community Server 5.7.30 is started
```

- To execute SQL scripts:

```bash
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
```

- Credentials in the container are `root/root`.

### How to Import a SQL Dump

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
```

