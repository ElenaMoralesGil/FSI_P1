import pandas as pd

usecols=["image","MEL","NV","BCC","AK","BKL","DF","VASC","SCC","UNK"]
csv = pd.read_csv(".dataset/ISIC_2019_Training_Metadata.csv", index_col="image", usecols=usecols)

print(csv.head())