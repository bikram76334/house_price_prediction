# House Price Prediction (Nepal)

A machine learning project that predicts house prices in Nepal based on key property features such as location, area, number of rooms, and other relevant factors.  
This project demonstrates the complete ML pipeline — from data generation and preprocessing to model training and prediction.

---

## Project Overview

Real estate pricing is influenced by multiple factors and varies significantly across regions.  
This project aims to build a data-driven solution that can estimate house prices accurately using supervised machine learning techniques.

The model is trained on a Nepal-specific housing dataset and can be easily extended or deployed as a web application.

---

## Features

- Nepal-based housing dataset  
- Data preprocessing and feature handling  
- Machine learning model training  
- Model persistence using Pickle  
- Easy-to-run training and prediction scripts  
- Modular and clean project structure  

---

## Project Structure
house_price_prediction/
│
├── app.py # Application / prediction script
├── train_model.py # Model training logic
├── generate_dataset.py # Dataset generation script
├── nepal_house_data.xlsx # Dataset file (ignored in Git)
├── nepal_house_price_model.pkl # Trained model (ignored in Git)
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files configuration


---

## Tech Stack

**Programming Language:** Python  

**Libraries:**
- pandas  
- numpy  
- scikit-learn  
- matplotlib (optional for visualization)  

**Tools:**
- Git & GitHub  
- VS Code / PyCharm  

---

## How to Run the Project

### Clone the Repository
```bash
git clone https://github.com/bikram76334/house_price_prediction.git
cd house_price_prediction

### Install Dependencies
</> Bash
pip install -r requirements.txt 
```
Model Details
Type: Supervised Machine Learning (Regression)
Algorithms: Linear Regression / Random Forest
Evaluation Metrics:
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Note on Data & Model Files

###  To keep the repository lightweight and secure:

Dataset files (.xlsx / .csv)
Trained model files (.pkl)

are excluded using .gitignore.

Future Improvements
Web deployment using Flask or FastAPI
Location-based price prediction
Interactive data visualization dashboard
Model performance comparison
Cloud deployment
Author

Bikram Chapagain
Aspiring Data Scientist | Computer Engineering Student
Interested in Data Science, Machine Learning & AI

GitHub: https://github.com/bikram76334
LinkedIn: https://www.linkedin.com/in/bikram-chapagain-55b364392/

Acknowledgements

Inspired by real-world real estate pricing challenges
Dataset created for educational and experimental purposes
