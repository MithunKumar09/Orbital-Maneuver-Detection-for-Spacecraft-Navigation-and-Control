# src/evaluation.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def evaluate_maneuver_detection(detected_data, reference_data):
    merged_data = detected_data.merge(reference_data, left_index=True, right_index=True, how='inner')

    y_true = merged_data['Detected_Maneuver']
    y_pred = merged_data['Detected_Maneuver']
    
    # Evaluate the accuracy, precision, recall, f1_score, roc_auc
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='binary'),
        'recall': recall_score(y_true, y_pred, average='binary'),
        'f1_score': f1_score(y_true, y_pred, average='binary'),
        'roc_auc': roc_auc_score(y_true, y_pred)
    }
    
    return metrics

