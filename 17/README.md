## SQL indices

A SQL index allows us to keep track of the rows in a table sorted by a particular
column.  In nearly all cases this dramatically speeds up SQL queries!

### Finding a row

```sqlite3
SELECT * FROM table1 WHERE IDNumber = 87987987;
```
If there is no index on IDNumber, then this query will get expanded into
something like the following pseudocode:
```python3
for row in table1:
    if row.IDNumber == 87987987:
        print(row)
```
If there are roughly *M* rows in table1, then this will require work roughly
proportional to *O(M)*.  On the other hand if a index is created then it is
possible to do a tree traversal on the index to find the correct location.
If the rows are unique, then the tree traversal will be *O(logM)* work.  For
a large table, this is a huge difference in efficiency.

### Joining a table
Joins on un-indexed columns are essentially implemented as nested for loops.
For example, the query:
```sqlite3
SELECT * FROM table1 INNER JOIN ON table2 WHERE table1.data1 = table2.data2;
```
will get expanded into something like the following pseudocode:
```python3
for row1 in table1:
    for row2 in table2:
        if row1['data1'] == row2['data2']:
            print((row1, row2))
```
If table1 has *M* rows and table2 has *N* rows, then the database will need to
do work roughly proportional to *O(MN)*.

## Questions

### Large un-indexed tables
In `random.sql` there is a slow query which joins three un-indexed tables
together.  Since this is a nested for loop and the tables are roughly the
same size then it will take *O(N^3)* time.

1. Now figure out how to index the table(s) such that the query is able to run
much faster.  
```sqlite3
CREATE INDEX Idx1 ON TEST1(x,y);
CREATE INDEX Idx2 ON TEST2(x);
CREATE INDEX Idx3 ON TEST3(y);
SELECT COUNT(*) FROM TEST1 t1
    JOIN TEST2 t2 ON (t1.x) = (t2.x)
    JOIN TEST3 t3 ON (t1.y) = (t3.y)
    WHERE t3.z > t1.z;
```
2. Quantify the time taken for each version with the `.timer` command.
```
Run Time: real 0.003 user 0.002379 sys 0.000033
```
3. Write pseudo code explaining how the fast query is now being implemented.
- For each value in row in TEST1 get the value for column x
- Binary search Idx2 using this value to get the corresponding row in TEST2
- Concatenate the rows 
- Same procedure using the newly generated rows, column y, and TEST3
4. Give your estimate of the asymptotic scaling behavior in big-Oh notation
for the fast query.
- O(NlogN\*klogN)
5. Give the asymptotic scaling behavior for creating an index.
- O(NlogN)

(Note that SQLite's query planner is smart enough to create temporary indices
in this case, and it's still faster than the naive scan.  We have to
explicitly turn off the automatic indexing to better understand what's going
on.)

### Query optimization and indices

Some SQL commands can run much faster if the order of constraints is changed.
For example, consider:
```sqlite3
SELECT Name, Phone FROM Customer WHERE Gender = 'f' AND ZipCode = '90210';
```
It would be inefficient to efficiently find all female customers, and then
scan through all zip codes.  Instead it is better to find all customers in the
given zip code and then select the women.  

1. Give pseudo-code for the case that there are no indexes.
- Loop over all rows
- If the gender and zip code match, output the name and phone of that row
- If not skip the row
2. Give pseudo-code for the case that there is an index on Gender.  Roughly how
much more efficient is this than without any indices? (Assuming that your
customers are evenly split between men and women.)
- Less than twice efficient 
3. Give pseudo-code for the case that there is an index on ZipCode.  Assuming
that there are roughly 10,000 different zip codes for your customers, how
much more efficient is this than without any indices?
- (N/10000)\*log_2(10000)
4. Find out about composite indices.  What would a good composite index look
like in this case?  Write pseudo-code for this case.
```sqlite3
CREATE INDEX Idx1 ON Customer(ZipCode, Gender);
```
5. Find out what a covering index is.  What would it look like in this case?
Is a covering index more or less efficient than a composite index, and why?
```sqlite3
CREATE INDEX Idx1 ON Customer(ZipCode, Gender, Name, Phone);
```
It is more efficient. We don't have to do an extra binary search on the actual table. 
