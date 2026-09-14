import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def show_animation(matrix_module):

    SIZE = matrix_module.SIZE
    A = matrix_module.A
    B = matrix_module.B
    C = matrix_module.C
    lock = matrix_module.lock

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(11, 5.5)
    )

    fig.patch.set_facecolor("#F7FBFA")

    # Matrix A - Sky Blue
    image_A = axes[0].imshow(
        A,
        cmap="GnBu",
        interpolation="nearest",
        vmin=1,
        vmax=10
    )

    axes[0].set_title(
        "Matrix A",
        fontsize=14,
        fontweight="bold",
        color="#38A9D6",
        pad=8
    )

    # Matrix B - Light Green
    image_B = axes[1].imshow(
        B,
        cmap="Greens",
        interpolation="nearest",
        vmin=1,
        vmax=10
    )

    axes[1].set_title(
        "Matrix B",
        fontsize=14,
        fontweight="bold",
        color="#70B77E",
        pad=8
    )

    # Matrix C - Pink
    image_C = axes[2].imshow(
        C,
        cmap="RdPu",
        interpolation="nearest"
    )

    axes[2].set_title(
        "Matrix C = A × B",
        fontsize=14,
        fontweight="bold",
        color="#E8759A",
        pad=8
    )

    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])

    fig.suptitle(
        "Live Matrix Multiplication Using Threads",
        fontsize=17,
        fontweight="bold",
        color="#496B67",
        y=0.96
    )

    status = fig.text(
        0.5,
        0.08,
        "Starting matrix multiplication...",
        ha="center",
        fontsize=10,
        fontweight="bold",
        color="#52706B"
    )

    progress_ax = fig.add_axes(
        [0.25, 0.025, 0.5, 0.025]
    )

    progress_ax.set_xlim(
        0,
        SIZE * SIZE
    )

    progress_ax.set_ylim(
        0,
        1
    )

    progress_ax.set_xticks([])
    progress_ax.set_yticks([])

    progress_bar = progress_ax.barh(
        0,
        0,
        height=1,
        color="#E8759A"
    )

    def update(frame):

        with lock:
            current_C = C.copy()
            completed = matrix_module.completed
            row = matrix_module.current_row
            col = matrix_module.current_col

        image_C.set_data(current_C)

        total = SIZE * SIZE

        percentage = (
            completed / total
        ) * 100

        progress_bar[0].set_width(
            completed
        )

        if completed < total:

            status.set_text(
                f"Processing row {row + 1} / {SIZE}   "
                f"column {col + 1} / {SIZE}   |   "
                f"Progress: {percentage:.1f}%"
            )

        else:

            status.set_text(
                "✓ Matrix multiplication completed successfully"
            )

        return (
            image_A,
            image_B,
            image_C
        )

    animation = FuncAnimation(
        fig,
        update,
        interval=40,
        blit=False,
        cache_frame_data=False
    )

    plt.subplots_adjust(
        left=0.04,
        right=0.96,
        top=0.84,
        bottom=0.15,
        wspace=0.12
    )

    plt.show()
