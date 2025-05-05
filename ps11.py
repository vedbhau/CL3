#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ArtificialImmuneSystem:
    def __init__(self, n_detectors=100, radius=0.5):
        self.n_detectors = n_detectors  # Number of detector cells
        self.radius = radius            # Detection radius
        self.detectors = None           # Will store our detector cells
    
    def generate_detectors(self, normal_data):
        """Generate detector cells that don't match normal patterns"""
        n_features = normal_data.shape[1]
        detectors = []
        
        while len(detectors) < self.n_detectors:
            # Generate random candidate detector
            candidate = np.random.uniform(low=normal_data.min(), 
                                         high=normal_data.max(), 
                                         size=n_features)
            
            # Check if candidate doesn't match any normal sample
            match = False
            for sample in normal_data:
                if np.linalg.norm(candidate - sample) < self.radius:
                    match = True
                    break
            
            if not match:
                detectors.append(candidate)
        
        self.detectors = np.array(detectors)
    
    def predict(self, X):
        """Classify samples as normal (0) or damaged (1)"""
        predictions = []
        for sample in X:
            damaged = False
            for detector in self.detectors:
                if np.linalg.norm(detector - sample) < self.radius:
                    damaged = True
                    break
            predictions.append(1 if damaged else 0)
        return np.array(predictions)

# Generate synthetic structural health monitoring data
# Features could be vibration frequencies, mode shapes, etc.
# Class 0 = normal structure, Class 1 = damaged structure
X, y = make_classification(n_samples=1000, n_features=5, n_classes=2, 
                          n_clusters_per_class=1, random_state=42)

# Split into training (normal data only) and test sets
X_normal = X[y == 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the AIS (only use normal data for training)
ais = ArtificialImmuneSystem(n_detectors=150, radius=0.8)
ais.generate_detectors(X_normal)

# Test the classifier
y_pred = ais.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Number of detectors generated: {len(ais.detectors)}")

