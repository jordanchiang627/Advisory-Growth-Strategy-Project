# flake8: noqa

import pandas as pd
import matplotlib.pyplot as plt

def proportion_pie_charts(df):

    prop_cols = [col for col in df.columns if 'Proportion' in col]

    for region in df["Geographic Area Name"].unique():
        region_data = df[df["Geographic Area Name"] == region].iloc[0]
        proportions = region_data[prop_cols].values
        labels = [col.replace(" Proportion", "") for col in prop_cols]

        plt.figure(figsize=(8,6))
        wedges, texts, autotexts = plt.pie(proportions, labels = None, autopct = "%1.1f%%", startangle = 140)
        plt.title(f"Age Proportions for {region}")
        plt.axis=("equal")

        legend_labels = [f"{label}" for label, value in zip(labels, proportions)]
        plt.legend(wedges, legend_labels, title = "Age Groups", loc = "center left", bbox_to_anchor = (1, 0.5))

        file_name = f"EDA_Img/AgeProp_{region}.png"
        plt.savefig(file_name, bbox_inches = "tight")
        plt.close()

        print(f"Pie Chart saved as {file_name}")

demographics = pd.read_csv("CleanedDataR3/demographics_r3.csv")
demographics = demographics.drop(["Working Age", "Working Age Proportion"], axis = 1)
proportion_pie_charts(demographics)
