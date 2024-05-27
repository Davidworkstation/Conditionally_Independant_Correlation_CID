import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

import numpy as np
from scipy.stats import norm
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Create Z for equation 1 and 2
col1, col2 = st.columns([8,11])
N = col1.number_input(label='N, sample size', min_value=150, max_value=1000000, step=1, value=10000)
a = col1.slider(label='a, Correlation parameter', min_value=-1.0, max_value=1.0, step=0.01, value = 0.5)
M = col1.number_input(label='M, Market parameter', min_value=-3.0, max_value=3.0, step=0.01, value= 1.0)
axlinesq = col1.checkbox(label='Axis Lines Toggle', value=True)
legendq = col1.checkbox(label='Legend', value=False)
initial_state = st.session_state.get('initial_state', 0)
if col1.button('Rerun'):
    st.session_state['initial_state'] = initial_state + 1



Z1 = norm.ppf(np.random.rand(N)) #norm ppf functions like norminverse(rand()) from excel
Z2 = norm.ppf(np.random.rand(N))

x1 = a * M + np.sqrt(1 - a ** 2) * Z1
x2 = a * M + np.sqrt(1 - a ** 2) * Z2

# Convert equations to a dataframe
df = pd.DataFrame({
    'x1': np.array(x1),
    'x2': np.array(x2)
})


fig = go.Figure()
fig.update_xaxes(range=[-4, 4], title_text="X1")  
fig.update_yaxes(range=[-4, 4], title_text="X2")  

single_point = go.Scatter(
    x=[M],
    y=[M],
    mode='markers',
    marker=dict(size=10, color = '#ffbcd9'),
    name=f'Market Factor = {M:.3f}',
    showlegend=legendq
)
other_points = go.Scatter(
    x=df['x1'],
    y=df['x2'],
    mode='markers',
    marker=dict(size=1),
    name=f'Correlational Points = {a:.3f}',
    showlegend=legendq
)

line_x = go.Line(
    x=[-5,5],
    y=[0,0],
    line=dict(color='#808080', width=1, dash='dash'),
    name='x axis',
    showlegend=False
)

line_y = go.Line(
    x=[0,0],
    y=[-5,5],
    line=dict(color='#808080', width=1, dash='dash'),
    name='y axis',
    showlegend=False
)

fig.add_trace(other_points)
fig.add_trace(single_point)
    
if axlinesq:  
    fig.add_trace(line_x)
    fig.add_trace(line_y)

fig.update_yaxes(showgrid=False)
fig.update_xaxes(showgrid=False)
fig.update_yaxes(zeroline=True)
fig.update_layout(title='Conditionally Independent Correlation Copula',
                  title_x=0.3,
                  title_y=0.95  # Center vertically
                  )
col2.plotly_chart(fig)

# print data at the end
correlation_matrix = df.corr()
correlation_coefficient = correlation_matrix.loc['x1', 'x2']
st.write("Corr(X1,X2):", correlation_coefficient)
col2.write('The Conditionally Independent Copula (CID) is a statistical model used to describe the joint distribution of multiple variables. It assumes that the variables are marginally independent but can exhibit dependence when conditioned on a subset of variables. This allows CID to capture complex dependencies that traditional copulas may overlook.')
