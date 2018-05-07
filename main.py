import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from TwoLayerNet import TwoLayerNet
from Common.layers import *
from Common.optimizers import *
from Common.Exporter import *

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
accs=[]
print(x_train[0], x_train[0].shape)
def main(params=None):
    network = TwoLayerNet(input_size=784, hidden_size=150, output_size=10, params=params)
    optimizer = SGD()
    iters_num = 10000 # 何回勾配を見る...?
    train_size = x_train.shape[0]
    batch_size = 100 # 何等分する?

    learning_rate = 0.00018

    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    iter_per_epoch = max(train_size / batch_size, 1)

    for i in range(iters_num):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        grad = network.gradient(x_batch, t_batch)
        params = network.params
        #optimizer.update(params, grad)

        for key in ("W1", "b1", "W2", "b2"):
        #for key in ("W1", "b1", "W2", "b2", "W3", "b3"):
            #print(key, network.params[key].shape, grad[key].shape)
            params[key] -= learning_rate * grad[key]

        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)

        if i%iter_per_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
            print("train_acc->",train_acc,"test_acc->", test_acc)
    return network.params

def test(network):
    x, t = x_test,t_test

    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)
        if p == t[i]:
            # print(y,sum(y))
            # print(p)
            #print(t[i],"\n====================================================")
            accuracy_cnt += 1
        else:
            # showImg(x[i])
            pass

    print("IN TEST CASES","accuracy: "+str(float(accuracy_cnt)/len(x)))

def predict(network, x):
    W1, W2 = network["W1"],network["W2"]
    b1, b2 = network["b1"],network["b2"]
    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    y = softmax(a2)
    return y

def sigmoid(a):
    return 1 / (1 + np.exp(-a))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

if __name__ == '__main__':
    result = main()
    test(result)
    Ex = Exporter()
    Ex.exportNparray(result)
    #for a in range(10):
    #    result = main(result)
    #    test(result)
