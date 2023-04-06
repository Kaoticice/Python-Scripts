## Linear Regression

# Strategy
# 1) Design model (input, output size, forward pass)
# 2) construct loss and optimizer
# 3) Training loop
#   Forward pass: Compute prediction
#   Backwards pass: gradients
#   Update our weights
#   Iterate

import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

## 0) Prepare data

# Generate a regression data set
# DON'T FORGET THE NOISE!! LOL
x_numpy, y_numpy = datasets.make_regression(n_samples = 100, n_features = 1, noise = 20, random_state = 1)

x = torch.from_numpy(x_numpy.astype(np.float32))
y = torch.from_numpy(y_numpy.astype(np.float32))

# reshape data using .view and .shape
y = y.view(y.shape[0], 1)

n_samples, n_features = x.shape

## 1) Model

# one layer
input_size = n_features
output_size = 1 # Number of values per sample we put in
model = nn.Linear(input_size, output_size)

## 2) Loss and optimizer

# Use built in function from pytorch
# Calculates the mean squared error.
learning_rate = 0.01
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)

## 3) Training Loop

# Define # epochos
num_epochs = 100

# For loop iterates through all epochs
for epoch in range(num_epochs):
  # forward pass and loss
  y_predicted = model(x)
  loss = criterion(y_predicted, y)

  # Backward pass

  # Loss propogation backward, calculates gradients for us. 
  loss.backward()

  # Update
  optimizer.step()

  # Empty gradients
  optimizer.zero_grad()

  if (epoch + 1) % 10 == 0:
    print(f'epoch: {epoch + 1}, loss = {loss.item():.4f}')

## 4) plot 

# detach tensor, generates new tensor where our gradient calculation is false. 
# once you've detached the gradient calculation, convert it to numpy with .numpy()
predicted = model(x).detach().numpy()
plt.plot(x_numpy, y_numpy, 'ro')
plt.plot(x_numpy, predicted, 'b')
plt.show()