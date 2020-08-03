# Influence - The Python Extender You Asked For

With influence you can extend python with things like two-dimensional lists, fractions, string subtractors, etc. You can also upgrade python with things it doesn't have like arrays!

# Overview

The influence python library was created with one sole purpose, helping you do things that can't be done in standard python with ease

  - Extender Library: Sub-package of influence that extends things that are already in python, such as lists, strings, and doing math
  - Upgrader Library: Sub-package of influence that adds things to python that it doesn't have already, like arrays

# Usage

Below is how to install and use the influence library in your own programs!

### Installation

```sh
$ pip install influence
or 
$ python3 -m pip install -U influence
```

The influence package has two package dependencies, numpy and matplotlib (used for grapher and agrapher classes)

### Extender Library

The influence subpackage that extends python's built-in features

##### Cout

Cout (common output) has only one module, printer, that helps print tuples, lists, dicts, etc. nicely

Importing:
```py
from influence.extender.cout import printer
#or
from influence.extender.cout.printer import Printer
```

###### Printer Class

Methods:
```py
Printer.print_list(list) #prints a list nicely
Printer.print_tuple(tuple) #prints a tuple nicely
Printer.print_dictionary(dict) #prints a dict nicely
Printer.print_all(ender, *items) 
#prints all of items, if ender is False, prints each item on new line
#else all items are printed on the same line
```

##### Cin

Cin (common input), has one module, input, that handles input specifically

Importing:
```py
from influence.extender.cin import input
#or 
from influence.extender.cin.input import Input
```

###### Input Class

Methods:
```py
value = Input.input(t, prompt=None)
#stores input into value
#prompt will be printed, defaults to None
#raises ValueError if input does not match type t
#raises TypeError if t not able to be casted from input
```

##### List

List extends python's built-in lists by adding multidimensional lists and other list extenders

###### List2D Class

Creates a 2D list of a square size

Importing:
```py
from influence.extender.list import multilist
#or
from influence.extender.list.multilist import List2D
```

Initializing:
```py
l = List2D(rows=1, cols=1) 
#creates the list to have rows number of rows and cols number of cols
```

Methods:
```py
l[r_index][c_index] = item
#sets value at r_index and c_index to item
#raises IndexError if index out of bounds
l[r_index].append(item)
#since this is a list, if you wish to append the list
#you can do it this way instead of settings
l[r_index][c_index]
#returns value at r_index and c_index
#raises IndexError if index out of bounds
l.print()
#prints the list
l.remove(r_index, c_index)
#removes the value at r_index and c_index
#returns true if removed, false if index out of bounds
item in l
#returns true if item in l, false otherwise
l.index(item)
#returns indices of item if found in list
#returns [-1] otherwise
l.__len__() / len(l)
#returns the length of l
l.__str__() / str(l)
#returns l as a str
l.__delitem__(key) / del l[key]
#deletes row key from l
#raises IndexError if key out of bounds
```

###### RaggedList Class

Creates a 2D list, but doesn't need to be of n x n size, inherits from List2D, and therefore has a dependency to influence.extender.list.multilist

Importing:
```py
from influence.extender.list import ragged
#or
from influence.extender.list.ragged import RaggedList
```

Initializing:
```py
r = RaggedList(rows=1, cols=1)
#creates a ragged list starting with rows rows and cols cols
#defaults to one for both if no arguments are given
```

Methods:
```py
r.print()
#prints the ragged list
r.in_bounds(r_index, c_index)
#returns true if r_index and c_index are in bounds of the list
#returns false otherwise
r.set(r_index, c_index, item)
#sets value at r_index and c_index to item if in bounds
#else extends the ragged list so r_index and c_index are in bounds
r.get(r_index, c_index)
#returns value at r_index and c_index if in bounds
#else returns None
item in r
#returns true if item is in r, else returns false
r.index(item)
#returns the indices of item if in r
#else returns [-1]
r.__len__() / len(r)
#returns the length of r
```

###### AsList Class

Used to turn strings into lists, duplicate class found in string subpackage

Importing:
```py
from influence.extender.list import aslist
#or
from influence.extneder.list.aslist import AsList
```

Methods:
```py
AsList.character_list(string)
#returns string as a list of characters
AsList.word_list(string)
#returns string as a list with each word
#a word is found when a space is reached in the string
#spaces are not included in the list
AsList.word_list_with_spaces(string)
#same as AsList.word_list(string) except spaces are part of the list
```

