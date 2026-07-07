<<<<<<< HEAD
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("report.pdf")

pdf.drawString(100,750,"AI Disaster Prediction Report")

pdf.drawString(100,720,"Risk : High")

pdf.save()

=======
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("report.pdf")

pdf.drawString(100,750,"AI Disaster Prediction Report")

pdf.drawString(100,720,"Risk : High")

pdf.save()

>>>>>>> 8bf753ab96844de6f412956b5129f8d13d0c50c5
print("PDF Created")