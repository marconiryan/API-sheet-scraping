# API Sheet Scraping
Scraping do Google Sheets para API 
```
pip install -r requirements.txt
```
``` 
python -m uvicorn main:app --reload
```

#### Example GET request from localhost
```Javascript
 fetch("localhost:port")
            .then((Response) => {return Response.json()})
             .then((data) => {console.log(data);})
            .catch(console.log("Erro"))
```
