## Séminaire FRA6730 — Littérature et culture numérique
##### UdeM automne 2025

Ce dépôt contient l'ensemble des documents et figures liés au séminaire FRA6730 (Littérature et culture numérique).

---

### Décembre 2025 -> Projet final : vers un modèle de l'événement théâtral

Ce git contient une étude de cas qui cherche à implémenter un modèle de l'*événement théâtral* tel qu’il est actuellement développé au sein du projet STAGE et dans le cadre de ma thèse. Cette étude de cas porte sur le Théâtre de l’Odéon à Paris et, plus spécifiquement, utilise les informations issues du programme de saison afin de modéliser quatre de ses spectacles. Le format final du modèle prend la forme d’une collection de fichiers JSON par spectacle.

| id   | événement                     | excel                  | json                                   |
|------|-------------------------------|------------------------|----------------------------------------|
| od_1 | *Le Passé* à Odéon               | clean_csv (row[0])     | a-final & b-final & multiple c          |
| od_2 | *Musée Duras* à Odéon            | clean_csv (row[1])     | a-final & b-final & multiple c          |
| od_3 | *Honda Romance* à Odéon          | clean_csv (row[2])     | a-final & b-final & multiple c          |
| od_4 | *Pallaksch Pallaksch!* à Odéon   | clean_csv (row[3])     | a-final & b-final & multiple c          |

*Les quatre spectacles sélectionnés sont d’abord modélisés dans un tableau Excel, puis représentés à travers de multiples fichiers JSON.*

Les informations du programme ont été retranscrites d’abord manuellement au format d’un [tableau Excel](./data/excel/clean-csv.xlsx), puis au format JSON à travers des fonctions en Python écrites spécifiquement pour cet exercice. Le dépôt Git contient l’ensemble du [code](./scripts/) (reproductible), ainsi que les [fichiers JSON](./data/json/) qui visent à représenter chacun des quatre spectacles. Enfin, cet exercice de modélisation est accompagné d’une [discussion](./text/description.md) sur ses possibilités et ses limites.


```
FRA-6730/
├── README.md
├── assets/
│   ├── images/(files)
│   └── pdf/ (files)
├── data/
│   ├── excel/
│   │   └── (four files)
│   └── json/
│       ├── od_1/
│       │   ├── a-conceptual/
│       │   ├── b-production/
│       │   └── c-shows/
│       ├── od_2/
│       │   ├── a-conceptual/
│       │   ├── b-production/
│       │   └── c-shows/
│       ├── od_3/
│       │   ├── a-conceptual/
│       │   ├── b-production/
│       │   └── c-shows/
│       └── od_4/
│           ├── a-conceptual/
│           ├── b-production/
│           └── c-shows/
├── scripts/
│   ├── (7 scripts (a->g))
│   ├── utils.py
│   └── z-disclaimer.md
├── text/
│   ├── description.md
│   ├── 
│   └── 
└── requirements.txt
```
*La structure du git.*

---



### Octobre 2025 -> proposition de projet de semestre

Ma proposation de modélisation d'un spectacle théâtral (lire [ici](performance-théâtre/projet-performance-pitch.md)), s’appuie sur des idées développées au sein du projet [STAGE](https://stage-to-data.huma-num.fr/) au cours de la première année de mon doctorat à l’Université Rennes 2. Ce [travail](https://github.com/stage-to-data/linked-art-pa) collectif est en cours, et je propose de travailler sur un projet existant, pour mieux comprendre les enjeux théoriques et sociopolitiques liés aux choix, simplifications et présupposés qu’implique notre modélisation, que je pourrais ensuite intégrer à ma thèse. Pourtant, je me demande si ce projet correspond bien aux enjeux du séminaire, puisqu'on cherche à modéliser un « événement » et le « choix » du modèle est déjà fait, même s'il s'agit d'un modèle ouvert que je peux toujours modifier.






@ Antonios Lagarias
