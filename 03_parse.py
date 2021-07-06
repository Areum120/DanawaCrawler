from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
import json

with open('./crawl_result/303.html', encoding='utf-8') as f:
    bsobj = BeautifulSoup(f.read(), 'html.parser')

    tb = bsobj.find('table', {'class':'recordTable'})
    # p = parser.make2d(tb)
    # df = pd.DataFrame(p[2:], columns=p[0])
    # print(df)
    trs = tb.find_all('tr')

    name = ''
    res = []
    for tr in trs:
        if tr.has_attr('name'):
            title = tr.find('td', {'class': 'title'})
            try:
                sub_name = title.find('span').text
            except Exception as e:
                print(e)

            try:
                quentity = tr.find('td',{'class':'num'}).text
            except Exception as e:
                print(e)
            obj = {'car_name': name, 'sub_name': sub_name, 'quentity': quentity}
            res.append(obj)
        else:
            # name없는 경우
            try:
                name = tr.find('td', {'class':'title'}).find('a').find('img')['alt'].strip()
            except:
                pass
    with open('./303.json', 'w+') as f:
        f.write(json.dumps(res))