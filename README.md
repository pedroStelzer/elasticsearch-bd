# ElasticSearch (NoSQL Database)

## Overview

Elasticsearch is a distributed, RESTful search and analytics engine designed for horizontal scalability, reliability, and easy management. It is commonly used for storing, searching, and analyzing large volumes of data quickly and in near real-time. This project demonstrates basic usage of Elasticsearch for a database seminar, including setup and simple queries.

## Project Structure

- `docker-compose.yaml`: Defines the Elasticsearch and Kibana services for local development.
- `main.py`: Python script to connect to Elasticsearch, create an index, insert documents, and perform a search query.

## How to Run

### 1. Start Elasticsearch and Kibana with Docker Compose

Make sure you have Docker and Docker Compose installed.

Open a terminal in this project folder and run:

```shell
docker-compose up -d
```

- Elasticsearch will be available at [http://localhost:9200](http://localhost:9200)
- Kibana (for visualization) will be available at [http://localhost:5601](http://localhost:5601)

### 2. Run the Python Example

Install the required Python package:

```shell
pip install elasticsearch
```

Then run the script:

```shell
python main.py
```

This will:
- Connect to Elasticsearch
- Create an index called `produtos` (if it doesn't exist)
- Insert sample product documents
- Query for products in the "Eletrônicos" category and print the results

## Notes

- Make sure Elasticsearch is running before executing the Python script.
- Kibana can be used to visualize and interact with the data stored in Elasticsearch.

---