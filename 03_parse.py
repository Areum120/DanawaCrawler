from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
import json


# brands = [303,304,307,"312,316",326,"321,322",337,329,328,349,371,376,413,422,618,367,459,394,399,381,440,436,445,404,408,409,390,385,622,491,486,500,537,617]
brands = [362]
for brand in brands[:1]:
    with open(f'./crawl_result/{brand}_21.html', encoding='utf-8') as f:
        bsobj = BeautifulSoup(f.read(), 'html.parser')

    tb = bsobj.find('table', {'class':'recordTable'})
    # p = parser.make2d(tb)
    # df = pd.DataFrame(p[2:], columns=p[0])
    # print(df)
    if tb != None:
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
        with open(f'./{brand}_21.json', 'w+') as f:
            f.write(json.dumps(res))