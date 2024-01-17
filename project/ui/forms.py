# from django import forms

# class PdfForm(forms.Form):
#     pdf_file = forms.FileField()
#     pages_to_summarize = forms.CharField(max_length=255)
# In pdf_summarizer/forms.py

# from django import forms
# from .models import UploadedPDF  # Assuming you have a model for uploaded PDFs

# class UploadPDFForm(forms.ModelForm):
#     class Meta:
#         model = UploadedPDF  # Assuming you have a model named UploadedPDF
#         fields = ['pdf_file']
