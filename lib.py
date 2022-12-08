from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PATHS AND FILES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

PROJECT_ROOT_DIR_PATH = Path(__file__).parent.absolute()  # project root dir path
DATA_DIR_PATH = PROJECT_ROOT_DIR_PATH / "data"  # data dir path


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# FUNCTIONS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def degree_array(g: nx.Graph) -> np.array:
    """
    List of degrees of a nx.Graph
    """
    return np.array([degree for node, degree in g.degree()])


def logarithmic_bins(values: np.array, n_bins: int) -> np.array:
    """
    Calculate logarithmic bins for a specific
    array of values.
    """
    # np.geomspace(min(values), max(values) + 1, num=n_bins) is functionally equivalent
    return np.logspace(np.log10(min(values)), np.log10(max(values) + 1), n_bins + 1)


def plot_distribution(
    values,
    title,
    xlabel,
    bins=None,
    x_scale: str = "linear",
    y_scale: str = "linear",
) -> None:
    """Plot the distribution of an array of values."""
    plt.hist(values, bins=bins, density=True, edgecolor="black")
    # plt.grid(True, which="both", ls="-")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Density")
    plt.xscale(x_scale)
    plt.yscale(y_scale)


def plot_vertical_line(x, label: str) -> None:
    """
    Adds a vertival line to a matplotlib plot.
    """
    plt.axvline(x=x, color="red", label=label)


def plot_labeled_scatter(x, y, x_label, y_label, title) -> None:
    """
    Create and show labeled scatter plot while enforcing
    the setting of labels and title in the plot.
    """
    plt.grid(True, which="both", ls="-")
    plt.scatter(x, y, alpha=0.5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
