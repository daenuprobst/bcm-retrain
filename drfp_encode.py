import re
import pandas as pd
import numpy as np
from drfp import DrfpEncoder


def main():
    df = pd.read_csv("original/combined.txt", names=["rxn"])
    df["ec"] = df.rxn.apply(lambda x: x.split(">>")[0].split("|")[1])
    df["rxn"] = df.rxn.apply(lambda x: re.sub(r"\|.*?\>\>", ">>", x))
    df["ec1"] = df.ec.str.split(".", expand=True)[0]
    df["ec2"] = df.ec.str.split(".", expand=True)[1]
    df["ec3"] = df.ec.str.split(".", expand=True)[2]
    df["ec4"] = df.ec.str.split(".", expand=True)[3]

    df["fps"] = DrfpEncoder.encode(df.rxn)
    df.to_pickle("brenda-original.pkl")


if __name__ == "__main__":
    main()
