import numpy as np
import matplotlib.pyplot as plt

def analyze_ph(samples=100):
    """Analyze pH levels"""
    ph_levels = np.random.normal(7.0, 0.5, samples)
    
    print(f"Average pH: {np.mean(ph_levels):.2f}")
    print(f"pH Range: {np.min(ph_levels):.2f} - {np.max(ph_levels):.2f}")
    
    plt.figure(figsize=(8, 5))
    plt.hist(ph_levels, bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('pH Level')
    plt.ylabel('Frequency')
    plt.title('Distribution of Water pH Levels')
    plt.axvline(7.0, color='red', linestyle='--', label='Neutral pH')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return ph_levels

def calculate_wqi(turbidity, dissolved_oxygen):
    """Calculate Water Quality Index"""
    wqi = (dissolved_oxygen * 0.6 + (10 - turbidity) * 0.4) * 10
    
    print(f"Water Quality Index: {wqi:.1f}")
    if wqi > 80:
        status = "Excellent"
    elif wqi > 60:
        status = "Good"
    elif wqi > 40:
        status = "Fair"
    else:
        status = "Poor"
    
    print(f"Status: {status}")
    return wqi, status