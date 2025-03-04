import pandas as pd

# flake8: noqa

def save_csv(df, file_path):
    df.to_csv(file_path, index = False)
    print(f"DataFrame successfully saved to {file_path}")

def age_proportions(df, col1, col2, new_column):
    """
    This function will take column 1 and divide it by column 2 to find the wanted proportion 
    """
    df[new_column] = (df[col1]/df[col2].replace(0, pd.NA)*100).round(2)
    return df

def sum_columns(df, columns_to_sum, new_column):
    df[new_column] = df[columns_to_sum].sum(axis = 1)
    return df

demographics = pd.read_csv("CleanedDataR2/demogrpahics_r2.csv")

demographics["Dependants"] = (demographics["Under 5 years"] + demographics["5 to 9 years"] + demographics["10 to 14 years"] + 
demographics["15 to 19 years"] + demographics["20 to 24 years"])


demographics["Working Age"] = (demographics["25 to 34 years"] + demographics["35 to 44 years"] + demographics["45 to 54 years"] + 
demographics["55 to 59 years"] + demographics["60 to 64 years"])

demographics["Retired"] = (demographics["65 to 74 years"] + demographics["75 to 84 years"] + demographics["85 years and over"])

demographics["Primary Stage Investors"] = (demographics["35 to 44 years"] + demographics["45 to 54 years"] + 
demographics["55 to 59 years"] + demographics["60 to 64 years"])
demographics["Early Stage Investors"] = demographics["25 to 34 years"]

age_proportions(demographics, "Dependants", "Total population", "Dependants Proportion")
age_proportions(demographics, "Working Age", "Total population", "Working Age Proportion")
age_proportions(demographics, "Retired", "Total population", "Retired Proportion")
age_proportions(demographics, "Early Stage Investors", "Working Age", "Early Stage Proportion of Working Age")
age_proportions(demographics, "Primary Stage Investors", "Working Age", "Primary Stage Proportion of Working Age")

demographics = demographics[['Geography', 'Geographic Area Name', 'Total population', 'Dependants', 'Dependants Proportion', 'Early Stage Investors', 'Early Stage Proportion of Working Age',
'Primary Stage Investors', 'Primary Stage Proportion of Working Age', 'Working Age', 'Working Age Proportion', 'Retired', 'Retired Proportion']]

econmetrics = pd.read_csv("CleanedDataR2/econmetrics_r2.csv")

column_groups = {
    "Low Income - Households" : ["Total households - Less than $10,000", "Total households - $10,000 to $14,999", "Total households - $15,000 to $24,999"],
    "Middle Income - Households" : ["Total households - $25,000 to $34,999", "Total households - $35,000 to $49,999", "Total households - $50,000 to $74,999"],
    "Upper Middle Income - Households" : ["Total households - $75,000 to $99,999", "Total households - $100,000 to $149,999"],
    "High Income - Households" : ["Total households - $150,000 to $199,999", "Total households - $200,000 or more"],
    "Low Income - Families" : ["Families - Less than $10,000", "Families - $10,000 to $14,999", "Families - $15,000 to $24,999"],
    "Middle Income - Families" : ["Families - $25,000 to $34,999", "Families - $35,000 to $49,999", "Families - $50,000 to $74,999"],
    "Upper Middle Income - Families" : ["Families - $75,000 to $99,999", "Families - $100,000 to $149,999"],
    "High Income - Families" : ["Families - $150,000 to $199,999", "Families - $200,000 or more"]
}

for new_col, cols in column_groups.items():
    econmetrics =  sum_columns(econmetrics, cols, new_col)

econ_prop_groups = {
    "Proportion: Low Income - Households" : ["Low Income - Households", "Total households"],
    "Proportion: Middle Income - Households" : ["Middle Income - Households", "Total households"],
    "Proportion: Upper Middle Income - Households" : ["Upper Middle Income - Households", "Total households"],
    "Proportion: High Income - Households" : ["High Income - Households", "Total households"],
    "Proportion: Low Income - Families" : ["Low Income - Families", "Families"],
    "Proportion: Middle Income - Families" : ["Middle Income - Families", "Families"],
    "Proportion: Upper Middle Income - Families" : ["Upper Middle Income - Families", "Families"],
    "Proportion: High Income - Families" : ["High Income - Families", "Families"]
}

for new_column, (col1, col2) in econ_prop_groups.items():
    econmetrics = age_proportions(econmetrics, col1, col2, new_column)

econmetrics = econmetrics[["Geography", "Geographic Area Name", "Total households", "Total households - Median household income (dollars)", "Families", "Families - Median family income (dollars)", "Low Income - Households",
"Proportion: Low Income - Households", "Middle Income - Households", "Proportion: Middle Income - Households",  "Upper Middle Income - Households",  "Proportion: Upper Middle Income - Households",
"High Income - Households", "Proportion: High Income - Households", "Low Income - Families", "Proportion: Low Income - Families", "Middle Income - Families", "Proportion: Middle Income - Families",
"Upper Middle Income - Families", "Proportion: Upper Middle Income - Families", "High Income - Families", "Proportion: High Income - Families"]]

households = pd.read_csv("CleanedDataR2/households_r2.csv")

keep_columns = ["Nonfmaily household: Average household size", "Total: Average household size", "Total: Average family size"]
households = households.drop(
    households.select_dtypes(include=['float']).columns.difference(keep_columns),
    axis = 1
)

#save_csv(demographics, "CleanedDataR3/demographics_r3.csv")
#save_csv(econmetrics, "CleanedDataR3/econmetrics_r3.csv")
save_csv(households, "CleanedDataR3/households_r3.csv")
