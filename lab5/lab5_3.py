# lab5_3.py: ดึง longitude และ latitude ออกมาแสดงผล (Cell 12)
import pandas as pd

df = pd.read_csv("sample_data/california_housing_test.csv")
xs = df["longitude"]
ys = df["latitude"]

print("xs (longitude):")
print(xs)
print("\nys (latitude):")
print(ys)

