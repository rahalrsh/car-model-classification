## Car Model Classification


### Overview
This model was trained on a relatively small dataset of around 2800 images of 4 vehicle classes (~700 images per class).
Since the dataset is relatively small, the classification model was trained by transfer learning and fine-tuning an existing model
The base model used here is a VGG16 network pre-trained on the imagenet dataset.
By adding an extra GlobalAveragePooling2D layer, a few Dense layers and 50% Dropout for regularization, I trained the model as below

Training was done in 2 steps
1) Firstly, by freezing the weights of the pre-trained model and training for few epochs.
2) Finally, by un-freezing the weights of the pre-trained model and training for few epochs. This step was done by setting a low learning rate to avoid damaging the pre-trained weights

I also used image augmentation techniques like random image flipping, zooming and brightness adjustments to expand the size of a training dataset. 
The final model is able to identify the different vehicle models with an overall accuracy of 91%

### Model Summary
<img src="https://github.com/rahalrsh/car-model-classification/blob/main/public/ModelSummary.png">

### Download the Dataset 
You can download the dataset from [Download Dataset](https://drive.google.com/drive/folders/1xlXPt7UOc1eTYVrw02qxi50pQ0NBkLPG?usp=sharing)
