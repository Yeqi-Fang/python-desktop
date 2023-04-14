import numpy as np
import datetime


# add two number
def add(a, b):
    return a + b
# return a string of the datetime
def get_datetime():
    return str(datetime.datetime.now())


# get a random string with a-z and 0-9
def get_random_string():
    return ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz0123456789'), 10))

# get a random string with both letters and numbers with the length of 20
def get_random_string_20():
    return ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz0123456789'), 20))

# get a random string with both letters and numbers with the length of 20 without reptation
def get_random_string_20_without_reptation():
    return ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz0123456789'), 20, replace=False))

a = get_random_string_20()
print(a)
b = get_random_string_20_without_reptation()
print(b)

def add_two(a, b):
    return a + b

def get_a_simple_CNN_model():
    # using pytorch
    import torch
    import torch.nn as nn
    import torch.nn.functional as F

    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            # 1 input image channel, 6 output channels, 5x5 square convolution
            # kernel
            self.conv1 = nn.Conv2d(1, 6, 5)
            self.conv2 = nn.Conv2d(6, 16, 5)
            # an affine operation: y = Wx + b
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            # Max pooling over a (2, 2) window
            x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
            # If the size is a square you can only specify a single number
            x = F.max_pool2d(F.relu(self.conv2(x)), 2)
            x = x.view(-1, self.num_flat_features(x))
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

        def num_flat_features(self, x):
            size = x.size()[1:]  # all dimensions except the batch dimension
            num_features = 1
            for s in size:
                num_features *= s
            return num_features

    net = Net()
    return net