# Example Array search in python

Test Platform : Intel DevCloud
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

def find_solution(a, position):
    index = np.where(a%2 == 0)
    solution = position[index]

    return solution

def main():

    a = np.random.randint(1, 1000, 100000)
    position_a = np.arange(0, 100000)

    b = np.random.randint(1, 1000, 500000)
    position_b = np.arange(0, 500000)

    c = np.random.randint(1, 1000, 10000000)
    position_c = np.arange(0, 10000000)

    start = time.perf_counter()
    result = find_solution(a, position_a)
    end = time.perf_counter()
    diff = end - start

    start_b = time.perf_counter()
    result_b = find_solution(b, position_b)
    end_b = time.perf_counter()
    diff_b = end_b - start_b

    start_c = time.perf_counter()
    result_c = find_solution(c, position_c)
    end_c = time.perf_counter()
    diff_c = end_c - start_c

    print('time taken : 100000 = ', diff)
    print('time taken : 500000 = ', diff_b)
    print('time taken : 10000000 = ', diff_c)

if __name__ == '__main__':
    main()
```

Output

Test 1
```
time taken : 100000 =  0.0013521886430680752
time taken : 500000 =  0.0074658519588410854
time taken : 10000000 =  0.12290216004475951
```

Test 2
```
time taken : 100000 =  0.001336882822215557
time taken : 500000 =  0.007380989845842123
time taken : 10000000 =  0.11984780803322792
```

Test 3
```
time taken : 100000 =  0.0013324674218893051
time taken : 500000 =  0.007385942153632641
time taken : 10000000 =  0.120196633040905
```

Test 4
```
time taken : 100000 =  0.0013367990031838417
time taken : 500000 =  0.007460077293217182
time taken : 10000000 =  0.12051121704280376
```
