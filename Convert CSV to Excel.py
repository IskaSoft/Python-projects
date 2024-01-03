import pandas as pd
import numpy as np
# Reading the csv file
df_new = pd.read_csv('Names.csv')
# saving xlsx file
myfile = pd.ExcelWriter('Names.xlsx')
df_new.to_excel(myfile, index = False)
myfile.save()