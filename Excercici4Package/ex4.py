import matplotlib.pyplot as plt



def countvalues(dataframe, subject):
    # Filtrem i tractem el dataset
    economydf = filtrar(dataframe, "economy")
    # el printem
    printar(economydf, subject)

    # Filtrem ara per subject infected i ho desem en un altre df
    infectedf = filtrar(dataframe, "infected")
    # Calculem els percentatjes
    percentvery = (infectedf['ppl_very'].sum()/infectedf['sample_size'].sum())*100
    percentnotatall = (infectedf['ppl_not_at_all'].sum() / infectedf['sample_size'].sum()) * 100
    # Els printem
    print("percentatge very: {}%".format(percentvery))
    print("percentatge not_at_all: {}%".format(percentnotatall))
    grafic4('People_Very', 'People_Not_At_All', percentvery, percentnotatall, " % Persones", "Satisfacció", "% de persones preocupades o no per infected")


def printar(df, subject):
    # Printem a la consola els valors
    print("Valors per subject {}".format(subject))
    pplvery = df['ppl_very'].sum()
    pplnot = df['ppl_not_at_all'].sum()
    print("Very: {}".format(pplvery))
    print("Not at All: {}".format(pplnot))
    # Finalment, grafiquem
    # Cal tancar el grafic per a seguir amb l'execució
    grafic4('People_Very', 'People_Not_At_All', pplvery, pplnot, "Persones", "Satisfacció", "Nombre de persones preocupades o no per l'economia")


def filtrar(dataframe, subject1):
    df = dataframe[dataframe['subject'].str.contains(subject1, case=False)].copy()
    # Afegim els valors en funció del samplesize a dues noves columnes
    df['ppl_very'] = df['very'] / 100 * df['sample_size']
    df['ppl_not_at_all'] = df['not_at_all'] / 100 * df['sample_size']
    return df


def grafic4(label1, label2, valor1, valor2, leyenday, leyendax, titulo):
    # Declaramos valors per l'eix x
    eje_x = [label1, label2]

    # Declaramos valors per l'eix y
    eje_y = [valor1, valor2]

    # Fem la grafica
    plt.bar(eje_x, eje_y)

    # Llegenda de l'eix x
    plt.ylabel(leyenday)

    # Legenda en el eje x
    plt.xlabel(leyendax)

    # Títol de Grafica
    plt.title(titulo)

    # Mostrem Grafica
    plt.show()

#Funcio per a l'excercici 4.4
def grades(df):
    df['538 Grade']=df['538 Grade'].str[0]
    print(df.groupby('538 Grade').size())


