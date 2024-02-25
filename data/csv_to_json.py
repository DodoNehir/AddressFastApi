import csv
import json


FILENAME = "KIKcd_H.20230703.CSV"
JSONFILE = "data.json"

with open(FILENAME, "rb") as txt :
  field_names = txt.readline().decode('cp949').split(',')

with open(FILENAME, "r", encoding='cp949') as txt :
  data = csv.DictReader(txt.readlines(), fieldnames=field_names)

  with open(JSONFILE, 'w', encoding='utf-8-sig') as jsf:
    json.dump(list(data), jsf, ensure_ascii=False)