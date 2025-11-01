import pandas as pd
import numpy as np
import sys
from datetime import datetime
from scipy import stats

# =====================================================
# הגדרת Logger - כותב גם למסך וגם לקובץ MD
# =====================================================
class TeeLogger:
    """מחלקה שכותבת גם למסך וגם לקובץ MD מעוצב"""
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, 'w', encoding='utf-8')
        
        # כתיבת כותרת MD
        self.log.write("# 📊 דוח ניתוח סטטיסטי מקיף - Superstore Dataset\n\n")
        self.log.write(f"**תאריך:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
        self.log.write(f"**שעה:** {datetime.now().strftime('%H:%M:%S')}\n\n")
        self.log.write(f"**קובץ מקור:** data_cleaned.csv\n\n")
        self.log.write("---\n\n")
        self.log.write("## 📋 תוכן עניינים\n\n")
        self.log.write("1. [Part 1: Foundation](#part-1-foundation)\n")
        self.log.write("2. [Part 2: Distributions & Relationships](#part-2-distributions--relationships)\n")
        self.log.write("3. [Part 3: Profitability](#part-3-profitability)\n")
        self.log.write("4. [Part 4: Category Breakdown](#part-4-category-breakdown)\n")
        self.log.write("5. [Part 5: Operational Analysis](#part-5-operational-analysis)\n")
        self.log.write("6. [Part 6: Time Series Analysis](#part-6-time-series-analysis)\n")
        self.log.write("7. [Part 7: Combined Analysis](#part-7-combined-analysis)\n")
        self.log.write("8. [Part 8: Top & Bottom Lists](#part-8-top--bottom-lists)\n\n")
        self.log.write("---\n\n")
    
    def write(self, message):
        self.terminal.write(message)
        md_message = message.replace("="*80, "\n---\n")
        self.log.write(md_message)
    
    def flush(self):
        self.terminal.flush()
        self.log.flush()
    
    def close(self):
        self.log.write("\n---\n\n")
        self.log.write(f"**הסתיים בשעה:** {datetime.now().strftime('%H:%M:%S')}\n\n")
        self.log.write("---\n\n")
        self.log.write("*דוח זה הופק אוטומטית על ידי סקריפט הניתוח הסטטיסטי*\n")
        self.log.close()

# הפעלת הלוגר
log_file = 'statistical_analysis_report.md'
logger = TeeLogger(log_file)
sys.stdout = logger

print("="*80)
print("🚀 התחלת ניתוח סטטיסטי מקיף")
print("="*80)
print()

# =====================================================
# טעינת הנתונים
# =====================================================
print("📥 טעינת קובץ הנתונים הנקי...")
df = pd.read_csv('data_cleaned.csv')

# המרת תאריכים
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# חישוב ימי משלוח
df['Delivery_Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# יצירת עמודות זמן
df['Year'] = df['Order Date'].dt.year
df['Quarter'] = df['Order Date'].dt.quarter
df['Month'] = df['Order Date'].dt.month
df['DayOfWeek'] = df['Order Date'].dt.day_name()

# זיהוי עמודות One-Hot
segment_cols = [c for c in df.columns if c.startswith('Segment_')]
region_cols = [c for c in df.columns if c.startswith('Region_')]
category_cols = [c for c in df.columns if c.startswith('Category_')]
subcategory_cols = [c for c in df.columns if c.startswith('Sub-Category_')]
shipmode_cols = [c for c in df.columns if c.startswith('Ship Mode_')]

# המרה חזרה לעמודות קטגוריאליות לניתוח
def decode_onehot(row, cols, prefix):
    """המרה מ-One-Hot חזרה לקטגוריה"""
    for col in cols:
        if row[col] == 1:
            return col.replace(prefix, '')
    return prefix.replace('_', '') + '_Base'  # הקטגוריה שהושמטה ב-drop_first

df['Segment'] = df.apply(lambda row: decode_onehot(row, segment_cols, 'Segment_'), axis=1)
df['Region'] = df.apply(lambda row: decode_onehot(row, region_cols, 'Region_'), axis=1)
df['Category'] = df.apply(lambda row: decode_onehot(row, category_cols, 'Category_'), axis=1)
df['Sub_Category'] = df.apply(lambda row: decode_onehot(row, subcategory_cols, 'Sub-Category_'), axis=1)
df['Ship_Mode'] = df.apply(lambda row: decode_onehot(row, shipmode_cols, 'Ship Mode_'), axis=1)

print(f"✅ נטענו {len(df):,} שורות מהקובץ\n")

# =====================================================
# PART 1: FOUNDATION
# =====================================================
print("="*80)
print("📊 PART 1: FOUNDATION")
print("="*80)
print()

# ----------------------------------------
# 1. סקירה כללית
# ----------------------------------------
print("### 1️⃣ סקירה כללית (Dataset Overview)\n")

overview_data = {
    'Metric': [
        'Total Rows',
        'Total Columns',
        'Start Date',
        'End Date',
        'Date Range (Days)',
        'Date Range (Months)',
        'Memory Usage (MB)'
    ],
    'Value': [
        f"{len(df):,}",
        df.shape[1],
        df['Order Date'].min().strftime('%Y-%m-%d'),
        df['Order Date'].max().strftime('%Y-%m-%d'),
        (df['Order Date'].max() - df['Order Date'].min()).days,
        round((df['Order Date'].max() - df['Order Date'].min()).days / 30, 1),
        round(df.memory_usage(deep=True).sum() / 1024**2, 2)
    ]
}

overview_df = pd.DataFrame(overview_data)
print(overview_df.to_markdown(index=False))
print("\n")

# ----------------------------------------
# 2. Missing Data & Quality
# ----------------------------------------
print("### 2️⃣ Missing Data & Quality Check\n")

missing_data = pd.DataFrame({
    'Column': df.columns,
    'Missing Count': df.isnull().sum().values,
    'Missing %': (df.isnull().sum().values / len(df) * 100).round(2)
})
missing_data = missing_data[missing_data['Missing Count'] > 0]

if len(missing_data) > 0:
    print("**⚠️ Columns with Missing Values:**\n")
    print(missing_data.to_markdown(index=False))
else:
    print("✅ **No Missing Values Found**")

print("\n**Quality Checks:**\n")

quality_checks = []
# בדיקת ערכים שליליים
quality_checks.append({
    'Check': 'Negative Sales',
    'Count': len(df[df['Sales'] < 0]),
    'Status': '✅ OK' if len(df[df['Sales'] < 0]) == 0 else '⚠️ Found'
})
quality_checks.append({
    'Check': 'Negative Quantity',
    'Count': len(df[df['Quantity'] < 0]),
    'Status': '✅ OK' if len(df[df['Quantity'] < 0]) == 0 else '⚠️ Found'
})
quality_checks.append({
    'Check': 'Discount > 1',
    'Count': len(df[df['Discount'] > 1]),
    'Status': '✅ OK' if len(df[df['Discount'] > 1]) == 0 else '⚠️ Found'
})
quality_checks.append({
    'Check': 'Discount < 0',
    'Count': len(df[df['Discount'] < 0]),
    'Status': '✅ OK' if len(df[df['Discount'] < 0]) == 0 else '⚠️ Found'
})

quality_df = pd.DataFrame(quality_checks)
print(quality_df.to_markdown(index=False))
print("\n")

# ----------------------------------------
# 3. Descriptive Statistics
# ----------------------------------------
print("### 3️⃣ סטטיסטיקות תיאוריות (Descriptive Statistics)\n")

numeric_cols = ['Sales', 'Quantity', 'Discount', 'Profit', 'Delivery_Days']
desc_stats = df[numeric_cols].describe().T

# הוספת עמודות נוספות
desc_stats['Range'] = desc_stats['max'] - desc_stats['min']
desc_stats['Variance'] = df[numeric_cols].var()

# עיצוב
desc_stats = desc_stats[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'Range', 'Variance']]
desc_stats = desc_stats.round(2)

print(desc_stats.to_markdown())
print("\n")

# ----------------------------------------
# 4. Key Performance Indicators
# ----------------------------------------
print("### 4️⃣ מדדים עיקריים (Key Performance Indicators)\n")

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)
avg_order_value = total_sales / total_orders
overall_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
profitable_orders = len(df[df['Profit'] > 0])
profitable_pct = (profitable_orders / total_orders * 100)

