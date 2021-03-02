# PHSX_815_Project1

INSTRUCTIONS
The DiceRollSum.py file uses a random class to produce the sum of two rolled dice. The default probabilities for a die are equal for the 6 numbers.

Number of rolls, number of experiments, and probabilities for individual number rolled can be specified from the command line using "-Nroll", "-Nexp", "-prob1", "-prob2", "-prob3", "-prob4", and "-prob5", respectively.

However, the DiceAnalysis.py file has been coded to perform a statistical analysis for ONLY a null hypothesis with default values and an alternative hypothesis with probabilities as follows: 1 - 2/5, 2 - 2/5, 3 - 1/20, 4 - 1/20, and 5 - 1/20.

The outputs from the DiceRollSum should be piped to text files.

Once the user has two text files for hypothesis testing, they can then run the DiceAnalysis.py script, specifiying the input text files at the command line using "-input0" and "-input1."
The desired alpha value can be directly changed inside the code. Beta is automatically calculated from this.

The DiceAnalysis.py file will produce a plot comparing the sum probability distributions as well as a plot comparing the log likelihood ratios. 