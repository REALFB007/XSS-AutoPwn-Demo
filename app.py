# app.py - SHOW LIVE LOGS ON WEB

from flask import Flask, render_template, request, send_file, Response
import subprocess, os, time

app = Flask(__name__)

def run_scan():
    yield "<pre>=== XSS-AutoPwn LOG ===\n"
    yield f"[+] Starting scan at {time.strftime('%H:%M:%S')}\n\n"

    # 1. SCANNER
    yield "[1/3] Running scanner.py...\n"
    result = subprocess.run(["python", "scanner.py"], capture_output=True, text=True)
    yield result.stdout or result.stderr
    yield "\n"

    # 2. EXPLOIT
    yield "[2/3] Taking screenshot...\n"
    result = subprocess.run(["python", "exploit.py"], capture_output=True, text=True)
    yield result.stdout or result.stderr
    yield "\n"

    # 3. REPORT
    yield "[3/3] Generating PDF...\n"
    result = subprocess.run(["python", "report.py"], capture_output=True, text=True)
    yield result.stdout or result.stderr
    yield "\n"

    # Copy image
    os.makedirs("static", exist_ok=True)
    if os.path.exists("reports/proof.png"):
        os.system("cp reports/proof.png static/")

    yield "\n[+] SCAN COMPLETE! <a href='/result'>View Result</a></pre>"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return Response(run_scan(), mimetype='text/html')
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/download')
def download():
    return send_file("reports/XSS_Report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
