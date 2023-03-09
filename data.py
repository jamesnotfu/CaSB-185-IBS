import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

# load data from CSV file
df = pd.read_csv("prevotella.csv")

# perform two-sample t-test
IBS = df[df["hc"] == 1]["hits"]
HC = df[df["hc"] == 0]["hits"]
t, p = ttest_ind(IBS, HC, equal_var=False)

# create scatter plot with regression line
sns.regplot(x="hc", y="hits", data=df, ci=None)

# add title and axis labels
plt.title("Lachnospira abundance in IBS vs. HC Patients")
plt.xlabel("IBS [0] / No IBS [1]")
plt.ylabel("# of Hits")

# add t-test results to plot
if p < 0.05:
    plt.text(0, df["hits"].max(), f"t-test p-value = {p:.3f}\nSignificant", ha="left", va="top")
else:
    plt.text(0, df["hits"].max(), f"t-test p-value = {p:.3f}\nNot significant", ha="left", va="top")

# display plot
plt.show()
