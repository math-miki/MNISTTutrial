import pickle
import numpy as np
class Exporter:
    def __init__(self):
        pass
    def exportNparray(self, npArray):
        np.savez("params.npz", W1=npArray["W1"], b1=npArray["b1"], W2=npArray["W2"], b2=npArray["b2"])
    def exportToPKL(self, data):
        with open("data.pickle", "wb") as f:
            pickle.dump(data, f)
