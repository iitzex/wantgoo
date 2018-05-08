import pandas as pd
from requests_html import HTMLSession
from tabulate import tabulate

s = '1323|1338|1533|1535|2356|2368|2420|2450|2454|2495|2608|2615|2636|2707|3010|3033|3528|3653|4916|5007|5234|5288|6112|6183|6189|6443|8422|8463'

params = (('stockNos', s), )


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
