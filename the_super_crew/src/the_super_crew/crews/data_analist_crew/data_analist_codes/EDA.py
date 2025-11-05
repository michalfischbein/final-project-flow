import pandas as pd
import numpy as np
import sys
from datetime import datetime

# =====================================================
# הגדרת Logger - כותב גם למסך וגם לקובץ MD
# =====================================================
class TeeLogger:
    """מחלקה שכותבת גם למסך וגם לקובץ MD מעוצב"""
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, 'w', encoding='utf-8')
        
        # כתיבת כותרת MD מעוצבת
        self.log.write("# 📊 דוח ניקוי וקידוד נתונים - Superstore Dataset\n\n")
        self.log.write(f"**תאריך:** {datetime.now().strftime('%Y-%m-%d')}\n\n")
        self.log.write(f"**שעה:** {datetime.now().strftime('%H:%M:%S')}\n\n")
        self.log.write("---\n\n")
        
        self.in_code_block = False
        self.section_number = 0
    
    def write(self, message):
        self.terminal.write(message)
        
        # זיהוי כותרות שלבים והמרה ל-MD headers
        if "שלב" in message and ":" in message:
            self.section_number += 1
            # המרת "שלב X:" ל-Markdown header
            md_message = message.replace("🗑️", "🗑️ ##").replace("📅", "📅 ##").replace("💰", "💰 ##")
            md_message = md_message.replace("🗺️", "🗺️ ##").replace("🔍", "🔍 ##").replace("🔢", "🔢 ##")
            md_message = md_message.replace("✔️", "✔️ ##").replace("💾", "💾 ##").replace("📥", "📥 ##")
            if "##" not in md_message and "שלב" in message:
                md_message = "## " + message
        else:
            md_message = message
        
        # המרת קווי הפרדה
        md_message = md_message.replace("="*80, "\n---\n")
        
        # זיהוי פלטי pandas והכנסתם לקוד בלוק
        if "<class 'pandas" in md_message or "RangeIndex:" in md_message:
            if not self.in_code_block:
                self.log.write("\n```\n")
                self.in_code_block = True
        elif self.in_code_block and (md_message.strip().startswith("🗑️") or 
                                      md_message.strip().startswith("📅") or
                                      md_message.strip().startswith("💰") or
                                      md_message.strip() == ""):
            if "None" in md_message or "dtype:" in md_message:
                pass  # ממשיכים בקוד בלוק
            else:
                self.log.write("```\n\n")
                self.in_code_block = False
        
        self.log.write(md_message)
    
    def flush(self):
        self.terminal.flush()
        self.log.flush()
    
    def close(self):
        if self.in_code_block:
            self.log.write("\n```\n\n")
        
        self.log.write("\n---\n\n")
        self.log.write("## ✅ סיכום\n\n")
        self.log.write(f"- **הושלם בהצלחה בשעה:** {datetime.now().strftime('%H:%M:%S')}\n")
        self.log.write(f"- **זמן ריצה:** כמה שניות\n")
        self.log.write(f"- **קבצים שנוצרו:**\n")
        self.log.write(f"  - `data_cleaned.csv`\n")
        self.log.write(f"  - `data_cleaning_log.md` (קובץ זה)\n\n")
        
        self.log.close()

# הפעלת הלוגר
log_file = 'data_cleaning_log.md'
logger = TeeLogger(log_file)
sys.stdout = logger

print("="*80)
print("🚀 התחלת תהליך ניקוי וקידוד נתונים")
print("="*80)

# =====================================================
# שלב 1: קריאת הקובץ המקורי
# =====================================================
print("\n📥 שלב 1: קריאת הקובץ המקורי...")
df = pd.read_csv('superstore.csv')
print(f"✅ נטען קובץ עם {df.shape[0]} שורות ו-{df.shape[1]} עמודות")

# הצגת מידע ראשוני
print("\n📊 מידע על הקובץ המקורי:")
print(df.info())
print("\n🔍 5 שורות ראשונות:")
print(df.head())

# =====================================================
# שלב 2: הסרת עמודות מיותרות
# =====================================================
print("\n🗑️ שלב 2: הסרת עמודות מיותרות...")
cols_to_drop = [
    'Row ID',           # מזהה שורה - לא נחוץ
    'Order ID',         # מזהה ייחודי - 5000+ ערכים
    'Customer ID',      # מזהה ייחודי - 793 ערכים
    'Customer Name',    # שמות לקוחות - 793 ערכים
    'Product ID',       # מזהה מוצר - 1862 ערכים
    'Product Name',     # שם מוצר - 1850 ערכים
    'City',             # עיר - 531 ערכים (יותר מדי)
    'Country',          # מדינה - רק ערך אחד (United States)
    'Postal Code'       # מיקוד - לא רלוונטי
]

print(f"עמודות להסרה: {cols_to_drop}")
df = df.drop(columns=cols_to_drop)
print(f"✅ הוסרו {len(cols_to_drop)} עמודות. נשארו {df.shape[1]} עמודות")

# =====================================================
# שלב 3: טיפול בתאריכים
# =====================================================
print("\n📅 שלב 3: המרת עמודות תאריך...")
date_cols = ['Order Date', 'Ship Date']

for col in date_cols:
    print(f"  המרת {col} ל-datetime...")
    
    # פתרון לפורמטים מעורבבים: נסה כמה פורמטים
    # הקובץ מכיל שני פורמטים: dd.mm.yyyy ו-mm/dd/yyyy
    df[col] = pd.to_datetime(df[col], format='mixed', dayfirst=False, errors='coerce')
    
    # בדיקת ערכים שלא הומרו
    null_dates = df[col].isnull().sum()
    if null_dates > 0:
        print(f"  ⚠️ אזהרה: {null_dates} תאריכים לא תקינים ב-{col}")
    else:
        print(f"  ✅ כל התאריכים ב-{col} הומרו בהצלחה ({df[col].notna().sum()} תאריכים)")

