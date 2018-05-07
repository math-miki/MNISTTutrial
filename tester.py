import sys, os
sys.path.append(os.pardir)
import numpy as np

class Tester:
    def __init__(self, W1,b1,W2,b2):
        self.W1 = W1
        self.b1 = b1
        self.W2 = W2
        self.b2 = b2

    def predict(self, x):
        a1 = np.dot(x,self.W1) + self.b1
        z1 = self.sigmoid(a1)
        a2 = np.dot(z1,self.W2) + self.b2
        y = self.softmax(a2)
        return np.argmax(y)

    def sigmoid(self, a):
        return 1 / (1 + np.exp(-a))

    def softmax(self, a):
        c = np.max(a)
        exp_a = np.exp(a-c)
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a
        return y
