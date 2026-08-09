import boto3
import json
import mysql.connector

secret_name = "project3/database-credentials"
region = "ap-south-1"

client = boto3.client("secretsmanager", region_name=region)

response = client.get_secret_value(SecretId=secret_name)

secret = json.loads(response["SecretString"])

db = mysql.connector.connect(
    host=secret["host"],
    user=secret["username"],
    password=secret["password"]
)

print("Database connected successfully!")
