import numpy as np


# sigmoid function
def nonlin(x, deriv=False):
    if (deriv == True):
        return (x * (1 - x))

    return 1 / (1 + np.exp(-x))


# input data
x = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output data
y = np.array(([0],
              [1],
              [1],
              [0],))

# seeding - functionality starting at 1
np.random.seed(1)

# synapses
syn0 = 2 * np.random.random((3, 4)) - 1  # 3 inputs, 4 outputs
syn1 = 2 * np.random.random((4, 1)) - 1  # 4 inputs, 1 output

# training
for j in range(60000):
    # building layers
    l0 = x
    l1 = nonlin(np.dot(l0, syn0))  # syn0 dauginam is l0
    l2 = nonlin(np.dot(l1, syn1))

    # backpropagation - machine learning is here
    l2_error = y - l2
    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))

    # calculating deltas
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)

    # updating our synapsis
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print("Output after training")
print(l2)

