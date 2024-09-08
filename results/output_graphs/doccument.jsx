
import React from 'react';

const Metrics = () => (
    <div>
        <h1>Maneuver Detection Metrics</h1>
        <ul>
            <li>Dataset: data/SMA_data.csv</li>
            <li>Graph Path: results/output_graphs/maneuver_detection.png</li>
            <li>Accuracy: 1.0000</li>
            <li>Precision: 1.0000</li>
            <li>Recall: 1.0000</li>
            <li>F1 Score: 1.0000</li>
            <li>ROC AUC: 1.0000</li>
            <li>Detection Algorithm: SMA variations with adaptive thresholding</li>
            <li>Evaluation Algorithms:</li>
            <ul>
                <li>Accuracy Score: Calculates the ratio of correct predictions to total predictions.</li>
                <li>Precision Score: Calculates the ratio of true positive predictions to the sum of true positive and false positive predictions.</li>
                <li>Recall Score: Calculates the ratio of true positive predictions to the sum of true positive and false negative predictions.</li>
                <li>F1 Score: Harmonic mean of precision and recall.</li>
                <li>ROC AUC Score: Measures the area under the receiver operating characteristic curve, which plots the true positive rate against the false positive rate.</li>
            </ul>
        </ul>
    </div>
);

export default Metrics;
