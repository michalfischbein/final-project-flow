# 📊 דוח ניתוח סטטיסטי מקיף - Superstore Dataset

**תאריך:** 2025-11-02

**שעה:** 20:40:13

**קובץ מקור:** data_cleaned.csv

---

## 📋 תוכן עניינים

1. [Part 1: Foundation](#part-1-foundation)
2. [Part 2: Distributions & Relationships](#part-2-distributions--relationships)
3. [Part 3: Profitability](#part-3-profitability)
4. [Part 4: Category Breakdown](#part-4-category-breakdown)
5. [Part 5: Operational Analysis](#part-5-operational-analysis)
6. [Part 6: Time Series Analysis](#part-6-time-series-analysis)
7. [Part 7: Combined Analysis](#part-7-combined-analysis)
8. [Part 8: Top & Bottom Lists](#part-8-top--bottom-lists)

---


---

🚀 התחלת ניתוח סטטיסטי מקיף

---


📥 טעינת קובץ הנתונים הנקי...
✅ נטענו 9,994 שורות מהקובץ


---

📊 PART 1: FOUNDATION

---


### 1️⃣ סקירה כללית (Dataset Overview)

| Metric              | Value      |
|:--------------------|:-----------|
| Total Rows          | 9,994      |
| Total Columns       | 43         |
| Start Date          | 2014-01-02 |
| End Date            | 2017-12-30 |
| Date Range (Days)   | 1458       |
| Date Range (Months) | 48.6       |
| Memory Usage (MB)   | 6.54       |


### 2️⃣ Missing Data & Quality Check

✅ **No Missing Values Found**

**Quality Checks:**

| Check             |   Count | Status   |
|:------------------|--------:|:---------|
| Negative Sales    |       0 | ✅ OK    |
| Negative Quantity |       0 | ✅ OK    |
| Discount > 1      |       0 | ✅ OK    |
| Discount < 0      |       0 | ✅ OK    |


### 3️⃣ סטטיסטיקות תיאוריות (Descriptive Statistics)

|               |   count |   mean |    std |      min |   25% |   50% |    75% |      max |   Range |   Variance |
|:--------------|--------:|-------:|-------:|---------:|------:|------:|-------:|---------:|--------:|-----------:|
| Sales         |    9994 | 229.86 | 623.25 |     0.44 | 17.28 | 54.49 | 209.94 | 22638.5  | 22638   |  388434    |
| Quantity      |    9994 |   3.79 |   2.23 |     1    |  2    |  3    |   5    |    14    |    13   |       4.95 |
| Discount      |    9994 |   0.16 |   0.21 |     0    |  0    |  0.2  |   0.2  |     0.8  |     0.8 |       0.04 |
| Profit        |    9994 |  28.66 | 234.26 | -6599.98 |  1.73 |  8.67 |  29.36 |  8399.98 | 15000   |   54877.8  |
| Delivery_Days |    9994 |   9.35 |  95.41 |  -322    |  2    |  4    |  61    |   214    |   536   |    9102.76 |


### 4️⃣ מדדים עיקריים (Key Performance Indicators)

| KPI                   | Value         |
|:----------------------|:--------------|
| Total Sales           | $2,297,200.86 |
| Total Profit          | $286,397.02   |
| Total Orders          | 9,994         |
| Average Order Value   | $229.86       |
| Overall Profit Margin | 12.47%        |
| Profitable Orders     | 8,058         |
| Profitable Orders %   | 80.63%        |
| Loss-Making Orders    | 1,936         |
| Loss-Making Orders %  | 19.37%        |



---

📊 PART 2: DISTRIBUTIONS & RELATIONSHIPS

---


### 5️⃣ ניתוח התפלגויות (Distribution Analysis)

| Variable   |   Skewness | Skew Interpretation   |   Kurtosis | Kurt Interpretation   |
|:-----------|-----------:|:----------------------|-----------:|:----------------------|
| Sales      |     12.973 | Right-skewed          |    305.312 | Heavy-tailed          |
| Quantity   |      1.279 | Right-skewed          |      1.992 | Heavy-tailed          |
| Discount   |      1.684 | Right-skewed          |      2.41  | Heavy-tailed          |
| Profit     |      7.561 | Right-skewed          |    397.189 | Heavy-tailed          |


### 6️⃣ זיהוי חריגות (Outliers Detection)

| Variable   | IQR Outliers   | IQR %   |   Z-Score Outliers | Z-Score %   |
|:-----------|:---------------|:--------|-------------------:|:------------|
| Sales      | 1,167          | 11.68%  |                127 | 1.27%       |
| Quantity   | 170            | 1.70%   |                113 | 1.13%       |
| Discount   | 856            | 8.57%   |                300 | 3.00%       |
| Profit     | 1,881          | 18.82%  |                107 | 1.07%       |


### 7️⃣ מטריצת קורלציות (Correlation Matrix)

**Correlation Matrix:**

|               |   Sales |   Quantity |   Discount |   Profit |   Delivery_Days |
|:--------------|--------:|-----------:|-----------:|---------:|----------------:|
| Sales         |   1     |      0.201 |     -0.028 |    0.479 |           0.007 |
| Quantity      |   0.201 |      1     |      0.009 |    0.066 |          -0.006 |
| Discount      |  -0.028 |      0.009 |      1     |   -0.219 |           0.02  |
| Profit        |   0.479 |      0.066 |     -0.219 |    1     |           0.021 |
| Delivery_Days |   0.007 |     -0.006 |      0.02  |    0.021 |           1     |


**Strong Correlations (|r| > 0.5):**

*No strong correlations found (threshold: |r| > 0.5)*



---

💰 PART 3: PROFITABILITY

---


### 8️⃣ ניתוח רווחיות (Profitability Analysis)

| Metric                    | Value        |
|:--------------------------|:-------------|
| Average Profit Margin     | 12.03%       |
| Median Profit Margin      | 27.00%       |
| Profitable Orders         | 8,058        |
| Profitable Orders %       | 80.63%       |
| Loss-Making Orders        | 1,871        |
| Loss-Making Orders %      | 18.72%       |
| Break-Even Orders         | 65           |
| Total Profit (Profitable) | $442,528.31  |
| Total Loss (Loss-Making)  | $-156,131.29 |
| Net Profit                | $286,397.02  |


### 9️⃣ ניתוח השפעת הנחות (Discount Impact Analysis)

**Correlations with Discount:**

| Variable      |   Correlation with Discount |
|:--------------|----------------------------:|
| Sales         |                      -0.028 |
| Profit        |                      -0.219 |
| Quantity      |                       0.009 |
| Profit Margin |                      -0.864 |


**Analysis by Discount Range:**

| Discount_Range   |   Orders |   Avg Sales |      Total Sales |   Avg Profit |   Total Profit |   Avg Margin % |
|:-----------------|---------:|------------:|-----------------:|-------------:|---------------:|---------------:|
| No Discount      |     4798 |      226.74 |      1.08791e+06 |        66.9  |      320988    |          34.02 |
| 0-10%            |       94 |      578.4  |  54369.3         |        96.06 |        9029.18 |          15.58 |
| 10-20%           |     3709 |      213.58 | 792153           |        24.74 |       91756.3  |          17.48 |
| 20-30%           |      227 |      454.74 | 103227           |       -45.68 |      -10369.3  |         -11.55 |
| 30%+             |     1166 |      222.59 | 259543           |      -107.21 |     -125007    |         -91.47 |



---

📂 PART 4: CATEGORY BREAKDOWN

---


### 🔟 ניתוח לפי Segment

| Segment      |   Orders |   Avg Sales |     Total Sales |   Avg Profit |   Total Profit |   Avg Quantity |   Avg Discount |   Orders % |   Sales % |   Profit Margin % |
|:-------------|---------:|------------:|----------------:|-------------:|---------------:|---------------:|---------------:|-----------:|----------:|------------------:|
| Corporate    |     3020 |      233.82 | 706146          |        30.46 |        91979.1 |           3.84 |           0.16 |      30.22 |     30.74 |             13.03 |
| Home Office  |     1783 |      240.97 | 429653          |        33.82 |        60298.7 |           3.78 |           0.15 |      17.84 |     18.7  |             14.03 |
| Segment_Base |     5191 |      223.73 |      1.1614e+06 |        25.84 |       134119   |           3.76 |           0.16 |      51.94 |     50.56 |             11.55 |


### 1️⃣1️⃣ ניתוח לפי Region

| Region      |   Orders |   Avg Sales |   Total Sales |   Avg Profit |   Total Profit |   Avg Quantity |   Avg Discount |   Orders % |   Sales % |   Profit Margin % |
|:------------|---------:|------------:|--------------:|-------------:|---------------:|---------------:|---------------:|-----------:|----------:|------------------:|
| East        |     2848 |      238.34 |        678781 |        32.14 |        91522.8 |           3.73 |           0.15 |      28.5  |     29.55 |             13.48 |
| Region_Base |     2323 |      215.77 |        501240 |        17.09 |        39706.4 |           3.78 |           0.24 |      23.24 |     21.82 |              7.92 |
| South       |     1620 |      241.8  |        391722 |        28.86 |        46749.4 |           3.83 |           0.15 |      16.21 |     17.05 |             11.93 |
| West        |     3203 |      226.49 |        725458 |        33.85 |       108418   |           3.83 |           0.11 |      32.05 |     31.58 |             14.94 |


### 1️⃣2️⃣ ניתוח לפי Category

| Category        |   Orders |   Avg Sales |   Total Sales |   Avg Profit |   Total Profit |   Avg Quantity |   Avg Discount |   Orders % |   Sales % |   Profit Margin % |
|:----------------|---------:|------------:|--------------:|-------------:|---------------:|---------------:|---------------:|-----------:|----------:|------------------:|
| Category_Base   |     2121 |      349.83 |        742000 |         8.7  |        18451.3 |           3.79 |           0.17 |      21.22 |      32.3 |              2.49 |
| Office Supplies |     6026 |      119.32 |        719047 |        20.33 |       122491   |           3.8  |           0.16 |      60.3  |      31.3 |             17.04 |
| Technology      |     1847 |      452.71 |        836154 |        78.75 |       145455   |           3.76 |           0.13 |      18.48 |      36.4 |             17.4  |


### 1️⃣3️⃣ ניתוח לפי Sub-Category

**Top 5 Most Profitable Sub-Categories:**

| Sub_Category      |   Orders |   Total Sales |   Total Profit |   Profit Margin % |
|:------------------|---------:|--------------:|---------------:|------------------:|
| Copiers           |       68 |      149528   |        55617.8 |             37.2  |
| Phones            |      889 |      330007   |        44515.7 |             13.49 |
| Sub-Category_Base |      775 |      167380   |        41936.6 |             25.05 |
| Paper             |     1370 |       78479.2 |        34053.6 |             43.39 |
| Binders           |     1523 |      203413   |        30221.8 |             14.86 |


**Bottom 5 Sub-Categories (Least Profitable):**

| Sub_Category   |   Orders |   Total Sales |   Total Profit |   Profit Margin % |
|:---------------|---------:|--------------:|---------------:|------------------:|
| Machines       |      115 |     189239    |        3384.76 |              1.79 |
| Fasteners      |      217 |       3024.28 |         949.52 |             31.4  |
| Supplies       |      190 |      46673.5  |       -1189.1  |             -2.55 |
| Bookcases      |      228 |     114880    |       -3472.56 |             -3.02 |
| Tables         |      319 |     206966    |      -17725.5  |             -8.56 |


### 1️⃣4️⃣ ניתוח לפי State (Top 10)

**Top 10 States by Sales:**

| State        |   Orders |   Total Sales |   Total Profit |   Profit Margin % |
|:-------------|---------:|--------------:|---------------:|------------------:|
| California   |     2001 |      457688   |        76381.4 |             16.69 |
| New York     |     1128 |      310876   |        74038.6 |             23.82 |
| Texas        |      985 |      170188   |       -25729.4 |            -15.12 |
| Washington   |      506 |      138641   |        33402.7 |             24.09 |
| Pennsylvania |      587 |      116512   |       -15560   |            -13.35 |
| Florida      |      383 |       89473.7 |        -3399.3 |             -3.8  |
| Illinois     |      492 |       80166.1 |       -12607.9 |            -15.73 |
| Ohio         |      469 |       78258.1 |       -16971.4 |            -21.69 |
| Michigan     |      255 |       76269.6 |        24463.2 |             32.07 |
| Virginia     |      224 |       70636.7 |        18598   |             26.33 |


**Top 10 States by Profit:**

| State      |   Orders |   Total Sales |   Total Profit |   Profit Margin % |
|:-----------|---------:|--------------:|---------------:|------------------:|
| California |     2001 |      457688   |       76381.4  |             16.69 |
| New York   |     1128 |      310876   |       74038.6  |             23.82 |
| Washington |      506 |      138641   |       33402.7  |             24.09 |
| Michigan   |      255 |       76269.6 |       24463.2  |             32.07 |
| Virginia   |      224 |       70636.7 |       18598    |             26.33 |
| Indiana    |      149 |       53555.4 |       18382.9  |             34.33 |
| Georgia    |      184 |       49095.8 |       16250    |             33.1  |
| Kentucky   |      139 |       36591.8 |       11199.7  |             30.61 |
| Minnesota  |       89 |       29863.2 |       10823.2  |             36.24 |
| Delaware   |       96 |       27451.1 |        9977.37 |             36.35 |


**Bottom 5 States:**

| State          |   Orders |   Total Sales |   Total Profit |   Profit Margin % |
|:---------------|---------:|--------------:|---------------:|------------------:|
| Texas          |      985 |      170188   |      -25729.4  |            -15.12 |
| Ohio           |      469 |       78258.1 |      -16971.4  |            -21.69 |
| Pennsylvania   |      587 |      116512   |      -15560    |            -13.35 |
| Illinois       |      492 |       80166.1 |      -12607.9  |            -15.73 |
| North Carolina |      249 |       55603.2 |       -7490.91 |            -13.47 |



---

⚙️ PART 5: OPERATIONAL ANALYSIS

---


### 1️⃣5️⃣ ניתוח לפי Ship Mode

| Ship_Mode      |   Orders |   Avg Sales |      Total Sales |   Avg Profit |   Total Profit |   Avg Delivery Days |   Orders % |   Profit Margin % |
|:---------------|---------:|------------:|-----------------:|-------------:|---------------:|--------------------:|-----------:|------------------:|
| Same Day       |      543 |      236.4  | 128363           |        29.27 |        15891.8 |                0.56 |       5.43 |             12.38 |
| Second Class   |     1945 |      236.09 | 459194           |        29.54 |        57446.6 |                5.19 |      19.46 |             12.51 |
| Ship Mode_Base |     1538 |      228.5  | 351428           |        31.84 |        48969.8 |                6.72 |      15.39 |             13.93 |
| Standard Class |     5968 |      227.58 |      1.35822e+06 |        27.49 |       164089   |               12.18 |      59.72 |             12.08 |


### 1️⃣6️⃣ ניתוח Quantity

**Quantity Distribution:**

|   Quantity |   Orders |   Percentage |
|-----------:|---------:|-------------:|
|          1 |      899 |         9    |
|          2 |     2402 |        24.03 |
|          3 |     2409 |        24.1  |
|          4 |     1191 |        11.92 |
|          5 |     1230 |        12.31 |
|          6 |      572 |         5.72 |
|          7 |      606 |         6.06 |
|          8 |      257 |         2.57 |
|          9 |      258 |         2.58 |
|         10 |       57 |         0.57 |


**Average Quantity by Category:**

| Category        |   Avg Quantity |   Median Quantity |   Total Quantity |
|:----------------|---------------:|------------------:|-----------------:|
| Category_Base   |           3.79 |                 3 |             8028 |
| Office Supplies |           3.8  |                 3 |            22906 |
| Technology      |           3.76 |                 3 |             6939 |


### 1️⃣7️⃣ ניתוח זמן משלוח (Delivery Time Analysis)

**Overall Delivery Statistics:**

| Metric                |   Value |
|:----------------------|--------:|
| Average Delivery Days |    9.35 |
| Median Delivery Days  |    4    |
| Min Delivery Days     | -322    |
| Max Delivery Days     |  214    |
| Std Dev Delivery Days |   95.41 |


**Delivery Time by Ship Mode:**

| Ship_Mode      |   Avg Days |   Median Days |   Min Days |   Max Days |
|:---------------|-----------:|--------------:|-----------:|-----------:|
| Same Day       |       0.56 |             0 |        -87 |         31 |
| Second Class   |       5.19 |             4 |       -322 |        153 |
| Ship Mode_Base |       6.72 |             3 |       -320 |         92 |
| Standard Class |      12.18 |             5 |       -320 |        214 |



---

📈 PART 6: TIME SERIES ANALYSIS

---


### 1️⃣8️⃣ ניתוח שנתי (Yearly Trends)

|   Year |   Orders |   Total Sales |   Total Profit |   Total Quantity |   Profit Margin % |   Sales Growth % |   Profit Growth % |
|-------:|---------:|--------------:|---------------:|-----------------:|------------------:|-----------------:|------------------:|
|   2014 |     1993 |        484248 |        49544   |             7581 |             10.23 |           nan    |            nan    |
|   2015 |     2102 |        470533 |        61618.6 |             7979 |             13.1  |            -2.83 |             24.37 |
|   2016 |     2587 |        609206 |        81795.2 |             9837 |             13.43 |            29.47 |             32.74 |
|   2017 |     3312 |        733215 |        93439.3 |            12476 |             12.74 |            20.36 |             14.24 |


### 1️⃣9️⃣ ניתוח רבעוני (Quarterly Analysis)

|    |   Orders |   Total Sales |   Total Profit |   Profit Margin % |
|:---|---------:|--------------:|---------------:|------------------:|
| Q1 |     1964 |        513870 |        78257.3 |             15.23 |
| Q2 |     2230 |        458335 |        57666.5 |             12.58 |
| Q3 |     2694 |        620181 |        69383.9 |             11.19 |
| Q4 |     3106 |        704815 |        81089.3 |             11.51 |


### 2️⃣0️⃣ ניתוח חודשי (Monthly Trends)

|     |   Orders |   Total Sales |   Total Profit |   Profit Margin % |
|:----|---------:|--------------:|---------------:|------------------:|
| Jan |      597 |        161084 |        25167.1 |             15.62 |
| Feb |      548 |        132721 |        23753.7 |             17.9  |
| Mar |      819 |        220065 |        29336.6 |             13.33 |
| Apr |      697 |        147031 |        12267.2 |              8.34 |
| May |      826 |        166420 |        24234.4 |             14.56 |
| Jun |      707 |        144884 |        21164.9 |             14.61 |
| Jul |      740 |        161227 |        10008.6 |              6.21 |
| Aug |      816 |        209964 |        24820.3 |             11.82 |
| Sep |     1138 |        248989 |        34554.9 |             13.88 |
| Oct |      808 |        184356 |        22336.9 |             12.12 |
| Nov |     1213 |        271694 |        26435.1 |              9.73 |
| Dec |     1085 |        248765 |        32317.3 |             12.99 |


### 2️⃣1️⃣ ניתוח לפי יום בשבוע (Day of Week)

| DayOfWeek   |   Orders |   Total Sales |   Total Profit |   Avg Sales per Order |
|:------------|---------:|--------------:|---------------:|----------------------:|
| Monday      |     1816 |        391280 |        53286.4 |                215.46 |
| Tuesday     |     1255 |        323853 |        33343.7 |                258.05 |
| Wednesday   |      716 |        190566 |        29027.1 |                266.15 |
| Thursday    |     1418 |        304758 |        38877.3 |                214.92 |
| Friday      |     1626 |        405232 |        48075.9 |                249.22 |
| Saturday    |     1525 |        309794 |        39659.1 |                203.14 |
| Sunday      |     1638 |        371718 |        44127.6 |                226.93 |



---

🔀 PART 7: COMBINED ANALYSIS

---


### 2️⃣2️⃣ ניתוח משולב: Region × Category

**Profit Margin % Matrix:**

| Region      |   Category_Base |   Office Supplies |   Technology |
|:------------|----------------:|------------------:|-------------:|
| East        |            1.46 |             19.96 |        17.91 |
| Region_Base |           -1.75 |              5.32 |        19.77 |
| South       |            5.77 |             15.91 |        13.44 |
| West        |            4.55 |             23.82 |        17.58 |


**Total Sales Matrix:**

| Region      |   Category_Base |   Office Supplies |   Technology |
|:------------|----------------:|------------------:|-------------:|
| East        |          208291 |            205516 |       264974 |
| Region_Base |          163797 |            167026 |       170416 |
| South       |          117299 |            125651 |       148772 |
| West        |          252613 |            220853 |       251992 |


### 2️⃣3️⃣ ניתוח משולב: Segment × Category

**Profit Margin % Matrix:**

| Segment      |   Category_Base |   Office Supplies |   Technology |
|:-------------|----------------:|------------------:|-------------:|
| Corporate    |            3.31 |             17.44 |        17.92 |
| Home Office  |            3.18 |             20.84 |        16.63 |
| Segment_Base |            1.79 |             15.48 |        17.42 |


**Total Sales Matrix:**

| Segment      |   Category_Base |   Office Supplies |   Technology |
|:-------------|----------------:|------------------:|-------------:|
| Corporate    |          229020 |            230676 |       246450 |
| Home Office  |          121931 |            124418 |       183304 |
| Segment_Base |          391049 |            363952 |       406400 |



---

🏆 PART 8: TOP & BOTTOM LISTS

---


### 2️⃣4️⃣ Top & Bottom עסקאות (Transactions)

**Top 10 Most Profitable Transactions:**

| Order Date   | State        | Category        | Sub_Category   |    Sales |   Profit |   Profit_Margin |
|:-------------|:-------------|:----------------|:---------------|---------:|---------:|----------------:|
| 2016-02-10   | Indiana      | Technology      | Copiers        | 17500    |  8399.98 |              48 |
| 2017-03-23   | Washington   | Technology      | Copiers        | 14000    |  6719.98 |              48 |
| 2017-11-17   | Delaware     | Technology      | Copiers        | 10500    |  5039.99 |              48 |
| 2016-12-17   | Michigan     | Office Supplies | Binders        |  9892.74 |  4946.37 |              50 |
| 2014-09-23   | Minnesota    | Office Supplies | Binders        |  9449.95 |  4630.48 |              49 |
| 2017-10-22   | New York     | Technology      | Copiers        | 11200    |  3919.99 |              35 |
| 2015-03-16   | Georgia      | Office Supplies | Binders        |  6354.95 |  3177.47 |              50 |
| 2016-02-02   | Virginia     | Technology      | Machines       |  8749.95 |  2799.98 |              32 |
| 2016-04-10   | Rhode Island | Technology      | Copiers        |  5399.91 |  2591.96 |              48 |
| 2017-01-16   | Michigan     | Office Supplies | Binders        |  5443.96 |  2504.22 |              46 |


**Top 10 Most Loss-Making Transactions:**

| Order Date   | State          | Category        | Sub_Category   |    Sales |   Profit |   Profit_Margin |
|:-------------|:---------------|:----------------|:---------------|---------:|---------:|----------------:|
| 2016-11-25   | Ohio           | Technology      | Machines       |  4499.98 | -6599.98 |       -146.667  |
| 2017-04-11   | North Carolina | Technology      | Machines       |  7999.98 | -3839.99 |        -48      |
| 2014-07-26   | Texas          | Office Supplies | Binders        |  2177.58 | -3701.89 |       -170      |
| 2017-04-17   | Colorado       | Technology      | Machines       |  2549.99 | -3399.98 |       -133.333  |
| 2017-07-12   | Illinois       | Office Supplies | Binders        |  1889.99 | -2929.48 |       -155      |
| 2015-12-15   | Ohio           | Technology      | Machines       |  1799.99 | -2639.99 |       -146.667  |
| 2017-11-19   | Texas          | Office Supplies | Binders        |  1525.19 | -2287.78 |       -150      |
| 2015-01-28   | North Carolina | Category_Base   | Tables         |  4297.64 | -1862.31 |        -43.3333 |
| 2016-08-04   | Texas          | Office Supplies | Binders        |  1088.79 | -1850.95 |       -170      |
| 2014-03-18   | Florida        | Technology      | Machines       | 22638.5  | -1811.08 |         -8      |


### 2️⃣5️⃣ Top ימים במכירות (Top Sales Days)

| Order Date   |   Total Sales |   Orders |   Total Profit |
|:-------------|--------------:|---------:|---------------:|
| 2014-03-18   |       28106.7 |       11 |        -954.71 |
| 2016-02-10   |       18453   |        7 |        8738.8  |
| 2017-10-22   |       15158.9 |       12 |        4539.83 |
| 2017-03-23   |       14816.1 |        8 |        6818.63 |
| 2014-08-09   |       14228.4 |       27 |       -1452.69 |
| 2017-11-17   |       13694.9 |       16 |        5895.4  |
| 2015-08-11   |       12197   |       27 |        4006.64 |
| 2016-12-17   |       12185.1 |        7 |        4654    |
| 2014-11-17   |       11544.3 |       13 |        1954.13 |
| 2015-09-17   |       11525   |       23 |       -1194.28 |


### 2️⃣6️⃣ דפוסים חריגים (Anomalies & Patterns)

**Sub-Categories with Negative Profit:**

| Sub_Category   |   Orders |   Total Sales |   Total Profit |   Profit Margin % |
|:---------------|---------:|--------------:|---------------:|------------------:|
| Tables         |      319 |      206966   |      -17725.5  |             -8.56 |
| Bookcases      |      228 |      114880   |       -3472.56 |             -3.02 |
| Supplies       |      190 |       46673.5 |       -1189.1  |             -2.55 |


**Regions with Below Average Profit Margin:**

| Region      |   Total Sales |   Total Profit |   Profit Margin % |
|:------------|--------------:|---------------:|------------------:|
| Region_Base |        501240 |        39706.4 |              7.92 |
| South       |        391722 |        46749.4 |             11.93 |


**Months with Highest Sales (Top 3):**

|     |   Orders |   Total Sales |   Total Profit |
|:----|---------:|--------------:|---------------:|
| Nov |     1213 |        271694 |        26435.1 |
| Sep |     1138 |        248989 |        34554.9 |
| Dec |     1085 |        248765 |        32317.3 |


**Months with Lowest Sales (Bottom 3):**

|     |   Orders |   Total Sales |   Total Profit |
|:----|---------:|--------------:|---------------:|
| Feb |      548 |        132721 |        23753.7 |
| Jun |      707 |        144884 |        21164.9 |
| Apr |      697 |        147031 |        12267.2 |



---

✅ ניתוח הסתיים בהצלחה!

---


📄 דוח נשמר בקובץ: statistical_analysis_report.md


---

**הסתיים בשעה:** 20:40:14

---

*דוח זה הופק אוטומטית על ידי סקריפט הניתוח הסטטיסטי*
