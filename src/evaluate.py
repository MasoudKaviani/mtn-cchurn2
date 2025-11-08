import pandas as pd
import pickle
import json
import yaml
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

test_df = pd.read_csv('data/processed/test.csv')
X_test = test_df.drop('custcat', axis=1)
y_test = test_df['custcat']

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

y_pred = model.predict(X_test)

metrics = {
    'accuracy': float(accuracy_score(y_test, y_pred)),
    'precision': float(precision_score(y_test, y_pred, average='weighted')),
    'recall': float(recall_score(y_test, y_pred, average='weighted')),
    'f1_score': float(f1_score(y_test, y_pred, average='weighted'))
}

with open('metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print("✓ Model evaluated:")
for metric, value in metrics.items():
    print(f"  {metric}: {value:.4f}")