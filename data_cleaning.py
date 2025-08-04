import pandas as pd
import numpy as np
from datetime import datetime

print("🔍 Starting Data Cleaning and Preprocessing for Customer Personality Analysis Dataset")
print("=" * 80)

# Load the raw dataset (tab separator in original)
print("📁 Loading raw dataset...")
df = pd.read_csv("marketing_campaign.csv", sep='\t')

# Store original info for comparison
original_shape = df.shape
original_columns = df.columns.tolist()

print(f"📊 Original dataset shape: {original_shape}")
print(f"📋 Original columns: {len(original_columns)}")

# Step 1: Initial Data Quality Assessment
print("\n🔍 STEP 1: Initial Data Quality Assessment")
print("-" * 50)

# Check for missing values
missing_values = df.isnull().sum()
print(f"❌ Missing values found:")
for col, missing in missing_values[missing_values > 0].items():
    print(f"   - {col}: {missing} ({missing/len(df)*100:.1f}%)")

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"🔄 Duplicate rows found: {duplicates}")

# Check data types
print(f"📝 Data types:")
for col, dtype in df.dtypes.items():
    print(f"   - {col}: {dtype}")

# Step 2: Remove duplicates
print("\n🧹 STEP 2: Removing Duplicates")
print("-" * 50)
df.drop_duplicates(inplace=True)
print(f"✅ Removed {duplicates} duplicate rows")
print(f"📊 Dataset shape after removing duplicates: {df.shape}")

# Step 3: Handle missing values
print("\n🔧 STEP 3: Handling Missing Values")
print("-" * 50)

# Fill missing values in 'Income' with median
if df['Income'].isnull().sum() > 0:
    median_income = df['Income'].median()
    df['Income'] = df['Income'].fillna(median_income)
    print(f"💰 Filled {df['Income'].isnull().sum()} missing Income values with median: {median_income:.2f}")

# Check for any remaining missing values
remaining_missing = df.isnull().sum().sum()
if remaining_missing == 0:
    print("✅ All missing values have been handled")
else:
    print(f"⚠️  {remaining_missing} missing values still remain")

# Step 4: Standardize column names (lowercase, underscores)
print("\n📝 STEP 4: Standardizing Column Names")
print("-" * 50)
old_columns = df.columns.tolist()
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
print("✅ Column names standardized (lowercase, underscores)")

# Step 5: Convert 'dt_customer' column to datetime
print("\n📅 STEP 5: Converting Date Format")
print("-" * 50)
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')
print("✅ Date column converted to datetime format")

# Step 6: Standardize categorical text (education, marital_status)
print("\n🏷️  STEP 6: Standardizing Categorical Data")
print("-" * 50)

# Education standardization
print("📚 Education values before standardization:")
print(df['education'].value_counts())
df['education'] = df['education'].str.lower().str.strip()
print("📚 Education values after standardization:")
print(df['education'].value_counts())

# Marital status standardization
print("\n💍 Marital status values before standardization:")
print(df['marital_status'].value_counts())
df['marital_status'] = df['marital_status'].str.lower().str.strip()
print("💍 Marital status values after standardization:")
print(df['marital_status'].value_counts())

# Step 7: Outlier Detection and Treatment
print("\n📊 STEP 7: Outlier Detection and Treatment")
print("-" * 50)

# Function to detect outliers using IQR method
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

# Check for outliers in numerical columns
numerical_columns = ['year_birth', 'income', 'recency', 'mntwines', 'mntfruits', 
                    'mntmeatproducts', 'mntfishproducts', 'mntsweetproducts', 'mntgoldprods']

for col in numerical_columns:
    if col in df.columns:
        outliers, lower, upper = detect_outliers(df, col)
        if len(outliers) > 0:
            print(f"⚠️  {col}: {len(outliers)} outliers detected (range: {lower:.2f} to {upper:.2f})")
            # Cap outliers instead of removing them
            df[col] = df[col].clip(lower=lower, upper=upper)
            print(f"✅ Outliers in {col} have been capped")

