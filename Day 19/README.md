# SQL Functions

## Aggregate Functions

```sql
-- Select the minimum salary from the employee table
SELECT MIN(salary) FROM employee;

-- Select the maximum salary from the employee table
SELECT MAX(salary) FROM employee;

-- Select the sum of salaries from the employee table
SELECT SUM(salary) FROM employee;

-- Select the average salary from the employee table
SELECT AVG(salary) FROM employee;

-- Select the count of salaries from the employee table
SELECT COUNT(salary) FROM employee;
```

## Number Functions

```sql
-- Round the average salary from the employee table
SELECT ROUND(AVG(salary)) FROM employee;

-- Select the absolute value of the average salary from the employee table
SELECT ABS(AVG(salary)) FROM employee;

-- Select 2 raised to the power of 3
SELECT POW(2, 3);

-- Select the square root of 2
SELECT SQRT(2);

-- Select the remainder of 34 divided by 3
SELECT MOD(34, 3);
```

## Character Functions

```sql
-- Select the length of names from the employee table
SELECT LENGTH(name), name FROM employee;

-- Concatenate id and name from the employee table
SELECT CONCAT(id, name) FROM employee;

-- Select the position of 'a' in names from the employee table
SELECT INSTR(name, 'a'), name FROM employee;

-- Select the substring of names from the 2nd to the 6th character from the employee table
SELECT SUBSTR(name, 2, 6) FROM employee;

-- Trim spaces from the string 'chess'
SELECT TRIM('           chess         ');

-- Reverse the names from the employee table
SELECT REVERSE(name), name FROM employee;
```

## Find Even Age Employees

```sql
-- Select all employees with an even age
SELECT * FROM employee WHERE age % 2 = 0;
```

## Find Palindrome Names

```sql
-- Select all employees where the name is a palindrome
SELECT * FROM employee WHERE name = REVERSE(name);
```

## Group By Clause

```sql
-- Select the count of employees by job
SELECT COUNT(*), job FROM employee GROUP BY job;

-- Select the count of employees by department number, ordered by department number
SELECT dept_no, COUNT(*) FROM employee GROUP BY dept_no ORDER BY dept_no;

-- Select the job, maximum salary, minimum salary, and count of employees by job
SELECT job, MAX(salary), MIN(salary), COUNT(*) FROM employee GROUP BY job;

-- Select the sum of salaries by department number where the name does not start with 's', grouped by department number
SELECT dept_no, SUM(salary) FROM emp_details WHERE name NOT LIKE 's%' GROUP BY dept_no;
```

## Dates

```sql
-- Select the current date and time
SELECT SYSDATE();

-- Add a column for the date of joining to the employee table
ALTER TABLE employee ADD doj DATE;

-- Update the date of joining for specific employees
UPDATE employee SET doj = '2024-03-11' WHERE id IN (113, 106, 118);
```

## Having Clause

```sql
-- Select the count of employees by job where the count is greater than 2
SELECT COUNT(*), job FROM employee GROUP BY job HAVING COUNT(*) > 2;
```

## Constraints

### Creating a Table with Constraints

```sql
-- Create a table with unique, not null, and default constraints
CREATE TABLE myTable (
    id INT UNIQUE,
    name VARCHAR(225) NOT NULL,
    age INT
);

-- Insert values into the myTable table
INSERT INTO myTable VALUES (1, 'Rohit', 20);

-- Alter the table to add a default salary value
ALTER TABLE myTable ADD salary INT DEFAULT 100000;
INSERT INTO myTable (id, name, age) VALUES (2, 'Rushi', 20);

-- Add a check constraint on the marks column
ALTER TABLE myTable ADD marks FLOAT CHECK (marks > 75);

-- Add a primary key constraint on the eid column
ALTER TABLE myTable ADD eid INT PRIMARY KEY;
```

### Creating a Table with Auto Increment and Primary Key

```sql
-- Create a student table with auto increment primary key
CREATE TABLE student (
    stud_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(225)
);

-- Describe the student table
DESC student;

-- Insert values into the student table
INSERT INTO student (name) VALUES ('Rohit');
INSERT INTO student (name) VALUES ('Abhishith');
INSERT INTO student (name) VALUES ('Bhargav');

-- Select all records from the student table
SELECT * FROM student;
```

### Creating a Table with Foreign Key

```sql
-- Create a college table
CREATE TABLE college (
    cid INT,
    name VARCHAR(225),
    city VARCHAR(225)
);

-- Describe the college table
DESC college;

-- Add a foreign key constraint on the cid column referencing the student table
ALTER TABLE college ADD FOREIGN KEY (cid) REFERENCES student (stud_id);

-- Insert values into the college table
INSERT INTO college VALUES (1, 'SRGEC', 'GDLV');
```

### Task: Create Three Tables for an Employee Management System

#### Employee Personal Table

```sql
-- Create the emp_personal table with primary key
CREATE TABLE emp_personal (
    id INT PRIMARY KEY,
    name VARCHAR(225),
    age INT
);
```

#### Department Table

```sql
-- Create the dept table with foreign key
CREATE TABLE dept (
    dept_no INT,
    emp_id INT,
    name VARCHAR(225),
    FOREIGN KEY (emp_id) REFERENCES emp_personal (id)
);
```

#### Work Table

```sql
-- Create the work table
CREATE TABLE work (
    designation VARCHAR(225),
    eid INT,
    salary INT,
    FOREIGN KEY (eid) REFERENCES emp_personal (id)
);
```
