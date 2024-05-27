import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

import numpy as np
from scipy.stats import norm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import glob


# Create a random a
a = np.random.rand()

# Create M
M = norm.ppf(np.random.rand())

# Equations
def CID_basemodel(a, M, defa): #array_test is essentially the idiosyncratic factor of the company, or the default probabilities of the portfolio
    return a * M + np.sqrt(1 - a ** 2) * defa

# Define the directory path
directory_path = r'/Users/risaiah/Desktop/GitHub Repositories/Data-Science-Econometrics-Personal/CID Econometrics/CID_Data'

# Use glob to find all CSV files
csv_files = glob.glob(os.path.join(directory_path, "*.csv"))

portfolio_dictionary = {}

for csv_file in csv_files:
    datadf = pd.read_csv(csv_file)
    # Use the file name (without path) as the key
    file_name = os.path.basename(csv_file)
    portfolio_dictionary[file_name] = datadf
    print(f"Loaded {file_name}")

for key, value in portfolio_dictionary.items():
    defaults = value["Default Probabilities"]
    x_values = defaults.apply(lambda defa: CID_basemodel(a, M, defa)) 
    value["Independant Causation Identifiers (x)"] = x_values

x_dictionary = {}


for key, value in portfolio_dictionary.items():
    xvals = value['Independant Causation Identifiers (x)']
    x_dictionary[key] = xvals

x_values_dataframe = pd.DataFrame(x_dictionary)

x_dictionary_simplified = {}

for key, value in portfolio_dictionary.items():
    x_val_simpl = []
    xvals = value['Independant Causation Identifiers (x)']
    xmin, x25, xmedian, x75, xmax = np.min(xvals), np.percentile(xvals, 25), np.median(xvals), np.percentile(xvals, 75), np.max(xvals)
    x_val_simpl.extend([xmin, x25, xmedian, x75, xmax])
    x_dictionary_simplified[key] = x_val_simpl

x_dictionary_simplified = pd.DataFrame(x_dictionary_simplified)
print(x_dictionary_simplified)
                     

# plot data frame in seaborn 
palette = sns.color_palette('pastel', len(x_values_dataframe.columns) - 1)
plt.figure(figsize=(11,8))
for i in range(1, len(x_dictionary_simplified.columns)):
    sns.scatterplot(x = x_dictionary_simplified[x_dictionary_simplified.columns[0]], y = x_dictionary_simplified[x_dictionary_simplified.columns[i]], color=palette[i - 1])
plt.scatter(M, M, color='#ffbcd9', zorder=5, label='M')
plt.axvline(0, color='grey', linestyle='--')
plt.axhline(0, color='grey', linestyle='--')
plt.xlabel(f'{x_dictionary_simplified.columns[0]}')    
plt.ylabel(f'{x_dictionary_simplified.columns[1:]}')
plt.title('CID (X1,X2)')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.legend(x_dictionary_simplified.columns)
plt.show()


# print data at the end
correlation_matrix = x_values_dataframe.corr()
print('-' * 20)
print("M =", M)
print("a =", a)
for i in range(1, len(x_values_dataframe.columns)):
    correlation_coefficient = correlation_matrix.loc[x_values_dataframe.columns[0], x_values_dataframe.columns[i]]
    print('-' * 20)
    print(f"Corr({x_values_dataframe.columns[0]},{x_values_dataframe.columns[i]}):", correlation_coefficient)
    print('-' * 20)
