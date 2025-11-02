# 📊 דוח ניקוי וקידוד נתונים - Superstore Dataset

**תאריך:** 2025-11-02

**שעה:** 20:06:51

---


---

🚀 התחלת תהליך ניקוי וקידוד נתונים

---


📥 ## שלב 1: קריאת הקובץ המקורי...
✅ נטען קובץ עם 9994 שורות ו-21 עמודות

📊 מידע על הקובץ המקורי:

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9994 entries, 0 to 9993
Data columns (total 21 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Row ID         9994 non-null   int64  
 1   Order ID       9994 non-null   object 
 2   Order Date     9994 non-null   object 
 3   Ship Date      9994 non-null   object 
 4   Ship Mode      9994 non-null   object 
 5   Customer ID    9994 non-null   object 
 6   Customer Name  9994 non-null   object 
 7   Segment        9994 non-null   object 
 8   Country        9994 non-null   object 
 9   City           9994 non-null   object 
 10  State          9994 non-null   object 
 11  Postal Code    9994 non-null   int64  
 12  Region         9994 non-null   object 
 13  Product ID     9994 non-null   object 
 14  Category       9994 non-null   object 
 15  Sub-Category   9994 non-null   object 
 16  Product Name   9994 non-null   object 
 17  Sales          9994 non-null   float64
 18  Quantity       9994 non-null   int64  
 19  Discount       9994 non-null   float64
 20  Profit         9994 non-null   float64
dtypes: float64(3), int64(3), object(15)
memory usage: 1.6+ MB
None```



🔍 5 שורות ראשונות:
   Row ID        Order ID  Order Date   Ship Date  ...     Sales Quantity Discount    Profit
0       1  CA-2016-152156   11.8.2016  11.11.2016  ...  261.9600        2     0.00   41.9136
1       2  CA-2016-152156   11.8.2016  11.11.2016  ...  731.9400        3     0.00  219.5820
2       3  CA-2016-138688   6.12.2016   6/16/2016  ...   14.6200        2     0.00    6.8714
3       4  US-2015-108966  10.11.2015  10/18/2015  ...  957.5775        5     0.45 -383.0310
4       5  US-2015-108966  10.11.2015  10/18/2015  ...   22.3680        2     0.20    2.5164

[5 rows x 21 columns]

🗑️ ## שלב 2: הסרת עמודות מיותרות...
עמודות להסרה: ['Row ID', 'Order ID', 'Customer ID', 'Customer Name', 'Product ID', 'Product Name', 'City', 'Country', 'Postal Code']
✅ הוסרו 9 עמודות. נשארו 12 עמודות

📅 ## שלב 3: המרת עמודות תאריך...
  המרת Order Date ל-datetime...
  ✅ כל התאריכים ב-Order Date הומרו בהצלחה (9994 תאריכים)
  המרת Ship Date ל-datetime...
  ✅ כל התאריכים ב-Ship Date הומרו בהצלחה (9994 תאריכים)
✅ עמודות תאריך הומרו ל-datetime64

💰 ## שלב 4: בדיקת עמודת Discount...
  Discount - min: 0.0, max: 0.8
  ✅ כל ערכי Discount בטווח תקין (0-1)

🗺️ ## שלב 5: המרת State לטיפוס string...
  State לפני: object
  State אחרי: string
  ✅ State הומר ל-string - 49 מדינות שונות

🔍 ## שלב 6: בדיקת ערכים חסרים...
  ✅ אין ערכים חסרים!

🔢 ## שלב 7: One-Hot Encoding על קטגוריות מתאימות...

סיכום עמודות קטגוריאליות:
  • Ship Mode: 4 ערכים ייחודיים
  • Segment: 3 ערכים ייחודיים
  • Region: 4 ערכים ייחודיים
  • Category: 3 ערכים ייחודיים
  • Sub-Category: 17 ערכים ייחודיים

  עמודות לפני One-Hot: 12
  עמודות אחרי One-Hot: 33
  ✅ נוספו 26 עמודות One-Hot

✔️ ## שלב 8: בדיקה סופית...

📋 טיפוסי עמודות סופיים:
Order Date                  datetime64[ns]
Ship Date                   datetime64[ns]
State                       string[python]
Sales                              float64
Quantity                             int64
Discount                           float64
Profit                             float64
Ship Mode_Same Day                   int64
Ship Mode_Second Class               int64
Ship Mode_Standard Class             int64
Segment_Corporate                    int64
Segment_Home Office                  int64
Region_East                          int64
Region_South                         int64
Region_West                          int64
Category_Office Supplies             int64
Category_Technology                  int64
Sub-Category_Appliances              int64
Sub-Category_Art                     int64
Sub-Category_Binders                 int64
Sub-Category_Bookcases               int64
Sub-Category_Chairs                  int64
Sub-Category_Copiers                 int64
Sub-Category_Envelopes               int64
Sub-Category_Fasteners               int64
Sub-Category_Furnishings             int64
Sub-Category_Labels                  int64
Sub-Category_Machines                int64
Sub-Category_Paper                   int64
Sub-Category_Phones                  int64
Sub-Category_Storage                 int64
Sub-Category_Supplies                int64
Sub-Category_Tables                  int64
dtype: object

📊 סיכום הקובץ הסופי:
  • שורות: 9,994
  • עמודות: 33
  • גודל זיכרון: 2.99 MB

📝 עמודות בקובץ הסופי:

  עמודות נומריות (30):
    - Category_Office Supplies
    - Category_Technology
    - Discount
    - Profit
    - Quantity
    - Region_East
    - Region_South
    - Region_West
    - Sales
    - Segment_Corporate
    - Segment_Home Office
    - Ship Mode_Same Day
    - Ship Mode_Second Class
    - Ship Mode_Standard Class
    - Sub-Category_Appliances
    - Sub-Category_Art
    - Sub-Category_Binders
    - Sub-Category_Bookcases
    - Sub-Category_Chairs
    - Sub-Category_Copiers
    - Sub-Category_Envelopes
    - Sub-Category_Fasteners
    - Sub-Category_Furnishings
    - Sub-Category_Labels
    - Sub-Category_Machines
    - Sub-Category_Paper
    - Sub-Category_Phones
    - Sub-Category_Storage
    - Sub-Category_Supplies
    - Sub-Category_Tables

  עמודות תאריך (2):
    - Order Date
    - Ship Date

  עמודות טקסט (1):
    - State

💾 ## שלב 9: שמירת הקובץ...
✅ הקובץ נשמר בהצלחה: data_cleaned.csv


---

🎉 תהליך הניקוי והקידוד הושלם בהצלחה!

---


📄 קובץ פלט: data_cleaned.csv
📊 9,994 שורות × 33 עמודות

✨ הקובץ מוכן לניתוח סטטיסטי ולמתן לסוכנים!

---


---

## ✅ סיכום

- **הושלם בהצלחה בשעה:** 20:06:52
- **זמן ריצה:** כמה שניות
- **קבצים שנוצרו:**
  - `data_cleaned.csv`
  - `data_cleaning_log.md` (קובץ זה)