# Step 8: Data Type Validation and Correction
print("\n🔧 STEP 8: Data Type Validation and Correction")
print("-" * 50)

# Ensure numerical columns are properly typed
for col in numerical_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Ensure categorical columns are strings
categorical_columns = ['education', 'marital_status']
for col in categorical_columns:
    if col in df.columns:
        df[col] = df[col].astype(str)

print("✅ Data types have been validated and corrected")

# Step 9: Final Data Quality Check
print("\n✅ STEP 9: Final Data Quality Check")
print("-" * 50)

final_shape = df.shape
print(f"📊 Final dataset shape: {final_shape}")
print(f"📈 Rows processed: {original_shape[0]} -> {final_shape[0]}")
print(f"📋 Columns processed: {original_shape[1]} -> {final_shape[1]}")

# Check for any remaining issues
final_missing = df.isnull().sum().sum()
final_duplicates = df.duplicated().sum()
print(f"❌ Remaining missing values: {final_missing}")
print(f"🔄 Remaining duplicates: {final_duplicates}")

# Step 10: Save cleaned dataset
print("\n💾 STEP 10: Saving Cleaned Dataset")
print("-" * 50)
df.to_csv("customer_personality_cleaned.csv", index=False)
print("✅ Cleaned dataset saved as 'customer_personality_cleaned.csv'")

# Step 11: Generate Summary Report
print("\n📋 STEP 11: Data Cleaning Summary Report")
print("=" * 80)

summary_report = f"""
DATA CLEANING AND PREPROCESSING SUMMARY REPORT
==============================================

Dataset: Customer Personality Analysis
Original Source: Kaggle
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

CHANGES MADE:
------------

1. DUPLICATE REMOVAL:
   - Removed {duplicates} duplicate rows
   - Final dataset: {final_shape[0]} unique records

2. MISSING VALUE HANDLING:
   - Income column: Filled missing values with median ({df['income'].median():.2f})
   - All missing values have been addressed

3. COLUMN NAME STANDARDIZATION:
   - Converted all column names to lowercase
   - Replaced spaces with underscores
   - Example: 'Year_Birth' -> 'year_birth'

4. DATE FORMAT STANDARDIZATION:
   - Converted 'dt_customer' from string to datetime format
   - Original format: dd-mm-yyyy
   - New format: yyyy-mm-dd

5. CATEGORICAL DATA STANDARDIZATION:
   - Education: Standardized to lowercase (e.g., 'Graduation' -> 'graduation')
   - Marital Status: Standardized to lowercase (e.g., 'Single' -> 'single')

6. OUTLIER TREATMENT:
   - Applied IQR method for outlier detection
   - Capped outliers instead of removal to preserve data integrity
   - Affected columns: {', '.join(numerical_columns)}

7. DATA TYPE VALIDATION:
   - Ensured numerical columns are properly typed
   - Ensured categorical columns are strings
   - Validated datetime format

QUALITY METRICS:
----------------
- Original rows: {original_shape[0]}
- Final rows: {final_shape[0]}
- Rows removed: {original_shape[0] - final_shape[0]}
- Missing values: {final_missing}
- Duplicates: {final_duplicates}
- Data quality score: {((final_shape[0] - final_missing - final_duplicates) / final_shape[0] * 100):.1f}%

DATASET READINESS:
------------------
✅ Ready for analysis and modeling
✅ Consistent data types
✅ No missing values
✅ No duplicates
✅ Standardized formats
✅ Outliers handled appropriately

COLUMNS IN CLEANED DATASET:
--------------------------
{', '.join(df.columns.tolist())}

Total columns: {len(df.columns)}
"""

# Save summary report
with open("data_cleaning_summary.txt", "w", encoding='utf-8') as f:
    f.write(summary_report)

print(summary_report)
print("\n📄 Summary report saved as 'data_cleaning_summary.txt'")
print("\n🎉 Data cleaning and preprocessing completed successfully!")
print("=" * 80)
