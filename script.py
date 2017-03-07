# import numpy as np
# import matplotlib.pyplot as plt
#
# font = {'family': 'serif',
#         'color': 'darkred',
#         'weight': 'normal',
#         'size': 16,
#         }
#
# x = np.linspace(0.0, 5.0, 100)
# y = np.cos(2 * np.pi * x) * np.exp(-x)
#
# plt.plot(x, y, 'k')
# plt.title('Damped exponential decay', fontdict=font)
# plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
# plt.xlabel('time (s)', fontdict=font)
# plt.ylabel('voltage (mV)', fontdict=font)
#
# # Tweak spacing to prevent clipping of ylabel
# plt.subplots_adjust(left=0.15)

#######################################################################################################################
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

years = YearLocator()  # every year
months = MonthLocator()  # every month
yearsFmt = DateFormatter('%Y')

x = [
    datetime.strptime('2016-05-12', '%Y-%m-%d'),
    datetime.strptime('2016-05-13', '%Y-%m-%d'),
    datetime.strptime('2016-05-14', '%Y-%m-%d'),
    datetime.strptime('2016-05-15', '%Y-%m-%d'),
    datetime.strptime('2016-05-16', '%Y-%m-%d'),
]
y = [5, 9, 20, 100, 2]

fig, ax = plt.subplots()
ax.plot_date(x, y, '-')


# # format the ticks
# ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.autoscale_view()


ax.fmt_xdata = DateFormatter('%Y-%m-%d')
ax.grid(True)

fig.autofmt_xdate()

#######################################################################################################################
import io

with io.BytesIO() as buf:
    plt.savefig(buf, format='png')
    plt.savefig('result.png')

