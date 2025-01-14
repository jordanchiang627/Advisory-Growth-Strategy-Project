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
# print(demographics.head(5))

demographics = demographics[['GEO_ID', 'NAME', 'DP05_0001E', 'DP05_0002E', 'DP05_0003E', 'DP05_0005E', 'DP05_0006E', 'DP05_0007E',
'DP05_0008E', 'DP05_0009E', 'DP05_0010E', 'DP05_0011E', 'DP05_0012E', 'DP05_0013E', 'DP05_0014E', 'DP05_0015E',
'DP05_0016E', 'DP05_0017E', 'DP05_0037E', 'DP05_0038E', 'DP05_0039E', 'DP05_0040E', 'DP05_0047E', 'DP05_0060E', 'DP05_0061E', 'DP05_0076E']]

econmetrics = pd.read_csv("BayArea_EconMetrics/ACSDP5Y2023.DP03-Data.csv")


econmetrics = econmetrics[['GEO_ID', 'NAME', 'DP03_0001E', 'DP03_0002E', 'DP03_0003E', 'DP03_0004E', 'DP03_0005E', 'DP03_0007E', 'DP03_0033E',
'DP03_0034E', 'DP03_0035E', 'DP03_0036E', 'DP03_0037E', 'DP03_0038E', 'DP03_0039E', 'DP03_0040E', 'DP03_0041E', 'DP03_0042E', 'DP03_0043E',
'DP03_0044E', 'DP03_0045E', 'DP03_0052E', 'DP03_0052E', 'DP03_0053E', 'DP03_0054E', 'DP03_0055E', 'DP03_0056E', 'DP03_0057E', 'DP03_0058E',
'DP03_0059E', 'DP03_0060E', 'DP03_0061E', 'DP03_0062E', 'DP03_0075E', 'DP03_0076E', 'DP03_0077E', 'DP03_0078E', 'DP03_0079E', 'DP03_0080E',
'DP03_0081E', 'DP03_0082E', 'DP03_0083E', 'DP03_0084E', 'DP03_0085E', 'DP03_0086E']]

demographics = clean_and_save(demographics, 'CleanedData/demographics.csv')
econmetrics = clean_and_save(econmetrics, 'CleanedData/econmetrics.csv')
