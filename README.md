# Task 1: Data Cleaning and Preprocessing

## 📌 Objective
To clean and preprocess the raw marketing dataset by handling missing values, removing duplicates, fixing inconsistent formats, and preparing it for analysis.

## 📊 Dataset
**Customer Personality Analysis**  
- Source: [Kaggle - Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)
- Original file: `marketing_campaign.csv`

## 🛠️ Tools Used
- Python (Pandas)
- Microsoft Excel (for viewing & verifying)

## 🧼 Data Cleaning Summary
- **Duplicates:** Removed duplicate rows.
- **Missing Values:** Filled missing values in the `Income` column using the median.
- **Column Names:** Renamed all columns to lowercase with underscores (snake_case).
- **Date Format:** Converted `Dt_Customer` to `datetime` format (`dd-mm-yyyy`).
- **Categorical Text:** Standardized `Education` and `Marital_Status` fields to lowercase.
- **Data Types:** Verified and corrected data types for consistency.

## 📁 Files Included
- `marketing_campaign.csv` – Original dataset
- `customer_personality_cleaned.csv` – Final cleaned dataset
- `data_cleaning.py` – Python script used for cleaning
- `README.md` – Documentation of the task and steps followed

## ✅ Output
Cleaned dataset saved as:  
`customer_personality_cleaned.csv`
