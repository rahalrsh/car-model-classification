# Car Model Classification

## Overview

Developing a computer vision application to identify a vehicle model from a given image is an interesting and challenging problem to solve.
Challenge of this problem is that different vehicle models can appear very similar and the same vehicle can look different and hard to identify depending on lighting conditions, 
angle and many other factors. In this project, I decided to train a Convolutional Neural Network(CNN) to generate a model that can identify a given vehicle model. 
This project is broken down into 3 sections as below

1) web-scraper

    For this project, I decided to write a web scrapper to download vehicle images from multiple websites like TrueCar.com and Kijiji.com to create my own data set.
By doing this, I was able to generate more challenging dataset that resembles an accurate real world problem.  
ou can download this dataset from the link provided in the next section.

2) cars-classifier

    Since the dataset was relatively small, the classification model was trained by transfer learning and fine-tuning a VGG16 network. I also used 
augmentation techniques like random image flipping, zooming and brightness adjustments to expand the size of a training dataset. 
The final model is able to identify the different vehicle models with an overall accuracy of 91%

3) web-app

    As the last step of this project, I developed a python FastAPI based web service so that an end-user can use this model to upload a vehicle image and get a prediction.


## Dataset

4 Vehicle Models (2015 - 2021 Builds)
- Accura - RDX
- Honda - Civic
- Honda - CRV
- Toyota - RAV4

Training dataset - 2826 Images

Testing dataset - 587 Images

<img src="https://github.com/rahalrsh/car-model-classification/blob/main/public/Dataset.png" width="75%">


## Download the Dataset 
You can download the dataset from [Download Dataset](https://drive.google.com/drive/folders/1xlXPt7UOc1eTYVrw02qxi50pQ0NBkLPG?usp=sharing)


## Download the Trained Model
You can download the trained model from [Download Model](https://drive.google.com/drive/folders/1xlXPt7UOc1eTYVrw02qxi50pQ0NBkLPG?usp=sharing)

## Get Predictions
#### Raw predictions results from the trained model are shown below
<img src="https://github.com/rahalrsh/car-model-classification/blob/main/public/Pred-1.png" width="75%">
<img src="https://github.com/rahalrsh/car-model-classification/blob/main/public/Pred-2.png" width="75%">

<br/>

#### You may also use the FastApi based web server to get predictions in JSON format as well
<img src="https://github.com/rahalrsh/car-model-classification/blob/main/public/Fast-API-Request.png" width="75%">
<img src="https://github.com/rahalrsh/car-model-classification/blob/main/public/Fast-API-Response.png" width="75%">

## Train Your Own Model

#### 1. Prepare the dataset
- You may download the dataset I generated from the above link
- Alternatively, you may create your own dataset by following the instructions in the web-scraper project
- Copy the train and test sets to cars-classifier/data/cars
- Directory structure should look like this
```
        cars-classifier/data/cars
        │
        └───train
        │   │
        │   └───Acura - RDX
        │   │   │   01.jpg
        │   │   │   02.jpg
        │   │   │   ...
        │   │   
        │   │───Honda - CRV
        │   │   │   01.jpg
        │   │   │   02.jpg
        │   │   │   ...
        │
        └───test
        │   └───Acura - RDX
        │   │   │   01.jpg
        │   │   │   02.jpg
        │   │   │   ...
        │   │   
        │   │───Honda - CRV
        │   │   │   01.jpg
        │   │   │   02.jpg
        │   │   │   ...
```

#### 2. Train the Model
- You may modify the create_model_vgg() method to use a different base model
- You may also add you own layers and train the model
- Please refer to instructions under cars-classifier project on how to adjust hyperparameters and other settings
- Once the training is done, your model will get saved to cars-classifier/saved_models directory


#### 3. Run the web server
- Setup the web server locally by following the instructions in the web-scraper project
- Copy the trained model to web-app/cars-be/saved_models directory
- Run `uvicorn main:app --reload` and navigate to `http://127.0.0.1:8000/docs`
- Navigate to /prediction endpoint, Choose File and hit Execute
- You will get a server response in JSON format as below
```
        Code 200
        Response body
        {
          "prediction": "Toyota - RAV4",
          "accuracy": 0.995089590549469
        }
```  
