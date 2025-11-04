import pandas as pd

df = pd.DataFrame({
    'Item': ['Book', 'Pen', 'Bag', 'Shoes', 'Watch'],
    'Cost': [30, 5, 45, 60, 80]
})

df['Tax'] = df['Cost'] * 0.10
df['Total'] = df['Cost'] + df['Tax']

filtered = df[df['Total'] > 50]

print(filtered)
