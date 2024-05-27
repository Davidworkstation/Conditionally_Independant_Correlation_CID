import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

import numpy as np
from scipy.stats import norm
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create Z for equation 1 and 2
N = 10000
Z1 = norm.ppf(np.random.rand(N)) #norm ppf functions like norminverse(rand()) from excel
Z2 = norm.ppf(np.random.rand(N))

# Create a 
a = np.random.rand()

# Create M
M = norm.ppf(np.random.rand())

# Equations
x1 = a * M + np.sqrt(1 - a ** 2) * Z1
x2 = a * M + np.sqrt(1 - a ** 2) * Z2

# Convert equations to a dataframe
df = pd.DataFrame({
    'x1': x1,
    'x2': x2
})

# plot data frame in seaborn 
plt.figure(figsize=(15,15))
sns.scatterplot(data=df, x='x1', y='x2')
plt.scatter(M, M, color='red', zorder=5, label='M')

plt.axvline(0, color='grey', linestyle='--')
plt.axhline(0, color='grey', linestyle='--')
plt.xlabel('x1')    
plt.ylabel('x2')
plt.title('CID (X1,X2)')
plt.show()

# print data at the end
correlation_matrix = df.corr()
correlation_coefficient = correlation_matrix.loc['x1', 'x2']
print("Corr(X1,X2):", correlation_coefficient)

print("M =", M)
print("a =", a)

#creating a subplot to show multiple instances
fig, axes = plt.subplots(3, 3, figsize =(15,15))
axes = axes.flatten()

for ax in axes:
    N = 1000
    Z1 = norm.ppf(np.random.rand(N)) 
    Z2 = norm.ppf(np.random.rand(N))
    a = np.random.rand()
    M = norm.ppf(np.random.rand())
    x1 = a * M + np.sqrt(1 - a ** 2) * Z1
    x2 = a * M + np.sqrt(1 - a ** 2) * Z2

    df = pd.DataFrame({
        'x1': x1,
        'x2': x2
    })
    
    sns.scatterplot(data=df, x='x1', y='x2', ax=ax)
    ax.scatter(M, M, color='red', zorder=5, label='M')
    ax.axvline(0, color='grey', linestyle='--')
    ax.axhline(0, color='grey', linestyle='--')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_title(f'CID (X1,X2) \n Corr(X1,X2): {df.corr().iloc[0,1]:.2f} \n M={M:.2f}, a={a:.2f}')
    ax.set_ylim(-3.5,3.5)
    ax.set_xlim(-3.5,3.5)
    
    

plt.tight_layout()
plt.show()
