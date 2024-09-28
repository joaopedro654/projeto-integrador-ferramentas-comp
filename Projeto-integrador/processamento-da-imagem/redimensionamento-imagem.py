# Redimensionar a imagem
resized_image = cv2.resize(image_rgb, (200, 200))

# Exibir imagem redimensionada
plt.imshow(resized_image)
plt.axis('off')
plt.show()
