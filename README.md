# Spam Email SMS Classifier using Machine Learning
A Machine Learning project that classifies SMS messages as Spam or Ham using Python, Scikit-learn, and Streamlit.

## Overview
This project is a Machine Learning application that classifies SMS or email messages as **Spam** or **Not Spam**. The model is trained using a labeled dataset and predicts whether a message is spam based on its content.

## Features
- Detects spam messages
- User-friendly web interface using Streamlit
- Machine Learning-based prediction
- Fast and easy to use

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle

## Dataset
The project uses the `spam.csv` dataset containing labeled spam and ham messages.

## Project Structure
```
spam_email_sms_classifier/
│── app.py
│── train_model.py
│── spam.csv
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md
│── Project_Report.pdf
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumitoinam14-alt/spam_email_sms_classifier.git
```

2. Open the project folder:
```bash
cd spam_email_sms_classifier
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## Output
- Enter a message in the text box.
- Click **Predict**.
- The application will display whether the message is **Spam** or **Not Spam**.

## Live Demo

🔗 **Streamlit App:**  
https://spam-email-sms-classifier.streamlit.app

## Author

**Sumit Oinam**  
B.Tech CSE (5th Semester)  
Roll No: 242025033

## License

This project is created for educational purposes.
