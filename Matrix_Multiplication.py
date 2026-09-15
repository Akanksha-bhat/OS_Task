import tensorflow as tf
import numpy as np
import threading

SIZE = 100

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

C = np.zeros((SIZE, SIZE), dtype=np.float32)

lock = threading.Lock()

completed = 0
current_row = 0
current_col = 0


def calculate_element(row, col):
    global completed

    result = 0

    for k in range(SIZE):
        result += A[row][k] * B[k][col]

    with lock:
        C[row][col] = result
        completed += 1


def matrix_multiplication():
    global current_row
    global current_col

    threads = []

    for row in range(SIZE):
        for col in range(SIZE):

            current_row = row
            current_col = col

            t = threading.Thread(
                target=calculate_element,
                args=(row, col)
            )

            threads.append(t)
            t.start()

    for t in threads:
        t.join()


def start_multiplication():
    thread = threading.Thread(
        target=matrix_multiplication
    )

    thread.start()

    return thread
