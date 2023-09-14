## Inheritance vs Composition
## Questions:

### 1. Identity Access Management - IAM
I coded the answer to this question in the Forum IAM.ipynb file

### 2. Bug or feature?
Notice that a tomato can now also appear inside a fruit salad without any
errors.  Is this a bug or a feature?  Make arguments for both sides.

It makes sense that an object can be hybrid (having attributes of both classes), provided none of the inherited attributes clash. If an object can only be one color and fruits must be blue, while vegetables must be red, it makes no sense that an object can be both colors. Hence, I think it is only a bug if there are attribute conflicts that are unresolvable. 


### 3. Liskov Substitution principle
 At the REPL, typing `type(x)` will show what type of variable `x` is, while `dir(x)` will reveal all the methods that x has.

 Work through the simple types (e.g. list, int, float, string) and find out whether it is possible to call the following code with an instance of that type.  Is it possible to find an instance that works, while another instance (of the same type) fails?  

```python3
def liskov_substitution_principle(x):
    x = x % x
    x = x * 2
    print(x)
```
 Is this a violation of the Liskov substitution principle? Why or why not?
 
 For all of those data types and for all instances of them, the second comamnd should work. 
 
 The first command doesn't work at all for strings and lists. However, all instances of ints and floats will work (they allways give 0 as an answer. The only exception is if x == 0 or 0.0. 
 
 I don't think this is a violation of Liskov substitution. All ints and floats are initialized as 0 and 0.0 respectively. Being able to carry out the x % x operation is an added functionality to the based description of the class. 

 [Helpful reading](https://docs.python.org/3.5/library/operator.html)

### 4. (Optional) Multiple inheritance bug
There is a subtle bug in the initialization of a tomato.  Identify the bug,
and then fix the bug!
