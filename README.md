# Machine Learning: Naive Bayes Classifier

Here I have used a 2-class Naive Bayes algorithm with an apriori decision
rule using a multinomial estimation for the classes and a gaussian estimation for the
attributes.
## Description
Given are the two data sets named Example and Gauss2 as tsv (tabular separated values). This program is able to read both 
data sets and treat the first value of each line as the class (A or B). The output of the algorithm is
a single tsv file per data set, which contains a row for each class. The last (third) row contains the absolute number of misclassifications for the data. So the solution would look exactly like Example_NB_Solution.tsv provided in the repository.

## Implementation
The program accepts the following parameters:
1. data - The location of the data le (e.g. /media/data/Example.tsv)
2. output - Where the output tsv should be written to.
The program is run from Command line or Terminal as shown below:
"python3 nb.py --data Example.tsv --output Example_NB_Solution.tsv"

## Notes

This program is done from scratch using very simple and basic libraries of python without any optimizations or shortcuts. I have done it in this way so that each and every step is clear to me regarding the algorithm. This is one my assignments from the Machine Learning course of my university.

## Acknowledgements



