# ==============================================================================
# 2. MATPLOTLIB & SEABORN: PROFESSIONAL VISUALIZATIONS
# ==============================================================================
print("\n" + "="*60)
print("             2. MATPLOTLIB & SEABORN SOLUTIONS")
print("="*60)

# Data Preparation for Plot 2.3 (Satisfaction by Day)
satisfaction_by_day = df.groupby('Day_of_Week')['Satisfaction'].mean().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# Data Preparation for Plot 2.4 (Sale Categories)
category_counts = df['Category'].value_counts()

# Create a 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Professional Data Visualizations (2x2 Subplot Grid)', fontsize=16, y=1.02)


## Plot 2.1: Category Revenue (Horizontal Bar Chart)
ax1 = axes[0, 0]
# Use the category_summary DataFrame from the Pandas task
sns.barplot(
    x='Total_Revenue',
    y=category_summary.index,
    data=category_summary.reset_index(),
    ax=ax1,
    palette='viridis'
)
ax1.set_title('2.1 Total Revenue by Category (Sorted)', fontsize=12)
ax1.set_xlabel('Total Revenue ($)')
ax1.set_ylabel('Category')
# Add values on bars (labels)
for i, (revenue, category) in enumerate(zip(category_summary['Total_Revenue'], category_summary.index)):
    ax1.text(revenue + 10, i, f'${revenue:,.0f}', va='center')


## Plot 2.2: Transaction Distribution (Histogram with KDE)
ax2 = axes[0, 1]
sns.histplot(
    df['Total_Sale_Amount'],
    kde=True, # Show KDE overlay
    ax=ax2,
    color='purple',
    bins=15
)
ax2.set_title('2.2 Distribution of Total Sale Amounts (with KDE)', fontsize=12)
ax2.set_xlabel('Total Sale Amount ($)')
ax2.set_ylabel('Frequency')
# Show mean and median lines
mean_val = df['Total_Sale_Amount'].mean()
median_val = df['Total_Sale_Amount'].median()
ax2.axvline(mean_val, color='red', linestyle='--', label=f'Mean ({mean_val:.2f})')
ax2.axvline(median_val, color='green', linestyle='-', label=f'Median ({median_val:.2f})')
ax2.legend()


## Plot 2.3: Satisfaction by Day (Line Plot with Markers)
ax3 = axes[1, 0]
satisfaction_by_day.plot(
    kind='line',
    marker='o', # Add markers
    ax=ax3,
    color='darkorange'
)
ax3.set_title('2.3 Average Customer Satisfaction by Day of Week', fontsize=12)
ax3.set_xlabel('Day of Week')
ax3.set_ylabel('Average Satisfaction (1-5)')
ax3.tick_params(axis='x', rotation=0)
ax3.grid(True, linestyle='--', alpha=0.7) # Add grid lines


## Plot 2.4: Sale Categories (Pie Chart with Percentages)
ax4 = axes[1, 1]
# Calculate percentages for the labels
wedges, texts, autotexts = ax4.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct='%1.1f%%', # Display percentages (e.g., 25.0%)
    startangle=90,
    wedgeprops={'edgecolor': 'black'},
    colors=sns.color_palette("Set2") # Use distinct colors
)
ax4.set_title('2.4 Count of Transactions by Sale Category', fontsize=12)
ax4.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout() # Adjust layout to prevent overlap
plt.show()