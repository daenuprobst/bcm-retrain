import re
import pandas as pd
import numpy as np
from drfp import DrfpEncoder


def main():
    df = pd.read_csv("all_unmapped_reactions.csv")
    df = df.rename(
        columns={
            "ID": "id",
            "EC_NUM": "ec",
            "RXN": "rxn",
            "RXN_TEXT": "rxn_text",
            "ORIG_RXN_TEXT": "orig_rxn_text",
            "REVERSIBLE": "reversible",
        }
    )
    df["ec1"] = df.ec.str.split(".", expand=True)[0]
    df["ec2"] = df.ec.str.split(".", expand=True)[1]
    df["ec3"] = df.ec.str.split(".", expand=True)[2]
    df["ec4"] = df.ec.str.split(".", expand=True)[3]

    df["fps"] = DrfpEncoder.encode(df.rxn)
    df.to_pickle("all_unmapped_reactions.pkl")


if __name__ == "__main__":
    main()
