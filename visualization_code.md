# Visualization Code

```markdown
## Recommended Visualizations

### Chart 1: Optimize Discount Strategies
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('/Users/michalfischbein/projects/final project flow/data_cleaned.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Discount', y='Profit')

# Add titles and labels
plt.title('Relationship between Discount Percentage and Profit Margins')
plt.xlabel('Discount Percentage')
plt.ylabel('Profit Margin')

# Save the plot
plt.savefig('scatter_discount_vs_profit.png')
plt.show()
```

### Chart 2: Boost Marketing Efforts during High-Growth Seasons
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('/Users/michalfischbein/projects/final project flow/data_cleaned.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Aggregate sales over time
sales_time = df.resample('M', on='Order Date').sum()

# Plot line chart
plt.figure(figsize=(12, 6))
plt.plot(sales_time.index, sales_time['Sales'])

# Titles and labels
plt.title('Sales Volume Over Time with Peak Period Annotations')
plt.xlabel('Order Date')
plt.ylabel('Sales Volume')

# Save plot
plt.savefig('line_sales_over_time.png')
plt.show()
```

### Chart 3: Analyze and Mimic Successful Outlier Events
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('/Users/michalfischbein/projects/final project flow/data_cleaned.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Identify outliers based on sales
df['is_outlier'] = (np.abs(df['Sales'] - df['Sales'].mean()) > 3 * df['Sales'].std())

# Aggregate sales over time
sales_time = df.resample('M', on='Order Date').sum()

# Plot bar chart
plt.figure(figsize=(12, 6))
plt.bar(sales_time.index, sales_time['Sales'], color=['red' if is_out else 'blue' for is_out in sales_time['is_outlier']])

# Add titles and labels
plt.title('Sales Volume with Outliers Highlighted')
plt.xlabel('Order Date')
plt.ylabel('Sales Volume')

# Save plot
plt.savefig('bar_sales_outliers.png')
plt.show()
```
```