import pandas as pd
import matplotlib.pyplot as plt

CPI = pd.read_csv("", index_col="", parse_date="")

CPI["MA_X"] = CPI[""].rolling(X).mean().