kpis = pd.DataFrame({
    'KPI': [
        'Total Sales',
        'Total Profit',
        'Total Orders',
        'Average Order Value',
        'Overall Profit Margin',
        'Profitable Orders',
        'Profitable Orders %',
        'Loss-Making Orders',
        'Loss-Making Orders %'
    ],
    'Value': [
        f"${total_sales:,.2f}",
        f"${total_profit:,.2f}",
        f"{total_orders:,}",
        f"${avg_order_value:.2f}",
        f"{overall_margin:.2f}%",
        f"{profitable_orders:,}",
        f"{profitable_pct:.2f}%",
        f"{total_orders - profitable_orders:,}",
        f"{100 - profitable_pct:.2f}%"
    ]
})

print(kpis.to_markdown(index=False))
print("\n")

# =====================================================
# PART 2: DISTRIBUTIONS & RELATIONSHIPS
# =====================================================
print("="*80)
print("📊 PART 2: DISTRIBUTIONS & RELATIONSHIPS")
print("="*80)
print()

# ----------------------------------------
# 5. Distributions Analysis
# ----------------------------------------
print("### 5️⃣ ניתוח התפלגויות (Distribution Analysis)\n")

dist_analysis = []
for col in ['Sales', 'Quantity', 'Discount', 'Profit']:
    skew = df[col].skew()
    kurt = df[col].kurtosis()
    
    dist_analysis.append({
        'Variable': col,
        'Skewness': round(skew, 3),
        'Skew Interpretation': 'Right-skewed' if skew > 0.5 else ('Left-skewed' if skew < -0.5 else 'Symmetric'),
        'Kurtosis': round(kurt, 3),
        'Kurt Interpretation': 'Heavy-tailed' if kurt > 1 else ('Light-tailed' if kurt < -1 else 'Normal')
    })

