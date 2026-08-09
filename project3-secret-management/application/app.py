import boto3
import json

SECRET_NAME = "project3/db-credentials"
REGION_NAME = "us-east-1"

# Create Secrets Manager client
client = boto3.client(
    "secretsmanager",
    region_name=REGION_NAME
)

# Retrieve secret
response = client.get_secret_value(
    SecretId=SECRET_NAME
)

# Convert secret JSON into Python dictionary
secret = json.loads(response["SecretString"])

DB_USERNAME = secret["username"]
DB_PASSWORD = secret["password"]

print("=== Secure Application Configuration ===")
print(f"Database Username: {DB_USERNAME}")
print("Database Password: [RETRIEVED SECURELY]")

print("\nApplication started successfully!")
