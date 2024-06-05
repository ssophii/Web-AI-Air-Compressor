import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_analysis(data):
    # Convert relevant columns to numeric, ignoring non-numeric columns
    numeric_data = data.select_dtypes(include=[np.number])
    
    # Placeholder for the results dictionary
    results = {}
    
    max_val = numeric_data.max()
    min_val = numeric_data.min()
    
    results['max_val'] = max_val.to_dict()
    results['min_val'] = min_val.to_dict()
    
    # Visualize spread of data
    plt.figure(figsize=(10, 6))
    numeric_data.hist(bins=50)
    plt.savefig('static/data_histogram.png')
    
    return results