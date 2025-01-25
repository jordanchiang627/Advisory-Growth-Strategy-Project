import pandas as pd

# flake8: noqa

def save_csv(df, file_path):
    df.to_csv(file_path, index = False)
    print(f"DataFrame successfully saved to {file_path}")

demographics = pd.read_csv("CleanedDataR2/demogrpahics_r2.csv")

demographics["Dependants"] = (demographics["Under 5 years"] + demographics["5 to 9 years"] + demographics["10 to 14 years"] + 
demographics["15 to 19 years"] + demographics["20 to 24 years"])


demographics["Working Age"] = (demographics["25 to 34 years"] + demographics["35 to 44 years"] + demographics["45 to 54 years"] + 
demographics["55 to 59 years"] + demographics["60 to 64 years"])

demographics["Retired"] = (demographics["65 to 74 years"] + demographics["75 to 84 years"] + demographics["85 years and over"])

demographics["Primary Stage Investors"] = (demographics["35 to 44 years"] + demographics["45 to 54 years"] + 
demographics["55 to 59 years"] + demographics["60 to 64 years"])
demographics["Early Stage Investors"] = demographics["25 to 34 years"]


demographics = demographics[['Geography', 'Geographic Area Name', 'Total population', 'Male', 'Female', 'Dependants', 'Early Stage Investors', 'Primary Stage Investors',
'Working Age', 'Retired']]

save_csv(demographics, "CleanedDataR3/demographics_r3.csv")

