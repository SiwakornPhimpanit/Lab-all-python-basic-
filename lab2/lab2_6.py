import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lab2/sample_data/california_housing_test.csv")
xs = df["longitude"]
ys = df["latitude"]
print(xs)

print("Thunyarat")

plt.scatter(xs, ys)
plt.title("Thunyarat")
plt.show()
