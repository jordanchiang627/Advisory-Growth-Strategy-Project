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



save_csv(demographics, "CleanedDataR3/demographics_r3.csv")

