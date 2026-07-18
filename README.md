Spam Email/SMS Classifier using Machine Learning
Submitted By

Name:
Roll No.:
Department:
College:

Abstract

Spam emails and SMS messages are a major source of online fraud and unwanted communication. This project develops a machine learning model that automatically classifies a message as Spam or Not Spam (Ham). The application uses Natural Language Processing (NLP), a TF-IDF Vectorizer, and the Multinomial Naive Bayes algorithm. A web interface built with Streamlit allows users to enter a message and receive an instant prediction.

1. Project Title

Spam Email/SMS Classifier using Machine Learning

2. Project Description

The Spam Email/SMS Classifier is a machine learning application that predicts whether a given email or SMS message is spam or not. The project uses text preprocessing, feature extraction with TF-IDF, and a Multinomial Naive Bayes classifier. The application is deployed using Streamlit Community Cloud, making it accessible through any web browser.

3. Objectives
Detect spam messages automatically.
Reduce unwanted email and SMS.
Demonstrate machine learning for text classification.
Deploy the model as an online web application.
4. Key Features
Spam and Ham classification
User-friendly web interface
Real-time prediction
Machine Learning based detection
Fast response time
Online deployment using Streamlit
5. Technology Stack
Component	Technology
Programming Language	Python 3.13
IDE	Visual Studio Code
Machine Learning	Scikit-learn
Data Processing	Pandas
NLP	TF-IDF Vectorizer
Model	Multinomial Naive Bayes
Frontend	Streamlit
Version Control	Git & GitHub
Deployment	Streamlit Community Cloud
6. System Architecture
User Input
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Multinomial Naive Bayes Model
      │
      ▼
Prediction
      │
      ▼
Spam / Not Spam
7. Project Pipeline
Collect dataset
Load dataset using Pandas
Clean unnecessary columns
Convert labels into numerical values
Split training and testing data
Convert text using TF-IDF Vectorizer
Train Multinomial Naive Bayes model
Evaluate performance
Save trained model
Deploy with Streamlit
8. Installation

Install Python 3.13

Clone repository

git clone https://github.com/yourusername/spam_email_sms_classifier.git

Install dependencies

pip install -r requirements.txt

Run application

streamlit run app.py
9. Usage
Open the Streamlit application.
Enter an email or SMS message.
Click Predict.
The application displays whether the message is Spam or Not Spam.
10. Input

Plain text email or SMS message.

Example
Congratulations! You have won ₹50,000. Click here now.
11. Output

Example Output

Prediction: SPAM

or

Prediction: NOT SPAM
12. Dataset Source

SMS Spam Collection Dataset

Source:
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

Dataset Size

Total Messages: 5572
Ham Messages: 4825
Spam Messages: 747
13. Results
Accuracy

96.23%

Precision
Class	Precision
Ham	0.96
Spam	1.00
Recall
Class	Recall
Ham	1.00
Spam	0.72
F1 Score
Class	F1 Score
Ham	0.98
Spam	0.84
14. Requirements
Software
Python 3.13
VS Code
Git
GitHub
Python Libraries
pandas
scikit-learn
streamlit
joblib
15. Challenges Faced
Understanding machine learning workflow.
Cleaning dataset.
Handling missing columns.
Saving trained model correctly.
Deploying on Streamlit Community Cloud.
Managing file paths during deployment.
Uploading project to GitHub.
16. Future Improvements
Support multiple languages.
Deep learning based classifier.
Email attachment analysis.
Image spam detection.
Higher accuracy with larger datasets.
Mobile application integration.
User authentication.
17. Conclusion

The Spam Email/SMS Classifier successfully classifies text messages into Spam and Not Spam using machine learning. The model achieved an accuracy of 96.23% and was deployed as a web application using Streamlit. This project demonstrates the practical use of Natural Language Processing and Machine Learning in solving real-world communication security problems.

18. References
Scikit-learn Documentation
Streamlit Documentation
Pandas Documentation
Kaggle SMS Spam Collection Dataset
Python Official Documentation
