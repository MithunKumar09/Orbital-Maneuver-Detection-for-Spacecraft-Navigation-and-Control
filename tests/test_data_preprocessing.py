# tests/test_data_preprocessing.py
import unittest
import pandas as pd
from src.data_preprocessing import load_data, clean_data

class TestDataPreprocessing(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Load data once for all tests to avoid repetition."""
        cls.data_path = 'data/SMA_data.csv'
        cls.data = load_data(cls.data_path)
    
    def test_load_data(self):
        """Test if the data is loaded correctly."""
        self.assertIsInstance(self.data, pd.DataFrame)
        self.assertFalse(self.data.empty, "Data should not be empty")

    def test_clean_data(self):
        """Test cleaning of data with missing values and duplicates."""
        # Create dummy data with missing values and duplicates
        data = pd.DataFrame({
            'DateTime': pd.date_range('2024-01-01', periods=5, freq='D'),
            'SMA': [7000, None, 7002, 7003, None]
        }).set_index('DateTime')
        
        # Clean the data
        cleaned_data = clean_data(data)
        
        # Check if missing values are filled and duplicates removed
        self.assertFalse(cleaned_data.isnull().any().any(), "Data should not have missing values")
        self.assertEqual(cleaned_data.shape[0], 3, "Data should have 3 rows after cleaning")

if __name__ == '__main__':
    unittest.main()