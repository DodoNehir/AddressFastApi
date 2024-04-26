import json
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from pathlib import Path

JSONFILE = "data/data.json"
BASEDIR = Path(__file__).parent

app = FastAPI()



@app.get('/')
def get_data(
    text :  str
  ) : 
  
    with open(JSONFILE, 'r', encoding='utf-8-sig') as js :
        data = json.loads(js.read())

    filtered = filter(lambda x :  text in x.get('시도명') or text in x.get('시군구명') or text in x.get('읍면동명'), data)

    return list(filtered)
        
@app.get('/pd')
def get_data_pd(
   city: str,
   district: str,
   dong: str,
) :

    data = pd.read_csv(BASEDIR / "data/KIKcd_H.20230703.CSV", encoding='cp949')
    filtered = data[
        (data['시도명'].notnull() & data['시도명'].str.contains(city)) &
        (data["시군구명"].notnull() & data['시군구명'].str.contains(district)) &
        (data['읍면동명'].notnull() & data['읍면동명'].str.contains(dong))
    ]

    if filtered.empty:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")
    return json.loads(filtered.to_json(force_ascii=False, orient='records'))


