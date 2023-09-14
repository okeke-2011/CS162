## Data Normalization
Data normalization refers to the degree to which potentially-shared
information is moved into separate tables.

## Questions
### Definitions of normalization
Search the internet and find good definitions and examples of the following:
- First normal form: A database where each cell is single valued, each coloumn entry is of the same type, and all rows are uniquely identified
- Second normal form: For all tables in the database, in addition to all 1NF constraints, all attributes should be dependent on the primary key
- Third normal form: For all tables in the database, in addition to all 2NF constraints, all fields not have transitive dependencies. So in general, it's the process of engineering your data table the right way, so that every value has independence, and your procedural changes don't damage other parts of your data table as you execute them.
- Denormalization: Denormalization is a database optimization technique in which we add redundant data to one or more tables. This can help us avoid costly joins in a relational database. Note that denormalization does not mean not doing normalization. It is an optimization technique that is applied after doing normalization. 
- Composite key: Two or more fields that when combined form a unique identifier (these field can togther be used as a primary key). 

Simple examples given [here]( https://www.essentialsql.com/get-ready-to-learn-sql-database-normalization-explained-in-simple-english/), and [here](https://www.youtube.com/watch?v=UrYLYV7WSHM)
but you might find better resources.

### Road racing association
##### Description
You are contracted out to set up a database for an association of road-runners.
They organize many different races through-out the year. Some of the races get
put into different challenges.  So for example, there could be the following
races:
- The ruby marathon
- The bridge challenge
- The sea to mountain sprint
- Flat and fast marathon
- The wine route stroll

And there could be two challenges:
- **The marathon challenge:**
    - the ruby marathon;
    - the flat and fast marathon.
- **The terrain challenge:**
    - the bridge challenge;
    - the sea to mountain;
    - the ruby marathon.

Notice that not all races belong to a challenge, and some races belong to more
than one challenge.  These challenges repeat every year, but
with subtle differences sometimes (e.g. a new race might be included,
or a particular race is unable to be run that year).

The association needs to be able to keep track of which runners entered
which races, and what their running times were.  A few weeks after the
final race in a particular challenge has been run, the results will get
emailed or posted out.

##### Design
1. Design all the SQL tables you need to capture the above requirements.
2. Write the `CREATE TABLE` statements to implement your design.
3. `INSERT` some example data that you have made up.
4. Write a SQL query to find the top 3 fastest women runners for a given race.
5. Write a SQL query to find all the runners' email addresses that
successfully finished the marathon challenge.

**Bring your design to class and be prepared to explain it**
