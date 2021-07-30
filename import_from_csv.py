from datetime import *
import sys 
import csv
import os
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# source: https://github.com/flor2468/affective_computing


def readCSV(filename):
    data = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            for header, value in row.items():
              try:
                data[header].append(value)
              except KeyError:
                data[header] = [value]

    return data


# data processing for plotting
def processDataToFloat(data, fieldname):
    liste = []
    for x in data[fieldname]:
        try:
            y = float(x)
            liste.append(y)
        except:
            pass
    return liste


def processDataToDate(data, fieldname):
    liste = []
    for x in data[fieldname]:
        try:
            mytime = datetime.strptime(str(x),"%Y-%m-%d %H:%M:%S.%f")
            # print(mytime)
            liste.append(mytime)
        except:
            try:
                mytime = datetime.strptime(str(x),"%Y-%m-%d %H:%M:%S")
                # print(mytime)
                liste.append(mytime)
            except:
                try:
                    mytime = datetime.strptime(str(x),"%H:%M:%S.%f")
                    # print(mytime)
                    liste.append(mytime)
                except:
                    try: 
                        mytime = datetime.strptime(str(x),"%H:%M:%S")
                        # print(mytime)
                        liste.append(mytime)
                    except:
                        pass
    return liste


def get_time_data(data, fieldname):
    liste = []
    for x in data[fieldname]:
        liste.append(x)

    return liste
    

def processDataToString(data, fieldname):
    liste = []
    for x in data[fieldname]:
        try:
            y = str(x)
            liste.append(y)
        except:
            pass
    return liste
