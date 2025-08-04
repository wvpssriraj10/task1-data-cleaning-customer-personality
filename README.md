# Task 1: Data Cleaning and Preprocessing

## 📋 Project Overview

This project demonstrates comprehensive data cleaning and preprocessing techniques applied to the **Customer Personality Analysis** dataset from Kaggle. The goal is to transform raw, messy data into a clean, structured format ready for analysis and modeling.

## 🎯 Objectives

- Identify and handle missing values
- Remove duplicate records
- Standardize text values and formats
- Convert date formats to consistent types
- Rename column headers for uniformity
- Check and fix data types
- Detect and treat outliers
- Generate comprehensive quality reports

## 📊 Dataset Information

**Dataset**: Customer Personality Analysis  
**Source**: Kaggle  
**Original Format**: CSV with tab separators  
**Size**: 2,240 rows × 29 columns  
**Domain**: Marketing/Customer Analytics

### Key Features:
- Customer demographics (age, education, marital status, income)
- Purchase behavior (wine, fruits, meat, fish, sweets, gold products)
- Marketing campaign responses
- Web and store visit patterns

## 🛠️ Tools Used

- **Python 3.13**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical operations
- **Built-in Python libraries** - datetime, file I/O

## 📁 Project Structure

```
Task 1 Data Cleaning and Preprocessing/
├── marketing_campaign.csv          # Original raw dataset
├── data_cleaning.py               # Main cleaning script
├── customer_personality_cleaned.csv # Cleaned dataset
├── data_cleaning_summary.txt      # Detailed summary report
└── README.md                      # This file
```

## 🚀 How to Run

1. **Prerequisites**: Ensure Python 3.x and pandas are installed
   ```bash
   pip install pandas numpy
   ```

2. **Run the cleaning script**:
   ```bash
   python data_cleaning.py
   ```

3. **Check outputs**:
   - `customer_personality_cleaned.csv` - Cleaned dataset
   - `data_cleaning_summary.txt` - Detailed summary report

## 🔧 Data Cleaning Steps

### 1. **Initial Assessment**
- Analyzed dataset structure and data types
- Identified missing values and duplicates
- Assessed overall data quality

### 2. **Duplicate Removal**
- Removed 0 duplicate rows (dataset was already clean)

### 3. **Missing Value Handling**
- Found 24 missing values in Income column (1.1%)
- Filled missing values with median income (51,381.50)

### 4. **Column Name Standardization**
- Converted all column names to lowercase
- Replaced spaces with underscores
- Example: `Year_Birth` → `year_birth`

### 5. **Date Format Standardization**
- Converted `dt_customer` from string to datetime
- Original format: `dd-mm-yyyy`
- New format: `yyyy-mm-dd`

### 6. **Categorical Data Standardization**
- **Education**: Standardized to lowercase
  - `Graduation` → `graduation`
  - `PhD` → `phd`
  - `Master` → `master`
  - `2n Cycle` → `2n cycle`
  - `Basic` → `basic`

- **Marital Status**: Standardized to lowercase
  - `Married` → `married`
  - `Together` → `together`
  - `Single` → `single`
  - `Divorced` → `divorced`
  - `Widow` → `widow`
  - `Alone` → `alone`
  - `Absurd` → `absurd`
  - `YOLO` → `yolo`

### 7. **Outlier Detection and Treatment**
- Applied IQR (Interquartile Range) method
- Detected outliers in multiple numerical columns
- **Capped outliers** instead of removal to preserve data integrity
- Affected columns: `year_birth`, `income`, `mntwines`, `mntfruits`, `mntmeatproducts`, `mntfishproducts`, `mntsweetproducts`, `mntgoldprods`

### 8. **Data Type Validation**
- Ensured numerical columns are properly typed
- Validated categorical columns as strings
- Confirmed datetime format

## 📈 Results and Quality Metrics

### Before Cleaning:
- **Rows**: 2,240
- **Columns**: 29
- **Missing Values**: 24 (1.1%)
- **Duplicates**: 0
- **Data Quality Score**: 98.9%

### After Cleaning:
- **Rows**: 2,240
- **Columns**: 29
- **Missing Values**: 0 (0%)
- **Duplicates**: 0
- **Data Quality Score**: 100%

### Key Improvements:
✅ **100% Complete Data** - No missing values  
✅ **No Duplicates** - All records are unique  
✅ **Consistent Formats** - Standardized text and dates  
✅ **Proper Data Types** - Validated and corrected  
✅ **Outlier Treatment** - Handled appropriately  
✅ **Ready for Analysis** - Clean, structured dataset  

## 📊 Data Quality Insights

### Missing Values Analysis:
- **Income column**: 24 missing values (1.1%)
- **Strategy**: Filled with median value to preserve distribution

### Outlier Analysis:
- **Year of Birth**: 3 outliers (very old/young customers)
- **Income**: 8 outliers (extremely high/low incomes)
- **Purchase Amounts**: Multiple outliers in spending categories
- **Strategy**: Capped outliers to prevent data loss while maintaining statistical integrity

### Categorical Data Distribution:
- **Education**: 5 categories (Graduation most common at 50.3%)
- **Marital Status**: 8 categories (Married most common at 38.6%)

## 🎓 Learning Outcomes

This project demonstrates mastery of:

1. **Data Quality Assessment** - Identifying issues in raw data
2. **Missing Value Strategies** - Choosing appropriate imputation methods
3. **Outlier Detection** - Using statistical methods (IQR)
4. **Data Standardization** - Consistent formatting across categories
5. **Type Validation** - Ensuring proper data types
6. **Documentation** - Comprehensive reporting and documentation

## 🔍 Interview Questions Addressed

This project answers common data analyst interview questions:

1. **What are missing values and how do you handle them?**
   - Identified 24 missing income values and filled with median

2. **How do you treat duplicate records?**
   - Checked for duplicates and removed them (found 0 in this dataset)

3. **Difference between dropna() and fillna() in Pandas?**
   - Used fillna() to preserve data integrity instead of dropping rows

4. **What is outlier treatment and why is it important?**
   - Applied IQR method and capped outliers to maintain statistical validity

5. **Explain the process of standardizing data.**
   - Standardized column names, categorical values, and date formats

6. **How do you handle inconsistent data formats?**
   - Converted date strings to datetime objects and standardized text

7. **What are common data cleaning challenges?**
   - Demonstrated handling of missing values, outliers, and inconsistent formats

8. **How can you check data quality?**
   - Implemented comprehensive quality metrics and reporting

## 📝 Files Description

- **`data_cleaning.py`**: Main Python script with comprehensive cleaning logic
- **`customer_personality_cleaned.csv`**: Final cleaned dataset ready for analysis
- **`data_cleaning_summary.txt`**: Detailed report of all changes made
- **`README.md`**: Project documentation and guide

## 🎯 Next Steps

The cleaned dataset is now ready for:
- Exploratory Data Analysis (EDA)
- Customer segmentation
- Predictive modeling
- Marketing campaign optimization
- Business intelligence dashboards

---

**Author**: Data Analyst Intern  
**Date**: August 2024  
**Tools**: Python, Pandas, NumPy  
**Dataset**: Customer Personality Analysis (Kaggle) 