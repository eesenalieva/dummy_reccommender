###  CODING SOLUTIONS FOR THE ASSESSMENT ASSIGNMENT AT SPICED ACADEMY
### SUBMITTED ON MARCH 28, 2022


# Task1. Read the csv file
import pandas as pd
import csv
with open ("datapoints.csv") as data:
    data = pd.read_csv("datapoints.csv")
    print(data.shape)
    print(data.head)

# Correlation between X and Y
cor_xy = data.corr()
print(cor_xy)

#Task2. Create a Scatterplot
import matplotlib.pyplot as plt
x = data["x"]
y_true = data["y"]
#Scatterplot for X and Y
plt.title("Scatterplot for X and Y")
plt.xlabel("X variable")
plt.ylabel("Y_true variable")
plt.scatter(x,y_true)
plt.show()

#Task3. Set the slope a to 10 and the intercept b to 0. Calculate y_pred for every value of x
y_pred = [item*10 for item in x]
# displaying X and Y_predicted
list_X = x
list_Y = y_pred
print("X |   Y_predicted")
for col_X, col_Y in zip(list_X, list_Y):
    print(col_X , "|", col_Y)

# Task4. MSE calculation
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_pred) # MSE calculated
print("MSE at a=10 and b=0 - ", mse) # MSE coded outcome confirmed by the semi-manual calculation in Excel

#Task5.Find a value for a that gives the lowest possible MSE.
import numpy as np
a = 10
tmp_MSE = np.infty
tmp_a = a
for i in range(100):
    Y_2 = (a-0.1*(i-1))*x
    tmp_a = (a-0.1*(i-1))
    MSE = np.square(np.subtract(y_true, Y_2)).mean()
    if MSE < tmp_MSE: # MSE comparison
        tmp_MSE = MSE
        tmp_A = tmp_a
print("A for the minimal MSE - ", tmp_A)
print("Minimal MSE - ", tmp_MSE)

#Task6. Repeat the procedure with b (initially b = 0)
b = 0
tmp_MSE = np.infty
tmp_b = b
for i in range(100):
    Y_pred = 10*x+(0-0.1*(i-1))
    tmp_b = (0-0.1*(i-1))
    MSE = np.square(np.subtract(y_true, Y_pred)).mean()
    if MSE < tmp_MSE: # temporary MSE comparison
        tmp_MSE = MSE
        tmp_B = b - tmp_b
print("B for the minimal MSE - ", tmp_B)
print("The minimal MSE - ", tmp_MSE)





