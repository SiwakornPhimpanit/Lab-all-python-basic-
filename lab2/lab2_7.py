import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lab2/sample_data/california_housing_test.csv")
xs = df["longitude"]
ys = df["latitude"]

print("Thunyarat")

plt.figure(figsize=(10, 8))
plt.scatter(xs, ys, c=df['median_house_value'], s=df['population']/100, cmap='viridis', alpha=0.4)
plt.colorbar(label='Median House Value')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('California Housing: Median House Value and Population Density - Thunyarat')
plt.show()
