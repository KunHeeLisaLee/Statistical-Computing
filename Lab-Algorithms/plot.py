import matplotlib.pyplot as plt


def plot(a_s, b_s, total_loss, method):
    """
    Input: a_s(history of a), b_s(history of b),
    total_loss(history of loss), method
    Output: plots of a_s, b_s, total_loss as a function of t"""
    step_loss = range(len(total_loss))
    step_params = range(len(a_s))

    plt.subplot(1, 3, 1)
    plt.plot(step_params, a_s, label='a')
    plt.xlabel('Step')
    plt.ylabel('a')
    plt.title(f"{method}: a vs. steps")
    plt.grid()

    plt.subplot(1, 3, 2)
    plt.plot(step_params, b_s, label='b')
    plt.xlabel('Step')
    plt.ylabel('b')
    plt.title(f"{method}: b vs. steps")
    plt.grid()

    plt.subplot(1, 3, 3)
    plt.plot(step_loss, total_loss, label='Loss')
    plt.xlabel('Step')
    plt.ylabel('Loss')
    plt.title(f"{method}: Loss vs. steps")
    plt.grid()

    plt.tight_layout()
    plt.show()
