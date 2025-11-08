git init
dvc init

dvc add data/telecomchurn.csv
git add data/telecomchurn.csv.dvc data/.gitignore
git commit -m "Add raw data"

dvc repro

dvc metrics show

dvc repro

dvc exp run --set-param train.n_estimators=200

dvc remote add -d minio s3://dvc-storage
dvc remote modify minio endpointurl http://minio:9000
dvc remote modify minio access_key_id minioadmin
dvc remote modify minio secret_access_key minioadmin123

git add .dvc/config
git add .dvc/.gitignore


dvc add data/telecomchurn.csv

dvc push

git add data/telecomchurn.csv.dvc data/.gitignore
git commit -m "Add raw data with DVC"

dvc repro

dvc push

dvc metrics show
cat metrics.json

dvc status