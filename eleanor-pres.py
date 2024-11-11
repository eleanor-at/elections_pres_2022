import pandas as pd
import numpy as np

df = pd.read_excel('votes-pres-2022.xlsx')

df.head(10)

colonnes = df.columns
print(len(colonnes)), print(colonnes)


df.dtypes

# +
#on veut obtenir les memes statistiques par département,
#on corrige le type des colonnes devant être des nombres pour 
#pouvoir les sommer

df['Code du département'] = pd.to_numeric(df['Code du département'])
df.dtypes
# -

donnees_num = df.select_dtypes(include = 'number')
print(donnees_num.columns)

#ON NE CONSERVE QUE LES DONNÉES PERTINENTES, SOMMER LES POURCENTAGES RELATIFS À UNE COMMUNE N'A PAS DE SENS
donnees_num.groupby('Code du département').sum()[[
'Inscrits', 'Abstentions', 'Votants', 'Blancs', 'Nuls', 'Exprimés', 'N°Panneau 1', 'Voix 1','N°Panneau 2', 'Voix 2', 'N°Panneau 3', 'Voix 3',
'N°Panneau 4', 'Voix 4','N°Panneau 5', 'Voix 5', 'N°Panneau 6', 'Voix 6','N°Panneau 7', 'Voix 7','N°Panneau 8', 'Voix 8',
'N°Panneau 9', 'Voix 9', 'N°Panneau 10', 'Voix 10','N°Panneau 11', 'Voix 11', 'N°Panneau 12', 'Voix 12',]]
