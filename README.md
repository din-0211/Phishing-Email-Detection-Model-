# PhishGuard - AI Powered Phishing Email Detector

## Project Overview

PhishGuard is a web-based cybersecurity application developed using Flask that helps users identify phishing emails through automated analysis. The system examines suspicious email content and determines whether an email is legitimate or potentially malicious.

The project provides a user-friendly dashboard, detailed reporting system, analyst management module, and email threat detection capabilities.

---

## Features

### Email Analysis
- Analyze suspicious email content
- Detect phishing indicators
- Generate security assessment results

### Dashboard
- Total analyzed emails
- Phishing email statistics
- Safe email statistics
- Detection overview chart

### Reports
- View all analyzed emails
- Security analysis history
- Print report functionality
- Detection score tracking

### Analyst Management
- Create analyst profiles
- Manage analyst information
- Generate analyst ID cards
- Print analyst identification cards

### Security Monitoring
- Monitor phishing activity
- Track email threats
- Review detection trends

---

## Technology Stack

### Backend
- Python
- Flask
- SQLite

### Frontend
- HTML5
- CSS3
- JavaScript

### Libraries
- Chart.js
- Jinja2

---

## Project Structure

```text
phishing-email-detector/
│
├── app.py
├── database.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── analyze.html
│   ├── reports.html
│   └── settings.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── models/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/phishguard.git
```

### Enter Project Directory

```bash
cd phishguard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running The Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Dashboard Modules

### Security Dashboard
Displays:

- Total analyzed emails
- Phishing detection count
- Safe email count
- Detection overview chart

### Reports Module

Displays:

- Sender
- Subject
- Result
- Detection score
- Analysis date

### Settings Module

Provides:

- Analyst management
- Analyst profile view
- ID card generation
- Print functionality

---

## Future Improvements

- Machine Learning Model Integration
- Email Header Analysis
- URL Reputation Checking
- Threat Intelligence Integration
- PDF Report Export
- User Authentication
- Role-Based Access Control
- Real-Time Email Monitoring

---

## Learning Objectives

This project demonstrates:

- Flask Web Development
- Cybersecurity Concepts
- Phishing Detection
- Database Management
- Frontend Development
- Security Dashboard Design
- Report Generation

---

## Author

**Deepika S**

Cybersecurity Project Developer

PhishGuard - AI Powered Phishing Email Detector

---

## License

This project is developed for educational and cybersecurity learning purposes. 