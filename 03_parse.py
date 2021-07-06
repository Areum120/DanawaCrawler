from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd

with open('./crawl_result/303.html', encoding='utf-8') as f:
    bsobj = BeautifulSoup(f.read(), 'html.parser')

    tb = bsobj.find('table', {'class':'recordTable'})
    p = parser.make2d(tb)
    df = pd.DataFrame(p[2:], columns=p[0])
    print(df)