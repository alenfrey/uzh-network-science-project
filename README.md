# Network Science Project Fall 2022

This repository contains the code for the final project of the network
science class at UZH.

## Team Members

* Alexey Buyakofu 22-737-225
* Alen Frey 22-732-473
* Keisuke Yokota 22-738-165
* Said Haji Abukar 19-724-718

## Abstract

The recent paper [Structural measures of similarity and complementarity in complex networks](https://www.nature.com/articles/s41598-022-20710-w) describes algorithms for measuring properties of similarity and complementarity in networks. In the final project, we replicate the results of this paper and test the algorithms on additional social networks with differing sizes.

The suggestion to test the structural coefficients on social networks with different sizes is also mentioned in the paper, where the authors mention that the structural coefficients of complementarity are more likely to be high in large social networks, which if true would be in stark contrast to the fact that usually social networks in general are more driven by similarity. We test this hypothesis by comparing the structural coefficients of small and large social networks. Furthermore, we differentiate by online and offline social networks. 

>Our results also point to important differences between social and biological networks. The former, with some
exceptions of course, tend to be dominated by similarity while the latter are more structurally diverse, which
probably reflects their heterogeneous functional properties and complex evolutionary history (we study this in
more detail in “Structural diversity across the tree of life” section). **However, it seems that large online social
networks also feature increased complementarity relatively often (see Fig. 6A). Thus, it may be worthwhile to
study differences between small and large as well as offline and online social networks in the future.** In particular,
to our best knowledge it is not yet clear what social processes are responsible for significantly high amounts of
quadrangles in large online social networks.  
> -- <cite> [Structural measures of similarity and complementarity in complex networks](https://www.nature.com/articles/s41598-022-20710-w) </cite>

## Installation

Python 3.10 is used for this project.
To install the packages, run the following commands in the **project root directory**.

Create virtual environment and activate (optional but recommended)

```bash
virtualenv venv
source venv/bin/activate
```

Install the packages

```bash
pip install -r requirements.txt
```

Download the datasets
To download the datasets used, run the following scripts in order:
1. group_available_datasets.ipynb 
2. download_datasets.py

After this, everthing is ready to run the other notebooks and scripts. 

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
- [x] Explore and visualise properties of the datasets (explore_network_properties.ipynb)
  - [x] Online Networks 
    - [x] Load the datasets and check basic stats
    - [x] Create additional visualisations and statistics
  - [x] Offline Networks
    - [x] Load the datasets and check basic stats
    - [x] Create additional visualisations and statistics 
- [x] Reproduce the results of the paper with their methodology (paper_replication folder)
- [x] ~~Implement the algorithms from the paper in networkx~~ -> tested and works already
  - [x] ~~Structural similarity~~
  - [x] ~~Structural complementarity~~
- [x] Port the script from the paper to networkx instead igraph and graph-tool
- [x] Reproduce the results of the paper on other social networks
  - [x] Large online networks
  - [x] Small online networks
  - [x] Large offline networks
  - [x] Small offline networks 
 - [x] Do analysis on all the networks simultaneously
- [x] Finish report
- [x] Create presentation slides
- [x] Film video presentation


## Checklist for Submission

- [x] all code used
- [x] all data used
- [x] written report
- [x] video presentation (20 min)
- [x] slides of presentation



## Individual Contributions

|    | File                             | Description                            | Contributor   |
|---:|:---------------------------------|:---------------------------------------|:--------------|
|  0 | project_proposal.pdf             | Project Proposal                       | Keisuke, Alen |
|  1 | explore_network_properties.ipynb | Exploration of available datasets      | Alen          |
|  2 | lib.py                           | Library for functions                  | Alen          |
|  3 | group_available_datasets.ipynb   | Group and structure available datasets | Alen          |
|  4 | paper_replication/*              | Relplicate paper results               | Alen          |
|  5 | download_datasets.ipynb          | Download script for social networks    | Alen          |
|  6 | original_method_large_online.ipynb(template)| analyze the networks(large online)(template for others)    | Alen          |
|  7 | visualise_results_large_online.ipynb(template)| visualize the analysis(large online)(template for others)| Alen          |
|  8 | original_method_large_offline.ipynb| analyze the networks(large offline)    | Alexey          |
|  9 | visualise_results_large_offline.ipynb| visualize the analysis(large offline)| Alexey          |
| 10 | original_method_small_online.ipynb| analyze the networks(small online)    | Keisuke          |
| 11 | visualise_results_small_online.ipynb| visualize the analysis(small online)| Keisuke          |
| 12 | original_method_small_offline.ipynb| analyze the networks(small_offline)    | Said          |
| 13 | social_networks_small_offline.ipynb| analyze the networks(small_offline)    | Said          |
| 14 | visualise_results_small_offline.ipynb| visualize the analysis(small_offline)| Keisuke           |
| 15 | overall_exploration.ipynb        | visualize the analysis(all networks)   | Alen          |
| 16 | Exercise_X__Model___Report (1).pdf | Written report of project              | Said          |
| 17 | Presentation.pptx                | Presentation of project(slides)        | Kei(1-12),Alexey(13-)|
| 18 | Presentation.pptx                | Presentation of project(presentation)  | Kei(1-12),Alexey(13-)|

