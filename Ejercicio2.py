import cv2
import numpy as np
import matplotlib.pyplot as plt


#imagen_original = cv2.imread('hist6.jpg')

imagen_original = cv2.imread("hist10_1.jpg")

#imagen_gray = cv2.imread('hist6.jpg', cv2.IMREAD_GRAYSCALE)

imagen_gray = cv2.imread('hist10_1.jpg', cv2.IMREAD_GRAYSCALE)

histOriginal = cv2.calcHist([imagen_original], [0], None, [256], [0, 256])

plt.plot(histOriginal, color = 'black')
plt.show()

cantidad_pixeles = imagen_gray.size
shape = imagen_gray.shape
height = shape[0]
width = shape[1]

print("Imagen original, dType: ", imagen_gray.dtype)

print("Imagen original, dimensiones: ", shape)
print("Imagen original, tamaño total de los pixeles: ", cantidad_pixeles)
#print("Original image: pixel min: ", imagen_gray.min())
#print("Original image: pixel max: ", imagen_gray.max())


#######################RECORTAR################################


img = cv2.imread(".png")
#crop_img = imagen_gray[y:y+h, x:x+w]
crop_img= imagen_original[280:400,170:260]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)



# implementacion de algoritmo de Histogram Equalization 

# inicializmos los valores del algoritmo
L = 256
S_n = []
imagen_array1D = imagen_gray.flatten().tolist()

suma_acumulada = 0

# Realizamos S_n
for index in range(L):
    P_n = imagen_array1D.count(index) / cantidad_pixeles
    suma_acumulada = suma_acumulada + P_n
    s_k = int(round(suma_acumulada * (L - 1)))
    S_n.append(s_k)


#Realizamos el mapeo lineal
for index in range(cantidad_pixeles):
    imagen_array1D[index] = S_n[imagen_array1D[index]]


#Mostramos la imagen g(x,y)
imagen = np.asarray(imagen_array1D)
imagen = imagen.reshape(height, width)
print("Tamaño de la magen final : ", imagen.size)
print("Dimensiones de la imagen final: ", imagen.shape)

#cv2.imwrite("imagenResultado.jpg", imagen)

cv2.imwrite("imagenResultado2.jpg", imagen)
