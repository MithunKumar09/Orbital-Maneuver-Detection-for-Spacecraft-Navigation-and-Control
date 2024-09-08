#tests/test_evaluation.py
import unittest
import pandas as pd
from src.evaluation import evaluate_maneuver_detection

class TestEvaluation(unittest.TestCase):
    
    def test_evaluate_detection(self):
        """Test evaluation metrics for maneuver detection."""
        true_data = pd.DataFrame({
            'Datetime': pd.date_range(start='2023-01-01', periods=10, freq='H'),
            'Maneuver': [0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
        }).set_index('Datetime')
        
        detected_data = pd.DataFrame({
            'Datetime': pd.date_range(start='2023-01-01', periods=10, freq='H'),
            'Detected_Maneuver': [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
        }).set_index('Datetime')
        
        metrics = evaluate_maneuver_detection(detected_data, true_data)
        
        self.assertGreaterEqual(metrics['accuracy'], 0, "Accuracy should be a non-negative value")
        self.assertGreaterEqual(metrics['precision'], 0, "Precision should be a non-negative value")
        self.assertGreaterEqual(metrics['recall'], 0, "Recall should be a non-negative value")
        self.assertGreaterEqual(metrics['f1_score'], 0, "F1 Score should be a non-negative value")

if __name__ == '__main__':
    unittest.main()