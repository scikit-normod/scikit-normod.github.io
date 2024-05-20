#############
API Reference
#############

This is an example on how to document the API of your own project.

.. currentmodule:: sknormod



Models
======

OLS
---

.. autosummary::
   :toctree: generated/
   :template: class.rst

   NormodOLS


GAM
---

.. autosummary::
   :toctree: generated/
   :template: class.rst

   gam.GAM
   gam.GAMLS
   gam.GAMLSS


Meta-regression
---------------

.. autosummary::
   :toctree: generated/
   :template: class.rst

   metareg.NormodMetaregLS


Datasets
========

.. autosummary::
   :toctree: generated/
   :template: function.rst

   datasets.make_gaussian
   datasets.make_lss_SHASHo2

Plotting
========

.. autosummary::
   :toctree: generated/
   :template: function.rst

   plotting.plot_scatter_with_lines

Atypicality scoring
===================

.. autosummary::
   :toctree: generated/
   :template: function.rst

   atypicality.multi_atypicality_scorer
   atypicality.multi_roc_auc_score

Metrics
=======

.. autosummary::
   :toctree: generated/
   :template: function.rst

   metrics.logarithmic_score
   metrics.calibration_descriptives
