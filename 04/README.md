# Session 2.2

> In this pre class work, you will be performing two tasks: 
> 
> 1. Add a new language support into a existing game (see part 3) 
> 2. Implement random number generators (see part 4)
> 
> Be sure you read through the prompt carefully and understand the expected outcome.
### 1. Get started
To set up a suitable [environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) for this session's code:

**Windows**
```bash
$ set PYTHONENCODING='utf-8 python3 blackjack.py'
```
**MacOS**
```bash
$ export PYTHONENCODING='utf-8 python3 blackjack.py'
```
For Windows (python3 -> python, from here on out):
```bash
$ python blackjack.py
```
And you should be able to play a simplified form of blackjack.

### 2. Read `blackjack.py` and identify its structure

The exercise for today's seminar is to refactor this program into a well-designed, object-oriented program. Labeling a program as object-oriented does not make it inherently good, and what follows is a short justification of why we should care about good design and object-orientation.

For this course, we will define a program to be well designed if:
>There are many potential features that could be added to the program, and each feature only requires a small number of locations to edited.

This is arguably *the* key aspect of good design.  It is the only requirement that allows a project to grow in scale and complexity.  If you have a project of millions of lines of code (e.g. the linux kernel, a modern web-browser) then good design is essential.  Consider a large project that is badly designed (ie. adding a single feature usually affects the entire codebase) then progress will necessarily be very slow.  Not only will an engineer need to understand millions of lines of code, but they will also need to synchronously make changes in many locations (to avoid introducing bugs).  This bad project also has the side effect that whenever one new feature is rolled out by another team then it will most likely affect the progress of all other teams ("stepping on each other's toes").

The thing that can save us is the notion of abstraction.  We can break down a large project into many small subsystems.  Each subsystem can hide the complexity of the implementation from other subsystems. This decouples what a subsystem does from how it does it.  

This notion of good design doesn't necessarily lead us into object-oriented principles, and there have been other interesting approaches (eg. google functional programming techniques).  However historically object-orientation has been the most successful and scaled to the largest projects.

Phew! That was quite a long aside.  Let's get back to today's task of getting a better codebase for our little Blackjack project.  This is a poorly designed project because all sorts of things are done all over the place.

### 3. Add support for another language

Run the following code in bash:
```bash
$ LANG=zh_CN python3 blackjack.py
```
And the blackjack program is in Chinese.

Minerva is a very multicultural institution with many different languages being spoken.  While we use English in the classroom, we certainly should accommodate non-native speakers if they want to play blackjack in their leisure time and in their native language. The best way to do this is to abstract way how a particular point in the game is presented to the user.

A bad implementation will require a single global variable called language and have code littered with if statements like (please excuse my google translate):

```python
if LANGUAGE == 'en':
    print('You have gone bust!')
elif LANGUAGE == 'de':
    print('Du bist Pleite gegangen!')
elif LANGUAGE == 'es':
    print('¡Te has vuelto loco!')
```

External Web resources could be found [here](https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/).

