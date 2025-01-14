import pandas as pd

# flake8: noqa

def clean_and_save(df, filename):
    """""
    Cleans a dataframe by setting the first row as the header

    Parameters:
    - df (dataframe): The dataframe to clean
    - filename (str): The file path where the csv will be saved to

    Returns:
    - dataframe: In case of later use
    """
    df.columns = df.iloc[0]
    df = df.drop(0).reset_index(drop=True)
    df.to_csv(filename, index=False)
    print(df.head(5))
    print(f"Data successfully cleaned and saved to {filename}")
    return(df)

demographics = pd.read_csv("BayArea_DemoHousing/ACSDP5Y2023.DP05-Data.csv")
demographics = demographics[['GEO_ID', 'NAME', 'DP05_0001E', 'DP05_0002E', 'DP05_0003E', 'DP05_0005E', 'DP05_0006E', 'DP05_0007E',
'DP05_0008E', 'DP05_0009E', 'DP05_0010E', 'DP05_0011E', 'DP05_0012E', 'DP05_0013E', 'DP05_0014E', 'DP05_0015E',
'DP05_0016E', 'DP05_0017E', 'DP05_0037E', 'DP05_0038E', 'DP05_0039E', 'DP05_0040E', 'DP05_0047E', 'DP05_0060E', 'DP05_0061E', 'DP05_0076E']]

econmetrics = pd.read_csv("BayArea_EconMetrics/ACSDP5Y2023.DP03-Data.csv")
econmetrics = econmetrics[['GEO_ID', 'NAME', 'DP03_0001E', 'DP03_0002E', 'DP03_0003E', 'DP03_0004E', 'DP03_0005E', 'DP03_0007E', 'DP03_0033E',
'DP03_0034E', 'DP03_0035E', 'DP03_0036E', 'DP03_0037E', 'DP03_0038E', 'DP03_0039E', 'DP03_0040E', 'DP03_0041E', 'DP03_0042E', 'DP03_0043E',
'DP03_0044E', 'DP03_0045E', 'DP03_0052E', 'DP03_0052E', 'DP03_0053E', 'DP03_0054E', 'DP03_0055E', 'DP03_0056E', 'DP03_0057E', 'DP03_0058E',
'DP03_0059E', 'DP03_0060E', 'DP03_0061E', 'DP03_0062E', 'DP03_0075E', 'DP03_0076E', 'DP03_0077E', 'DP03_0078E', 'DP03_0079E', 'DP03_0080E',
'DP03_0081E', 'DP03_0082E', 'DP03_0083E', 'DP03_0084E', 'DP03_0085E', 'DP03_0086E']]

education = pd.read_csv("BayArea_Education/ACSST5Y2023.S1501-Data.csv")
education = education[['GEO_ID', 'NAME', 'S1501_C01_001E', 'S1501_C01_002E', 'S1501_C01_003E', 'S1501_C01_004E', 'S1501_C01_005E', 'S1501_C01_006E', 'S1501_C01_007E', 'S1501_C01_008E', 'S1501_C01_009E',
'S1501_C01_010E', 'S1501_C01_011E', 'S1501_C01_012E', 'S1501_C01_013E', 'S1501_C01_014E', 'S1501_C01_015E', 'S1501_C01_059E', 'S1501_C01_060E', 'S1501_C01_061E', 'S1501_C01_062E', 'S1501_C01_063E', 'S1501_C01_064E']]

households = pd.read_csv("BayArea_Households/ACSST5Y2023.S1101-Data.csv")
households = households[['GEO_ID', 'NAME', 'S1101_C01_001E', 'S1101_C01_002E', 'S1101_C01_003E', 'S1101_C01_004E', 'S1101_C01_005E', 'S1101_C01_006E', 'S1101_C01_007E', 'S1101_C01_008E', 'S1101_C01_009E', 'S1101_C01_010E', 'S1101_C01_011E',
'S1101_C01_012E', 'S1101_C01_013E', 'S1101_C01_014E', 'S1101_C02_001E', 'S1101_C02_002E', 'S1101_C02_003E', 'S1101_C02_004E', 'S1101_C02_005E', 'S1101_C02_006E', 'S1101_C02_007E', 'S1101_C02_008E', 'S1101_C02_009E', 'S1101_C02_010E', 'S1101_C02_011E',
'S1101_C02_012E', 'S1101_C02_013E', 'S1101_C02_014E', 'S1101_C03_001E', 'S1101_C03_002E', 'S1101_C03_003E', 'S1101_C03_004E', 'S1101_C03_005E', 'S1101_C03_006E', 'S1101_C03_007E', 'S1101_C03_008E', 'S1101_C03_009E', 'S1101_C03_010E', 'S1101_C03_011E',
'S1101_C03_012E', 'S1101_C03_013E', 'S1101_C03_014E', 'S1101_C04_001E', 'S1101_C04_002E', 'S1101_C04_003E', 'S1101_C04_004E', 'S1101_C04_005E', 'S1101_C04_006E', 'S1101_C04_007E', 'S1101_C04_008E', 'S1101_C04_009E', 'S1101_C04_010E', 'S1101_C04_011E',
'S1101_C04_012E', 'S1101_C04_013E', 'S1101_C04_014E', 'S1101_C05_001E', 'S1101_C05_002E', 'S1101_C05_003E', 'S1101_C05_004E', 'S1101_C05_005E', 'S1101_C05_006E', 'S1101_C05_007E', 'S1101_C05_008E', 'S1101_C05_009E', 'S1101_C05_010E', 'S1101_C05_011E',
'S1101_C05_012E', 'S1101_C05_013E', 'S1101_C05_014E']]

demographics = clean_and_save(demographics, 'CleanedData/demographics.csv')
econmetrics = clean_and_save(econmetrics, 'CleanedData/econmetrics.csv')
education = clean_and_save(education, 'CleanedData/education.csv')
households = clean_and_save(households, 'CleanedData/households.csv')
