FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN git config --global user.email "user@example.com" && \
    git config --global user.name "DVC User" && \
    git config --global init.defaultBranch main

COPY setup-minio.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/setup-minio.sh

CMD ["/bin/bash"]