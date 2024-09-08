#tests/test_feature_extraction.py

import unittest
import pandas as pd
from src.feature_extraction import extract_features

class TestFeatureExtraction(unittest.TestCase):
    
    def test_extract_features(self):
        """Test feature extraction functionality."""
        data = pd.DataFrame({
            'Datetime': pd.date_range(start='2023-01-01', periods=10, freq='H'),
            'SMA': [100, 101, 102, 103, 104, 110, 111, 112, 113, 114]
        }).set_index('Datetime')
        
        features = extract_features(data)
        
        self.assertTrue('Feature1' in features.columns, "Feature1 should be in the extracted features")
        self.assertTrue('Feature2' in features.columns, "Feature2 should be in the extracted features")
        self.assertEqual(features.shape[0], 10, "Number of rows in features should match input data")

if __name__ == '__main__':
    unittest.main()