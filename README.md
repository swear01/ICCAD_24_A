# Readme of ICCAD_24_A
Final Project For Intro to EDA/ CAD contest 2024 Problem A

# Overview
This project is developed in Python and does not require any additional compilers.

# Files and Execution

First, please run "pip install -r requirements.txt" to install the required packages.
(Actually, only tqdm is required)
Then, change the directory to the project root directory.


main.py
This file adheres to the format requirements of the CAD contest. However, we do not recommend running this file directly. Instead, please use run_all.py to see the results.

run_all.py
This script includes all combinations of netlists and cost estimators. A netlist is optimized through logic synthesis simulated annealing and technological mapping simulated annealing. The cost results are displayed in the terminal.
Run this file directly. It may take up to an hour to complete, but you can stop it at any time.