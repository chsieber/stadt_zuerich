import urllib.request
import json
import pandas as pd

from pandas import json_normalize


path='C:\\Users\\Christian Sieber\\Git_Repos\\aaa'

with urllib.request.urlopen("https://openerz.metaodi.ch/api/calendar.json?region=zurich&start=2023-01-01&end=2023-12-31&sort=date&offset=0&lang=de") as url:
    data = json.load(url)



df = json_normalize(data, 'results')
df.head(2)
df.to_csv("output.csv", index=False, sep=',', encoding="utf-8") #write to csv file




# with open(data, encoding='utf-8') as inputfile:
#     df = pd.read_json(inputfile)
#     print(df)

# df.to_csv(os.path.join(path,r'green1.csv'), encoding='utf-8', sep=',' , quotechar='"', index=False)


