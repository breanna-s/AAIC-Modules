"""
Water Quality Analysis Module
Functions for analyzing water quality parameters
"""

import numpy as np
import matplotlib.pyplot as plt


def analyze_ph(samples=100, mean_ph=7.0, std_dev=0.5):
    """
    Analyze pH levels in water samples
    
    Parameters:
    -----------
    samples : int
        Number of samples to analyze (default: 100)
    mean_ph : float
        Expected mean pH (default: 7.0)
    std_dev : float
        Standard deviation (default: 0.5)
        
    Returns:
    --------
    ph_levels : array
        Array of pH measurements
    """
    ph_levels = np.random.normal(mean_ph, std_dev, samples)
    
    print("=" * 50)
    print("pH ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Number of samples: {samples}")
    print(f"Average pH: {np.mean(ph_levels):.2f}")
    print(f"Standard deviation: {np.std(ph_levels):.2f}")
    print(f"pH Range: {np.min(ph_levels):.2f} - {np.max(ph_levels):.2f}")
    
    # Determine water quality based on pH
    avg_ph = np.mean(ph_levels)
    if 6.5 <= avg_ph <= 8.5:
        print("✓ pH is within safe drinking water range (6.5-8.5)")
    else:
        print("⚠ pH is outside safe drinking water range!")
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.hist(ph_levels, bins=20, edgecolor='black', alpha=0.7, color='skyblue')
    plt.xlabel('pH Level', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Distribution of Water pH Levels', fontsize=14, fontweight='bold')
    plt.axvline(7.0, color='green', linestyle='--', linewidth=2, label='Neutral pH (7.0)')
    plt.axvline(6.5, color='orange', linestyle='--', linewidth=1, label='Safe range limits')
    plt.axvline(8.5, color='orange', linestyle='--', linewidth=1)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    return ph_levels


def calculate_wqi(turbidity, dissolved_oxygen, temperature=20):
    """
    Calculate Water Quality Index
    
    Parameters:
    -----------
    turbidity : float
        Turbidity in NTU (0-10 scale, lower is better)
    dissolved_oxygen : float
        Dissolved oxygen in mg/L (higher is better)
    temperature : float
        Water temperature in Celsius (default: 20)
        
    Returns:
    --------
    wqi : float
        Water Quality Index (0-100)
    status : str
        Quality classification
    """
    # Calculate WQI using weighted average
    # DO weight: 60%, Turbidity weight: 40%
    wqi = (dissolved_oxygen * 0.6 + (10 - turbidity) * 0.4) * 10
    
    # Determine status
    if wqi > 80:
        status = "Excellent"
        emoji = "🌟"
    elif wqi > 60:
        status = "Good"
        emoji = "✓"
    elif wqi > 40:
        status = "Fair"
        emoji = "⚠"
    else:
        status = "Poor"
        emoji = "✗"
    
    print("=" * 50)
    print("WATER QUALITY INDEX")
    print("=" * 50)
    print(f"Turbidity: {turbidity:.1f} NTU")
    print(f"Dissolved Oxygen: {dissolved_oxygen:.1f} mg/L")
    print(f"Temperature: {temperature:.1f}°C")
    print(f"\nWater Quality Index: {wqi:.1f}/100")
    print(f"Status: {emoji} {status}")
    print("=" * 50)
    
    return wqi, status


def compare_samples(sample_a, sample_b, param_name="pH"):
    """
    Compare two sets of water samples
    
    Parameters:
    -----------
    sample_a : array-like
        First set of measurements
    sample_b : array-like
        Second set of measurements
    param_name : str
        Name of parameter being measured
    """
    mean_a = np.mean(sample_a)
    mean_b = np.mean(sample_b)
    std_a = np.std(sample_a)
    std_b = np.std(sample_b)
    
    print(f"\nCOMPARISON: {param_name}")
    print("-" * 40)
    print(f"Sample A - Mean: {mean_a:.2f}, Std: {std_a:.2f}")
    print(f"Sample B - Mean: {mean_b:.2f}, Std: {std_b:.2f}")
    print(f"Difference: {abs(mean_a - mean_b):.2f}")
    
    # Visual comparison
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.hist(sample_a, bins=15, alpha=0.7, color='blue', label='Sample A', edgecolor='black')
    plt.hist(sample_b, bins=15, alpha=0.7, color='red', label='Sample B', edgecolor='black')
    plt.xlabel(param_name)
    plt.ylabel('Frequency')
    plt.title('Distribution Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.boxplot([sample_a, sample_b], labels=['Sample A', 'Sample B'])
    plt.ylabel(param_name)
    plt.title('Box Plot Comparison')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def generate_sample_data(location="River", days=30):
    """
    Generate realistic sample water quality data
    
    Parameters:
    -----------
    location : str
        Location name (default: "River")
    days : int
        Number of days of data (default: 30)
        
    Returns:
    --------
    data : dict
        Dictionary with pH, turbidity, and dissolved_oxygen arrays
    """
    np.random.seed(42)  # For reproducibility
    
    data = {
        'ph': np.random.normal(7.2, 0.3, days),
        'turbidity': np.random.uniform(2, 8, days),
        'dissolved_oxygen': np.random.normal(8.5, 1.5, days),
        'temperature': np.random.normal(18, 3, days)
    }
    
    print(f"Generated {days} days of data for {location}")
    print(f"Parameters: pH, Turbidity, Dissolved Oxygen, Temperature")
    
    return data


def plot_time_series(data, title="Water Quality Over Time"):
    """
    Plot water quality parameters over time
    
    Parameters:
    -----------
    data : dict
        Dictionary with parameter arrays
    title : str
        Plot title
    """
    days = len(data['ph'])
    time = np.arange(1, days + 1)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # pH
    axes[0, 0].plot(time, data['ph'], marker='o', color='blue', linewidth=2)
    axes[0, 0].axhline(7.0, color='green', linestyle='--', alpha=0.5, label='Neutral')
    axes[0, 0].set_xlabel('Day')
    axes[0, 0].set_ylabel('pH')
    axes[0, 0].set_title('pH Levels')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    
    # Turbidity
    axes[0, 1].plot(time, data['turbidity'], marker='s', color='brown', linewidth=2)
    axes[0, 1].set_xlabel('Day')
    axes[0, 1].set_ylabel('Turbidity (NTU)')
    axes[0, 1].set_title('Turbidity')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Dissolved Oxygen
    axes[1, 0].plot(time, data['dissolved_oxygen'], marker='^', color='green', linewidth=2)
    axes[1, 0].axhline(8.0, color='red', linestyle='--', alpha=0.5, label='Min. healthy')
    axes[1, 0].set_xlabel('Day')
    axes[1, 0].set_ylabel('Dissolved Oxygen (mg/L)')
    axes[1, 0].set_title('Dissolved Oxygen')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    
    # Temperature
    axes[1, 1].plot(time, data['temperature'], marker='d', color='red', linewidth=2)
    axes[1, 1].set_xlabel('Day')
    axes[1, 1].set_ylabel('Temperature (°C)')
    axes[1, 1].set_title('Water Temperature')
    axes[1, 1].grid(True, alpha=0.3)
    
    fig.suptitle(title, fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()