import numpy as np
import matplotlib.pyplot as plt
from tifffile import tifffile as tiff

image = np.array(tiff.imread('D:\\ccv_pdgfb_take3_average_correct_cvmap.tif'))

plt.imshow(image)
print(np.nanpercentile(image, 10))
plt.clim(0,np.nanpercentile(image, 10))
plt.colorbar()
plt.show()
plt.title('CV Map')
print("Done :)")