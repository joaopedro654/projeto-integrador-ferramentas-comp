# Converter para escala de cinza
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Exibir imagem em escala de cinza
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()
