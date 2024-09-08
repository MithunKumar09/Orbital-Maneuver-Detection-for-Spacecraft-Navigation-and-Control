# src/data_preprocessing.py

import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load the orbital data from a CSV file.
    """
    data = pd.read_csv(file_path)
    data['Datetime'] = pd.to_datetime(data['Datetime'])
    data.set_index('Datetime', inplace=True)
    return data

def clean_data(data):
    """
    Clean the orbital data by filling missing values and removing duplicates.
    """
    data['SMA'] = data['SMA'].ffill()

    # Remove duplicate entries
    data = data[~data.index.duplicated(keep='first')]

    # Handle outliers - Removing spikes or setting limits on reasonable SMA values
    sma_std = data['SMA'].std()
    sma_mean = data['SMA'].mean()
    # Example of outlier removal (change this based on real data characteristics)
    data['SMA'] = np.where((data['SMA'] > sma_mean + 3 * sma_std) | (data['SMA'] < sma_mean - 3 * sma_std), np.nan, data['SMA'])
    data['SMA'] = data['SMA'].interpolate()  # Handle outliers with interpolation

    return data
