# src/maneuver_detection.py
import pandas as pd
from src.feature_extraction import extract_sma_change

def detect_maneuvers(data, window=1, threshold=0.5):
    """
    Detect maneuvers in the orbital data, with improvements to handle subtle changes.
    """
    # Extract SMA variations with smoothing
    sma_variations = extract_sma_change(data, window=window)
    
    # Smooth further if needed to remove noise
    sma_variations_smoothed = sma_variations.rolling(window=window).mean()
    
    # Detect significant changes (maneuvers) using a dynamic threshold
    # Adjust the threshold to be adaptive based on standard deviation
    sma_std = sma_variations_smoothed.std()
    adaptive_threshold = max(threshold, sma_std)
    
    maneuvers = (sma_variations_smoothed > adaptive_threshold).astype(int)
    
    data['Detected_Maneuver'] = maneuvers
    return data