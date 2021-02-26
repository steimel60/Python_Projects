import pandas as pd
import re
from datetime import datetime

data = pd.read_excel('example.xlsx')

date_format = '%Y-%m-%d'
today = datetime.today().strftime('%Y-%m-%d')
rows = len(data.index)
row = 0

while row < rows:

    print(data['Date Ordered'][row])
    now = datetime.strptime(today, date_format)

    last_str = str(data['Date Ordered'][row])
    pattern = re.search(r'\d{4}-\d{2}-\d{2}', last_str).group()
    last_order = datetime.strptime(pattern, date_format)

    delta = now - last_order
    print(delta.days)
    row += 1
