import pandas as pd
import matplotlib.pyplot as plt

bd = pd.read_csv("dataset.csv")

plt.bar(bd['certificate'].value_counts().index, bd['certificate'].value_counts().values);