Complete the following steps to add support for your language:
1. Locate the position for pygettext.py and msgfmt.py. For Mac, they are located in your Python3 folder, in examples/Tools/i18n/; For Windows, they are in \Tools\i18n.

    <details>
    <summary>How to find File Location on <b>Mac</b> (click to expand)</summary>

    You can do this in either way below:

    (1) Using the following command to find python3 folder location:
      
      ```bash
      $ which python3
      ```

    (2) Use GUI tricks: Drag the finder file to your terminal, then copy paste the path 
    ![file-location-trick-for-mac](https://media.giphy.com/media/Ud3ljJftswha4M6a7C/giphy.gif)

    </details>
    For Windows

    ```bash
    where python
    ```

2. You have to make sure you are in the right working directory for session_04 (..\cs162\session_04):
- For a guide on changing directories (Windows) refer to here: https://www.howtogeek.com/659411/how-to-change-directories-in-command-prompt-on-windows-10/ 
- For mac here: https://www.macworld.com/article/221277/command-line-navigating-files-folders-mac-terminal.html
- On windows, you must use the command prompt as an administrator: https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/ 


3. Create a symbolic link to pygettext.py file
- For windows run the following command:
```bash
> mklink pygettext.py "C:\<PATH TO PYTHON>\Python38\Tools\i18n\pygettext.py"
```
- For mac run the following command:
```bash
> sudo ln -s "<PATH TO SESSION 4>/cs162/session_04" "<PATH TO PYTHON3>/examples/Tools/i18n/pygettext.py"
```
If all goes well, you should be able to see the pygettext.py file in session_04.
To read more about symbolic links see here (you will likely work with them in future): https://www.howtogeek.com/howto/16226/complete-guide-to-symbolic-links-symlinks-on-windows-or-linux/

4. Run the following command: (pygettext.py should be in the same folder)
```bash
> pygettext.py -d blackjack blackjack.py
```


5. This will generate a .pot file. Download PoEdit here: https://poedit.net/download
- Open your new .pot file from ...Tools\i18n\blackjack.pot
- Choose the new language you want to use. Standardized Script-Language codes are here: https://www.softaculous.com/docs/admin/scripts-language-codes/ 
- You can either translate by manually typing into "translation" or use their auto-generated translations on right panel

6. In pcw directory (under session_04\locale) create a new folder: <YOUR_LANGUAGE_CODE>\LC_MESSAGES

7. Save translation in PoEdit to this new sub-sub directory as "blackjack"
- PoEdit will handle the extensions
- This will create a .mo and .po file. Whatever you do DO NOT EDIT THEM DIRECTLY
- You can also just save as is, and then manually change the name of the .mo file to "blackjack.mo"
- Your sub-directories should be formatted exactly the same as for zh_CN\LC_MESSAGES

8. In Bash terminal run:

Windows:
```bash
$ LANG=<your_new_language_code> python blackjack.py
```
Mac:
```bash
$ LANG=<your_new_language_code> python3 blackjack.py
```

9. The Blackjack game should now run in the new language you have chosen. Repeat for as many languages as desired!

Think about the following question:
1. Did you write any code?
2. Did the translation process require any knowledge about programming?
3. Why this is a good implementation of abstraction?

### 4. Refactor a better random number generator

Before walking into this session, look through both class Card & CardDeck. Here's the original version of card representation:

```python
def get_deck():
    '''Return a list of the all 52 playing cards.
    This list is sorted and always in the same order.
    '''
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    rank = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    cards = list(itertools.product(rank, ['of'], suits))
    return [" ".join(l) for l in cards]
```

Think about the following question:
1. Which of them suit abstraction better?
2. If we want to support a new poker game, e.g. 24 points, which one provides a better basic structure for additional features?

In a real project, we would (and should) use the facilities provided by python in the `random` module. However, this will give you the opportunity to design a simple class and see how the refactored code is (hopefully) simpler and better separated.

The current implementation of random function within blackjack is badly designed. Think about whether there are any leaks in the current version of implementation, and whether it satisfies the concept of abstraction.

Also, it turns out that [RANDU](https://en.wikipedia.org/wiki/RANDU) is actually a bad random number generator (and RANDU was used by many real scientific computing centers for over a decade).  A better choice is to use a lagged fibonacci generator (which is what is actually used in the `random` module).

There is some example code for you to use in the file `mersenne.py` (this python code is adapted from [here](http://code.activestate.com/recipes/578056-mersenne-twister/)).

Identify the following:
1. The current implementation refers to the data for the random number generator in many lines. Identify each line of code where this happens.
2. If we are using a random number generator, what functionality do we actually care about?

Program the following:
1. Build a random number generator function based on the RANDU implementation code with minimal comments
2. Build a random number generator function based on the Mersenne twister code with minimal comments
3. Refactor your blackjack code. Create a new random number generator class that can switch easily switch between either number-generating function
4. Implement this class throughout code

_HINT 1_: Since the goal is to swap between two random classes easily, this is what we want to have from blackjack code:

```python
from random import Mersenne, RANDU
rand = RANDU(seed)

class CardDeck():
  ...
  def pop_rand(self):
    ind = rand.sample()
```
From this code, we can change the random method by changing initiation of ```rand``` to ```rand = Mersenne(seed)```. How can you design ```Mersenne``` class and ```RANDU``` class to achieve our goal?

_HINT 2_: Example for ```Mersenne``` class and ```RANDU``` class implementation

```python
# Class design
class Mersenne:
  def __init__(self, seed=None):
    if seed is None:
      self.seed = ...
    else:
      self.seed = seed
    self._initalize()
  def _initalize(self):
    ...
  def _generate_numbers(self)
    ...
  def sample(self):
    ...

class RANDU:
  def __init__(self, seed=None, c=65539, m=2147483648):
    self.c = c
    self.m = m
    if seed is None:
      ...
    else:
      ...
  def sample(self):
    ...
```

### 5. (Optional) Implement more Blackjack rules

Find out what the full set of rules are for blackjack.  There are many subtleties that have been left out of the current implementation.  Find one such subtlety and implement it in the refactored codebase.  If you have done a good job of design then adding a new rule should affect a small number of locations in the codebase.  Think about how it would have been implemented in the old design, and whether this is an improvement or not.
