import pandas as pd
import numpy as np
from faker import Faker
from scipy.stats import norm

size_of_data = 10000 #assumes a constant dataframe length across all models 
mu = 0
sigma = [0.1, 0.3, 0.5, 0.6, 0.9]

#initializes the random naming module
fake = Faker()
Faker.seed(0)

def generate_single_portfolio_dataframe(size_of_data,mu,sigma, normal = True):
    company_names = []

    for i in range(size_of_data):
        z = fake.company()
        company_names.append(z)
        
    company_names = np.array(company_names)
    if normal == True:
        default_probabilities = np.array(np.random.normal(mu,sigma,size_of_data))
    else:
        default_probabilities = np.random.lognormal(mu, sigma, size_of_data)

    dataframe = pd.DataFrame({
        'Company':company_names,
        'Default Probabilities':default_probabilities
    })

    return dataframe

for i in range(0,5):
    dfname = str(f'Default_Portfolio_{i}_Normal_Dist_Sigma_{sigma[i]}')
    generate_single_portfolio_dataframe(size_of_data, mu, sigma[i], normal = True).to_csv(path_or_buf=f"/Users/risaiah/Desktop/GitHub Repositories/Data-Science-Econometrics-Personal/CID Econometrics/CID_Data/{dfname}.csv")

