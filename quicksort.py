import numpy as np

class randomArray:

    def __init__(self, n):
        np.random.randint(0,10,n)

    def print(self):
        pass


if __name__ == '__main__':
    ar = randomArray(5)
    print(ar)
    