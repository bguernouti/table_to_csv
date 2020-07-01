"""
the important dependencies "pandas and BeautifulSoup"
must be correctly installed
"python -m pip install pandas BeautifulSoup4"

you can check the full list in file "requirements.txt"
"""

import pandas as pd
from bs4 import BeautifulSoup

# --------------------------------------------

"""
file name to be parsed
steps: 
1- copy considered file to project repository. 
2- dont use '/' at start, and write his complete name with extension ex. "test.txt" 
"""

filename = '2.txt'

#-------------------------------------------

"""
Final result should be Headers columns, and Rows with same range of columns
We do initialize them here.
"""

list_header = []
data = []

# -----------------------------------------------------------

# We open the file with the parser
soup = BeautifulSoup(open(filename), 'html.parser')

"""
First Step : 
"""

# We recover all rows "tr" in the file
rows = soup.find_all("tr")

# We consider the first row is the Header
thead = rows[0]

# We get all columns of first row to make them headers columns
thead_columns = thead.find_all("td")

for head in thead_columns:
    list_header.append(head.get_text()) # Here we get the text of the column only.

# --------------------------------------------------

"""
Second Step : 
"""
# We saved header columns in the variable list_header
# we can delete it now from all Rows variable,
# then process to recover text of each column and store theme in data
rows.pop(0)

for row in rows:
    row_columns = []
    for col in row.find_all("td"):
        row_columns.append(col.get_text()) # text of column
    data.append(row_columns) # push the data variable

dataFrame = pd.DataFrame(data=data, columns=list_header) # init

dataFrame.to_csv('scrap.csv', index=False, sep="|") # build the csv file seperator "|"

# To run this simply : "python main.py"