##### String

Allows for a couple new things to be done with strings

###### AsList Class

Used to turn strings into lists, duplicate class found in list subpackage

Importing:
```py
from influence.extender.string import aslist
#or
from influence.extneder.string.aslist import AsList
```

Methods:
```py
AsList.character_list(string)
#returns string as a list of characters
AsList.word_list(string)
#returns string as a list with each word
#a word is found when a space is reached in the string
#spaces are not included in the list
AsList.word_list_with_spaces(string)
#same as AsList.word_list(string) except spaces are part of the list
```

###### Subtract Class

Allows for subtracting of strings, but does not change the input string, instead returns a new string

Importing:
```py
from influence.extender.string import subtract
#or
from influence.extender.string.subtract import Subtract
```

Methods:
```py
Subtract.subtract(initial, remove)
#removes the first instance of remove from initial
#returns a new string
#remove can be multiple letters, but must be a string
Subtract.subtract_all(initial, remove)
#removes all instances of remove from initial
#returns a new string
#remove can be multiple letters, but must be a string
```

##### Math

#Const Class

Gives the user access to constants in math

Importing:
```py
from influence.extender.math import const
#or
from influence.extender.math.const import MathConstants
```

Fields:
```py
MathConstants.pi #returns the value of pi
MathConstants.e #returns the value of e
MathConstants.tau #returns the value of tau
MathConstants.phi #returns the value of phi
```

###### Stats Class

Allows for statistics with int or float datasets

Importing:
```py
from influence.extender.math import stats
#or
from influence.extender.math.stats import Stats
```

Methods:
```py
Stats.min(dataset)
#returns the lowest value in dataset
Stats.max(dataset)
#returns the highest value in dataset
Stats.range(dataset)
#returns the range of the dataset (max - min)
Stats.mean(dataset)
#returns the mean of the dataset
Stats.variance(dataset)
#returns the variance of the dataset
Stats.standard_deviation(dataset)
#returns the standard deviation of the dataset
Stats.median(dataset)
#returns the median of the dataset
Stats.mode(dataset)
#returns the mode of the dataset as a list
```

###### Cos Class

Does permutations and combinations equations, inherits from Stats, and therefore has a dependency to influence.extender.math.stats

Importing:
```py
from influence.extender.math import cos
#or
from influence.extender.math.cos import Combinatorics
```

Methods:
```py
Combinatorics.factorial(num)
#returns the factorial of num
Combinatorics.P(n, r)
#returns the permutations equation (n! / (n-r)!)
Combinatorics.C(n, r)
#returns the combinations equation (n! / [(n-r)! * r!])
```

###### Frac Class

Represents a fraction

Importing:
```py
from influence.extender.math import frac
#or
from influence.extender.math.frac import Fraction
```

Initializing:
```py
f = Fraction(num, denom)
#initializes a fraction to numerator num and denominator denom
```

Methods:
```py
f.simplify()
#simplifies this fraction, if possible
f.__float__() / float(f)
#returns the float value of the fraction
f.__int__() / int(f)
#returns the int value of the fractions
f.__str__() / str(f)
#returns the fraction as a string
f.to_mixed_number(self)
#returns f as a mixed number
```

Compare:
```py
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
#fraction allows for
f1 < f2
f1 <= f2
f1 == f2
f1 > f2
f1 >= f2
```

###### MixedNum Class

Represents a mixed number

Importing:
```py
from influence.extender.math import mixednum
#or
from influence.extender.math.mixednum import MixedNumber
```

Initializing:
```py
m = MixedNumber(coeff, num, denom)
#creates a mixed number with a coefficient coeff, numerator num
#and denominator denom
```

Methods:
```py
m.simplify()
#simplifies this mixed number, if possible
m.__float__() / float(m)
#returns the float value of the mixed number
m.__int__() / int(m)
#returns the int value of the mixed number
m.__str__() / str(m)
#returns the mixed number as a str
m.to_fraction()
#returns the mixed number as a new improper fraction
```

Compare:
```py
m1 = MixedNumber(1, 2, 3)
m2 = MixedNumber(4, 5, 6)
#fraction allows for
m1 < m2
m1 <= m2
m1 == m2
m1 > m2
m1 >= m2
```

###### Grapher Subpackage

Allows for graphing equations

