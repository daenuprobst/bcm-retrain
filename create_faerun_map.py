import gzip
import pickle
from pathlib import Path
import pandas as pd
import tmap as tm
from faerun import FaerunPlot
from matplotlib.colors import ListedColormap


def main():
    df = pickle.load(gzip.open("all_unmapped_reactions.pkl.gz", "rb"))
    df = df.astype({"ec1": int, "ec2": int, "ec3": int})

    te = tm.embed(
        df.fps,
        layout_generator=tm.layout_generators.AnnoyLayoutGenerator(
            k=60,
            kc=60,
            node_size=1 / 65,
            mmm_repeats=1,
            sl_repeats=6,
            sl_extra_scaling_steps=5,
            n_trees=16
        ),
    )

    custom_cmap = ListedColormap(
        [
            "#e41a1c",
            "#377eb8",
            "#4daf4a",
            "#984ea3",
            "#ff7f00",
            "#ffff33",
            "#a65628",
        ],
        name="custom",
    )

    fp = FaerunPlot(thumbnail_fixed=True)
    fp.add_tmap_series(
        te,
        c=df.ec1,
        labels=df.rxn,
        categorical=True,
        cmap="Set2",
        tree_color="#282828",
        point_scale=0.75,
    )
    fp.save("all_unmapped_reactions", "smiles")


if __name__ == "__main__":
    main()
