# Analysis of Gaussian Process

## [When should we use Gaussian process regression rather than other methods for estimation?](https://www.quora.com/When-should-we-use-Gaussian-process-regression-rather-than-other-methods-for-estimation)
1. When there are complicated correlation between response variables
2. Lack of insight about model of a particular problem in the beginning

## [Computer Science: What are the pros and cons for using Gaussian process modeling for regression?](https://www.quora.com/Computer-Science-What-are-the-pros-and-cons-for-using-Gaussian-process-modeling-for-regression)
1. Pros: Non-parametric. Less hyperparameters tuning to get good fit
2. Cons: Computation time grows as data points increase. O(n^3)
3. Simple to use. Like a black box. Sparse GP regression is used to handle large datapoints

## [What are some advantages of using Gaussian Process Models vs Neural Networks?](https://www.quora.com/What-are-some-advantages-of-using-Gaussian-Process-Models-vs-Neural-Networks)
1. A way to do non-parametric bayesian inference and good for adding side information as prior over function
2. Cons: Target function is not smooth. Large datasets( > 2000 examples)

## [What are some advantages of using Gaussian Process Models vs SVMs?](https://www.quora.com/What-are-some-advantages-of-using-Gaussian-Process-Models-vs-SVMs)
1. Hyperparameters can be found via MLE
2. Can provide uncertainity in the prediction.
3. Automatic Relevance Determination for feature selection is available

## [Main advantages of Gaussian Process Models](http://stats.stackexchange.com/questions/207183/main-advantages-of-gaussian-process-models)
1. Inverse problem such as learning from demonstration
2. Given no hard data only correlation between them. Provide a way of measuring probable scenario
3. Cons: Given data with a lot of isotropic(uniform) behaviour 

## Applications of GP
1. [Geostastics where it is first used](https://en.wikipedia.org/wiki/Kriging)
2. Near optimal sensor placement 
3. Latent variable modeling and visualization
4. Modelinng dynamics
5. [Cambridge GP projects](http://mlg.eng.cam.ac.uk/pub/topics/#gp)
6. [Fraud Detection Application](http://www.redes.unb.br/lasp/files/papers/KMIS_2015_Pilon.pdf)
7. [Gaussian Process Motion Planning](http://www.cc.gatech.edu/~bboots3/files/GPMP.pdf)
8. [Modeling Diabetes development](http://dollar.biz.uiowa.edu/~street/research/chin_using_2011.pdf)
9. [Neil Lawrence's Talks](http://ml.sheffield.ac.uk/~neil/cgi-bin/publications/bibpage.cgi?type=talk&pageTitle=Neil%20Lawrence%27s%20Talks)
10. [Visualization with GP](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/talks/gplvm_ebi14.pdf)
11. [Personalized Health with GP](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/talks/personalized_health_manizales14.pdf)
12. [Modelling in the context of GP](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/talks/missingdata_tuebingen15.pdf)
13. [Deep Gaussian Process](http://staffwww.dcs.shef.ac.uk/people/N.Lawrence/talks/deepgp_icmldeep15.pdf)
14. [Image segmentation usingf GP](http://cs229.stanford.edu/proj2013/Hong-GaussianProcessedBasedImageSegmentationAndObjectDetection.pdf)
