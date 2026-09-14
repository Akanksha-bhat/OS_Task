import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
import numpy as np

import matrix_multiplication
import animation


# Start multiplication
calculation_thread = matrix_multiplication.start_multiplication()


# Show live animation
animation.show_animation(matrix_multiplication)


# Wait for all threads
calculation_thread.join()


# Get matrices
A = matrix_multiplication.A
B = matrix_multiplication.B
C = matrix_multiplication.C

SIZE = matrix_multiplication.SIZE


# TensorFlow verification
tensorflow_A = tf.constant(A)
tensorflow_B = tf.constant(B)

tensorflow_result = tf.matmul(
    tensorflow_A,
    tensorflow_B
).numpy()


# Calculate difference
difference = np.max(
    np.abs(C - tensorflow_result)
)


print()
print("==============================================")
print("       MATRIX MULTIPLICATION RESULTS")
print("==============================================")

print(f"Matrix A size       : {SIZE} x {SIZE}")
print(f"Matrix B size       : {SIZE} x {SIZE}")
print(f"Matrix C size       : {SIZE} x {SIZE}")
print(f"Threads used        : {SIZE * SIZE}")
print(f"Operations completed: {SIZE * SIZE:,}")

print()
print("First 5 x 5 elements of Matrix C:")
print()

print(
    np.array2string(
        C[:5, :5],
        formatter={
            "float_kind": lambda x: f"{x:6.0f}"
        }
    )
)

print()
print("Maximum difference from TensorFlow:", difference)

if np.allclose(
    C,
    tensorflow_result,
    rtol=1e-3,
    atol=1e-1
):
    print("Result verified successfully using TensorFlow.")
else:
    print("Result verification failed.")

print("==============================================")
