## How to run the cars-be web server

- `cd web-app/cars-be`
- Download the model from [Download Model](https://drive.google.com/drive/folders/1xlXPt7UOc1eTYVrw02qxi50pQ0NBkLPG?usp=sharing) and copy it under saved_models
- Rename downloaded model tp 'car_classification_model.h5'
- create a virtual environment with `python3 -m venv env`
- Activate virtual environment `source env/bin/activate`
- Install packages `pip install -r requirements.txt`
- Run the dev server with `uvicorn main:app --reload`
- Navigate to http://127.0.0.1:8000/docs
- Then, click on the /prediction endpoint and click on 'Try it out'
- Now select an vehicle image from 'Choose File' and hit Execute
- You will get a server response in JSON format as below

```
        {
          "prediction": "Toyota - RAV4",
          "accuracy": 0.995089590549469
        }
```  

<br/>
<img src="https://github.com/rahalrsh/car-model-classification/blob/main/public/Fast-API-Request.png" width="75%">
<img src="https://github.com/rahalrsh/car-model-classification/blob/main/public/Fast-API-Response.png" width="75%">
