# Insert. Update. Delete.

## Inserting Values into Specific Columns (Adding NULL Values to Other Columns)

```sql
INSERT INTO tableName (col1, col2, col3) VALUES (val1, val2, val3);
```

## Updating One Value in a Record

```sql
UPDATE tableName SET columnName = value WHERE columnName = value;
```

## Updating Entire Record

```sql
UPDATE tableName SET columnName1 = value1, columnName2 = value2, ... WHERE columnName = value;
```

## Deleting a Record

```sql
DELETE FROM tableName WHERE columnName = value;
```

## Comparison Operator

```sql
SELECT * FROM tableName WHERE columnName > value;
```

## Logical AND Operator

```sql
SELECT * FROM tableName WHERE columnName1 > value1 AND columnName2 > value2;
```

## Logical OR Operator

```sql
SELECT * FROM tableName WHERE columnName1 > value1 OR columnName2 > value2;
```

## Membership Operator (IN)

```sql
SELECT * FROM tableName WHERE columnName IN ('software', 'data analyst');
```

## NOT IN

```sql
SELECT * FROM tableName WHERE columnName NOT IN (val1, val2);
```

## BETWEEN

```sql
SELECT * FROM tableName WHERE columnName BETWEEN val1 AND val2;
```

## LIKE

### Using %: Holds Multiple Characters

```sql
-- Select all records where the name starts with 's'
SELECT * FROM tableName WHERE name LIKE 's%';

-- Select all records where the name contains 'um'
SELECT * FROM tableName WHERE name LIKE '%um%';

-- Select all records where the name ends with 'c'
SELECT * FROM tableName WHERE name LIKE '%c';
```

### Using \_: Holds a Single Character

```sql
-- Select all records where the second character of the name is 'u'
SELECT * FROM tableName WHERE name LIKE '_u%';

-- Select all records where the name contains at least one 's'
SELECT * FROM tableName WHERE name LIKE '%s%s%';

-- Select all records where the name contains consecutive 'e's
SELECT * FROM tableName WHERE name LIKE '%ee%';
```

**Escape Characters**

### Updating a Value with an Underscore

```sql
UPDATE tableName SET columnName = 'c_ess' WHERE columnName = 'chess';
```

### Selecting with an Escape Character

To use the `ESCAPE` clause correctly, ensure that the escape character is defined and used properly within the pattern. If you want to treat `_` as a literal underscore character, the query should look like this:

```sql
SELECT * FROM tableName WHERE columnName LIKE '%?_?%' ESCAPE '?'; 
-- Use ? to convert operator into character
```

## IS

```sql
SELECT * FROM tableName WHERE columnName IS NULL;
SELECT * FROM tableName WHERE columnName IS NOT NULL;
```

## ORDER BY

```sql
SELECT * FROM tableName ORDER BY columnName; 
-- By default ascending order, or you can use ASC

SELECT * FROM tableName ORDER BY columnName DESC;
-- Now it goes descending order
```