dist_df = pd.DataFrame(dist_analysis)
print(dist_df.to_markdown(index=False))
print("\n")

# ----------------------------------------
# 6. Outliers Detection
# ----------------------------------------
print("### 6️⃣ זיהוי חריגות (Outliers Detection)\n")

outliers_analysis = []

for col in ['Sales', 'Quantity', 'Discount', 'Profit']:
    # IQR Method
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    iqr_outliers = len(df[(df[col] < lower_bound) | (df[col] > upper_bound)])
    iqr_pct = (iqr_outliers / len(df) * 100)
    
    # Z-score Method
    z_scores = np.abs(stats.zscore(df[col]))
    z_outliers = len(df[z_scores > 3])
    z_pct = (z_outliers / len(df) * 100)
    
    outliers_analysis.append({
        'Variable': col,
        'IQR Outliers': f"{iqr_outliers:,}",
        'IQR %': f"{iqr_pct:.2f}%",
        'Z-Score Outliers': f"{z_outliers:,}",
        'Z-Score %': f"{z_pct:.2f}%"
    })

outliers_df = pd.DataFrame(outliers_analysis)
print(outliers_df.to_markdown(index=False))
print("\n")

# ----------------------------------------
# 7. Correlation Matrix
# ----------------------------------------
print("### 7️⃣ מטריצת קורלציות (Correlation Matrix)\n")

corr_cols = ['Sales', 'Quantity', 'Discount', 'Profit', 'Delivery_Days']
corr_matrix = df[corr_cols].corr()

print("**Correlation Matrix:**\n")
print(corr_matrix.round(3).to_markdown())
print("\n")

# Strong correlations
print("**Strong Correlations (|r| > 0.5):**\n")
strong_corrs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        corr_val = corr_matrix.iloc[i, j]
        if abs(corr_val) > 0.5:
            strong_corrs.append({
                'Variable 1': corr_matrix.columns[i],
                'Variable 2': corr_matrix.columns[j],
                'Correlation': round(corr_val, 3),
                'Strength': 'Strong Positive' if corr_val > 0.7 else ('Strong Negative' if corr_val < -0.7 else 'Moderate')
            })

