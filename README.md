# Network Science Project Fall 2022

This repository contains the code for the final project of the network
science class at UZH.

## Team Members

* Alexey Buyakofu 22-737-225
* Alen Frey 22-732-473
* Keisuke Yokota 22-738-165
* Said Haji Abukar

## Abstract

The recent paper [Structural measures of similarity and complementarity in complex networks](https://www.nature.com/articles/s41598-022-20710-w) describes algorithms for measuring properties of similarity and complementarity in networks. In the final project, we replicate the results of this paper and test the algorithms on additional social networks with differing scales.

The suggestion to test the structural coefficients on social networks with different sizes is also mentioned in the paper, where the authors mention that the structural coefficients of complementarity are more likely to be high in large social networks, which is in stark contrast to the fact that usually social networks in general are more driven by similarity. We test this hypothesis by comparing the structural coefficients of small and large social networks. Furthermore, we differentiate by online and offline social networks. 

>Our results also point to important differences between social and biological networks. The former, with some
exceptions of course, tend to be dominated by similarity while the latter are more structurally diverse, which
probably reflects their heterogeneous functional properties and complex evolutionary history (we study this in
more detail in “Structural diversity across the tree of life” section). However, it seems that large online social
networks also feature increased complementarity relatively often (see Fig. 6A). Thus, it may be worthwhile to
study differences between small and large as well as offline and online social networks in the future. In particular,
to our best knowledge it is not yet clear what social processes are responsible for significantly high amounts of
quadrangles in large online social networks.  
> -- <cite> [Structural measures of similarity and complementarity in complex networks](https://www.nature.com/articles/s41598-022-20710-w) </cite>

## Installation

Python 3.8.3 is used for this project.
To install the packages, run the following commandsa in the **project root directory**.
(You might want to create a virtual envirionment first)

```bash
pip install -r requirements.txt
```

## Data

Data used in this project is from the following sources:
* [Netzschleuder](https://networks.skewed.de/)

The authors of the original paper used **graph-tool** for downloading 
the files from the page mentioned above. We created our own script
to download the files without relying on graph-tool, since the
installation is cumbersome and forces the use of miniconda/anaconda
which is rather heavy.

## Open Tasks

- [x] Prepare datasets (group_available_datasets.ipynb)
  - [x] Find available datasets
  - [x] Group the datasets
- [x] Create reproducible dataset download script (download_datasets.ipynb)
- [ ] Explore and visualise properties of the datasets (explore_network_properties.ipynb)
  - [ ] Online Networks 
    - [x] Load the datasets and check basic stats
    - [ ] Create additional visualisations and statistics
  - [ ] Offline Networks
    - [ ] Load the datasets and check basic stats
    - [ ] Create additional visualisations and statistics 
- [ ] Implement the algorithms from the paper in networkx (optional)
  - [ ] Structural similarity
  - [ ] Structural complementarity
- [ ] Reproduce the results of the paper on other social networks
  - [ ] Large online networks
  - [ ] Small online networks
  - [ ] Large offline networks
  - [ ] Small offline networks 
- [ ] Finish report
- [ ] Create presentation slides
- [ ] Film video presentation


## Checklist for Submission

- [ ] all code used
- [ ] all data used
- [ ] written report
- [ ] video presentation (20 min)
- [ ] slides of presentation



## Individual Contributions

| File                 | Description       | Contributors   
|---|---|---|
| project_proposal.pdf | Project proposal       | Keisuke Yokota, Alen Frey  |   
| -                    | Data preparation       |                            |   
| -                    | Result Visualisation   |                            |   