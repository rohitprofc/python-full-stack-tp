# MySQL <img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original.svg" title="MySQL" alt="MySQL" width="55" height="55"/>

## Database: Organized Collection of Data

## Types of Databases

1. **RDBMS:** Relational Database Management Systems
2. **HDBMS:** Hierarchical Database Management Systems
3. **NDBMS:** Network Database Management Systems
4. **OODBMS:** Object-Oriented Database Management Systems
5. **NoSQL:** Non-Relational Database Management Systems

## Tools for SQL Database Management

| MySQL                                                                                                                                                 | PostgreSQL                                                                                                                                                       | SQLite                                                                                                                                           | MariaDB                                                                                                                                              | Oracle                                                                                                                                           | Access                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original-wordmark.svg" title="MySQL" alt="MySQL" width="55" height="55"/> | <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="PostgreSQL" alt="PostgreSQL" width="55" height="55"/> | <img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original.svg" title="SQLite" alt="SQLite" width="55" height="55"/> | <img src="https://github.com/devicons/devicon/blob/master/icons/mariadb/mariadb-original.svg" title="MariaDB" alt="MariaDB" width="55" height="55"/> | <img src="https://github.com/devicons/devicon/blob/master/icons/oracle/oracle-original.svg" title="Oracle" alt="Oracle" width="55" height="55"/> | <img src="https://res.cloudinary.com/dtdhmbtcg/image/upload/c_crop,w_1600,h_1600/v1721889266/Microsoft-Access-Logo_vy8mol.png" title="Access" alt="Access" width="55" height="55"/> |

## Tools for NoSQL Database Management

| MongoDB                                                                                                                                              | OrientDB                                                                                                                                                        | Redis                                                                                                                                        | CouchDB                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://github.com/devicons/devicon/blob/master/icons/mongodb/mongodb-original.svg" title="MongoDB" alt="MongoDB" width="55" height="55"/> | <img src="https://res.cloudinary.com/dtdhmbtcg/image/upload/v1721890322/orientdb_logo_mid_qwiiof.png" title="OrientDB" alt="OrientDB" width="100" height="55"/> | <img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original.svg" title="Redis" alt="Redis" width="55" height="55"/> | <img src="https://github.com/devicons/devicon/blob/master/icons/couchdb/couchdb-original.svg" title="CouchDB" alt="CouchDB" width="55" height="55"/> |

## Installing MySQL on Windows

### Step 1: Download MySQL Installer

