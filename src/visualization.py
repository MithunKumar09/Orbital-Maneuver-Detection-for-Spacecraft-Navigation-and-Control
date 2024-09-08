# src/visualization.py

import matplotlib.pyplot as plt

def plot_maneuvers(detected_data, output_file):
    """
    Plot the detected maneuvers and save the plot to a file.

    Parameters:
    detected_data (pd.DataFrame): Data with detected maneuvers.
    output_file (str): Path to the output file where the plot will be saved.
    """
    plt.figure(figsize=(12, 6))
    
    # Plot the SMA values
    plt.plot(detected_data.index, detected_data['SMA'], label='SMA', color='blue')
    
    # Highlight the detected maneuvers
    plt.scatter(detected_data.index, detected_data['SMA'], color='red', label='Detected Maneuvers', s=50, edgecolor='black')
    
    plt.xlabel('Datetime')
    plt.ylabel('SMA')
    plt.title('SMA with Detected Maneuvers')
    plt.legend()
    plt.grid(True)
    
    # Save the plot to the specified file
    plt.savefig(output_file)
    plt.close()

    print(f"Plot saved to {output_file}")