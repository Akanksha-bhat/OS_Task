# OS Task 1: Multithreading and Synchronization

## Project Overview

This project demonstrates two important Operating Systems concepts using **multithreading, synchronization, and thread coordination**.

The first program implements the **Producer-Consumer problem in Java**, where two threads share a fixed-size buffer and coordinate using synchronization. The second program performs **100 × 100 matrix multiplication using Python threads**, with each result element calculated by a separate thread. TensorFlow is used for matrix generation and verification, while Matplotlib provides a live animation of the calculation.

## Programs

### 1. Producer-Consumer Problem

The Producer-Consumer problem is implemented in **Java using threads**.

* A Producer generates 10 values from 10 to 100.
* A Consumer consumes all 10 values.
* A shared buffer is used to store the values.
* The buffer has a maximum capacity of 4 items.
* `LinkedList` is used to maintain FIFO order.
* `synchronized`, `wait()`, and `notifyAll()` are used for thread synchronization.
* `sleep()` and `join()` are used for controlling and coordinating the threads.

### 2. Matrix Multiplication Using Threads

The second program performs **100 × 100 matrix multiplication using Python threads**.

* Matrix A and Matrix B are generated using TensorFlow.
* Each element of the result matrix is calculated by a separate thread.
* A total of **10,000 threads** are created.
* A `Lock` is used to safely access the shared result matrix and progress counter.
* Matplotlib is used to display the calculation as a live animation.
* TensorFlow's `tf.matmul()` is used to verify the final result.
* NumPy is used for matrix storage, calculations, and result comparison.

## Repository Structure

```text
OS-Task-1/
│
├── ProducerConsumer.java
│
├── matrix_multiplication.py
├── animation.py
├── main.py
│
└── README.md
```

## Requirements

### Producer-Consumer

* Java JDK
* Any Java-supported IDE or terminal

### Matrix Multiplication

* Python 3
* TensorFlow
* NumPy
* Matplotlib

Install the Python libraries using:

```bash
pip install tensorflow numpy matplotlib
```

## How to Run

### Producer-Consumer

Compile the Java program:

```bash
javac ProducerConsumer.java
```

Run it using:

```bash
java ProducerConsumer
```

### Matrix Multiplication

Make sure the three Python files are in the same folder:

```text
matrix_multiplication.py
animation.py
main.py
```

Run the program using:

```bash
python main.py
```

A window will open showing:

* Matrix A
* Matrix B
* Matrix C = A × B
* Progress bar
* Current calculation progress

## Output

### Producer-Consumer Output

The program displays the values as they are produced and consumed. A typical output looks like:

```text
Produced: 10
Consumed: 10
Produced: 20
Produced: 30
Consumed: 20
Produced: 40
Produced: 50
Consumed: 30
Produced: 60
Consumed: 40
Produced: 70
Produced: 80
Consumed: 50
Produced: 90
Consumed: 60
Produced: 100
Consumed: 70
Consumed: 80
Consumed: 90
Consumed: 100

Producer and Consumer completed successfully.
```

The exact order can vary because the Producer and Consumer are running concurrently.

### Matrix Multiplication Output

During execution, a Matplotlib window displays the three matrices:

```text
┌─────────────┐  ┌─────────────┐  ┌─────────────────┐
│   Matrix A  │  │   Matrix B  │  │  Matrix C=A×B  │
│             │  │             │  │                 │
│   100 × 100 │  │   100 × 100 │  │    100 × 100    │
└─────────────┘  └─────────────┘  └─────────────────┘

        Processing row 45 / 100   column 72 / 100
        Progress: 45.8%
```

Matrix C is gradually filled while the threads perform the calculations. A progress bar at the bottom of the window shows how many of the 10,000 elements have been completed.

After the calculation finishes, the terminal displays information similar to:

```text


```

The values in the **5 × 5 output will be different on each run** because Matrix A and Matrix B are randomly generated.

## Concepts Demonstrated

### Producer-Consumer

* Java Threads
* `Runnable`
* Shared resources
* Synchronization
* `synchronized`
* `wait()`
* `notifyAll()`
* `sleep()`
* `join()`
* FIFO buffering

### Matrix Multiplication

* Python Threads
* Thread creation and joining
* Shared data
* `threading.Lock()`
* TensorFlow
* NumPy
* Matplotlib
* Live animation
* Result verification

## Expected Result

For the Producer-Consumer program, the Producer and Consumer run concurrently while waiting whenever the buffer is full or empty.

For the Matrix Multiplication program, Matrix C is gradually filled as the threads complete their calculations. At the end, the threaded result is compared with TensorFlow's result using `np.allclose()`.

If the results match within the specified tolerance, the program displays:

```text
Result verified successfully using TensorFlow.
```

## Conclusion

These two programs demonstrate how multithreading can be used to perform tasks concurrently while maintaining safe access to shared resources. The Producer-Consumer program focuses on synchronization and communication between threads, while the Matrix Multiplication program demonstrates thread-based computation, live visualization, and result verification.