if strong_corrs:
    strong_corrs_df = pd.DataFrame(strong_corrs)
    print(strong_corrs_df.to_markdown(index=False))
else:
    print("*No strong correlations found (threshold: |r| > 0.5)*")
print("\n")

# =====================================================
# PART 3: PROFITABILITY
# =====================================================
print("="*80)
print("💰 PART 3: PROFITABILITY")
print("="*80)
print()

# ----------------------------------------
# 8. Profitability Analysis
# ----------------------------------------
print("### 8️⃣ ניתוח רווחיות (Profitability Analysis)\n")

df['Profit_Margin'] = (df['Profit'] / df['Sales'] * 100).replace([np.inf, -np.inf], 0)

profit_analysis = pd.DataFrame({
    'Metric': [
        'Average Profit Margin',
        'Median Profit Margin',
        'Profitable Orders',
        'Profitable Orders %',
        'Loss-Making Orders',
        'Loss-Making Orders %',
        'Break-Even Orders',
        'Total Profit (Profitable)',
        'Total Loss (Loss-Making)',
        'Net Profit'
    ],
    'Value': [
        f"{df['Profit_Margin'].mean():.2f}%",
        f"{df['Profit_Margin'].median():.2f}%",
        f"{len(df[df['Profit'] > 0]):,}",
        f"{len(df[df['Profit'] > 0]) / len(df) * 100:.2f}%",
        f"{len(df[df['Profit'] < 0]):,}",
        f"{len(df[df['Profit'] < 0]) / len(df) * 100:.2f}%",
        f"{len(df[df['Profit'] == 0]):,}",
        f"${df[df['Profit'] > 0]['Profit'].sum():,.2f}",
        f"${df[df['Profit'] < 0]['Profit'].sum():,.2f}",
        f"${df['Profit'].sum():,.2f}"
    ]
})

print(profit_analysis.to_markdown(index=False))
print("\n")

# ----------------------------------------
# 9. Discount Impact Analysis
# ----------------------------------------
print("### 9️⃣ ניתוח השפעת הנחות (Discount Impact Analysis)\n")

print("**Correlations with Discount:**\n")
discount_corr = pd.DataFrame({
    'Variable': ['Sales', 'Profit', 'Quantity', 'Profit Margin'],
    'Correlation with Discount': [
        round(df['Discount'].corr(df['Sales']), 3),
        round(df['Discount'].corr(df['Profit']), 3),
        round(df['Discount'].corr(df['Quantity']), 3),
        round(df['Discount'].corr(df['Profit_Margin']), 3)
    ]
})
print(discount_corr.to_markdown(index=False))
print("\n")

print("**Analysis by Discount Range:**\n")
df['Discount_Range'] = pd.cut(df['Discount'], bins=[0, 0.01, 0.1, 0.2, 0.3, 1.0], 
                               labels=['No Discount', '0-10%', '10-20%', '20-30%', '30%+'],
                               include_lowest=True)

discount_range = df.groupby('Discount_Range', observed=True).agg({
    'Sales': ['count', 'mean', 'sum'],
    'Profit': ['mean', 'sum'],
    'Profit_Margin': 'mean'
}).round(2)

discount_range.columns = ['Orders', 'Avg Sales', 'Total Sales', 'Avg Profit', 'Total Profit', 'Avg Margin %']
print(discount_range.to_markdown())
print("\n")

# =====================================================
# PART 4: CATEGORY BREAKDOWN
# =====================================================
print("="*80)
print("📂 PART 4: CATEGORY BREAKDOWN")
print("="*80)
print()

# ----------------------------------------
# 10. Analysis by Segment
# ----------------------------------------
print("### 🔟 ניתוח לפי Segment\n")

segment_analysis = df.groupby('Segment').agg({
    'Sales': ['count', 'mean', 'sum'],
    'Profit': ['mean', 'sum'],
    'Quantity': 'mean',
    'Discount': 'mean'
}).round(2)

