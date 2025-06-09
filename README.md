# 🤖 Cloudops Agent Lambda (LangChain + AWS)

## 📝 Overview

CloudOps Agent is a serverless application that enables interaction with AWS EC2 services through conversational interfaces like WhatsApp and Siri. It uses Langchain with Gemini LLM to interpret user queries and respond with intelligent actions.

## ✅ Prerequisites

### AWS Services
This project utilizes the following AWS services:
- **AWS Lambda** – to run the backend logic
- **API Gateway** – to expose the Lambda as an HTTP endpoint
- **AWS Secrets Manager** – to securely store sensitive credentials
- **EC2** – to list, create, and stop instances
- **CloudFormation (SAM)** – to manage infrastructure as code


### 🔐 Required AWS Secrets

Secrets are securely accessed using AWS Secrets Manager via the get_secret function in utils.py. These secrets are injected at runtime and used to authenticate with external services like Twilio and Google Gemini.

Ensure the following secrets exist in AWS Secrets Manager:
- `TWILIO_ACCOUNT_SID` – Twilio Account SID for sending WhatsApp messages
- `TWILIO_AUTH_TOKEN` – Twilio Auth Token
- `GOOGLE_API_KEY` – API key for Gemini LLM
- `MY_WHATSAPP_ID` – Your WhatsApp number (with country code)

---

## 💬 Communication Channels

### 🗣️ Siri
The Lambda can be extended or integrated with Siri Shortcuts for voice-based commands that invoke the API.

### 📱 WhatsApp
Leverages Twilio’s WhatsApp Business API to receive and respond to messages, enabling command execution via chat.

---

## 🚀 Deployment

The project is deployed using AWS SAM CLI.

### 📂 SAM Template

File: `cloudopsagent/template.yaml`

Key components:
- **API Gateway** endpoint at `/genai`
- **Lambda function**: `my-cloudopsagent-lambda`
- **IAM Policies** for Secrets Manager and EC2
- **Environment parameters** for secret names

```bash
sam build --use-container
sam deploy --guided
```

## 📦 GitHub Actions (CI/CD)

This project includes a GitHub Actions pipeline for automatic deployment to AWS on every push to the `main` branch.

**Workflow location:** `.github/workflows/deploy.yml`

```yaml
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: dev
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v3
      - uses: aws-actions/setup-sam@v2
      - uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-south-1
      - run: |
          echo "🔨 Starting SAM build..."
          cd cloudopsagent
          sam build --use-container
          echo "✅ SAM build completed."
      - run: |
          echo "🚀 Starting deploy..."
          cd cloudopsagent
          sam deploy --no-confirm-changeset --no-fail-on-empty-changeset
          echo "✅ Deploy finished!"
```
Make sure to set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in your GitHub repository secrets.

---

## 👥 Authors

Built by the @Tanmay Chopade