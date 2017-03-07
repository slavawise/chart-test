import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)


fig, ax1 = plt.subplots(1, 1, sharex=True)

ax1.fill_between(x, 0, y1, facecolor='green', alpha=0.3)




# fig, (ax, ax1) = plt.subplots(2, 1, sharex=True)
# ax.plot(x, y1, x, y2, color='black')
# ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
# ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
# ax.set_title('fill between where')

import io

buf = io.BytesIO()
plt.savefig(buf, format='png')
plt.savefig('result.png')
buf.close()
