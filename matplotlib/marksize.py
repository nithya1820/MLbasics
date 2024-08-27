import matplotlib.pyplot as plt
import numpy as np
# markersize
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints,marker ='o',ms=20)
plt.plot(ypoints,linestyle='dashed')
plt.show()