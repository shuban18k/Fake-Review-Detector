from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

app = Flask(__name__)

# Initialize variables
model = None
vectorizer = None

def train_model():
    global model, vectorizer
    try:
        # Debug: Show files in directory
        print("Files in folder:", os.listdir('.'))
        
        # Load data with verification
        df = pd.read_csv('my_reviews.csv')
        print("Loaded data shape:", df.shape)
        
        # Validate columns
        if 'review_text' not in df.columns or 'is_fake' not in df.columns:
            raise ValueError("CSV must contain 'review_text' and 'is_fake' columns")
            
        # Check for NaN values
        print("Missing values:\n", df.isnull().sum())
        df = df.dropna()
        
        # Train model
        vectorizer = TfidfVectorizer(max_features=800)
        X = vectorizer.fit_transform(df['review_text'])
        y = df['is_fake']
        
        model = LogisticRegression(max_iter=1000)
        model.fit(X, y)
        
        # Save models
        joblib.dump(model, 'review_model.joblib')
        joblib.dump(vectorizer, 'vectorizer.joblib')
        print("Model trained successfully!")
        
    except Exception as e:
        print("TRAINING FAILED:", str(e))
        raise