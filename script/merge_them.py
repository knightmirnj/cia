import os
import pandas as pd

main_csv = pd.read_csv("../cia-factbook.csv")

xd = set()

for i in (os.listdir("../datasets")):

    curr_ds = pd.read_csv(f"../datasets/{i}")
    curr_ds.drop("number", axis=1, inplace=True)

    for j in curr_ds:
        curr_ds_column = j

    print(f"{i[:-4]}")
    print()

    for index, row in curr_ds.iterrows():
        print(row['country'], row[f'{curr_ds_column}'])

        main_csv.loc[main_csv.index[main_csv["country"] == row["country"]].tolist()[0], f"{i[:-4]}"] = row[
            f'{curr_ds_column}']

main_csv.drop("Unnamed: 1", axis=1, inplace=True)
main_csv.to_csv("../cia-factbook-alpha.csv", index=False)