Importing:
```py
from influence.extender.math.grapher.grapher import Equation
from influence.extender.math.grapher.grapher import GraphingError
from influence.extender.math.grapher.grapher import Grapher
```

Equation Class:

Represents an equation

Initializing:
```py
e = Equation(eq)
#eq cannot be inferred
#ie 4x+3 needs to be 4*x+3
#ie 4x^2+2 needs to be 4*(x**2)+3
```

GraphingError Class:

GraphingError.HostileAttackError is thrown when a hostile attack is detected with eval
GraphingError.InstanceError is thrown when graphing, the parameter is not an instance of Equation

Grapher Class:

```py
Grapher.graph(eq)
#graphs eq, if and only if isinstance(eq, Equation) returns True
```

###### Agrapher Subpackage

Asynchronous graphing is currently a WIP but are still able to be used

Importing:
```py
from influence.extender.math.agrapher.asyncgrapher import Equation
from influence.extender.math.agrapher.asyncgrapher import GraphingError
from influence.extender.math.agrapher.asyncgrapher import Grapher
```

Agrapher works in the same exact way except Grapher.graph(eq, timetoclose=None), can have a given timeout

### Upgrader Library

##### Array

Creates an array
An array is like a list, except it has a definite, unchangeable size, but elements can be changed inside of it (unlike a tuple)

###### Array Class

Makes an array

Importing:
```py
from influence.upgrader.array import arrays
#or
from influence.upgrader.array.arrays import Array
```

Initializing:
```py
arr = Array(capacity)
#initializes the array to its definite length 
```

Methods:
```py
arr[index]
#gets the value at index
arr[start:stop:step]
#returns a list from an array from a slice of start, stop, and step
#raises IndexError if index out of bounds
arr[index] = item
#sets the value at index to item
#raises IndexError if index out of bounds
arr.__iter__() / iter(arr)
#returns an iterator for the array
iterator.__next__() / next(iterator)
#gets the next element from the iterator
arr.print()
#prints the array
item in arr
#returns true if item is in arr, false otherwise
arr.index(item)
#returns the index of item if in arr
#returns -1 if not found
arr.__len__() / len(arr)
#returns the length of arr
not arr
#returns True if arr has a capacity of 0
arr.__str__() / str(arr)
#returns arr as a str
arr1 + arr2
arr1 += arr2
#adds the arrays together
```

###### Array2D Class

Creates a 2D Array, inherits from Array, and therefore has a dependency to influence.upgrader.array.arrays

Importing:
```py
from influence.upgrader.array import multiarray
#or
from influence.upgrader.array.multiarray import Array2D
```

Initializing:
```py
arr = Array2D(r, c)
#creates a 2D array to a fixed amount of rows (r) and columns (c)
```

Methods:
```py
arr[r_index][c_index]
#returns the value at r_index and c_index
#raises IndexError if index out of bounds
arr[r_index][c_index] = item
#sets value at r_index and c_index to item
#raises IndexError if index out of bounds
arr.print()
#prints the 2D array
item in arr
#returns true if item is in arr, false otherwise
arr.index(item)
#returns the indices of item in arr, if found
#returns [-1] otherwise
arr.__len__() / len(arr)
#returns length of arr
```

##### String

Package that extends on strings in python

###### StringBuffer Class

Makes strings mutable, like in java

Importing:
```py
from influence.upgrader.string import stringbuffer
#or
from influence.upgrader.string.stringbuffer import StringBuffer
```

Initializing:
```py
s = StringBuffer(str='')
#initializes a string buffer to str, empty if none entered
```

Methods:
```py
s.__len__() / len(s)
#returns the length of s
obj in s
#returns true if obj is in s, false otherwise
s.__iter__() / iter(s)
#returns an iterator for s
s.__next__() / next(s)
#gets next letter in s
s.__str__() / str(s)
#gets s as a normal string
s[index]
#gets letter at index
s[start:stop:step]
#gets letters starting at start, up to but discluding stop, incrementing by step
s[index] = item
#sets letter at index to item
s.append(append)
#appends append to s
s.index(obj)
#returns the index of obj in s
s.insert(index, obj)
#inserts obj at index
s.replace(start, stop, obj)
#replaces the chars from stop to stop (discluding stop) with obj
del s[index]
#deletes the char at index
s1 + s2
s1 += s2
#adds stringbuffers together
```

# License

MIT License

Copyright (c) 2020 RandomKiddo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.