#Gradient Descent for Iris
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
iris_data = pd.read_csv(url, names=column_names)

print(iris_data.head())

df = pd.DataFrame(data, columns=iris.variables.names + ['target'])


print(df.head())

X = df.drop('target', axis=1)
y = df['target']

X_normalized = (X - X.min()) / (X.max() - X.min())

X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

def compute_gradients(x, y, w, b):
    m = len(y)
    dw = np.dot(x.T, (np.dot(x, w) + b - y)) / m
    db = np.sum(np.dot(x, w) + b - y) / m
    return dw, db

def gradient_descent(x_train, y_train, w, b, learning_rate, num_iterations, threshold=None):
    costs = []
    for i in range(num_iterations):
        dw, db = compute_gradients(x_train, y_train, w, b)
        w -= learning_rate * dw
        b -= learning_rate * db
        cost = compute_cost(x_train, y_train, w, b)
        costs.append(cost)
        if threshold is not None and cost < threshold:
            break
        if i % 100 == 0:
            print(f"Iteration {i}, Cost: {cost}")
    return w, b, costs

def compute_cost(x_train, y_train, w, b):
    m = len(y_train)
    cost = np.sum((np.dot(x_train, w) + b - y_train) ** 2) / (2 * m)
    return cost

X_train = np.array(X_train)
y_train = np.array(y_train)
w_init = np.random.rand(X_train.shape[1], 1)
b_init = 0

learning_rate = 0.01
num_iterations = 1000
threshold = 0.01
w_trained, b_trained, costs = gradient_descent(X_train, y_train, w_init, b_init, learning_rate, num_iterations, threshold)

plt.plot(costs)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost vs Iterations")
plt.show()

final_cost = compute_cost(X_train, y_train, w_trained, b_trained)
print("Final Cost:", final_cost)
