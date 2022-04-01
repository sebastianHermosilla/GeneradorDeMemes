from google.colab.patches import cv2_imshow
import numpy as np
import random
import matplotlib.pyplot as plt
import cv2

Frases = ["No y tu mama", "¿A que venia?", "ia stoy arto",
          "tuvo weno el cumpleanos", "te falta calle", "XD", "Mucho texto", "En fin, la hipocresia"]

random.seed(10)
N = np.random.randint(0, 50)
n = np.random.randint(0, len(Frases))
print(N)


img = cv2.imread("Datos/" + str(N) + ".jpg")
forma = np.shape(img)
dim = (500, 500)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (250-len(Frases[0])*15, 420)
fontScale = 1
fontColor = (10, 80, 5)
thickness = 3
lineType = 2

cv2.putText(resized, Frases[n],
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            thickness,
            lineType)

cv2_imshow(resized)
