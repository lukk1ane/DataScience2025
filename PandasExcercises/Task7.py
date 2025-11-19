import pandas as pd

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Category': ['Electronics', 'Electronics', 'Clothes', 'Clothes', 'Toys', 'Toys', 'Sports', 'Sports'],
    'Price': [500, 1200, 300, 250, 150, 100, 800, 600],
    'Stock': [20, 5, 50, 30, 15, 8, 60, 2]
})

print(df.isnull())
print(df.notnull())

print("\nCategory counts:\n", df['Category'].value_counts())

print("\nTop 3 expensive:\n", df.nlargest(3, 'Price'))

print("\nLowest 2 stock:\n", df.nsmallest(2, 'Stock'))

print("\nShape:", df.shape)
print("Dimensions:", df.ndim)
