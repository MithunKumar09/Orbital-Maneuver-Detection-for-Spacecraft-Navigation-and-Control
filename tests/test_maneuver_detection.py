#tests/test_maneuver_detection.py
import unittest
import pandas as pd
from src.maneuver_detection import detect_maneuvers

class TestManeuverDetection(unittest.TestCase):
    
    def test_detect_maneuvers(self):
        """Test maneuver detection functionality."""
        data = pd.DataFrame({
            'Datetime': pd.date_range(start='2023-01-01', periods=10, freq='H'),
            'SMA': [100, 101, 102, 103, 104, 110, 111, 112, 113, 114]
        }).set_index('Datetime')
        
        detected_data = detect_maneuvers(data, window=1, threshold=5)
        
        self.assertIn('Maneuver', detected_data.columns, "Maneuver column should be present in the detected data")
        self.assertEqual(detected_data['Maneuver'].sum(), 1, "There should be 1 detected maneuver")

if __name__ == '__main__':
    unittest.main()