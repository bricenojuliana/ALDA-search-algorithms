# Comparison of Search Algorithms

This project compares the performance of three search algorithms:
1. **Linear Search**
2. **Binary Search**
3. **Ternary Search**

The goal is to analyze their time complexity, characteristics, and performance in different scenarios using Python. The project includes implementations of the algorithms, data generation, time measurement, unit tests, and performance graphs.


## Table of Contents

1. Introduction
2. Algorithms
   - Linear Search
   - Binary Search
   - Ternary Search
3. Project Structure
4. Setup
5. Usage
6. Testing
7. Results
8. Contributing
9. License


## Introduction

This project aims to compare the performance of three search algorithms:
- **Linear Search**: A simple algorithm that checks each element one by one.
- **Binary Search**: An efficient algorithm for sorted arrays that divides the search space in half.
- **Ternary Search**: A variation of binary search that divides the search space into three parts.

The comparison is done by measuring the execution time of each algorithm on arrays of different sizes and in different scenarios (e.g., best case, worst case, average case).


## Algorithms

### Linear Search
- **Time Complexity**: O(n)
- **Description**: Checks each element in the array sequentially until the target is found.
- **Use Case**: Works on both sorted and unsorted arrays.

### Binary Search
- **Time Complexity**: O(log n)
- **Description**: Efficiently searches a sorted array by repeatedly dividing the search interval in half.
- **Use Case**: Requires the array to be sorted.

### Ternary Search
- **Time Complexity**: O(log₃ n)
- **Description**: Similar to binary search but divides the search space into three parts.
- **Use Case**: Requires the array to be sorted.


## Project Structure

```
array-project/
├── src/
│   ├── search_algorithms.py       # Implementation of search algorithms
│   ├── data_generator.py          # Functions to generate random and sorted arrays
│   ├── executor.py                # Function to measure execution time
│   ├── test_search_algorithms.py  # Unit tests for the search algorithms
│   └── main.ipynb                 # Notebook for running and visualizing results
├── requirements.txt               # Dependencies for the project
└── README.md                      # Project documentation
```


## Setup

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/comparison-of-search-algorithms.git
   cd comparison-of-search-algorithms
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the project**:
   - Open the Jupyter Notebook (`main.ipynb`) to run the algorithms and visualize the results.
   - Alternatively, run the unit tests to verify the implementations:
     ```
     python -m unittest test_search_algorithms.py
     ```


## Usage

### Running the Algorithms
- Open the `main.ipynb` notebook.
- Execute the cells to generate performance graphs for:
  - Execution time vs array size (sorted and unsorted arrays).
  - Execution time vs position of the target element.
  - Comparison of average and worst-case scenarios.

### Running Unit Tests
- Run the following command to execute the unit tests:
  ```
  python -m unittest test_search_algorithms.py
  ```


## Testing

The project includes unit tests to ensure the correctness of the search algorithms. The tests cover:
- Searching for an element present in the array.
- Searching for an element not present in the array.
- Edge cases (e.g., empty array, single-element array).

To run the tests:
```
python -m unittest test_search_algorithms.py
```


## Results

The performance of the algorithms is visualized using graphs:
1. **Execution Time vs Array Size**: Compares how the algorithms scale with increasing array size.
2. **Execution Time vs Element Position**: Shows how the position of the target element affects performance.
3. **Average vs Worst Case**: Compares the performance in average and worst-case scenarios.



## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Acknowledgments

- This project was created as part of a learning exercise to compare search algorithms.
