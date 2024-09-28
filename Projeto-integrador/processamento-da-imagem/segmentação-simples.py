# Aplicar segmentação por limiar
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Exibir imagem segmentada
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.show()
