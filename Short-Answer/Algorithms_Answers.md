#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I


```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
I think this is O(n) as it grows exponentionally as per line 8  / line 9

```
b)  sum = 0
    for i in range(n):     On
      j = 1
      while j < n:    1/2N ? 
        j *= 2
        sum += 1
```

This seems like O(nlogn) as this is the larger code in line 15.  I'm thinking the while loop wouldn't affect it. 


O(nlogn)
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)   On? 
```
This is probably O(n). 

## Exercise II


Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Building is pre-sorted
1  ok 
2  ok 
3 f get broken
4 get broken
5 get broken
6 get broken 

Need to find the middle point,  so a binary search would work (Ologn)