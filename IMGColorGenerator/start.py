from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def get_dominant_colors(image_path, num_colors=5):
    img = Image.open(image_path)
    img = img.resize((150, 150))  # Resize for faster processing
    img_data = np.array(img)
    img_data = img_data.reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(img_data)

    colors = kmeans.cluster_centers_.astype(int)

    return colors

def plot_colors(colors):
    plt.figure(figsize=(8, 2))
    for i, color in enumerate(colors):
        plt.subplot(1, len(colors), i + 1)
        plt.axis("off")
        plt.imshow([[color / 255]])  # normalize RGB values
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path = "test_img.png"  # replace this with your image path
    colors = get_dominant_colors(image_path)
    plot_colors(colors)
