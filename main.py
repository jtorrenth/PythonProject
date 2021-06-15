
# Importem els fitxers necessaris
import Excercici1Package.ex1
import Excercici2Package.ex2
import Excercici3Package.ex3
import Excercici4Package.ex4


# Resolem l'excercici 1
print("+++++++++++ Excercici 1 ++++++++++++++")
Excercici1Package.ex1.find_count_pattern("data/covid_approval_polls.csv", ".pdf")
Excercici1Package.ex1.find_count_pattern("data/covid_approval_polls.csv", "Huffington Post")

# Informem a l'usuari de que ha acabat l'excercici 1:
print("Excercici 1 finalitzat.")

# Informem de la mateixa manera que comença l'excercici 2
print("+++++++++++ Excercici 2 ++++++++++++++")
df_approval = Excercici2Package.ex2.get_approval_polls('data/covid_approval_polls.csv')
df_concern = Excercici2Package.ex2.get_concern_polls('data/covid_concern_polls.csv')

# Fem un print dels df per a veure els resultats
print(df_approval)
print(df_concern)

print("Excercici 2 finalitzat.")
print("+++++++++++ Excercici 3 ++++++++++++++")

# Rebem els returns de la funció countValues2 de l'excercici 3
# i els desem en diccionaris
dictR = Excercici3Package.ex3.countValues2(df_approval, 'R')
dictD = Excercici3Package.ex3.countValues2(df_approval, 'D')
dictI = Excercici3Package.ex3.countValues2(df_approval, 'I')
dictall = Excercici3Package.ex3.countValues2(df_approval, 'all')

# Cridem a la funció que grafica i li passem els diccionaris per parametre
Excercici3Package.ex3.graficar(dictR, dictD, dictI, dictall)

print("Acaba l'excercici 3")
print("+++++++++++ Excercici 4 ++++++++++++++")

# En aquest cas el primer apartat el podem fer directament al main
# ja que es una sola linia
print("El nombre total de persones involucrades és {}".format(df_concern['sample_size'].sum()))
# Cridem a la funció que ens servirà per resoldre l'excercici 4.2 i 4.3
Excercici4Package.ex4.countvalues(df_concern, "economy")

# Rebem el dataset de pollsters
pollsters = Excercici2Package.ex2.get_pollster('data/pollster_ratings.xlsx')

# Calculem en funció dels graus
Excercici4Package.ex4.grades(pollsters)
