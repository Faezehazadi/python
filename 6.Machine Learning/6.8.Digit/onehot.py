import numpy as np
class OneHotEncoder:
    def fit_transform(self, y):
        """Custom implementation of OneHotEncoder"""
        n_classes = np.max(y) + 1
        one_hot = np.eye(n_classes)[y]
        return one_hot
    
    def inverse_transform(self, one_hot):
        """Custom implementation of OneHotDecoder"""
        return np.argmax(one_hot, axis=1)
