import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
import os

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

df = pd.read_csv('data/telecomchurn.csv')

df = df.dropna()

X = df.drop('custcat', axis=1)
y = df['custcat']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=params['prepare']['test_size'],
    random_state=params['prepare']['random_state']
)

os.makedirs('data/processed', exist_ok=True)

train_df = pd.concat([X_train, y_train], axis=1)
test_df = pd.concat([X_test, y_test], axis=1)

train_df.to_csv('data/processed/train.csv', index=False)
test_df.to_csv('data/processed/test.csv', index=False)

print(f"✓ Data prepared: {len(train_df)} train, {len(test_df)} test samples")