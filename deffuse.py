import numpy as np
import matplotlib.pyplot as plt


img = np.array(plt.imread('img.jpg')).astype(np.float32)
img = img / 255.0
plt.imshow(img)
plt.show()

