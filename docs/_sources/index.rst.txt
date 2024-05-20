scikit-normod
=============

Scikit-normod is a scientific library designed for normative modeling, offering
a familiar scikit-learn-like API. This package facilitates the fitting and
validation of normative models, the estimation of centiles, the transformation
of data to z-scores, and the calculation of summary atypicality scores.

.. warning::
   
   The library is in its early development stages. Expect bugs, missing
   features, and breaking changes.

.. warning::
   
   Really

Key Features
------------

.. grid:: 1 2 2 2 

  .. grid-item-card:: Models
      :columns: auto

    * Gaussian Homoskedastic

      * Ordinary Least Squares (OLS)
      * Generalized Additive Models (GAM)

    * Gaussian Heteroskedastic (Location-Scale):

      * Generalized Additive Models for Location Scale (GAMLS)

    * Location-Scale-Shape 

      * Generalized Additive Models for Location Scale Shape (GAMLSS)

    * Meta-Regression

      * Gaussian Homoskedastic
      * Gaussian Heteroskedastic


  .. grid-item-card:: Model Methods
      :columns: auto

    * Estimate quantiles
    * Transform data to z-scores
    * Transform data to quantiles 
    * *(not-implemented)* Quantiles and z-scores with uncertainity 
    * *(not-implemented)* Transfer/recalibrate model to new sites



  .. grid-item-card:: Anomaly Detection
      :columns: auto

    * Various anomaly scores including mean-z, min/max-z, z-over-threshold, and others


  .. grid-item-card:: Validation
      :columns: auto

    * Whole Model

      * Logarithmic score
      * *(not-implemented)* AIC, BIC, GAIC

    * Calibration

      * Mean, standard deviation, skewness, kurtosis, W

    * *(not-implemented)* Diagnostic plots

    * *(untested, probably broken)* scikit-learn grid search etc. 

  .. grid-item-card:: Ploting
      :columns: auto

    * Plot centiles (should be better)
    * *(not-implemented)* calibration plots: 

      * worm-plots
      * bucket-plots
      * qq
      * pp
      * centiles/distribution

  .. grid-item-card:: scikit-learn Compatibility
      :columns: auto

    * Grid search, pipelines, CV scorers, etc.
    * In theory should work
    * In practice not-tested, probably broken, maybe eventually


.. toctree::
   :maxdepth: 2
   :hidden:
   :titlesonly:
   
   auto_examples/index
   api

