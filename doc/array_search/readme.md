# Example Array search in python

Test Platform : Intel DevCloud (s001-n141)

Time complexity : Linear time complexity O(n)

Comment: Execution time grows as the size of input grows

```python3
"""
##########################################
# Array search
# Complexity : O(n)
##########################################
"""
import numpy as np
import time

def find_solution(a):
    index = np.where(a%2 == 0)
    print(index)

def linear_search(a):
    check = a % 2
    for i in range (len(check)):
        if check[i] == 0:
            print(i)

def main():
    a = np.array([1,2,3,4,5,6,7,8,9,10])
    find_solution(a)
    linear_search(a)
    
if __name__ = "__main__":
    main()
```




Possible optimization - search algorithm for equilibrium solution check

np.where vs linear_search for equilibrium_check (see python script : )

s001-n141

function 1: np.where()
function 2: linear_search()

Time test 1
```
Time taken to plot function 1: 0.27234696596860886 seconds
Time taken to plot function 2: 0.372000050265342 seconds
```

Time test 2
```
Time taken to plot function 1: 0.03602103888988495 seconds
Time taken to plot function 2: 0.05720120994374156 seconds
```

Time test 3
```
Time taken to plot function 1: 0.036510932724922895 seconds
Time taken to plot function 2: 0.04137762077152729 seconds
```

Time test 4
```
Time taken to plot function 1: 0.037083132192492485 seconds
Time taken to plot function 2: 0.041165427304804325 seconds
```

Time test dppy kernel Instance

cpu:

test 1
```
0.5990159017965198 seconds
```

test 2
```
0.6225333590991795 seconds
```

gpu:

test1
```
0.6654831650666893 seconds
```

test 2
```
6233123647980392 seconds
```