segment_analysis.columns = ['Orders', 'Avg Sales', 'Total Sales', 'Avg Profit', 'Total Profit', 'Avg Quantity', 'Avg Discount']
segment_analysis['Orders %'] = (segment_analysis['Orders'] / segment_analysis['Orders'].sum() * 100).round(2)
segment_analysis['Sales %'] = (segment_analysis['Total Sales'] / segment_analysis['Total Sales'].sum() * 100).round(2)
segment_analysis['Profit Margin %'] = (segment_analysis['Total Profit'] / segment_analysis['Total Sales'] * 100).round(2)

print(segment_analysis.to_markdown())
print("\n")

# ----------------------------------------
# 11. Analysis by Region
# ----------------------------------------
print("### 1️⃣1️⃣ ניתוח לפי Region\n")

region_analysis = df.groupby('Region').agg({
    'Sales': ['count', 'mean', 'sum'],
    'Profit': ['mean', 'sum'],
    'Quantity': 'mean',
    'Discount': 'mean'
}).round(2)

region_analysis.columns = ['Orders', 'Avg Sales', 'Total Sales', 'Avg Profit', 'Total Profit', 'Avg Quantity', 'Avg Discount']
region_analysis['Orders %'] = (region_analysis['Orders'] / region_analysis['Orders'].sum() * 100).round(2)
region_analysis['Sales %'] = (region_analysis['Total Sales'] / region_analysis['Total Sales'].sum() * 100).round(2)
region_analysis['Profit Margin %'] = (region_analysis['Total Profit'] / region_analysis['Total Sales'] * 100).round(2)

print(region_analysis.to_markdown())
print("\n")

# ----------------------------------------
# 12. Analysis by Category
# ----------------------------------------
print("### 1️⃣2️⃣ ניתוח לפי Category\n")

category_analysis = df.groupby('Category').agg({
    'Sales': ['count', 'mean', 'sum'],
    'Profit': ['mean', 'sum'],
    'Quantity': 'mean',
    'Discount': 'mean'
}).round(2)

category_analysis.columns = ['Orders', 'Avg Sales', 'Total Sales', 'Avg Profit', 'Total Profit', 'Avg Quantity', 'Avg Discount']
category_analysis['Orders %'] = (category_analysis['Orders'] / category_analysis['Orders'].sum() * 100).round(2)
category_analysis['Sales %'] = (category_analysis['Total Sales'] / category_analysis['Total Sales'].sum() * 100).round(2)
category_analysis['Profit Margin %'] = (category_analysis['Total Profit'] / category_analysis['Total Sales'] * 100).round(2)

print(category_analysis.to_markdown())
print("\n")

# ----------------------------------------
# 13. Analysis by Sub-Category
# ----------------------------------------
print("### 1️⃣3️⃣ ניתוח לפי Sub-Category\n")

subcat_analysis = df.groupby('Sub_Category').agg({
    'Sales': ['count', 'sum'],
    'Profit': ['sum'],
}).round(2)

subcat_analysis.columns = ['Orders', 'Total Sales', 'Total Profit']
subcat_analysis['Profit Margin %'] = (subcat_analysis['Total Profit'] / subcat_analysis['Total Sales'] * 100).round(2)
subcat_analysis = subcat_analysis.sort_values('Total Profit', ascending=False)

print("**Top 5 Most Profitable Sub-Categories:**\n")
print(subcat_analysis.head(5).to_markdown())
print("\n")

print("**Bottom 5 Sub-Categories (Least Profitable):**\n")
print(subcat_analysis.tail(5).to_markdown())
print("\n")

# ----------------------------------------
# 14. Analysis by State (Top 10)
# ----------------------------------------
print("### 1️⃣4️⃣ ניתוח לפי State (Top 10)\n")

state_analysis = df.groupby('State').agg({
    'Sales': ['count', 'sum'],
    'Profit': 'sum'
}).round(2)

state_analysis.columns = ['Orders', 'Total Sales', 'Total Profit']
state_analysis['Profit Margin %'] = (state_analysis['Total Profit'] / state_analysis['Total Sales'] * 100).round(2)

