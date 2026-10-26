# lab5_4.py: พล็อตจุดแผนที่ California พิกัดพื้นฐาน (Cell 13)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data/california_housing_test.csv")
xs = df["longitude"]
ys = df["latitude"]

print("Thunyarat")

plt.scatter(xs, ys)
plt.title("Thunyarat")
plt.show()

