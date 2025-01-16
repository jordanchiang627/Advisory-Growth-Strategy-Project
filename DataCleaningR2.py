import pandas as pd
import re

# flake8: noqa

demographics_cleaned = pd.read_csv('CleanedData/demographics.csv')
econmetrics_cleaned = pd.read_csv('CleanedData/econmetrics.csv')
education_cleaned = pd.read_csv('CleanedData/education.csv')
households_cleaned = pd.read_csv('CleanedData/households.csv')

def clean_column_names(column_names):
    cleaned_names = []
    for name in column_names:
        match = re.search(r'!![A-Z ]+!!', name)
        if match:
            cleaned_names.append(name.split(match.group(0))[-1].strip())
        else:
            cleaned_names.append(name.strip())
    return cleaned_names

def remove_and_replace(columns, to_remove = None, to_replace = None):
    cleaned_columns = []
    for col in columns:
        if to_remove:
            for remove in to_remove:
                col = col.replace(remove, "")
        if to_replace:
            for old, new in to_replace.items():
                col = col.replace(old, new)
        col = col.strip()
        cleaned_columns.append(col)
    return cleaned_columns

def save_csv(df, file_path):
    df.to_csv(file_path, index = False)
    print(f"DataFrame successfully saved to {file_path}")

demographics_cleaned.columns = clean_column_names(demographics_cleaned.columns)
econmetrics_cleaned.columns = clean_column_names(econmetrics_cleaned.columns)
education_cleaned.columns = clean_column_names(education_cleaned.columns)

#print("Cleaned Econmetrics Names:", econmetrics_cleaned.columns.tolist())
#print("Cleaned Education Names:", education_cleaned.columns.tolist())
#print("Cleaned Households Names:", households_cleaned.columns.tolist())

demographics_cleaned.columns = [
    col.split("!!")[-1].strip() for col in demographics_cleaned.columns
]
# print("Cleaned Column Names:", demographics_cleaned.columns.tolist())

econmetrics_cleaned.columns = [
    " - ".join(col.split("!!")[-2:]).strip() if "!!" in col else col
    for col in econmetrics_cleaned.columns
]

econmetrics_cleaned.columns = remove_and_replace(
    econmetrics_cleaned.columns,
    to_remove = [
        "INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS) - "
    ]
)
# print("Cleaned Econmetrics Names:", econmetrics_cleaned.columns.tolist())

education_cleaned.columns = remove_and_replace(
    education_cleaned.columns,
    to_remove = [
        "IN THE PAST 12 MONTHS (IN 2023 INFLATION-ADJUSTED DOLLARS)", "Estimate!!Total!!"
    ],
    to_replace = {
        "MEDIAN EARNINGS":"Median Earnings",
        "!!":" - "
    }
)
# print("Cleaned Education Names:", education_cleaned.columns.tolist())

households_cleaned.columns = [
    re.sub(r'!![A-Z ]+!!', '', col).strip() for col in households_cleaned.columns
]
households_cleaned.columns = remove_and_replace(
    households_cleaned.columns,
    to_remove = [
        "Estimate!!"
    ],
    to_replace = {
        "!!":" - "
    }
)
households_cleaned.columns = [
    re.sub(r'([a-z])([A-Z])', r'\1: \2', col).strip() for col in households_cleaned.columns
]

columns_to_drop = [col for col in households_cleaned.columns if (households_cleaned[col] == "(X)").all()]
households_cleaned = households_cleaned.drop(columns=columns_to_drop)
#households_cleaned = households_cleaned.loc[:, ~households_cleaned == "(X)".all()]

# print("Cleaned Households Names:", households_cleaned.columns.tolist())

save_csv(demographics_cleaned, "CleanedDataR2/demogrpahics_r2.csv")
save_csv(econmetrics_cleaned, "CleanedDataR2/econmetrics_r2.csv")
save_csv(education_cleaned, "CleanedDataR2/education_r2.csv")
save_csv(households_cleaned, "CleanedDataR2/households_r2.csv")