1. Visit the [MySQL Downloads page](https://dev.mysql.com/downloads/installer/).
2. Click on the "Download" button under "MySQL Installer for Windows".
3. Choose the appropriate installer:
   - `mysql-installer-web-community`: Smaller size, downloads only what you need.
   - `mysql-installer-community`: Full version, contains all MySQL products.

### Step 2: Run the MySQL Installer

1. Once the download is complete, run the installer.
2. You may need to grant administrative privileges.

### Step 3: Choose Setup Type

1. In the installer, choose the setup type:
   - **Developer Default**: Includes MySQL Server, MySQL Shell, MySQL Workbench, and connectors.
   - **Server Only**: Only installs the MySQL Server.
   - **Client Only**: Only installs MySQL clients.
   - **Full**: Installs all MySQL products.
   - **Custom**: Allows you to choose specific components.

### Step 4: Install MySQL Products

1. The installer will check for any requirements and download necessary components.
2. Click "Execute" to begin the installation process.
3. Wait for the installation to complete and click "Next".

### Step 5: Configuration

1. **Type and Networking**:

   - Select "Standalone MySQL Server".
   - Click "Next".

2. **Authentication Method**:

   - Choose "Use Strong Password Encryption for Authentication (RECOMMENDED)".
   - Click "Next".

3. **Accounts and Roles**:

   - Set the root password and create any additional user accounts.
   - Click "Next".

4. **Windows Service**:
   - Configure MySQL as a Windows Service.
   - Choose to start the MySQL Server at system startup if desired.
   - Click "Next".

### Step 6: Apply Configuration

1. Click "Execute" to apply the configuration settings.
2. Wait for the configuration to complete and click "Finish".

### Step 7: Complete Installation

1. The installer will display a summary of the installation process.
2. Click "Finish" to complete the installation.

### Step 8: Verify Installation

1. Open the MySQL Command Line Client.
2. Enter the root password you set during installation.
3. Run the following command to check the MySQL version: `SELECT VERSION();`

## MySQL Data Types

### Numeric Data Types

- **TINYINT**: A very small integer.
- **SMALLINT**: A small integer.
- **MEDIUMINT**: A medium-sized integer.
- **INT / INTEGER**: A standard integer.
- **BIGINT**: A large integer.
- **FLOAT**: A small (single-precision) floating-point number.
- **DOUBLE**: A normal-size (double-precision) floating-point number.
- **DECIMAL / NUMERIC**: A fixed-point number.

### Date and Time Data Types

- **DATE**: A date value in 'YYYY-MM-DD' format.
- **DATETIME**: A date and time value in 'YYYY-MM-DD HH:MM:SS' format.
- **TIMESTAMP**: A timestamp value in 'YYYY-MM-DD HH:MM:SS' format, automatically updated when a row is modified.
- **TIME**: A time value in 'HH:MM:SS' format.
- **YEAR**: A year value in either 2-digit or 4-digit format.

### String Data Types

- **CHAR**: A fixed-length string.
- **VARCHAR**: A variable-length string.
- **BINARY**: A fixed-length binary string.
- **VARBINARY**: A variable-length binary string.
- **TINYBLOB**: A very small BLOB (binary large object).
- **BLOB**: A small BLOB.
- **MEDIUMBLOB**: A medium-sized BLOB.
- **LONGBLOB**: A large BLOB.
- **TINYTEXT**: A very small text string.
- **TEXT**: A small text string.
- **MEDIUMTEXT**: A medium-sized text string.
- **LONGTEXT**: A large text string.
- **ENUM**: A string object with a value chosen from a list of permitted values.
- **SET**: A string object with zero or more values chosen from a list of permitted values.

### Spatial Data Types

- **GEOMETRY**: A general class to hold geometry values.
- **POINT**: A single location in coordinate space.
- **LINESTRING**: A curve with linear interpolation between points.
- **POLYGON**: A polygon.
- **MULTIPOINT**: A collection of points.
- **MULTILINESTRING**: A collection of line strings.
- **MULTIPOLYGON**: A collection of polygons.
- **GEOMETRYCOLLECTION**: A collection of geometry objects.

### JSON Data Type

- **JSON**: A JSON document.

## SQL Statements

### DDL: Data Definition Language (Manipulating Database Schema)

- CREATE
- ALTER
- RENAME
- TRUNCATE
- DROP

### DML: Data Manipulation Language (For Manipulating Records in Table)

- SELECT
- INSERT
- UPDATE
- DELETE

### DCL: Data Control Language

- GRANT
- REVOKE

### TCL: Transaction Control Language

- COMMIT
- ROLLBACK
- SAVEPOINT

## Syntax

### Creating Database

    create database dbName;
    show dbName;
    use dbName;

### Show Databases on Hard Disk

    show databases;

### Drop Database

    drop database dbName;

### Creating Table

    create table tableName(columnName1 datatype, columnName2 datatype, columnName3 datatype);

### Table Description

    desc tableName;

### Show Tables in Database

    show tables;

### Altering Table

#### Adding Column to Table

    alter table tableName add columnName datatype;

#### Dropping Column from Table

    alter table tableName drop columnName;

#### Renaming Table

    alter table tableName rename to newTableName;

### Inserting Values into Table

    insert into tableName values(col1Value1, col2Value1);
    insert into tableName values(col1Value2, col2Value2);

### Retrieving All Records from Table

    select * from tableName;
