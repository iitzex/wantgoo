import subprocess
from io import StringIO

import pandas as pd
from requests_html import HTML, HTMLSession
from tabulate import tabulate

pd.set_option('expand_frame_repr', False)

slist = '2356|3653|3010|2608|6183|5288|8926|5706|0050|1535|1338|1734|2615|1533|3528|2707|3033|2420|2450|2368|4916|2495|2636|0000|4104|1323|8422|2454|6443|5234'

params = (
    ('types', '2'),
    ('stockno', slist),
)


def loop():
    session = HTMLSession()
    r = session.post(
        'https://www.wantgoo.com/my/stocklist/renewcontentpartial',
        params=params)

    j = r.json()

    alist = []
    for i in j:
        h = HTML(html=i['htmlData'])
        td = h.find('td')
        data = []
        for l, k in enumerate(td):
            if l == 3:
                s = k.text.split(' ')
                data.append(s[0])
                data.append(s[1][1:-1])
                continue
            data.append(k.text)

        line = (','.join(data))
        alist.append(line)

    last = '\n'.join(alist)
    read_csv(last)


def read_csv(v):
    v = StringIO(v)
    s = pd.read_csv(v, index_col=0, header=None)
    s[4] = s[4].apply(pd.to_numeric)
    s = s.sort_values(by=[4], ascending=False)

    print(tabulate(s, showindex=False))


if __name__ == '__main__':
    loop()
