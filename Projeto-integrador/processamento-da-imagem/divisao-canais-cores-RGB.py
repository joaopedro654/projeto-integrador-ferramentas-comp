# Dividir os canais de cor
R, G, B = cv2.split(image_rgb)

# Exibir cada canal
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(R, cmap='Reds')
ax[0].set_title('Canal Vermelho')
ax[1].imshow(G, cmap='Greens')
ax[1].set_title('Canal Verde')
ax[2].imshow(B, cmap='Blues')
ax[2].set_title('Canal Azul')

for a in ax:
    a.axis('off')

plt.show()
