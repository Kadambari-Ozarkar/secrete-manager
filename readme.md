# 🔐 Centralized Secret Management System using AWS Secrets Manager and IAM Roles

## 📌 Table of Contents

* Introduction
* Problem Statement
* Project Objectives
* Solution Overview
* Architecture
* Technologies Used
* Features
* Project Structure
* Prerequisites
* Implementation Steps
* IAM Policy
* Application Workflow
* Security Validation
* Screenshots
* Future Enhancements
* Learning Outcomes
* Conclusion

# 📖 Introduction

Applications often require sensitive information such as database usernames, passwords, API keys, and authentication tokens. Storing these secrets directly in source code or configuration files is a major security risk.

This project demonstrates a secure method of managing application secrets using **AWS Secrets Manager** and **IAM Roles**. Instead of hardcoding credentials, the application retrieves them dynamically at runtime using the AWS SDK (Boto3).


# 🚨 Problem Statement

During a security audit, it was found that developers stored database credentials directly inside application code.

### ❌ Insecure Approach

```python
DB_USERNAME = "admin"
DB_PASSWORD = "Admin@123"
```

### Risks

* Passwords exposed in source code
* Secrets committed to GitHub repositories
* Difficult credential rotation
* High risk of unauthorized access
* Poor security compliance

---

# 🎯 Project Objectives

* Remove hardcoded credentials
* Store secrets securely in AWS Secrets Manager
* Retrieve secrets dynamically
* Authenticate using IAM Roles
* Eliminate AWS Access Keys from EC2
* Implement least privilege access
* Improve cloud security

---

# 💡 Solution Overview

This solution stores database credentials in AWS Secrets Manager.

The EC2 instance authenticates using an IAM Role and retrieves secrets securely through the AWS SDK without storing any credentials inside the application.

---

# 🏗 Architecture

```text
                    Developer
                         │
                         │
                 Deploy Application
                         │
                         ▼
              +----------------------+
              |     EC2 Instance     |
              |  Python Application  |
              +----------+-----------+
                         │
                  IAM Role Attached
                         │
                         ▼
           +----------------------------+
           | AWS Secrets Manager        |
           | Username & Password Stored |
           +-------------+--------------+
                         │
                   Secret Retrieved
                         │
                         ▼
                   Database Server
```

---

# 🛠 Technologies Used

| Technology          | Purpose                        |
| ------------------- | ------------------------------ |
| AWS EC2             | Host Application               |
| AWS Secrets Manager | Store Secrets                  |
| AWS IAM             | Authentication & Authorization |
| Python              | Application Development        |
| Boto3               | AWS SDK                        |
| Ubuntu              | Operating System               |

---

# ✨ Features

* Secure secret storage
* No hardcoded credentials
* Dynamic secret retrieval
* IAM Role authentication
* Least privilege access
* AWS SDK integration
* Secret encryption using AWS KMS
* Support for secret rotation
* Production-ready security approach

# 📁 Project Structure

```text
centralized-secret-management-system/
│
├── application/
│   ├── app.py
│   └── requirements.txt
│
├── hardcoded-example/
│   └── app_old.py
│
├── iam-policy/
│   └── secret-access-policy.json
│
├── screenshots/
│   ├── ec2.png
│   ├── secret-created.png
│   ├── iam-policy.png
│   ├── iam-role.png
│   ├── role-attached.png
│   ├── secret-retrieval.png
│   └── sts-verification.png
│
├── README.md
└── LICENSE
```

# ✅ Prerequisites

* AWS Account
* Ubuntu EC2 Instance
* Python 3.x
* AWS CLI
* IAM Permissions
* AWS Secrets Manager
* Internet Connectivity


# ⚙ Implementation Steps

## Step 1 — Launch EC2 Instance

* Launch Ubuntu EC2 instance.
* Configure Security Group.
* Connect using SSH.
* Install Python and required packages.

---

## Step 2 — Create Sample Application

Create a simple Python application with hardcoded credentials to demonstrate the security issue.

---

## Step 3 — Store Secrets

Create a secret in AWS Secrets Manager.

Secret Name:

```text
production/database/credentials
```

Secret Value:

```json
{
  "username": "dbadmin",
  "password": "StrongPassword123"
}
```
## Step 4 — Configure IAM

Create an IAM policy allowing only:

* secretsmanager:GetSecretValue

Attach the policy to an IAM Role.

Attach the IAM Role to the EC2 instance.

---

## Step 5 — Modify Application

Replace hardcoded credentials with AWS SDK calls.

The application retrieves credentials securely from AWS Secrets Manager during runtime.

---

## Step 6 — Validate Security

Verify:

* Application connects successfully.
* No AWS Access Keys stored.
* IAM Role authentication works.
* Secret retrieval succeeds.

---

# 🔑 IAM Policy

```json
{
    "Version":"2012-10-17",
    "Statement":[
        {
            "Effect":"Allow",
            "Action":[
                "secretsmanager:GetSecretValue"
            ],
            "Resource":"arn:aws:secretsmanager:REGION:ACCOUNT-ID:secret:production/database/credentials*"
        }
    ]
}

# 🔄 Application Workflow

```text
Application Starts
        │
        ▼
Authenticate using IAM Role
        │
        ▼
Connect to AWS Secrets Manager
        │
        ▼
Retrieve Secret
        │
        ▼
Extract Username & Password
        │
        ▼
Connect to Database
        │
        ▼
Application Runs Successfully

# 🔒 Security Improvements

| Before                       | After                      |
| ---------------------------- | -------------------------- |
| Hardcoded Passwords          | Secrets Manager            |
| Passwords in Source Code     | Dynamic Secret Retrieval   |
| Manual Credential Management | Centralized Management     |
| Static Credentials           | IAM Role Authentication    |
| Difficult Password Rotation  | Automatic Rotation Support |

# ✔ Security Validation

* Successfully retrieved secrets using AWS SDK.
* No AWS Access Key configured on the EC2 instance.
* IAM Role used for authentication.
* Database credentials removed from application code.
* Least privilege IAM policy implemented.

# 📸 Screenshots

Include screenshots of:

* EC2 Instance
* Secret Created
* Secret Value
* IAM Policy
* IAM Role
* IAM Role Attached to EC2
* Application Output
* Secret Retrieval
* AWS STS Verification

# 🚀 Future Enhancements

* Enable automatic secret rotation.
* Integrate Amazon RDS.
* Provision infrastructure using Terraform.
* Automate deployment using Jenkins.
* Add CloudWatch monitoring.
* Implement CloudTrail auditing.

# 📚 Learning Outcomes

* AWS Secrets Manager
* IAM Roles
* IAM Policies
* Boto3 SDK
* Secure Credential Management
* DevSecOps Best Practices
* Least Privilege Principle
* Cloud Security Fundamentals

# 🎯 Conclusion

This project demonstrates a secure and production-ready approach to secret management in AWS. By replacing hardcoded credentials with AWS Secrets Manager and IAM Roles, the application follows DevSecOps best practices, improves security, supports credential rotation, and minimizes the risk of sensitive data exposure.