print("**Top 10 States by Sales:**\n")
top_sales = state_analysis.sort_values('Total Sales', ascending=False).head(10)
print(top_sales.to_markdown())
print("\n")

print("**Top 10 States by Profit:**\n")
top_profit = state_analysis.sort_values('Total Profit', ascending=False).head(10)
print(top_profit.to_markdown())
print("\n")

print("**Bottom 5 States:**\n")
bottom_states = state_analysis.sort_values('Total Profit', ascending=True).head(5)
print(bottom_states.to_markdown())
print("\n")

# =====================================================
# PART 5: OPERATIONAL ANALYSIS
# =====================================================
print("="*80)
print("⚙️ PART 5: OPERATIONAL ANALYSIS")
print("="*80)
print()

# ----------------------------------------
# 15. Analysis by Ship Mode
# ----------------------------------------
print("### 1️⃣5️⃣ ניתוח לפי Ship Mode\n")

shipmode_analysis = df.groupby('Ship_Mode').agg({
    'Sales': ['count', 'mean', 'sum'],
    'Profit': ['mean', 'sum'],
    'Delivery_Days': 'mean'
}).round(2)

shipmode_analysis.columns = ['Orders', 'Avg Sales', 'Total Sales', 'Avg Profit', 'Total Profit', 'Avg Delivery Days']
shipmode_analysis['Orders %'] = (shipmode_analysis['Orders'] / shipmode_analysis['Orders'].sum() * 100).round(2)
shipmode_analysis['Profit Margin %'] = (shipmode_analysis['Total Profit'] / shipmode_analysis['Total Sales'] * 100).round(2)

print(shipmode_analysis.to_markdown())
print("\n")

# ----------------------------------------
# 16. Quantity Analysis
# ----------------------------------------
print("### 1️⃣6️⃣ ניתוח Quantity\n")

print("**Quantity Distribution:**\n")
quantity_dist = df['Quantity'].value_counts().sort_index()
quantity_df = pd.DataFrame({
    'Quantity': quantity_dist.index,
    'Orders': quantity_dist.values,
    'Percentage': (quantity_dist.values / len(df) * 100).round(2)
})
print(quantity_df.head(10).to_markdown(index=False))
print("\n")

print("**Average Quantity by Category:**\n")
qty_by_cat = df.groupby('Category')['Quantity'].agg(['mean', 'median', 'sum']).round(2)
qty_by_cat.columns = ['Avg Quantity', 'Median Quantity', 'Total Quantity']
print(qty_by_cat.to_markdown())
print("\n")

# ----------------------------------------
# 17. Delivery Time Analysis
# ----------------------------------------
print("### 1️⃣7️⃣ ניתוח זמן משלוח (Delivery Time Analysis)\n")

print("**Overall Delivery Statistics:**\n")
delivery_stats = pd.DataFrame({
    'Metric': [
        'Average Delivery Days',
        'Median Delivery Days',
        'Min Delivery Days',
        'Max Delivery Days',
        'Std Dev Delivery Days'
    ],
    'Value': [
        round(df['Delivery_Days'].mean(), 2),
        round(df['Delivery_Days'].median(), 2),
        df['Delivery_Days'].min(),
        df['Delivery_Days'].max(),
        round(df['Delivery_Days'].std(), 2)
    ]
})
print(delivery_stats.to_markdown(index=False))
print("\n")

print("**Delivery Time by Ship Mode:**\n")
delivery_by_mode = df.groupby('Ship_Mode')['Delivery_Days'].agg(['mean', 'median', 'min', 'max']).round(2)
delivery_by_mode.columns = ['Avg Days', 'Median Days', 'Min Days', 'Max Days']
print(delivery_by_mode.to_markdown())
print("\n")

# =====================================================
# PART 6: TIME SERIES ANALYSIS
# =====================================================
print("="*80)
print("📈 PART 6: TIME SERIES ANALYSIS")
print("="*80)
print()

# ----------------------------------------
# 18. Yearly Analysis
# ----------------------------------------
print("### 1️⃣8️⃣ ניתוח שנתי (Yearly Trends)\n")

