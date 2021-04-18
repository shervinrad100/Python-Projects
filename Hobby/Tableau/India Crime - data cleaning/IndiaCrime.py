# India Datasets
## Crime 

import pandas as pd

DistrictWiseCrimesCommitted_IPC2001_2012 = pd.read_csv(
        "E:\\DB_Data\\Kaggle\\India\\crime-in-india\\crime\\01_District_wise_crimes_committed_IPC_2001_2012.csv",
        header=0)

DistrictWiseCrimesCommitted_IPC2013 = pd.read_csv(
        "E:\\DB_Data\\Kaggle\\India\\crime-in-india\\crime\\01_District_wise_crimes_committed_IPC_2013.csv",
        header=0)

for index in range(DistrictWiseCrimesCommitted_IPC2001_2012.index[-1]):
    print(index)



# and DistrictWiseCrimesCommitted_IPC2013:
    