from reportlab.pdfgen import canvas

pdf = canvas.Canvas("report.pdf")

pdf.drawString(100,750,"AI Disaster Prediction Report")

pdf.drawString(100,720,"Risk : High")

pdf.save()

print("PDF Created")