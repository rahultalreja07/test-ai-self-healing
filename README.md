# Sorting Algorithms

This project contains implementations of various sorting algorithms in different programming languages.

## Description

The repository includes the following sorting algorithms:

*   **Bubble Sort** in JavaScript
*   **Insertion Sort** in Python
*   **Selection Sort** in Java

## Installation

No special installation is required. Make sure you have the necessary compilers or interpreters for the language you want to use.

*   For JavaScript, you need Node.js.
*   For Python, you need Python 3.
*   For Java, you need a Java Development Kit (JDK).

## Usage

You can use the provided functions in your own projects by importing them.

### JavaScript (Bubble Sort)

```javascript
const bubbleSort = require('./src/bubbleSort');

const arr = [5, 2, 9, 1, 5, 6];
const sortedArr = bubbleSort(arr);
console.log(sortedArr); // Output: [1, 2, 5, 5, 6, 9]
```

### Python (Insertion Sort)

```python
from src.insertion_sort import insertion_sort

arr = [5, 2, 9, 1, 5, 6]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [1, 2, 5, 5, 6, 9]
```

### Java (Selection Sort)

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 5, 6};
        SelectionSort.selectionSort(arr);
        System.out.println(Arrays.toString(arr)); // Output: [1, 2, 5, 5, 6, 9]
    }
}
```

## Examples

You can find example usage within the comments of each source file.