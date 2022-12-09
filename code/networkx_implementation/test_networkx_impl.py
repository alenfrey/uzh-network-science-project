from ward import fixture, test

import numpy as np  
import networkx as nx
import igraph as ig
from pathcensus import PathCensus
from lib import *
import random
random.seed(303)
np.random.seed(101)


@fixture
def kite_graph_nx():
    return nx.read_gml(TEST_GRAPH_DIR_PATH /"kite.gml")

@fixture
def kite_graph_ig():
    return ig.Graph.Read_GML(TEST_GRAPH_DIR_PATH / "kite.gml")

@test("compare loaded graphs")
def _(kite_nx=kite_graph_nx, kite_ig=kite_graph_ig): 
    assert kite_nx.isomorphic(kite_ig)