print(f"✅ עמודות תאריך הומרו ל-datetime64")

# =====================================================
# שלב 4: וידוא שהנחה בין 0 ל-1
# =====================================================
print("\n💰 שלב 4: בדיקת עמודת Discount...")
print(f"  Discount - min: {df['Discount'].min()}, max: {df['Discount'].max()}")

# בדיקה אם יש ערכים באחוזים (מעל 1)
if df['Discount'].max() > 1:
    print("  ⚠️ נמצאו ערכים מעל 1 - מבצע המרה מאחוזים לעשרוני...")
    df['Discount'] = df['Discount'] / 100
    print(f"  ✅ הומר. Discount חדש - min: {df['Discount'].min()}, max: {df['Discount'].max()}")

# חיתוך ערכים חריגים (אם יש)
out_of_range = df[(df['Discount'] < 0) | (df['Discount'] > 1)].shape[0]
if out_of_range > 0:
    print(f"  ⚠️ נמצאו {out_of_range} ערכים מחוץ לטווח 0-1")
    df['Discount'] = df['Discount'].clip(0, 1)
    print(f"  ✅ ערכים חתוכים לטווח 0-1")
else:
    print(f"  ✅ כל ערכי Discount בטווח תקין (0-1)")

# =====================================================
# שלב 5: המרת State לסטרינג מפורשות
# =====================================================
print("\n🗺️ שלב 5: המרת State לטיפוס string...")
print(f"  State לפני: {df['State'].dtype}")
df['State'] = df['State'].astype('string')
print(f"  State אחרי: {df['State'].dtype}")
print(f"  ✅ State הומר ל-string - {df['State'].nunique()} מדינות שונות")

# =====================================================
# שלב 6: בדיקת Missing Values
# =====================================================
print("\n🔍 שלב 6: בדיקת ערכים חסרים...")
missing = df.isnull().sum()
if missing.sum() > 0:
    print("  ⚠️ נמצאו ערכים חסרים:")
    print(missing[missing > 0])
else:
    print("  ✅ אין ערכים חסרים!")

# =====================================================
# שלב 7: One-Hot Encoding על קטגוריות קטנות בלבד
# =====================================================
print("\n🔢 שלב 7: One-Hot Encoding על קטגוריות מתאימות...")

# עמודות קטגוריאליות לקידוד
categorical_cols = ['Ship Mode', 'Segment', 'Region', 'Category', 'Sub-Category']

print("\nסיכום עמודות קטגוריאליות:")
for col in categorical_cols:
    n_unique = df[col].nunique()
    print(f"  • {col}: {n_unique} ערכים ייחודיים")

print(f"\n  עמודות לפני One-Hot: {df.shape[1]}")

# ביצוע One-Hot Encoding
df_featured = pd.get_dummies(
    df, 
    columns=categorical_cols, 
    drop_first=True,  # מסיר את הקטגוריה הראשונה למניעת multicollinearity
    dtype='int'       # עמודות חדשות יהיו int (0/1)
)

print(f"  עמודות אחרי One-Hot: {df_featured.shape[1]}")
print(f"  ✅ נוספו {df_featured.shape[1] - df.shape[1] + len(categorical_cols)} עמודות One-Hot")

# =====================================================
# שלב 8: בדיקה סופית ואישור
# =====================================================
print("\n✔️ שלב 8: בדיקה סופית...")

print("\n📋 טיפוסי עמודות סופיים:")
print(df_featured.dtypes)

print(f"\n📊 סיכום הקובץ הסופי:")
print(f"  • שורות: {df_featured.shape[0]:,}")
print(f"  • עמודות: {df_featured.shape[1]}")
print(f"  • גודל זיכרון: {df_featured.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# רשימת עמודות לפי קטגוריה
print("\n📝 עמודות בקובץ הסופי:")

numeric_cols = df_featured.select_dtypes(include=['float64', 'int64']).columns
date_cols_final = df_featured.select_dtypes(include=['datetime64']).columns
string_cols = df_featured.select_dtypes(include=['string', 'object']).columns

print(f"\n  עמודות נומריות ({len(numeric_cols)}):")
for col in sorted(numeric_cols):
    print(f"    - {col}")

print(f"\n  עמודות תאריך ({len(date_cols_final)}):")
for col in sorted(date_cols_final):
    print(f"    - {col}")

print(f"\n  עמודות טקסט ({len(string_cols)}):")
for col in sorted(string_cols):
    print(f"    - {col}")

# =====================================================
# שלב 9: שמירת הקובץ
# =====================================================
print("\n💾 שלב 9: שמירת הקובץ...")
output_file = 'data_cleaned.csv'
df_featured.to_csv(output_file, index=False)
print(f"✅ הקובץ נשמר בהצלחה: {output_file}")

# =====================================================
# סיכום סופי
# =====================================================
print("\n" + "="*80)
print("🎉 תהליך הניקוי והקידוד הושלם בהצלחה!")
print("="*80)
print(f"\n📄 קובץ פלט: {output_file}")
print(f"📊 {df_featured.shape[0]:,} שורות × {df_featured.shape[1]} עמודות")
print("\n✨ הקובץ מוכן לניתוח סטטיסטי ולמתן לסוכנים!")
print("="*80)

# סגירת הלוגר
logger.close()
sys.stdout = logger.terminal
print(f"\n💾 הלוג נשמר בקובץ: {log_file}")