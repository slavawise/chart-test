import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
import matplotlib.dates as mdates


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    date = [732768, 732775, 732782, 732789, 732796, 732803]
    closep = np.array([2, 5, 9, 6, 2, 7])

    ax1.plot_date(date, closep, '-', label='Price')

    # for legend
    # ax1.plot([], [], linewidth=5, label='loss', color='r', alpha=0.5)
    # ax1.plot([], [], linewidth=5, label='gain', color='g', alpha=0.5)

    ax1.fill_between(date, closep, closep[0], where=(closep > 0), facecolor='g', alpha=0.5)
    ax1.fill_between(date, closep, closep[0], where=(closep < 0), facecolor='r', alpha=0.5)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.grid(True)  # , color='g', linestyle='-', linewidth=5)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    # ax1.set_yticks([0, 25, 50, 75])

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    # plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()

    import io
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.savefig('result.png')
    buf.close()


graph_data('EBAY')
