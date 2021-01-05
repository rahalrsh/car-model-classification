from fastapi import FastAPI, File, UploadFile, HTTPException
from tensorflow import keras
from schemas.prediction import Prediction
from PIL import Image # Python Image Lib
from io import BytesIO
import numpy as np


app = FastAPI()

MODEL_PATH = 'saved_models/car_classification_model.h5'
model = keras.models.load_model(MODEL_PATH)
INPUT_SHAPE = model.layers[0].input_shape[0]
CAR_MODELS = ['Acura - RDX', 'Honda - CRV', 'Honda - Civic', 'Toyota - RAV4']


@app.get("/")
async def root():
    return { 'error': 'Use GET /prediction instead of the root route!' }


# Define the /prediction route
@app.post('/prediction/', response_model=Prediction)
async def prediction_route(file: UploadFile = File(...)):

    # Ensure that this is an image
    if file.content_type.startswith('image/') is False:
        # 400 - Bad Request
        raise HTTPException(status_code=400, detail=f'File \'{file.filename}\' is not an image.')

    try:
        # Read image contents
        contents = await file.read()
        pil_image = Image.open(BytesIO(contents))

        # Resize image
        pil_image = pil_image.resize((INPUT_SHAPE[1], INPUT_SHAPE[2]))

        # Remove Alpha channels
        if pil_image.mode == 'RGBA':
            pil_image = pil_image.convert('RGB')

        # Convert image into numpy
        numpy_image = np.array(pil_image).reshape((INPUT_SHAPE[1], INPUT_SHAPE[2], INPUT_SHAPE[3]))

        # Scale image
        numpy_image = numpy_image / 255

        # Get Prediction for image
        numpy_image = np.expand_dims(numpy_image, axis=0)
        pred = model.predict(numpy_image)[0]

        max_index = np.argmax(pred)
        pred_accuracy = pred[max_index]
        pred_car = CAR_MODELS[max_index]

        return {
            'prediction': pred_car,
            'accuracy': pred_accuracy,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail='Internal error.')
