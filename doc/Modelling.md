## Modelling Gaussian Processes

### Challenges ###
1. Defining covariance function.
 - dealing with muliple output GP with multiple indices
2. Non-gaussian function
 - transformation / link function to connect problem with additive model
 - handling different noise model (likelihood function, P(y | f))
  - probit noise model for classfication
  - ordered categories model
 - try to find a Gaussian Model to mimic the posterior produced. Solutions:
  - Expectation Propagation (EP) to match 2 distributions
  - variational approximation
  - Laplace approximation (speed wise the best)
3. Learning Covariance Parameters

### Advantages ###
1. Sustaining uncertainty 
2. Optimization of kernel parameters

## [Gaussian Process for Machine Learning Cambridge Tutorial](http://mlg.eng.cam.ac.uk/tutorials/06/es.pdf)

### Covariance Function ###
1. Log N(y | 0, K) = -(1/2 log |K| = regularizer / capacity) - ((y^tK^-1y) / 2 = data fit)
2. Increasing length scale allows more functions to be fitted

### Prediction with GP
 -  use GP as a Bayesian prior expressing beliefs about underlying function
 - link to data via noise model or likelihood
 - Likelihood / noise model: p(y | f) : N(f, sigma^2I)
 - Marginal likelihood: p(y) : N(0, K + sigma^2I)
 - p(y, y_t) = N(0, K_(N + T) + sigma^2I)
 - K_(N + T) = [K_N K_NT, K_TN, K_T]
 - p(y_t | y) = N(u_t, sigma_t) is the condition on training outputs
 - p(f | y) = p(y | f) * p(f) / p(y)


### Classification with GP
 - Uses sigmoidal likelihood p(y = +1 | f) = sigma(f)
 - Need to perform Gaussian approximatin to posterior because of non-gaussian likelihood
  - Laplace approximation: Second order Taylor approximation about mode of posterior
  - Expectation Propagation: minimizing KL-Divergence p(f | y) and q(f | y) by iterative way (better)

### GP latent variable model (GPLVM)
  - Probabilistic model for dimensionality reduction. Model each dimension (k) as independent GP with
  unknown low dimensional latent inputs

## [Automatic Model Construction with GP](http://www.cs.toronto.edu/~duvenaud/thesis.pdf)

### Model Selection ###
 - can computer marginal likelihood of a dataset given a particular model.
 - compare models using by using:
  - capacity of a model
  - fit to data

### Useful properties of GP ###
  - Expressivity: choice of covariance function express modelling assumption
  - Less overfitting because less parameters and regularization needed
  - Easy to analyze

### Limitations of GP ###
  - Slow inference
  - Choosing kernel
  - Dealing with non-gaussian predictive distribution

### Expressing structure with kernel ###
 - Kernel specifies which functions are likely under GP prior 
 - Stationary vs Non-stationary kernels
 - Construct covariance functions for multiple inputs using multiple SE (Square exponential) 
 matrices with different lengthscales -> ARD(Automatic Relevance Determination) that is a universal
 kernel that can learn any continuous function given enough data
 - Change point to show change from one kernel to another
 - Build invariance into kernels
 - Use one of k with short lenghtscale which indicates low correlation between categories
 - handle multiple output by adding extra index which indicates output of the value

### Automatic Model Description ###
 - Impact of multiplying a kernel
  - *SE*: converts global correlation structure into local correlation only
  - *Lin*: standard deviation of model to vary linearly
  - *Sigmoid*: function goes to zero before or after certain point
