import pandas as pd
from requests_html import HTMLSession
from tabulate import tabulate

slist = '2356|3653|3010|2608|6183|5288|8926|5706|0050|1535|1338|1734|2615|1533|3528|2707|3033|2420|2450|2368|4916|2495|2636|0000|4104|1323|8422|2454|6443|5234'

params = (('stockNos', slist), )


def loop():
    r = HTMLSession().post(
        'https://www.wantgoo.com/my/stocklist/instantquotation', params=params)

    df = pd.DataFrame(
        r.json(),
        columns=[
            'stockNo', 'name', 'change2', 'change2Percentage', 'deal', 'open',
            'high', 'low', 'last',
            'totalVolume', 'weekChange'
        ])
    df = df.set_index('stockNo')
    show(df)


def show(s):
    s = s.sort_values(by=['change2Percentage'], ascending=False)

    print(tabulate(s, headers='keys'))


if __name__ == '__main__':
    loop()
