## Analysis of a rather good report

## Modelling ##
 - each individual is modelled with separate GP over time
 - input variable: input location
 - target variable: (x, y, z) position of the person

### Qualitative Advantage ###
 - handles noisy and missing data (different sampling rate)
 - generates pdf of each individual which is used to predict expected crowd density at certain
 region
 - there exists correlation between current position and future position over time

### Important requirements ###
 - multiple output (x, y, z) solved using multi-class classification
 - computational power as different people modelled as GP

### Interpreting Output ###
 - using a small sample of people in the data to predict population density in a particular area
 - Integrate all people's pdf

### Implementation Details ###
 - different kernel functions
 - different MLE estimation method such as:
  - stochastic variational inference
  - BFGS direct optimization

### Additional Insights + Improvements ###
 - different GP models for big data as does not play well with high dimensional space
  - Stochastic Variance GP
  - Sparse GP
 - model using shortest path to a point instead of Cartesian coordinates

### Experimental evaluations ###
 - Real world dataset used
 - Experimental setup
  - comparing actual density with predicted density from GP sampling N random people
