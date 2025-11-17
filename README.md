#  Automated XSS Scanner
 
Built on **Kali Linux** using **Python, Flask, Selenium, DVWA**

---

## Features
- Login to DVWA
- Scan for reflected XSS
- Inject payload → Take screenshot
- Generate PDF report
- Web dashboard: `http://localhost:5000`

---

## Setup
```bash
git clone https://github.com/REALFB007/XSS-AutoPwn-Demo.git
cd XSS-AutoPwn-Demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker run --rm -it -p 8080:80 vulnerables/web-dvwa
python app.py
