import pandas as pd

# flake8: noqa

demographics = pd.read_csv("BayArea_DemoHousing/ACSDP5Y2023.DP05-Data.csv")
# print(demographics.head(5))

demographics = demographics[['GEO_ID', 'NAME', 'DP05_0001E', 'DP05_0002E', 'DP05_0003E', 'DP05_0005E', 'DP05_0006E', 'DP05_0007E',
'DP05_0008E', 'DP05_0009E', 'DP05_0010E', 'DP05_0011E', 'DP05_0012E', 'DP05_0013E', 'DP05_0014E', 'DP05_0015E',
'DP05_0016E', 'DP05_0017E', 'DP05_0037E', 'DP05_0038E', 'DP05_0039E', 'DP05_0040E', 'DP05_0047E', 'DP05_0060E', 'DP05_0061E', 'DP05_0076E']]
# print(demographics.head(5))
demographics.columns = demographics.iloc[0]
demographics = demographics.drop(0).reset_index(drop=True)
print(demographics.head(5))

demographics.to_csv('CleanedData/demographics.csv', index=False)