import numpy as np
import matplotlib.pyplot as plt
class MLP:
    def __init__(self, input_size, hidden_sizes, output_size, learning_rate):
        self.lr = learning_rate
        self.W1 = np.random.randn(input_size, hidden_sizes[0])
        self.B1 = np.random.randn(1, hidden_sizes[0])
        self.W2 = np.random.randn(hidden_sizes[0], hidden_sizes[1])
        self.B2 = np.random.randn(1, hidden_sizes[1])
        self.W3 = np.random.randn(hidden_sizes[1], output_size)
        self.B3 = np.random.randn(1, output_size)
    
    def sigmoid(self, X):
        return 1 / (1 + np.exp(-X))
    
    def softmax(self, X):
        exp_X = np.exp(X - np.max(X))  # For numerical stability
        return exp_X / np.sum(exp_X, axis=1, keepdims=True)
    
    def root_mean_squared_error(self, Y_true, Y_pred):
        return np.sqrt(np.mean((Y_true - Y_pred) ** 2))
    
    def forward(self, X):
        """Forward pass"""
        self.out1 = self.sigmoid(np.dot(X, self.W1) + self.B1)
        self.out2 = self.sigmoid(np.dot(self.out1, self.W2) + self.B2)
        self.out3 = self.softmax(np.dot(self.out2, self.W3) + self.B3)
        return self.out3
    
    def backward(self, X, Y):
        """Backward pass"""
        # Calculate error for output layer
        error = -2 * (Y - self.out3)
        grad_b3 = error
        grad_w3 = np.dot(self.out2.T, error)

        # Calculate error for second layer
        error = np.dot(error, self.W3.T) * self.out2 * (1 - self.out2)
        grad_b2 = error
        grad_w2 = np.dot(self.out1.T, error)

        # Calculate error for first layer
        error = np.dot(error, self.W2.T) * self.out1 * (1 - self.out1)
        grad_b1 = error
        grad_w1 = np.dot(X.T, error)

        # Update weights and biases
        self.W1 -= self.lr * grad_w1
        self.B1 -= self.lr * grad_b1.sum(axis=0)
        self.W2 -= self.lr * grad_w2
        self.B2 -= self.lr * grad_b2.sum(axis=0)
        self.W3 -= self.lr * grad_w3
        self.B3 -= self.lr * grad_b3.sum(axis=0)
    
    def fit(self, X_train, Y_train, X_test, Y_test, epochs=100):
        train_losses, train_accuracies = [], []
        test_losses, test_accuracies = [], []
        
        for epoch in range(epochs):
            # Forward pass and backward pass for training data
            Y_pred_train = self.forward(X_train)
            self.backward(X_train, Y_train)
            
            # Calculate loss and accuracy for training data
            train_loss = self.root_mean_squared_error(Y_train, Y_pred_train)
            train_accuracy = np.mean(np.argmax(Y_train, axis=1) == np.argmax(Y_pred_train, axis=1))
            train_losses.append(train_loss)
            train_accuracies.append(train_accuracy)
            
            # Forward pass for test data
            Y_pred_test = self.forward(X_test)
            
            # Calculate loss and accuracy for test data
            test_loss = self.root_mean_squared_error(Y_test, Y_pred_test)
            test_accuracy = np.mean(np.argmax(Y_test, axis=1) == np.argmax(Y_pred_test, axis=1))
            test_losses.append(test_loss)
            test_accuracies.append(test_accuracy)
            
            print(f"Epoch {epoch + 1}/{epochs} - Loss: {train_loss:.4f} - Accuracy: {train_accuracy:.4f} - Test Loss: {test_loss:.4f} - Test Accuracy: {test_accuracy:.4f}")
        
        # Plot loss and accuracy
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.plot(train_losses, label='Train Loss')
        plt.plot(test_losses, label='Test Loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.grid()
        plt.title('Loss Over Epochs')
        
        plt.subplot(1, 2, 2)
        plt.plot(train_accuracies, label='Train Accuracy')
        plt.plot(test_accuracies, label='Test Accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.title('Accuracy Over Epochs')
        plt.grid()
        plt.show()
    
    def predict(self, X):
        """Predict function"""
        Y_pred = self.forward(X)
        return np.argmax(Y_pred, axis=1)
    
    def evaluate(self, X, Y):
        """Evaluate function"""
        Y_pred = self.forward(X)
        accuracy = np.mean(np.argmax(Y, axis=1) == np.argmax(Y_pred, axis=1))
        loss = self.root_mean_squared_error(Y, Y_pred)
        return loss, accuracy