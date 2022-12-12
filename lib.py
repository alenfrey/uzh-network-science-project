import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import zstandard
import urllib.request
import pandas as pd
import json
import tempfile
import igraph as ig
import re

from pathcensus import PathCensus
from collections import namedtuple
from sparklines import sparklines
from pathlib import Path

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PATHS AND FILES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

PROJECT_ROOT_DIR_PATH = Path(__file__).parent.absolute()  # project root dir path
DATA_DIR_PATH = PROJECT_ROOT_DIR_PATH / "data"  # data dir path
ONLINE_DATA_DIR_PATH = DATA_DIR_PATH / "online"  # online networks data dir path
OFFLINE_DATA_DIR_PATH = DATA_DIR_PATH / "offline"  # offline networks data dir path

FIGURE_DIR_PATH = PROJECT_ROOT_DIR_PATH / "figures"  # figures dir path
CODE_DIR_PATH = PROJECT_ROOT_DIR_PATH / "code"

TEST_GRAPH_DIR_PATH = CODE_DIR_PATH / "networkx_implementation" / "test_graphs"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# FUNCTIONS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def degree_array(g: nx.Graph) -> np.array:
    """List of degrees of a nx.Graph."""
    return np.array([degree for node, degree in g.degree()])


def average_degree(g: nx.Graph) -> np.float64:
    """Average degree ⟨k⟩ of a nx.Graph."""
    return np.mean(degree_array(g))


def logarithmic_bins(values: np.array, n_bins: int) -> np.array:
    """
    Calculate logarithmic bins for a specific
    array of values.
    """
    # np.geomspace(min(values), max(values) + 1, num=n_bins) is functionally equivalent
    return np.logspace(np.log10(min(values)), np.log10(max(values) + 1), n_bins + 1)


def max_degree(g: nx.Graph):
    """Node with the highest degree
    in a nx.Graph.

    If there are multiple nodes with the maximum degree,
    then only of them is returned.

    Returns
    -------
    Named tuple where index 0 contains the id of
    the node with the highest degree, and index 1
    contains the degree.
    """
    MaxDegreeTuple = namedtuple(
        "MaxDegreeTuple", ["id", "degree"]
    )  # define max degree as named tuple
    return MaxDegreeTuple(*max(g.degree(), key=lambda t: t[1]))  # return namedtuple


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


def sparkline_str(x):
    bins = np.histogram(x)[0]
    sl = "".join(sparklines(bins))
    return sl
    sparkline_str.__name__ = "sparkline"


sparkline_str.__name__ = "sparkline"


def download_and_extract(url, out_path):
    """
    Download and extract a zstandard compressed file from a url.
    """
    dctx = zstandard.ZstdDecompressor()
    with urllib.request.urlopen(url) as url:
        dctx.copy_stream(url, open(out_path, "wb"))


def get_filename_from_url(url: str) -> str:
    """
    Get filename from url.
    """
    return url.split("/")[-1]


def get_group_name_from_url(url: str) -> str:
    """
    Get group from url.
    """
    return url.split("/")[-3]


def remove_file_suffix(filename: str) -> str:
    """
    Remove file suffix from filename.
    """
    return ".".join([filename.split(".")[0], filename.split(".")[1]])


def change_file_suffix(filename: str, suffix: str) -> str:
    """
    Change file suffix from filename.
    """
    return ".".join([filename.split(".")[0], suffix])


def get_all_netzschleuder_network_keys():
    with urllib.request.urlopen("https://networks.skewed.de/api/nets") as url:
        data = json.load(url)
        return list(data)


def get_netzschleuder_network_info(network_key):
    """
    Returns a dictionary with infos for a given network key
    """
    with urllib.request.urlopen(
        "https://networks.skewed.de/api/net/" + network_key
    ) as url:
        data = json.load(url)
        return data


def gml_cleaner(gml_file_path):
    """
    Cleans gml files from https://networks.skewed.de/
    """

    def valid_gml_filter(line):
        valid_content = "[" in line or "]" in line
        valid_fields = (
            "id" in line or "source" in line or "target" in line or "multigraph" in line
        )
        valid_split = len(line.split()) < 3
        return (valid_content or valid_fields) and valid_split

    def valid_gml_filter_special_cases(line):
        return not "_graphml_edge_id" in line

    with open(gml_file_path) as gml_file:
        lines = [line for line in gml_file] # get lines
        valid_lines = [line for line in (filter(valid_gml_filter, lines))] 
        valid_lines = [
            line for line in (filter(valid_gml_filter_special_cases, valid_lines))
        ]
        # networkx doesnt like loading multigraphs without this next line,
        # which inserts a multigraph line in the second line of the file
        valid_lines.insert(1, "multigraph 1\n") 
        #print(valid_lines[:3])

        #with open(DATA_DIR_PATH / "test.txt", "w") as output:
        #   for valid_line in valid_lines:
        #    output.write(valid_line)
        tf = tempfile.TemporaryFile()

        tf.write(bytes("".join(valid_lines), encoding="utf-8"))
        tf.seek(0)
    return tf


# convert between graph types
def igraph_to_networkx(graph: ig.Graph) -> nx.Graph:
    """Convert igraph to networkx."""
    return nx.from_edgelist(graph.get_edgelist())


def networkx_to_igraph(graph: nx.Graph) -> ig.Graph:
    """Convert networkx to igraph."""
    return ig.Graph.TupleList(graph.edges())


def get_digits_from_string(string: str) -> str:
    """Get digits from string."""
    return re.sub("[^0-9]", "", string)


def statistics(graph: ig.Graph) -> pd.DataFrame:
    """Function for calculating graph statistics."""
    paths = PathCensus(graph)
    coefs = paths.coefs("nodes")
    df = pd.DataFrame({
        "sim_g":   paths.similarity("global"),
        "sim":     coefs["sim"].mean(),
        "sim_e":   paths.similarity("edges").mean(),
        "comp_g":  paths.complementarity("global"),
        "comp":    coefs["comp"].mean(),
        "comp_e":  paths.complementarity("edges").mean(),
        "coefs":   [coefs]
    }, index=[0])
    return df



def preprocess_graph(g):
    g = nx.Graph(g)  # remove multiedges if graph is multigraph
    g.remove_edges_from(list(nx.selfloop_edges(g)))  # remove self-loops
    largest_cc = max(
        nx.connected_components(g), key=len
    )  # get largest connected component
    return g.subgraph(largest_cc).copy()
