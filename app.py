import os
import mysql.connector
import torch
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import BertTokenizer, BertForSequenceClassification
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# MySQL Connection
def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        port=19795,
        ssl_ca="/etc/ssl/certs/ca-certificates.crt"
    )

# Model
MODEL_PATH = "./bert_model"
TOKENIZER_PATH = "./tokenizer"

tokenizer = BertTokenizer.from_pretrained(TOKENIZER_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
model.to("cpu")
model.eval()

class CommentIn(BaseModel):
    comment: str

class FeedbackIn(BaseModel):
    comment_id: int
    feedback: str

class PredictIn(BaseModel):
    text: str

# Save Comment
@app.post("/comment")
def add_comment(data: CommentIn):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO comments (comment) VALUES (%s)",
        (data.comment,)
    )
    db.commit()

    comment_id = cursor.lastrowid
    cursor.close()
    db.close()

    return {"success": True, "comment_id": comment_id}

# Save Feedback
@app.post("/feedback")
def add_feedback(data: FeedbackIn):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO feedbacks (feedback_id, feedback) VALUES (%s, %s)",
        (data.comment_id, data.feedback)
    )
    db.commit()

    fid = cursor.lastrowid
    cursor.close()
    db.close()

    return {"success": True, "feedback_id": fid}

# AI API
@app.post("/predict")
def predict(data: PredictIn):
    inputs = tokenizer(
        data.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=1).item()

    return {"prediction": prediction}


@app.get("/comments")
def get_comments():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM comments")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results


@app.get("/feedbacks")
def get_feedbacks():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM feedbacks")
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results