yearly = df.groupby('Year').agg({
    'Sales': ['count', 'sum'],
    'Profit': 'sum',
    'Quantity': 'sum'
}).round(2)

yearly.columns = ['Orders', 'Total Sales', 'Total Profit', 'Total Quantity']
yearly['Profit Margin %'] = (yearly['Total Profit'] / yearly['Total Sales'] * 100).round(2)

# YoY Growth
yearly['Sales Growth %'] = yearly['Total Sales'].pct_change() * 100
yearly['Profit Growth %'] = yearly['Total Profit'].pct_change() * 100

print(yearly.round(2).to_markdown())
print("\n")

# ----------------------------------------
# 19. Quarterly Analysis
# ----------------------------------------
print("### 1️⃣9️⃣ ניתוח רבעוני (Quarterly Analysis)\n")

quarterly = df.groupby('Quarter').agg({
    'Sales': ['count', 'sum'],
    'Profit': 'sum'
}).round(2)

quarterly.columns = ['Orders', 'Total Sales', 'Total Profit']
quarterly['Profit Margin %'] = (quarterly['Total Profit'] / quarterly['Total Sales'] * 100).round(2)
quarterly.index = ['Q' + str(i) for i in quarterly.index]

print(quarterly.to_markdown())
print("\n")

# ----------------------------------------
# 20. Monthly Analysis
# ----------------------------------------
print("### 2️⃣0️⃣ ניתוח חודשי (Monthly Trends)\n")

monthly = df.groupby('Month').agg({
    'Sales': ['count', 'sum'],
    'Profit': 'sum'
}).round(2)

monthly.columns = ['Orders', 'Total Sales', 'Total Profit']
monthly['Profit Margin %'] = (monthly['Total Profit'] / monthly['Total Sales'] * 100).round(2)

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly.index = [month_names[i-1] for i in monthly.index]

print(monthly.to_markdown())
print("\n")

# ----------------------------------------
# 21. Day of Week Analysis
# ----------------------------------------
print("### 2️⃣1️⃣ ניתוח לפי יום בשבוע (Day of Week)\n")

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_analysis = df.groupby('DayOfWeek').agg({
    'Sales': ['count', 'sum'],
    'Profit': 'sum'
}).round(2)

day_analysis.columns = ['Orders', 'Total Sales', 'Total Profit']
day_analysis['Avg Sales per Order'] = (day_analysis['Total Sales'] / day_analysis['Orders']).round(2)

# סדר נכון לימים
day_analysis = day_analysis.reindex(day_order)

print(day_analysis.to_markdown())
print("\n")

# =====================================================
# PART 7: COMBINED ANALYSIS
# =====================================================
print("="*80)
print("🔀 PART 7: COMBINED ANALYSIS")
print("="*80)
print()

# ----------------------------------------
# 22. Region × Category
# ----------------------------------------
print("### 2️⃣2️⃣ ניתוח משולב: Region × Category\n")

print("**Profit Margin % Matrix:**\n")
region_cat_profit = df.groupby(['Region', 'Category']).agg({
    'Sales': 'sum',
    'Profit': 'sum'
})
region_cat_profit['Profit Margin %'] = (region_cat_profit['Profit'] / region_cat_profit['Sales'] * 100).round(2)
pivot_rc = region_cat_profit['Profit Margin %'].unstack()
print(pivot_rc.to_markdown())
print("\n")

print("**Total Sales Matrix:**\n")
pivot_sales = df.groupby(['Region', 'Category'])['Sales'].sum().unstack().round(2)
print(pivot_sales.to_markdown())
print("\n")

# ----------------------------------------
# 23. Segment × Category
# ----------------------------------------
print("### 2️⃣3️⃣ ניתוח משולב: Segment × Category\n")

print("**Profit Margin % Matrix:**\n")
seg_cat_profit = df.groupby(['Segment', 'Category']).agg({
    'Sales': 'sum',
    'Profit': 'sum'
})
seg_cat_profit['Profit Margin %'] = (seg_cat_profit['Profit'] / seg_cat_profit['Sales'] * 100).round(2)
pivot_sc = seg_cat_profit['Profit Margin %'].unstack()
print(pivot_sc.to_markdown())
print("\n")

