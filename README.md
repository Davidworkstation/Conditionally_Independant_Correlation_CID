# Conditionally_Independant_Correlation_CID
 The Conditionally Independent Copula (CID) is a statistical model used to describe the joint distribution of multiple variables. It assumes that the variables are marginally independent but can exhibit dependence when conditioned on a subset of variables. This allows CID to capture complex dependencies that traditional copulas may overlook.

## Installation
To install the project dependencies, run:
pip install -r requirements.txt

## Usage
Basic instructions on how to use the project:

On your computer, navigate to the repository's folder and type the following in the terminal:
streamlit run CID_streamlit_demo.py

note: depending on your python setup, you may have to include 'python' or 'python3' in front of the command.


## Project Structure
Overview of the project's structure:

project-root/

├── CID_data/

│ └── csv/ - Raw data files. Includes hypothetical company names, and default probabilities.

├── py/ - CID_multi_portfolio - A model that plots the CID model using the CID Data. Plots only the min, max, and quantiles.

├── png/ - CID_Output_Example - 9 plots showcasing the behavior of the CID.

├── py/ - CID_Single_Example - a single CID plot that showcases the model on theoretical data

├── py/ - CID_streamlit_demo - functional CID dashboard on streamlit

├── png/ - CID_streamlitapp_demo_image - image preview of the dashboard

├── png/ - Generate_Probability_Default_Data - generates CID data, based on different standard deviations.

├── .gitignore - Git ignore file

├── requirements.txt - Project dependencies

├── .gitatributes - Text handling

└── README.txt - This file

## Contact Information
For questions, please contact David Bannister at (https://www.linkedin.com/in/david-bannister-230a67191/).