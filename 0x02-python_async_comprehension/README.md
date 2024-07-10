# Asynchronous Comprehension Project

This project demonstrates the use of asynchronous comprehensions in Python. It includes creating asynchronous generators, using asynchronous comprehensions to collect values, and measuring the runtime of parallel comprehensions.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- Follow `pycodestyle` style guide (version 2.5.x)

## Tasks

### Task 0: Async Generator

Create a coroutine `async_generator` that loops 10 times, each time asynchronously waits 1 second, then yields a random number between 0 and 10.

### Task 1: Async Comprehensions

Create a coroutine `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`, then returns the 10 random numbers.

### Task 2: Run Time for Four Parallel Comprehensions

Create a coroutine `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather` and measures the total runtime.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/alx-backend-python.git
    ```

2. Navigate to the project directory:
    ```bash
    cd alx-backend-python/0x02-python_async_comprehension
    ```

3. Run the main files:
    ```bash
    ./0-main.py
    ./1-main.py
    ./2-main.py
    ```

## Author

- **Immanuella**

