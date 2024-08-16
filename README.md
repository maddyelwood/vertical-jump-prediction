# vertical-jump-prediction
Machine learning model for predicting vertical jump given strength and flexibility oriented features.

## Quick Setup
To download onto your own device, type these commands starting in your home directory:

```
git clone https://github.com/maddyelwood/vertical-jump-prediction vertical-jump-prediction
cd vertical-jump-prediction
pip install -r requirements.txt
```

## Data File
In order to build a model with strength and conditioning data, one must have access to teambuildr data in the form of a CSV file. This CSV file is not part of the GitHub repository. 

If one does not have access to teambuildr data, they can create their own CSV file including columns names ID, Estimated-Weight, Vert (Vertical), BS (Back Squat), BSS (Bulgarian Split Squat), Clean, and Gender. Other columns/features can be added but are not necessary to replicate this model.

## Usage
To create a model, run 'athlete-vert-predictor.py' using python3, changing the name of the inputted CSV file as necessarry.

Then, run 'run_model.py' to try out the model built by entering in data and receiving a vertical jump prediction!
