# -*- coding: utf-8 -*-
"""
Created on Sun May 11 15:38:08 2020

@author: MILAGROS PC
"""

import cv2
import matplotlib.pyplot as plt

imagen_resultado = cv2.imread('imagenResultado2.jpg')


#realizmos el histograma de la primera y segunda imagen 
hist2 = cv2.calcHist([imagen_resultado], [0], None, [256], [0, 256])

plt.plot(hist2, color = 'black')

plt.show()








    
