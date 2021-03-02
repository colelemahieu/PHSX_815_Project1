# import needed packages 
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from fractions import Fraction

# define the file inputs 
p0 = sys.argv.index("-input0")
p1 = sys.argv.index("-input1")

# initialize number of experiments
nexp0 = 0
nexp1 = 0

# count the number of experiments, file0
with open(sys.argv[p0+1], "r") as file0:
    for line in file0:
        nexp0 +=1

# get the file data, file0
with open(sys.argv[p0+1], "r") as file0:
    file0string = file0.read()
    file0list = file0string.split(" ")


# count the number of experiments, file1
with open(sys.argv[p1+1], "r") as file1:
    for line in file1:
        nexp1 += 1

# get the file data, file1
with open(sys.argv[p1+1], "r") as file1:
    file1string = file1.read()
    file1list = file1string.split(" ")
    
# get rid of the \n symbols
file0list_b = []
for x in file0list:
    file0list_b.append(x.strip())

file1list_b = []
for x in file1list:
    file1list_b.append(x.strip())

# delete empty spaces in the list
file0list_clean = [x for x in file0list_b if x]
file1list_clean = [x for x in file1list_b if x]

# calculate number of rolls per experiment
rolls_0 = len(file0list_clean)/nexp0
rolls_1 = len(file1list_clean)/nexp1

# get arrays of float dice sums
sum0 = []
sum1 = []
for i in range(0, len(file0list_clean)):
    sum0.append(float(file0list_clean[i]))
for i in range(0, len(file1list_clean)):
    sum1.append(float(file1list_clean[i]))

# make an array divided into subarrays for each experiment
array0 = np.array(sum0)
array1 = np.array(sum1)
sum0arr = np.reshape(array0, (-1, rolls_0))
sum1arr = np.reshape(array1, (-1, rolls_1))
    
# initialize LLR distribution arrays
LLR0 = []
LLR1 = []


# loop over rolls for each experiment to find LLR
for i in range(0, nexp0):
    LogLikeRatio_0 = float(0)
    for j in range(0, rolls_0):
        
        # the various prob. for H0
        if sum0arr[i][j]==7:
            LogLikeRatio_0 -=log(Fraction(6,36))
        elif (sum0arr[i][j]==6 or sum0arr[i][j]==8):
            LogLikeRatio_0 -=log(Fraction(5,36))
        elif (sum0arr[i][j]==5 or sum0arr[i][j]==9):
            LogLikeRatio_0 -=log(Fraction(4,36))
        elif (sum0arr[i][j]==4 or sum0arr[i][j]==10):
            LogLikeRatio_0 -=log(Fraction(3,36))
        elif (sum0arr[i][j]==3 or sum0arr[i][j]==11):
            LogLikeRatio_0 -=log(Fraction(2,36))
        else:
            LogLikeRatio_0 -=log(Fraction(1,36))

        # the various prob. for H1
        if sum0arr[i][j]==3:
            LogLikeRatio_0 += log(Fraction(128,400))
        elif sum0arr[i][j]==4:
            LogLikeRatio_0 += log(Fraction(80,400))
        elif sum0arr[i][j]==2:
            LogLikeRatio_0 += log(Fraction(64,400))
        elif sum0arr[i][j]==7:
            LogLikeRatio_0 += log(Fraction(34,400))
        elif sum0arr[i][j]==6:
            LogLikeRatio_0 += log(Fraction(33,400))
        elif sum0arr[i][j]==5:
            LogLikeRatio_0 += log(Fraction(32,400))
        elif sum0arr[i][j]==8:
            LogLikeRatio_0 += log(Fraction(19,400))
        elif sum0arr[i][j]==9:
            LogLikeRatio_0 += log(Fraction(4,400))
        elif sum0arr[i][j]==10:
            LogLikeRatio_0 += log(Fraction(3,400))
        elif sum0arr[i][j]==11:
            LogLikeRatio_0 += log(Fraction(2,400))
        else:
            LogLikeRatio_0 += log(Fraction(1,400))

    LLR0.append(LogLikeRatio_0)

