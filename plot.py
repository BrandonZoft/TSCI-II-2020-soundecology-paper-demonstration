import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

# ---------------------------------------------------------------
# Bosque de Manzanillo

# ubicacion de archivos
ubicacionACI = 'manzanillo_forest_results_acoustic_complexity_index_ACI.csv'
ubicacionADI = 'manzanillo_forest_results_acoustic_diversity_ADI.csv'
ubicacionH = 'manzanillo_forest_results_acoustic_entropy_H.csv'
ubicacionAEI = 'manzanillo_forest_results_acoustic_evenness_AEI.csv'
ubicacionBIO = 'manzanillo_forest_results_bioacoustic_index_BIO.csv'
ubicacionNDSI = 'manzanillo_forest_results_ndsi.csv'

# ejemplo de titulo: "Bosque de Manzanillo"
titulo = "Bosque de Manzanillo"

fig, axs = plt.subplots(2, 3)
data = []
x_labels = []

with open(ubicacionACI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[10])])
            x_labels.append(int(row[0][:-4]))


zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figACI = plt.figure()
plt.ylim((1200,2100))
axs[0, 0].plot(list1, list2, marker='o', color='black')
axs[0, 0].set_ylim((1200,2100))
axs[0, 0].set_title('ACI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
figACI.suptitle("{} ACI".format(titulo), fontsize=20)
figACI.savefig("{} ACI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionADI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figADI = plt.figure()
axs[0, 2].plot(list1, list2, marker='o', color='black')
axs[0, 2].set_title('ADI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((1.0,2.2))
figACI.suptitle("{} ADI".format(titulo), fontsize=20)
figACI.savefig("{} ADI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionH,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[10])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figH = plt.figure()
axs[0, 1].plot(list1, list2, marker='o', color='black')
axs[0, 1].set_title('H')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((0.65,0.9))
figH.suptitle("{} H".format(titulo), fontsize=20)
figH.savefig("{} H.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionAEI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 0].plot(list1, list2, marker='o', color='black')
axs[1, 0].set_title('AEI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((0.25,0.75))
figAEI.suptitle("{} AEI".format(titulo), fontsize=20)
figAEI.savefig("{} AEI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionBIO,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 1].plot(list1, list2, marker='o', color='black')
axs[1, 1].set_title('BIO')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((0,75))
figAEI.suptitle("{} BIO".format(titulo), fontsize=20)
figAEI.savefig("{} BIO.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionNDSI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[11])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 2].plot(list1, list2, marker='o', color='black')
axs[1, 2].set_title('NDSI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((-0.35,1.1))
figAEI.suptitle("{} NDSI".format(titulo), fontsize=20)
figAEI.savefig("{} NDSI.jpg".format(titulo))

fig.text(0.5, 0.04, 'Tiempo (24hrs)', ha='center')
fig.text(0.04, 0.5, 'Indice acustico', va='center', rotation='vertical')
fig.suptitle(titulo, fontsize=20)
fig.set_size_inches(12, 8)
fig.savefig("{} plots.jpg".format(titulo))

# ---------------------------------------------------------------
# Costa del caribe

# ubicacion de archivos
ubicacionACI = 'caribbean_coast_results_acoustic_complexity_index_ACI.csv'
ubicacionADI = 'caribbean_coast_results_acoustic_diversity_ADI.csv'
ubicacionH = 'caribbean_coast_results_acoustic_entropy_H.csv'
ubicacionAEI = 'caribbean_coast_results_acoustic_evenness_AEI.csv'
ubicacionBIO = 'caribbean_coast_results_bioacoustic_index_BIO.csv'
ubicacionNDSI = 'caribbean_coast_results_ndsi.csv'

# ejemplo de titulo: "Bosque de Manzanillo"
titulo = "Costa del caribe"

fig, axs = plt.subplots(2, 3)

data = []
x_labels = []

with open(ubicacionACI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[10])])
            x_labels.append(int(row[0][:-4]))


zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figACI = plt.figure()
plt.ylim((1200,2100))
axs[0, 0].plot(list1, list2, marker='o', color='black')
axs[0, 0].set_ylim((1200,2100))
axs[0, 0].set_title('ACI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
figACI.suptitle("{} ACI".format(titulo), fontsize=20)
figACI.savefig("{} ACI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionADI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figADI = plt.figure()
axs[0, 2].plot(list1, list2, marker='o', color='black')
axs[0, 2].set_title('ADI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((1.0,2.2))
figADI.suptitle("{} ADI".format(titulo), fontsize=20)
figADI.savefig("{} ADI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionH,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[10])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figH = plt.figure()
axs[0, 1].plot(list1, list2, marker='o', color='black')
axs[0, 1].set_title('H')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((0.65,0.9))
figH.suptitle("{} H".format(titulo), fontsize=20)
figH.savefig("{} H.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionAEI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 0].plot(list1, list2, marker='o', color='black')
axs[1, 0].set_title('AEI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((0.25,0.75))
figAEI.suptitle("{} AEI".format(titulo), fontsize=20)
figAEI.savefig("{} AEI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionBIO,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 1].plot(list1, list2, marker='o', color='black')
axs[1, 1].set_title('BIO')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((0,75))
figAEI.suptitle("{} BIO".format(titulo), fontsize=20)
figAEI.savefig("{} BIO.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionNDSI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[11])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 2].plot(list1, list2, marker='o', color='black')
axs[1, 2].set_title('NDSI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((-0.6,1.1))
figAEI.suptitle("{} NDSI".format(titulo), fontsize=20)
figAEI.savefig("{} NDSI.jpg".format(titulo))

fig.text(0.5, 0.04, 'Tiempo (24hrs)', ha='center')
fig.text(0.04, 0.5, 'Indice acustico', va='center', rotation='vertical')
fig.suptitle(titulo, fontsize=20)
fig.set_size_inches(12, 8)
fig.savefig("{} plots.jpg".format(titulo))


# ---------------------------------------------------------------
# Parque nacional del blanco

# ubicacion de archivos
ubicacionACI = 'blanco_national_park_results_acoustic_complexity_index_ACI.csv'
ubicacionADI = 'blanco_national_park_results_acoustic_diversity_ADI.csv'
ubicacionH = 'blanco_national_park_results_acoustic_entropy_H.csv'
ubicacionAEI = 'blanco_national_park_results_acoustic_evenness_AEI.csv'
ubicacionBIO = 'blanco_national_park_results_bioacoustic_index_BIO.csv'
ubicacionNDSI = 'blanco_national_park_results_ndsi.csv'

# ejemplo de titulo: "Bosque de Manzanillo"
titulo = "Parque nacional del blanco"

fig, axs = plt.subplots(2, 3)

data = []
x_labels = []

with open(ubicacionACI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[10])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figACI = plt.figure()
plt.ylim((1200,2100))
axs[0, 0].plot(list1, list2, marker='o', color='black')
axs[0, 0].set_ylim((1200,2100))
axs[0, 0].set_title('ACI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
figACI.suptitle("{} ACI".format(titulo), fontsize=20)
figACI.savefig("{} ACI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionADI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figADI = plt.figure()
axs[0, 2].plot(list1, list2, marker='o', color='black')
axs[0, 2].set_title('ADI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((1.0,2.2))
figADI.suptitle("{} ADI".format(titulo), fontsize=20)
figADI.savefig("{} ADI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionH,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[10])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figH = plt.figure()
axs[0, 1].plot(list1, list2, marker='o', color='black')
axs[0, 1].set_title('H')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
figH.suptitle("{} H".format(titulo), fontsize=20)
figH.savefig("{} H.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionAEI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 0].plot(list1, list2, marker='o', color='black')
axs[1, 0].set_title('AEI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((0.25,0.85))
figAEI.suptitle("{} AEI".format(titulo), fontsize=20)
figAEI.savefig("{} AEI.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionBIO,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[9])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 1].plot(list1, list2, marker='o', color='black')
axs[1, 1].set_title('BIO')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((0,75))
figAEI.suptitle("{} BIO".format(titulo), fontsize=20)
figAEI.savefig("{} BIO.jpg".format(titulo))

data = []
x_labels = []

with open(ubicacionNDSI,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        if row:
            data.append([float(row[11])])
            x_labels.append(int(row[0][:-4]))

zipped_lists = zip(x_labels, data)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
list1, list2 = [ list(tuple) for tuple in  tuples]

figAEI = plt.figure()
axs[1, 2].plot(list1, list2, marker='o', color='black')
axs[1, 2].set_title('NDSI')
plt.plot(list1, list2, marker='o', color='black')
plt.xlabel('Tiempo (24hrs)')
plt.ylabel('Indice acustico')
plt.ylim((-0.6,1.1))
figAEI.suptitle("{} NDSI".format(titulo), fontsize=20)
figAEI.savefig("{} NDSI.jpg".format(titulo))

fig.text(0.5, 0.04, 'Tiempo (24hrs)', ha='center')
fig.text(0.04, 0.5, 'Indice acustico', va='center', rotation='vertical')
fig.suptitle(titulo, fontsize=20)
fig.set_size_inches(12, 8)
fig.savefig("{} plots.jpg".format(titulo))