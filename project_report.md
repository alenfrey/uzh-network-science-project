# Network Science

# This report needs to be moved to either the Word or Latex template when its done.
# The words of this report can be counted by running `mwc project_report.m` in the terminal.

## Final Project Report

Alen Frey (Immatriculation Number1), Author2 (Immatriculation Number1), …. 

Network Science (HS22) 

Date

## Reproducing Structural measures of similarity and complementarity in complex networks

## Abstract

**Write abstract last after the rest of the report is done.**

## Introduction

The paper "Structural measures of similarity and complementatiry in complex networks" [1] proposes measures for determining if networks are formed by underlying mechanisms of similarity and/or complementarity. They attribute these properties to specific motifs, triangles for similarity and quadrangles for complementarity.

**Write more about the paper here - should be easily possible to get around pages from just summarizing the paper methods and results related to social networks that are important for our project.**

* Describe the similarity and complementarity measures
* Describe the motifs


## Social Network Analysis

Social network analysis is the study of social networks, which are networks of individuals or organizations that are connected by social relationships. There are many different measures that are commonly used in social network analysis to quantify and analyze the structure and properties of social networks. Some examples of these measures include:

    Degree: The degree of a node in a network is the number of connections it has to other nodes.
    Centrality: Centrality measures are used to identify the most important or influential nodes in a network. Examples of centrality measures include betweenness centrality, which measures the extent to which a node lies on the shortest path between other nodes, and closeness centrality, which measures the average distance from a node to all other nodes in the network.
    Clustering coefficient: The clustering coefficient of a node in a network measures the extent to which its neighbors are also connected to each other.
    Structural equivalence: Structural equivalence refers to the extent to which two nodes in a network have similar patterns of connections to other nodes.
    Homophily: Homophily is the tendency for individuals or organizations in a network to form connections with others who are similar to them in some way.

These are just a few examples of the many measures that are used in social network analysis. Overall, these measures can provide valuable insights into the structure and properties of social networks, and can be used to better understand the dynamics of social relationships.


## Similarity and Complementarity in Social Networks

Both similarity and complementarity are key properties of some types of social networks, they play a crucial role in the formation of the structures
present in these networks.

### Similarity

Social networks are networks of individuals or organizations that are connected by social relationships, such as friendship, kinship, or professional associations. 
These networks can be represented as graphs, with nodes representing the individuals or organizations and edges representing the relationships between them.

One important concept in the study of social networks is similarity, which refers to the extent to which two individuals or organizations have similar characteristics or behaviors. For example, two friends are likely to have similar interests, values, or opinions, while two organizations that belong to the same industry are likely to have similar business practices or goals.

Similarity is an important factor in the formation and maintenance of social relationships, as individuals and organizations are more likely to form connections with others who are similar to them in some way. Additionally, similarity can influence the strength and stability of social relationships, as stronger ties are often formed between individuals or organizations that are more similar to each other.

### Complementarity

In the context of social networks, complementarity refers to the extent to which two individuals or organizations have different, 
  rather than similar, characteristics or behaviors. For example, two friends may have complementary skills or interests, such as one friend who is good at sports and the other who is good at music.

Complementarity is an important factor in the formation and maintenance of social relationships, as individuals and organizations are often drawn to others who can provide something that they lack. For example, two friends with complementary skills may enjoy working on projects together, while two organizations with complementary products or services may benefit from collaborating on a joint venture.

Additionally, complementarity can influence the strength and stability of social relationships, as individuals and organizations may feel a stronger sense of mutual dependence when they have complementary rather than similar characteristics.

## Research Question

**Link the paper summary and results to our research question and describe it.**

In the paper, an open question is stated:
>Our results also point to important differences between social and biological networks. The former, with some
exceptions of course, tend to be dominated by similarity while the latter are more structurally diverse, which
probably reflects their heterogeneous functional properties and complex evolutionary history (we study this in
more detail in “Structural diversity across the tree of life” section). **However, it seems that large online social
networks also feature increased complementarity relatively often (see Fig. 6A). Thus, it may be worthwhile to
study differences between small and large as well as offline and online social networks in the future.** In particular,
to our best knowledge it is not yet clear what social processes are responsible for significantly high amounts of
quadrangles in large online social networks.  
> -- <cite> [Structural measures of similarity and complementarity in complex networks](https://www.nature.com/articles/s41598-022-20710-w) </cite>

In this project we test the stated hypothesis (marked in bold above) by comparing the structural coefficients of small and large online and offline social networks. 

## Datasets

We used all social datasets available from Netzschleuder, and split them into groups of online and offline social networks, and then into groups of small, medium and large networks. We only used undirected and unweighted networks.
To download the datasets, we have written a script that downloads the datasets and saves them locally in the `data` folder.


## Methods

**Describe the libraries used, also the ones used by Pathcensus**

* NEMtropy
* ...
In network science, there are many measures that can be used to analyze a network and understand its structure and properties. Some of these measures are correlated, meaning that they are related to each other in some way. For example, the degree centrality of a node in a network is directly related to its betweenness centrality, as nodes with a high degree (i.e. those that are connected to many other nodes) are more likely to have a high betweenness centrality. Similarly, the clustering coefficient of a node is related to its degree, as nodes with a high degree are more likely to form clusters within the network.

We check if the similarity and complementarity measures are correlated with some network measures. We also check if the similarity and complementarity measures are correlated with each other.

### Null Model

An undirected binary configuration model (UBCM) is a (exponential) random graph model that can be used to generate networks with a given degree sequence. To fit this model to a network, you would need to first determine the degree sequence of the network, which is a list of the degrees of all the nodes in the network.

Once you have the degree sequence, you can use it to generate a random graph using the configuration model. To do this, you would first create a list of stubs for each node, where the number of stubs for a node is equal to its degree. You would then randomly connect pairs of stubs until all of the stubs have been matched, resulting in a random graph with the same degree sequence as the original network.

It's important to note that the configuration model is a random graph model, so the resulting graph will not necessarily be identical to the original network. However, it will have the same degree sequence, which means that it will have the same overall structure in terms of the number and types of connections between nodes. Overall, fitting a configuration model to a network can be a useful way to generate a random graph with similar structural properties to the original network.

We fitted undirected binary configuration models (UBCM)to the networks, and sampled 200 samples from the fitted models. We then calculated the similarity and complementarity measures for each sample, and compared the results to the original network. We repeated this process for each network, and calculated the p-values for each measure.

## Summary

**Write a summary of the results here, i think it will probably be 1-2 pages.**



## Author Contributions

** THIS IS EXAMPLE TEXT ** 
The following is a sample text. All authors conceived and designed the project idea. P.M. and C.J.T. developed and wrote the business model. B.S. worked on the regulatory implications.  Y.Z. and X.Y. developed the technical implementation and wrote the technical section. Y.Z. wrote the critical overview of the plaftorm selected. All authors revised and accepted the final version of this document. 
** END OF EXAMPLE TEXT **


### References

> Talaga, S., & Nowak, A. (2022). Structural measures of similarity
> and complementarity in complex networks. Scientific Reports, 12(1), 16580.
> https://doi.org/10.1038/s41598-022-20710-w [1]
