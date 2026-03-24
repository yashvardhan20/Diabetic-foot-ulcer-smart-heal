# Diabetic Foot Ulcer Classification & Treatment Recommendation System

**RMIT University Capstone Thesis** – Smart Heal Healthcare  
**Model Accuracy: 94%** | TensorFlow CNN | Flask API | Shiny Prototype

## Project Overview
Developed an end-to-end AI system that classifies chronic wound images (Stage 1–3, Infected, Necrotic) and provides personalised treatment recommendations (Hydrocolloid, Alginate, Foam dressings, Antimicrobial). Addresses a major Australian healthcare challenge, 50,000+ people living with foot ulcers.

## Key Features & Achievements
- Trained Convolutional Neural Network (CNN) on 2,500+ labelled wound images
- Built Flask REST API (`app.py`) for real-time image upload and prediction
- Created Shiny web prototype for interactive treatment planning
- Performed data augmentation, HOG feature extraction, and full model training pipeline
- Delivered complete research report and pilot findings

## Repository Structure
- `data/` – labelling.csv (36+ labelled images)
- `notebooks/` – Training, augmentation & HOG processing
- `app/` – Flask prediction API + requirements.txt
- `prototype/` – Shiny treatment planner
- `reports/` – Full thesis & presentation

## Technologies
- **AI/ML**: Python, TensorFlow/Keras, CNN, ImageDataGenerator, HOG features
- **Backend**: Flask
- **Frontend/Prototype**: Shiny (R) + Streamlit-ready structure
- **Data**: Pandas, Pillow, scikit-image

## How to Run Locally
```bash
cd app
pip install -r requirements.txt
python app.py
