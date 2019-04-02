import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal



datos=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt', sep=';')
datos[0]=pd.to_datetime(datos[0], format='%d/%m/%Y/ %H:%M:%S')
datos.set_index([0], inplace=True)



