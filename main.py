import os
import sys
import pandas as pd
from bs4 import BeautifulSoup

path = '2.txt'

data = []

list_header = []
soup = BeautifulSoup(open(path), 'html.parser')

tables = soup.find_all("tr")
thead = tables[0]

thead_columns = thead.find_all("td")

for head in thead_columns:
    list_header.append(head.get_text())


data = []

tables.pop(0)

for table in tables:
    row_columns = []
    for col in table.find_all("td"):
        row_columns.append(col.get_text())
    data.append(row_columns)

dataFrame = pd.DataFrame(data=data, columns=list_header)

dataFrame.to_csv('scrap.csv', index=False, sep="|")
