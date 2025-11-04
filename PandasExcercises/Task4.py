import pandas as pd

df = pd.DataFrame({
    'A': range(1, 6),
    'B': list('abcde')
})

print("First 3 rows:\n", df.head(3))
print("\nLast 2 rows:\n", df.tail(2))

print("\nDefault head():\n", df.head())

print("\nhead(-2):\n", df.head(-2))
