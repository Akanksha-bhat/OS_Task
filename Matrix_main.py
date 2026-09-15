import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
import numpy as np

import matrix_multiplication
import animation


thread = matrix_multiplication.start_multiplication()

animation.show_animation(matrix_multiplication)

thread.join()


A = matrix_multiplication.A
B = matrix_multiplication.B
C = matrix_multiplication.C
size = matrix_multiplication.SIZE


tf_A = tf.constant(A)
tf_B = tf.constant(B)

tf_result = tf.matmul(tf_A, tf_B).numpy()


difference = np.max(np.abs(C - tf_result))


print()
print("==============================================")
print("          MATRIX MULTIPLICATION RESULTS")
print("==============================================")

print(f"Matrix A size        : {size} x {size}")
print(f"Matrix B size        : {size} x {size}")
print(f"Matrix C size        : {size} x {size}")
print(f"Threads used         : {size * size}")
print(f"Operations completed : {size * size:,}")

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

if np.allclose(C, tf_result, rtol=1e-3, atol=1e-1):
    print("Result verified successfully using TensorFlow.")
else:
    print("Result verification failed.")

print("==============================================")
