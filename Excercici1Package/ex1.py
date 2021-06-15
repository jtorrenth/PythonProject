# Fitxer de text pla per a les funcions que només usarem
# A l'excercici 1. L'execució final a la pràctica es du a terme al main
import re

# Definim la funcio main a la que passarem el fitxer i la regex a buscar


def find_count_pattern(file_path, regex):
    # Capturarem excepcions
    try:
        # instanciem la llista de patrons valids
        # Com patterns retorna una llista, podem igualar-ho
        llista = patterns(regex, file_path)
        # Printem el resultat
        print('The pattern ' + regex + ' appears {} times'.format(len(llista)))

    except FileNotFoundError as e:
        print(e)

# Retorna False/True segons si trobem patrons


def is_valid(regex, patro):
    # Cerquem la regex al patro, que en la funció patterns seràn
    # les linies individuals del csv
    return not re.search(regex, patro)


def patterns(regex, file_path):
    # instanciem la llista de patrons correctes
    pattern_list = []

    # Obrim el fitxer
    with open(file_path, 'r') as file:
        # Cada linea pot tenir el patro
        for linea in file:
            # Si is_Valid retorna false afegim a la llista
            if not is_valid(regex, linea):
                pattern_list.append(linea)
    return pattern_list