print("**Total Sales Matrix:**\n")
pivot_sales_sc = df.groupby(['Segment', 'Category'])['Sales'].sum().unstack().round(2)
print(pivot_sales_sc.to_markdown())
print("\n")

# =====================================================
# PART 8: TOP & BOTTOM LISTS
# =====================================================
print("="*80)
print("🏆 PART 8: TOP & BOTTOM LISTS")
print("="*80)
print()

# ----------------------------------------
# 24. Top & Bottom Transactions
# ----------------------------------------
print("### 2️⃣4️⃣ Top & Bottom עסקאות (Transactions)\n")

print("**Top 10 Most Profitable Transactions:**\n")
top_trans = df.nlargest(10, 'Profit')[['Order Date', 'State', 'Category', 'Sub_Category', 'Sales', 'Profit', 'Profit_Margin']]
top_trans_display = top_trans.copy()
top_trans_display['Order Date'] = top_trans_display['Order Date'].dt.strftime('%Y-%m-%d')
print(top_trans_display.to_markdown(index=False))
print("\n")

print("**Top 10 Most Loss-Making Transactions:**\n")
bottom_trans = df.nsmallest(10, 'Profit')[['Order Date', 'State', 'Category', 'Sub_Category', 'Sales', 'Profit', 'Profit_Margin']]
bottom_trans_display = bottom_trans.copy()
bottom_trans_display['Order Date'] = bottom_trans_display['Order Date'].dt.strftime('%Y-%m-%d')
print(bottom_trans_display.to_markdown(index=False))
print("\n")

# ----------------------------------------
# 25. Top Sales Days
# ----------------------------------------
print("### 2️⃣5️⃣ Top ימים במכירות (Top Sales Days)\n")

daily_sales = df.groupby('Order Date').agg({
    'Sales': ['sum', 'count'],
    'Profit': 'sum'
}).round(2)

daily_sales.columns = ['Total Sales', 'Orders', 'Total Profit']
top_days = daily_sales.nlargest(10, 'Total Sales')

top_days_display = top_days.copy()
top_days_display.index = top_days_display.index.strftime('%Y-%m-%d')
print(top_days_display.to_markdown())
print("\n")

# ----------------------------------------
# 26. Anomalies & Patterns
# ----------------------------------------
print("### 2️⃣6️⃣ דפוסים חריגים (Anomalies & Patterns)\n")

print("**Sub-Categories with Negative Profit:**\n")
negative_subcats = subcat_analysis[subcat_analysis['Total Profit'] < 0].sort_values('Total Profit')
if len(negative_subcats) > 0:
    print(negative_subcats.to_markdown())
else:
    print("*No sub-categories with negative profit*")
print("\n")

print("**Regions with Below Average Profit Margin:**\n")
avg_margin = (df['Profit'].sum() / df['Sales'].sum() * 100)
below_avg_regions = region_analysis[region_analysis['Profit Margin %'] < avg_margin][['Total Sales', 'Total Profit', 'Profit Margin %']]
if len(below_avg_regions) > 0:
    print(below_avg_regions.to_markdown())
else:
    print("*All regions are above average profit margin*")
print("\n")

print("**Months with Highest Sales (Top 3):**\n")
top_months = monthly.nlargest(3, 'Total Sales')[['Orders', 'Total Sales', 'Total Profit']]
print(top_months.to_markdown())
print("\n")

print("**Months with Lowest Sales (Bottom 3):**\n")
bottom_months = monthly.nsmallest(3, 'Total Sales')[['Orders', 'Total Sales', 'Total Profit']]
print(bottom_months.to_markdown())
print("\n")

# =====================================================
# סיכום
# =====================================================
print("="*80)
print("✅ ניתוח הסתיים בהצלחה!")
print("="*80)
print()
print(f"📄 דוח נשמר בקובץ: {log_file}")
print()

# סגירת הלוגר
logger.close()
sys.stdout = logger.terminal
print(f"\n💾 הדוח המלא נשמר בקובץ: {log_file}")
print("🎉 הניתוח הסטטיסטי הושלם!")