## [GAUSSIAN PROCESS FOR ACTIVITY MODELING AND ANOMALY DETECTION](http://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/II-3-W5/467/2015/isprsannals-II-3-W5-467-2015.pdf)

### Abstract ###
Complex activity modeling and identification of anomaly is one of the most
interesting and desired capabilities for automated video behavior analysis for traffic scene

### Details ###
 - using non-parametric GP to model semantic region which exploits spatial-temporal dependencies
 among activiy patterns using Gaussian Automatic Relevance Determination (ARD) kernel function and
 model activities
 - outperforms Hidden Markov Model on both sensitivity and robustness to noise
 - anomaly detection of ambulance or firetruck, illegal u-turn, jaywalking
 - using QMUL Junction Dataset


## [Designing Engaging Game Using Bayesian Optimization](https://www.cs.colorado.edu/~mozer/Research/Selected%20Publications/reprints/KhajahRoadsLindseyLiuMozer2016.pdf)

### Abstract ###
Using Gaussian process surrogate-based optimization, we conduct efficient
experiments to identify game design characteristics—specifically those
influencing difficulty—that lead to maximal engagement.

### Details ###
 - our work is to design games that maximize engagement for a population of users via manipulation
 of static difficulty
 - Bayesian optimization is a collection of three components: 
  - (1) Gaussian process regression to model design spaces,
  - (2) a probabilistic, generative theory of how observations (voluntary usage times) are produced,
  - (3) an active-selection policy that specifies what design to explore next.

## [The Player Kernel: Learning Team Strengths Based on Implicit Player Contributions](https://arxiv.org/pdf/1609.01176.pdf)

### Abstract ###
Connection between skill-based models of game outcomes and Gaussian process classification models
Redicting outcomes of football matches between national teams

### Details ###
 - GP provides 1) a principled way of dealing with uncertainty,
 2) rich models, specified through kernel functions
 - handles data sparsity and data stalenesd by analyzing club game
 - pairwise comparisons as GP classification

## [Gaussian Process for Recommender Systems](http://staff.ustc.edu.cn/~cheneh/paper_pdf/2011/QiLiu-KSEM11.pdf)

### Abstract ###
We propose a Gaussian process based recommendation model, which can aggregate all of above
factors into a unified system to make more appropriate and accurate recommendations

### Details ###
 - regularize covariance function to handle noise
 - MovieLens data set

## [Gaussian processes for survival analysis ](https://arxiv.org/pdf/1312.1591v2.pdf)

### Abstract ###
In this context, the covariates are regarded as the ‘inputs’ and the event times are the ‘outputs

### Details ###
 - Multiple output GP regression 

## [Gaussian Processes for Personalized e-Health Monitoring With Wearable Sensors](http://www.robots.ox.ac.uk/~davidc/pubs/tbme2013_gp.pdf)

### Abstract ###
proposal of a novel, patient-personalized system for analysis and inference
in  the  presence  of  data  uncertainty, typically caused by sensor artifact
and data incompleteness

### Details ###
 - means of performing inference using the noisy, potentially artifactual
 - well suited to the analysis of our time series of patient physiological data
 - outperform conventional methods of coping with artifactual or missing data

## [Interactive Design of Probability Density Functions for Shape Grammars](http://lgg.epfl.ch/publications/2015/proman/paper.pdf)

### Abstract ###
We present a framework that enables a user to interactively design a
probability density function (pdf) over such a shape space and to sample models
according to the designed pdf.

### Details ###
Interpolate user preference scores by combining multiple techniques:
function factorization, Gaussian process regression, auto- relevance detection, and l1 regularization

## [Predictive Modeling of Pedestrian Motion Patterns with Bayesian Nonparametrics](http://web.mit.edu/miaoliu/www/publications/scitech_gnc16.pdf)

### Abstract ###
Learn motion patterns from previous observations using Gaussian process (GP) regression, which are
then used for online prediction.

### Details ###
 - Since Markov models are only conditioned on the last observed position, they can generate
 poor predictions if di erent motion patterns exhibit signi cantly overlapping segments
 - overcome this problem by modeling motion patterns as velocity flow fields, 
 - predictions using a GP have a simple analytical form that can be easily integrated into a
 risk-aware path planner
 - Dirichlet process mixture of Gaussian processes

## [Mind the Nuisance: Gaussian Process Classification using Privileged Noise](https://papers.nips.cc/paper/5373-mind-the-nuisance-gaussian-process-classification-using-privileged-noise.pdf)

### Abstract ###
Allows the integration of additional knowledge into the training process of a classifier
In contrasst to standard GPC setting, the latent function is not just a nuisance but a feature

## [Approximations of Gaussian Process Uncertainties for Visual Recognition Problems](http://www.inf-cv.uni-jena.de/dbvmedia/de/Research/Various/Bodesheim13_AOG.pdf)

### Abstract ###
Gaussian  processes  offer  the  advantage  of  calculating  the classification
uncertainty in terms of predictive variance associated with the  classification
result

### Details ###
 - novelty detection to choose new samples to be trained
 - active learning using GP

## [Predicting Margin of Victory in NFL Games: Machine Learning vs. the Las Vegas Line](http://www.cs.cornell.edu/courses/cs6780/2010fa/projects/warner_cs6780.pdf)

## Abstract ##
We propose a simple framework which recommends a bet on a given game when it is deemed statistically favorable

### Details ###
 - The ability to generate confidence measures together with predictions seems
 to lend itself naturally to a betting scenario where one looks to balance the
 risk of placing a bet on a game with their relative certainty in its outcome
