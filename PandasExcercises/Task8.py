import pandas as pd

df = pd.DataFrame({
    'Student': ['Ana', 'Luka', 'Ana', 'Gio', 'Nino', 'Luka', 'Sopo', 'Mariam', 'Gio', 'Elene'],
    'Subject': ['Math', 'History', 'Physics', 'Math', 'CS', 'Physics', 'CS', 'Math', 'History', 'CS'],
    'Score': [85, 92, 78, 88, 65, 90, 82, 75, 81, 95],
    'Attendance': [90, 88, 80, 86, 70, 91, 95, 89, 85, 99]
})

# Identify duplicates based on Student column
print(df.duplicated(subset=['Student']))

# Remove duplicates, keep first occurrence
df_no_dup = df.drop_duplicates(subset=['Student'])
print("\nAfter dropping duplicates:\n", df_no_dup)

# Set index to Student
df_indexed = df.set_index('Student')
print("\nIndexed by Student:\n", df_indexed)

# loc[] - access by label (index)
print("\nloc['Luka']:\n", df_indexed.loc['Luka'])

# iloc[] - access by position
print("\niloc first 3:\n", df_indexed.iloc[:3])

# Query - filter using conditions
print("\nQuery > 80 score and > 85 attendance:\n",
      df.query('Score > 80 and Attendance > 85'))

# between() - filter by range
print("\nScores between 70 and 90:\n",
      df[df['Score'].between(70, 90)])
