# Automated XSS Vulnerability Assessment Tool

Built on **Kali Linux** using **Python, Flask, Selenium**, and **DVWA**

---

## Overview

This project is a **Python-based automated web security assessment tool** designed to identify and demonstrate **reflected Cross-Site Scripting (XSS) vulnerabilities** in **controlled and intentionally vulnerable environments**.

The tool is developed with an **educational and defensive security focus**, helping learners and developers understand insecure input handling and the impact of reflected XSS vulnerabilities, while promoting secure coding practices.

It utilizes:
- **Flask** for a lightweight web dashboard
- **Selenium** for automated browser-based interaction
- **ReportLab** for generating structured and professional PDF security reports

---

## Test Environment

**Damn Vulnerable Web Application (DVWA)**

DVWA is an intentionally vulnerable web application created for **learning and ethical security testing**.

 **Note:**This tool is intended to be used **only on authorized test environments** such as DVWA.
 
> It is **not designed for testing real-world or production systems**.

---

## Automated Capabilities

In a controlled testing environment, the tool automatically:

- Identifies relevant user input fields
- Tests inputs using multiple reflected XSS payloads
- Confirms vulnerability presence through controlled JavaScript execution
- Captures browser screenshots as validation evidence
- Generates structured PDF vulnerability reports
- Displays results via a simple local web interface

---

## Demo Video

[![Watch the Demo](thumbnail.png)](Xss-Demo.gif)

---

## Key Features

- Automated login to DVWA
- Reflected XSS vulnerability testing
- Browser-based validation with visual evidence
- PDF report generation for documentation and learning
- Local web dashboard accessible at:  
  `http://localhost:5000`

---

## Installation & Setup

```bash
git clone https://github.com/REALFB007/XSS-AutoPwn-Demo.git
cd XSS-AutoPwn-Demo

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

docker run --rm -it -p 8080:80 vulnerables/web-dvwa

python app.py
