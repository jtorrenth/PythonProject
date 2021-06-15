# En aquest fitxer tindrem tres funcions que llegiran tres fitxers
# i retornaran en cada cas la taula més optima per als excercicis 3, 4 i 5
# En el nostre cas, farem servir pandas read_csv ja que ens permetrà
# treballar amb el dataset de forma eficient. Per als fitxer més gran,
# covid_approvals_polls.csv, farem servir chunksize, ja que en fitxers
# grans, ho fa de forma més eficient. L'únic que cal tenir en compte es que
# despres cal concatenar els chunks que ens ha generat en un mateix df

# importem pandas
import pandas as pd


def get_pollster(file_path):
    # Llegim el excel
    data = pd.read_excel(file_path)
    # Filtrem per si no ha estat banejat
    rslt_df = data[data['Banned by 538'] == 'no']
    # Retornem el df
    return rslt_df


def get_approval_polls(file_path):
    # Llegim el csv amb chunksize = 1000 ja que el fitxer té aprox 2000 registres
    chunks = pd.read_csv(file_path, chunksize=1000)
    # Concatenem els chunks generats en un df
    data = pd.concat(chunks)

    # Treiem els valors sense tracking
    df = data[data.tracking == False]

    # generem un dataframe anomenat pollsters
    pollsters = get_pollster('data/pollster_ratings.xlsx')

    # Setejem index a la columna pollster de cada df
    df = df.set_index(['pollster'])
    pollsters = pollsters.set_index(['Pollster'])

    # Si l'index de pollster al df inicial está al df pollsters, l'afegim al df final
    final_df = df[df.index.isin(pollsters.index)]

    return final_df

# Aquesta funció que tenim a continuació en realitat fa el mateix que l'anterior
# L'unica diferencia és que no passa pels chunks, que ens ajuden quan tenim
# fitxers molt grans. No obstant, penso que seria interessant utilitzar la mateixa
# funció en comptes de tenir-ne dues de pràcticament iguals.
# en aquest cas seguirem amb ambdues funcions, pero cal dir que allà on es cridi
# get_concern_polls es podria cridar directament a get_approval_polls.
# en aquest sentit, també seria interessant canviar el nom de la funció, doncs
# en tindriem una de generica i no una per approvals i una altre per concerns.

def get_concern_polls(file_path):
    data = pd.read_csv(file_path)
    pollsters = get_pollster('data/pollster_ratings.xlsx')
    df = data[data.tracking == False]
    df = df.set_index(['pollster'])
    pollsters = pollsters.set_index(['Pollster'])
    final_df = df[df.index.isin(pollsters.index)]
    return final_df





