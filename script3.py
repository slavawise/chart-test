from __future__ import print_function
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import MONDAY
from matplotlib.finance import quotes_historical_yahoo
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter

date1 = datetime.date(2003, 9, 5)
date2 = datetime.date(2003, 12, 1)

# date1 = datetime.date(2017, 3, 1)
# date2 = datetime.date(2017, 3, 6)

# every monday
mondays = WeekdayLocator(MONDAY)

# every 3rd month
months = MonthLocator(range(1, 13))
monthsFmt = DateFormatter("%b '%y")

quotes = quotes_historical_yahoo('INTC', date1, date2)
if len(quotes) == 0:
    print('Found no quotes')
    raise SystemExit

dates = [datetime.date(2003, 12, 1), datetime.date(2003, 12, 2), datetime.date(2003, 12, 3), datetime.date(2003, 12, 4)]
opens = [1, 2, 3, 4]

fig, ax = plt.subplots()
ax.plot_date(dates, opens, '-')
# ax.xaxis.set_major_locator(months)
# ax.xaxis.set_major_formatter(monthsFmt)
# ax.xaxis.set_minor_locator(mondays)
ax.autoscale_view()
# ax.xaxis.grid(False, 'major')
# ax.xaxis.grid(True, 'minor')
ax.grid(True)

fig.autofmt_xdate()

plt.show()

import io

buf = io.BytesIO()
plt.savefig(buf, format='png')
plt.savefig('result.png')
buf.close()
