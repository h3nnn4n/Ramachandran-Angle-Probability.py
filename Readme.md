# Ramachandran-Angle-Probability.py
===================================

A simple python class to generate random angles based on the angle density extracted experimental data. This class
reads from a data file in (Py)Rosetta.

## Usage
--------

A simple example that uses matplotlib to generate plots for each aminoacid and a Ramachandran plot:

``` Python
    import matplotlib.pyplot as plt

    rama = Ramachandran()
    rama.load(path="/home/h3nnn4n/PyRosetta4.Release.python35.linux.release-147/"
                   "setup/pyrosetta/database/scoring/score_functions/rama/shapovalov/kappa75/all.ramaProb")
    rama.process()

    for k, v in rama.parsed_data.items():
        plt.imshow(v.transpose(), cmap='viridis', interpolation='nearest', origin="lower")
        plt.savefig(k + ".png")
```

To get a random angle for an amino acid one can use `phi, psi = rama.get_random_angle('T')`. Note that either the 1 or 3 letter name works.

This program relies on data released with (Py)Rosetta. Rosetta can be found here and it is free for academic use: https://www.rosettacommons.org/


LICENSE
-------

Only the files in this repository are released under the MIT liecense. Check the LICENSE file for more details.
The files belonging to (Py)Rosetta have their own licenses.