for i in range(0, nexp1):
    LogLikeRatio_1 = float(0)
    for j in range(0, rolls_1):
        
        # the various prob. for H0
        if sum1arr[i][j]==7:
            LogLikeRatio_1 -=log(Fraction(6,36))
        elif (sum1arr[i][j]==6 or sum1arr[i][j]==8):
            LogLikeRatio_1 -=log(Fraction(5,36))
        elif (sum1arr[i][j]==5 or sum1arr[i][j]==9):
            LogLikeRatio_1 -=log(Fraction(4,36))
        elif (sum1arr[i][j]==4 or sum1arr[i][j]==10):
            LogLikeRatio_1 -=log(Fraction(3,36))
        elif (sum1arr[i][j]==3 or sum1arr[i][j]==11):
            LogLikeRatio_1 -=log(Fraction(2,36))
        else:
            LogLikeRatio_1 -=log(Fraction(1,36))

        # the various prob. for H1
        if sum1arr[i][j]==3:
            LogLikeRatio_1 += log(Fraction(128,400))
        elif sum1arr[i][j]==4:
            LogLikeRatio_1 += log(Fraction(80,400))
        elif sum1arr[i][j]==2:
            LogLikeRatio_1 += log(Fraction(64,400))
        elif sum1arr[i][j]==7:
            LogLikeRatio_1 += log(Fraction(34,400))
        elif sum1arr[i][j]==6:
            LogLikeRatio_1 += log(Fraction(33,400))
        elif sum1arr[i][j]==5:
            LogLikeRatio_1 += log(Fraction(32,400))
        elif sum1arr[i][j]==8:
            LogLikeRatio_1 += log(Fraction(19,400))
        elif sum1arr[i][j]==9:
            LogLikeRatio_1 += log(Fraction(4,400))
        elif sum1arr[i][j]==10:
            LogLikeRatio_1 += log(Fraction(3,400))
        elif sum1arr[i][j]==11:
            LogLikeRatio_1 += log(Fraction(2,400))
        else:
            LogLikeRatio_1 += log(Fraction(1,400))

    LLR1.append(LogLikeRatio_1)

# sort the arrays
LLR0.sort()
LLR1.sort()

# enter desired alpha value
alpha = 0.05
lambda_c = len(LLR0)-int(floor((len(LLR0))*alpha))

# find beta
count = float(0)
for x in range(0,len(LLR1)):
    if LLR1[x] < LLR0[lambda_c]:
        count += 1
        
beta = count/len(LLR1)
    

# code for plotting
plt.figure()
plt.hist(LLR0, bins=100, density=True, alpha=0.65, label="$\\mathbb{H}_{0}$")
plt.hist(LLR1, bins=100, density=True, alpha=0.65, label="$\\mathbb{H}_{1}$")

# get axis limits 
left, right = plt.xlim()
bottom, top = plt.ylim()

plt.xlabel('$x = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
plt.ylabel("Probability")
plt.title("Log Likelihood Ratio (%i rolls per exp, %i exp)" %(rolls_0, nexp0))
plt.legend(loc="upper left",shadow=True)

plt.axvline(LLR0[lambda_c], color="k", linestyle="solid", linewidth=1.25)
plt.text(LLR0[lambda_c]+0.1, .95*top, "$\\lambda_{c}$", rotation=90)
plt.text(left+.2,.75*top, "$\\alpha$ = %.2f" %(alpha), fontweight="bold")
plt.text(left+.2,.70*top, "$\\beta$ = %.4f" %(beta), fontweight="bold")

# plot sum outcomes 
plt.figure()
plt.hist(sum0, bins=11, density=True, alpha=0.75, label="Fair Pair")
plt.hist(sum1, bins=11, density=True, alpha=0.75, label="Skewed Pair")
plt.xlabel("Two-Dice Sums")
plt.ylabel("Probability")
plt.title("Probability Distribution for the Sum of Two Dice")
plt.legend(loc="upper right", shadow=True)

bottom2, top2 = plt.ylim()
plt.text(9, .75*top2, "Experiments = %i" %(nexp0))
plt.text(9, .70*top2, "Rolls per exp = %i" %(rolls_0))

plt.show()
