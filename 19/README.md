## Unit testing
Unit testing is a great approach to minimizing bugs in your code.

There is an approach called Test Driven Development (TDD) which takes this to
the extreme.  Here you write tests beforehand which describe the expected
behavior of your code.


## Questions
### The prime bug report
As the author of a popular library called [`prime.py`](prime.py) you
occasionally receive bug reports from users who are using your library in their
application. The latest bug report was filed by someone using [`application.py`](application.py).

1. Run `application.py` and reproduce the error (it should be a math domain error).
2. Examine their code and find the bug.  
3. Now fix your library such that the library code handles this case in the most appropriate way
4. Write one (or more) unit tests to ensure that the bugs that you have fixed
are not reintroduced.
5. Bring your suggested fix to class ready to discuss it.

### More defensive testing
Another useful tool in TDD is the notion of code coverage.  

1. Install coverage with `pip3 install coverage`
2. Run the coverage tool on [`tests.py`](tests.py), and generate the html report.
(This can be done using the commands `coverage run tests.py` then `coverage report` and `coverage html`)
3. Using the coverage report, write more tests so that you achieve 100% code
  coverage of the `is_prime()` and `get_next_prime()`.
4. In the process of achieving 100% coverage, did you identify any new bugs?
  You may test with a smaller list of primes found 
  [here](https://primes.utm.edu/lists/small/10000.txt).
5. Bring your code to class ready to discuss it.  Be sure to remember which
tests you added from the coverage tool and which tests were introduced from the
original bug report.

### Probabilistic Primes
In practice the deterministic tests for prime number are too slow.  So as good
engineers, we have decided to trade correctness for speed.  The latest
(untested) feature is the `miller_rabin()` primal test.

- Add a few tests to achieve an acceptable level of coverage.
- How does Miller-Rabin compare with the old library in terms of speed?
  (Try run it on some really big numbers!)
- What is the probability of error? Is this a level of error you're comfortable with?
- Which would you prefer to use for a *very* important cryptographic
purpose?
- How do you test a library that is probabilistic in nature?

### Class project
For your class project write at least 5 unit tests which test the functionality
that you expect to have in any part of the system.  Since these tests will help
you ensure a working project it is in your own interests not to duplicate tests
already written by other students.  So you are encouraged here to collaborate
and maximize your expected coverage. (In some situations there might be limited
scope for unit tests, so there is no penalty for writing duplicate tests.)

Notice that you don't need to have written any functionality for the class
project, in order to start writing the unit tests.  Remember to run the tests
when you do start implementing the functionality.  Seeing a gradual increase in
the number of tests passing can be very motivating!

Bring your unit tests to class and be ready to discuss them.
- Test that a user must be logged in to post their profile to the main page
- Test that when a profile is clicked we are redirected to the correct profile's full detail page
- Test that when a user edits their info it edits on all parts of the website
- Test that logout works properly 
- Test that login in only happens once until log out

### (Optional) Optimization of prime library

In the library there have been several attempts at optimization.  For example
the get_next_prime function tests whether the initial x is even and increments
x if it is.  This allows us to only test the odd numbers (we know that an even
number is not prime).

Time the code with and without the optimizations.  Which optimizations give
noticeable speed improvements?  Rewrite `prime.py` using only optimizations that
work. Keep the new code as simple as possible.   Which code would you rather
maintain?
