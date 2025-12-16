import fitz
import os
from utils import clean_text, make_continuous, capitalize_after_comma, time_to_minutes, split_date_range, split_names
import pandas as pd
import re
import dateparser


IN_FOLDER='./data/excel'
OUT_FOLDER ='./data/excel'

file="odeon-raw.xlsx"
path= os.path.join(IN_FOLDER,file)
df=pd.read_excel(path)

cols = ["titre","sous-titre", "dates", "salle","production", "coproduction", "aide", "soutien"]
df[cols] = df[cols].map(clean_text)

cols= ["production", "coproduction", "aide", "soutien"]
df[cols] = df[cols].map(capitalize_after_comma)

cols= ["synopsis"]
df[cols] = df[cols].map(make_continuous)

cols= ["durée"]
df[cols] = df[cols].map(time_to_minutes)

df[["date_start", "date_end"]] = (
    df["dates"]
    .apply(split_date_range)
    .apply(pd.Series)
)

cols= [
    "vidéo",
    "cadre vidéo",
    "régie vidéo",
    "collaboration à la vidéo",

    "musique",
    "composition musicale",
    "composition musicale du satellite",
    "composition musicale du Choeur",
    "collaboration artistique pour la direction, l’adaptation et l’arrangement musical",

    "son",
    "collaboration au son",

    "mise en scène",
    "collaboration conception et mise en scène",
    "assistanat à la mise en scène",

    "scénographie",
    "collaboration à la scénographie",
    "recherche scénographique",
    "regard scénographique",
    "espaces",
    "accessoires",

    "régie générale",

    "traduction",

    "avec",

    "adaptation",
    "dramaturgie",

    "lumière",

    "costumes",
    "assistanat aux costumes",
    "masks",

    "collaboration artistique",

    "maquillages",

    "confection du satellite",
    "créateur des souffleurs",
    "surtitrage",
    "production",
    "coproduction",
    "coréalisation",
    "aide",
    "soutien",
    "works",
    "auteur"
]
df[cols] = df[cols].map(split_names)

file="clean-csv.xlsx"
path=os.path.join(OUT_FOLDER, file)
df.to_excel(path, index=False)

print(f'Text transformation complete!')