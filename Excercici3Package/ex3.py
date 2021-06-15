# En aquest fitxer codificarem les funcions necessàries per a fer l'excercici 3
# En el nostre cas, importarem numpy i matplotlib per a graficar
import numpy as np
import matplotlib.pyplot as plt

# Seguidament definim la funció a la que passarem un dataframe (conseguit al
# excercici anterior i la party


def countValues2(dataframe, party):
    # Filtrem el dataset
    approvaltrump = dataframe[dataframe['text'].str.contains("Trump", case=False) & dataframe['text'].str.contains("coronavirus", case=False)].copy()
    # Afegim els valors en funció del samplesize a dues noves columnes
    approvaltrump['ppl_approve'] = approvaltrump['approve']/100*approvaltrump['sample_size']
    approvaltrump['ppl_disapprove'] = approvaltrump['disapprove']/100*approvaltrump['sample_size']
    # Tornem a filtrar el dataset, en aquest cas per la party
    approvaltrump = approvaltrump[approvaltrump['party'].str.contains(party)]

    # Printem a la consola els valors per a cada party
    print("Valors per party {}".format(party))
    print(approvaltrump['ppl_approve'].sum())
    print(approvaltrump['ppl_disapprove'].sum())

    # Finalment, ens quedem les sumes a un dict data per a retornar-lo
    data = {
        'approve': approvaltrump['ppl_approve'].sum(),
        'disapprove': approvaltrump['ppl_disapprove'].sum(),
    }

    return data


# Funció que graficarà l'excercici 3, rep per parametre tres df
def graficar(dfr, dfd, dfi, dfall):
    N = 4
    approvals = (dfr.get('approve'), dfd.get('approve'), dfi.get('approve'), dfall.get('approve'))
    ind = np.arange(N)
    width = 0.35  # ample de les barres

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Setejem valors, color i with
    rects1 = ax.bar(ind, approvals, width, color='royalblue')

    # Fem el mateix per als disapprove
    disapprovals = (dfr.get('disapprove'), dfd.get('disapprove'), dfi.get('disapprove'), dfall.get('disapprove'))
    rects2 = ax.bar(ind + width, disapprovals, width, color='seagreen')

    # afegim informació estatica
    ax.set_ylabel('Numero de persones')
    ax.set_title('Numero de persones que approven o no les entrevistes de Trump')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(('R', 'D', 'I', 'All'))

    # Afegim la llegenda
    ax.legend((rects1[0], rects2[0]), ('Approve', 'Disapprove'))

    #Mostrem el gràfic
    plt.show()
