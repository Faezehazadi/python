import numpy as np

class Perceptron:
    def __init__(self, input_size, lr, epochs):
        self.w = np.zeros(input_size)  
        self.b = 0                     
        self.lr = lr                   
        self.epochs = epochs           
        self.loss_history = []         

    def fit(self, X_train, y_train):
        for epoch in range(self.epochs):
            total_loss = 0
            for xi, yi in zip(X_train, y_train):
                prediction = np.dot(xi, self.w) + self.b
                error = yi - prediction
                self.w += self.lr * error * xi
                self.b += self.lr * error
                total_loss += error ** 2
            self.loss_history.append(total_loss / len(y_train))

    def predict(self, X_test):
        return np.dot(X_test, self.w) + self.b

    def evaluate(self, X_test, y_test):
        predictions = self.predict(X_test)
        mse = np.mean((y_test - predictions) ** 2)
        return mse