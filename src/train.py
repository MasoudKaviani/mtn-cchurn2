import pandas as pd
import pickle
import yaml
import os
from sklearn.ensemble import RandomForestClassifier

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

train_df = pd.read_csv('data/processed/train.csv')
X_train = train_df.drop('custcat', axis=1)
y_train = train_df['custcat']

model = RandomForestClassifier(
    n_estimators=params['train']['n_estimators'],
    max_depth=params['train']['max_depth'],
    random_state=params['train']['random_state']
)

model.fit(X_train, y_train)

os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print(f"✓ Model trained with {params['train']['n_estimators']} estimators")