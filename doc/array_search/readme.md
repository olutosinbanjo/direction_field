# Array search and application in project

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

# Test script : [search.py](https://github.com/olutosinbanjo/direction_field/blob/83a2ba200cb3158449292126df666f51a89d67b3/doc/array_search/search.py)

s001-n140
Test np.where() (seconds):

test 1 
```
time taken : 100000 =  0.0012411139905452728
time taken : 500000 =  0.006467103958129883
time taken : 10000000 =  0.10884666489437222
```

test 2
```
time taken : 100000 =  0.0012382939457893372
time taken : 500000 =  0.0065603055991232395
time taken : 10000000 =  0.1098435684107244
```
Test Linear search (seconds):

test 1
```
time taken : 100000 =  0.0008704713545739651
time taken : 500000 =  0.004399575293064117
time taken : 10000000 =  0.07232033787295222
```

test 2
```
time taken : 100000 =  0.0008703693747520447
time taken : 500000 =  0.004338616039603949
time taken : 10000000 =  0.07246477669104934
```


# np.where vs linear_search for equilibrium_check (see python script : [equilibrium_check.py](https://github.com/olutosinbanjo/direction_field/blob/ddaf5d4bf659a945fff50b1cdde3b75863585ce8/doc/array_search/equilibrium_check.py))

(Possible optimization - search algorithm for equilibrium solution check)

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
0.6233123647980392 seconds
```
