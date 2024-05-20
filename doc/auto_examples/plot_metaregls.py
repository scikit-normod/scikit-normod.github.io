"""
Meta-regression
===============
Normative modeling when data are measured with errors
"""

#%%
# Imports
#--------
import numpy as np
import scipy
import matplotlib.pyplot as plt

from sknormod import NormodOLS
from sknormod.metareg import NormodMetaregLS
from sknormod.plotting import plot_scatter_with_lines
from sknormod.datasets import make_gaussian


#%%
# The problem
# -----------
n_subj = 100
age, y = make_gaussian(n_subj, interpolate_mu=[95, 98, 92])
# We also generate a quadratic feature of age to capture potential nonlinear
# relationships.
X = np.column_stack((age, age**2))

error_se = np.ones(len(y)) * 1.5
y_observed = y + scipy.stats.norm.rvs(scale=error_se, size=len(error_se))

scatter = plt.scatter(age, y_observed, zorder=2, label="Observed")
errorbar = plt.errorbar(age, y, yerr=error_se*2, fmt='o', color="red",
                        ecolor='black', zorder=1, label="True")
plt.title('TODO: make nicer plots')
plt.legend()
plt.show()

#%%
# Fit models
# ----------

normod_ols = NormodOLS()
normod_metareg = NormodMetaregLS()
normod_truth = NormodOLS()

normod_ols.fit(X, y_observed)
normod_metareg.fit(X, y_observed, y_se=error_se)
normod_truth.fit(X, y)

centiles = np.linspace(0.1, 0.9, 9)
centiles_ols = normod_ols.predict_distr_p(X, centiles)
centiles_metareg = normod_metareg.predict_distr_p(X, centiles)
centiles_truth = normod_truth.predict_distr_p(X, centiles)


#%%
# Plot
# ----
estimated_centiles = list((
    normod.predict_distr_p(X, np.linspace(0.1, 0.9, 9))
    for normod in [normod_ols, normod_metareg, normod_truth]
))


fig, axes = plt.subplots(1, 3, figsize=(12, 4))
titles = ["OLS", "Metareg", "True"]
for i_col, ax in enumerate(axes.flat):
    plt.sca(ax)
    plot_scatter_with_lines(age, y_observed,
                            lines=estimated_centiles[i_col], cbar=False)
    plt.scatter(age, y, color='red')
    ax.set_title(titles[i_col])
plt.tight_layout()
plt.show()



