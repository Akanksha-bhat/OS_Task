import tensorflow as tf
import numpy as np
import threading


SIZE = 100


# Create Matrix A and Matrix B using TensorFlow

A = tf.random.uniform(
    (SIZE, SIZE),
    minval=1,
    maxval=10,
    dtype=tf.float32
).numpy()

B = tf.random.uniform(
    (SIZE, SIZE),
    minval=1,
    maxval=10,
    dtype=tf.float32
).numpy()


# Result matrix

C = np.zeros(
    (SIZE, SIZE),
    dtype=np.float32
)


# Thread synchronization

lock = threading.Lock()


# Progress information

completed = 0
current_row = 0
current_col = 0


# Calculate one element of Matrix C

def calculate_element(row, col):

    global completed

    total = 0

    for k in range(SIZE):
        total += A[row][k] * B[k][col]

    with lock:
        C[row][col] = total
        completed += 1


# Matrix multiplication using threads

def matrix_multiplication():

    global current_row
    global current_col

    threads = []

    for i in range(SIZE):

        for j in range(SIZE):

            current_row = i
            current_col = j

            thread = threading.Thread(
                target=calculate_element,
                args=(i, j)
            )

            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()


# Start multiplication

def start_multiplication():

    calculation_thread = threading.Thread(
        target=matrix_multiplication
    )

    calculation_thread.start()

    return calculation_thread
