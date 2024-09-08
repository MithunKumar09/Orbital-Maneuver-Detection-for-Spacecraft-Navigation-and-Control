# src/feature_extraction.py

import pandas as pd

def extract_sma_change(data, window=1):
    """
    Extract the change in SMA, using smoothing to filter out noise.
    """
    # Smooth the SMA using a rolling mean to filter noise
    smoothed_sma = data['SMA'].rolling(window=window, min_periods=1).mean()
    
    sma_change = smoothed_sma.diff(periods=window)
    return sma_change

def extract_maneuver_threshold(sma_change, threshold):
    """
    Identify points where the change in SMA exceeds a threshold, which may indicate a maneuver.

    :param sma_change: pd.Series, change in SMA over time.
    :param threshold: float, the minimum change in SMA to be considered a maneuver.
    :return: pd.Series, boolean series where True indicates a maneuver.
    """
    return sma_change.abs() > threshold

def extract_features(data, window=1, threshold=5):
    """
    Extract features from the data, including smoothed SMA change and maneuver detection.
    """
    sma_change = extract_sma_change(data, window)
    
    # Identify maneuvers based on smoothed SMA changes
    maneuvers = extract_maneuver_threshold(sma_change, threshold)
    
    features = pd.DataFrame({
        'SMA Change': sma_change,
        'Maneuver': maneuvers
    })
    
    return features