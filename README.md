## Unit Testing Assignment

by Bill Gates and Jade


## Test Cases for unique


| Test case              |  Expected Result    |
|:---|:---|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| input not a list  |  raise TypeError       |
| boolean in list  |  return that boolean as normal value


## Test Cases for Fraction


| Test case             |  Expected Result    |
| :--- |:---|
| init method            |  initial fraction   |
| str method             |  shows fraction in the string form |
| add method             | the sum of two fractions as a new fraction. |
| sub method             | the minus result of two fractions as a new fraction. |
| mul method             | the multiplication of two fractions as a new fraction. |
| eq method              | check two function if there are equal or not. |
| gcd method             | the Greatest Common Divisor of numerator and denominator. |
| check 0/0              | check if user input 0/0 it'll output as 0/0 not an error. |