# SEAFuzz
SEAFuzz Experiment. src folder contains the implementations of SEAFuzz and AFL-DiPri.
The Initial seeds folder is the initial seeds we use.
Baselines are the benchmark fuzzers we use for comparison during our experiments.
date/raw is the raw data we test.
The docs folder contains various documents. experiment_setup.md: Instructions for setting up the experiment. implementation_and_baselines.md: Explanation of algorithm implementations (SEAFuzz and AFL-DiPri). crash_and_statistics.md: Data processing and statistics guide.
Note that the term "label" is used in our paper to better illustrate the design process. In the actual code implementation, we do not explicitly assign labels to seeds. Instead, we use an equivalent mechanism to distinguish different seeds, which serves the same purpose as the labels described in the paper.
