#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_excel('C:/Users/maxir/cours-info/elections_pres_2022/votes-pres-2022.xlsx')
df


# In[3]:


df.dtypes


# In[4]:


df.columns


# In[5]:


cellules_vides = df.isnull()
print(cellules_vides)


# In[6]:


nombre_cellules_vides = cellules_vides.sum().sum()
print(nombre_cellules_vides)
# pour vérifier que le dataframme est complet


# In[7]:


resultats = pd.DataFrame()
for i in range(1, 13):
    # Regrouper les voix par département
    df_voix = df.groupby('Code du département')[f'Voix {i}'].sum()
    # Ajouter cette série comme une colonne au DataFrame des résultats
    resultats[f'Nom {i}'] = df[f'Nom {i}'][1]
    resultats[f'Voix {i}'] = df_voix
print(resultats)
# résultats des élections par département


# In[8]:


# Identification des colonnes contenant des voix
colonnes_voix = [col for col in resultats.columns if 'Voix' in col]
total_voix_par_colonne = resultats[colonnes_voix].sum()
print("Voix pour chaque candidat :")
print(total_voix_par_colonne)
# nombre total de voix par candidat


# In[9]:


voix_series = pd.Series(total_voix_par_colonne)
total_voix = total_voix_par_colonne.sum()
# Calcul des pourcentages
pourcentages_series = (voix_series / total_voix) * 100
print("Pourcentages des voix par candidat :")
print(pourcentages_series)
# pourcentage correspondant à ce nombre de voix


# In[10]:


taux_abs = pd.DataFrame()
df_abs = df.groupby('Code du département')['Abstentions'].sum()
df_ins = df.groupby('Code du département')['Inscrits'].sum()
taux_abs['Abstentions'] = df_abs
taux_abs['Inscrits'] = df_ins
print(taux_abs)
# taux d'abstention par région


# In[11]:


taux_abs['Taux_abstention'] = (taux_abs['Abstentions'] / taux_abs['Inscrits']) * 100
print(taux_abs)


# In[12]:


nouveau = pd.DataFrame()
for i in range(1, 13):
    # Regrouper les voix par département
    df_voix = df.groupby('Code du département')[f'Voix {i}'].sum()
    nouveau[f'Voix {i}'] = df_voix
nouveau['Max_Value'] = nouveau.max(axis=1)
nouveau['Max_Column'] = nouveau.idxmax(axis=1)
nouveau['Inscrits'] = df.groupby('Code du département')['Inscrits'].sum()
nouveau['Points'] = nouveau.apply(lambda row: row['Inscrits'] if row['Max_Value'] == row[row['Max_Column']] else 0, axis=1) # le score maximal de voix remporte toutes les voix du département
print(nouveau)
# simuler les résultats d'élections selon le modèle américain


# In[13]:


points = pd.DataFrame()
for i in range(1, 13):
    points[f'points {i}'] = nouveau.apply(lambda row: row['Inscrits'] if row['Max_Column'] == f'Voix {i}' else 0,axis=1)
print (points)
# nombre de voix accumulées par département et par candidat


# In[14]:


colonnes_points = [col for col in points.columns if 'points' in col]
total_points_par_colonne = points[colonnes_points].sum()
print("Points pour chaque candidat :")
print(total_points_par_colonne)


# In[15]:


print (total_points_par_colonne.max(), total_points_par_colonne.idxmax())
# donne le candidat qui aurait alors remporté l'élection (ici points 3 est renvoyé ce qui correspond au nom 3)

