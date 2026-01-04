# report.py - Makes PDF with screenshot

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def make_report():
    print("[+] Creating PDF report...")

    # Create folder
    os.makedirs("reports", exist_ok=True)

    # PDF setup
    doc = SimpleDocTemplate("reports/XSS_Report.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("XSS-AutoPwn Report", styles['Title']))
    story.append(Spacer(1, 20))

    # Details
    story.append(Paragraph("Target: http://localhost:8080/vulnerabilities/xss_r/", styles['Normal']))
    story.append(Paragraph("Payload: &lt;script&gt;alert('XSS-AutoPwn')&lt;/script&gt;", styles['Normal']))
    story.append(Paragraph("Status: <font color='red'>VULNERABLE</font>", styles['Normal']))
    story.append(Spacer(1, 20))

    # Screenshot
    if os.path.exists("reports/proof.png"):
        img = Image("reports/proof.png", width=500, height=300)
        img.hAlign = 'CENTER'
        story.append(img)
    else:
        story.append(Paragraph("No screenshot found!", styles['Normal']))

    story.append(Spacer(1, 20))
    story.append(Paragraph("Fix: Sanitize user input with HTML escaping", styles['Normal']))

    # Build PDF
    doc.build(story)
    print("[+] PDF SAVED: reports/XSS_Report.pdf")

if __name__ == "__main__":
    make_report()
