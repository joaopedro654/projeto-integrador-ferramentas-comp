import cv2
import matplotlib.pyplot as plt

# Carregar imagem
image = cv2.imread('imagem/cavalo2.jpg')

# Converter BGR para RGB (OpenCV carrega em BGR por padrão)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Exibir a imagem
plt.imshow(image_rgb)
plt.axis('off')
plt.show()
