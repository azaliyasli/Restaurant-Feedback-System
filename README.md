# 🍽️ Restaurant Feedback System 
An end-to-end Restaurant Feedback System that collects user comments, analyzes sentiment using a fine-tuned BERT model, and stores comments & feedback in a cloud-hosted Aiven MySQL database.

## The system is deployed on Render, making it fully accessible online.

# 🚀 Features
- Save user comments to database
- Analyze comments using a fine-tuned BERT model
- Save feedback associated with comments
- Retrieve all comments and feedbacks
- CORS enabled for frontend integration
- AI inference optimized for CPU environments

# 🛠️ Tech Stack
## Backend
- FastAPI
- Python 3.10+
- MySQL
- mysql-connector-python
## AI / NLP
- Hugging Face Transformers
- BERT (fine-tuned for text classification)
- PyTorch
## Deployment
- Render
- Aiven
