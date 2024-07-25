# SQL Joins

## Creating Tables

```sql
-- Create the orders table
CREATE TABLE orders (
    OID INT,
    CID INT,
    ORDERNAME VARCHAR(225),
    PRICE INT
);

-- Create the customer table
CREATE TABLE customer (
    CID INT,
    NAME VARCHAR(225),
    SALARY INT,
    LOCATION VARCHAR(225),
    DOJ DATE
);
```

## Inner Join

```sql
-- Select data from orders and customer using an inner join
SELECT 
    customer.CID,
    customer.NAME,
    customer.LOCATION,
    orders.ORDERNAME,
    orders.PRICE
FROM 
    orders
INNER JOIN 
    customer 
ON 
    customer.CID = orders.CID;
```

## Right Join

```sql
-- Select data from orders and customer using a right join
SELECT 
    customer.CID,
    customer.NAME,
    customer.LOCATION,
    orders.ORDERNAME,
    orders.PRICE
FROM 
    orders
RIGHT JOIN 
    customer 
ON 
    customer.CID = orders.CID;
```

## Subqueries

```sql
-- Select names and salaries from emp_details where the SALARY is greater than the SALARY of 'Rohit'
SELECT 
    NAME, 
    SALARY 
FROM 
    emp_details 
WHERE 
    SALARY > (SELECT SALARY FROM emp_details WHERE NAME = 'Rohit');

-- Select names and department numbers from emp_details where the department number matches 'Rohit's department number
SELECT 
    NAME, 
    dept_no 
FROM 
    emp_details 
WHERE 
    dept_no = (SELECT dept_no FROM emp_details WHERE NAME = 'Rohit');

-- Select all records from emp_details where the job matches 'Rushi's job
SELECT 
    * 
FROM 
    emp_details 
WHERE 
    job = (SELECT job FROM emp_details WHERE NAME = 'Rushi');
```

## Importing SQL to Excel

### Checking Secure File Privilege

```sql
-- Show the secure file privilege path
SHOW VARIABLES LIKE 'secure_file_priv';
```

Output:
```
+------------------+------------------------------------------------+
| Variable_name    | Value                                          |
+------------------+------------------------------------------------+
| secure_file_priv | C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\ |
+------------------+------------------------------------------------+
```

### Exporting Data to CSV

```sql
-- Select data from emp_details and export to a CSV file
SELECT 
    * 
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\demo.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
FROM 
    emp_details;
```

## Importing Excel to SQL

### Creating Table in SQL

```sql
-- Create a sample table in SQL
CREATE TABLE SAMPLE (
    ID INT,
    NAME VARCHAR(22),
    JOB VARCHAR(22),
    SALARY INT
);
```

### Loading Data from Excel

```sql
-- Load data from an Excel file into the sample table
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\demo1.xlsx'
INTO TABLE SAMPLE
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';
```

## Connecting MySQL with VSCode

### Install MySQL Connector

```sh
pip install mysql-connector-python
```

### Sample Code to Connect and Fetch Data

```python
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=""
)

# Create a cursor object
mycursor = conn.cursor()

# Print connection success message
print("Connection successful")

# Execute SQL queries
mycursor.execute("SHOW DATABASES")
mycursor.execute("USE joins")
mycursor.execute("SHOW TABLES")
mycursor.execute("SELECT * FROM orders")

# Fetch and print the results
for i in mycursor:
    print(i)
```
