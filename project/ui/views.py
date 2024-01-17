from django.shortcuts import redirect, render
from httpx import request
import requests
from googletrans import Translator
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from django.http import JsonResponse
from PyPDF2 import PdfReader
import requests
import pyttsx3
from googletrans import Translator


# from pymongo import MongoClient

from django.http import JsonResponse
from django.template.loader import render_to_string

# from project.ui.forms import UploadPDFForm

# In pdf_summarizer/views.py

import os
import PyPDF2
import nltk
from django.shortcuts import render
from django.http import JsonResponse
from transformers import pipeline
from django.conf import settings

import fitz 

# try:
#     nltk.data.find('tokenizers/punkt')
# except LookupError:
#     nltk.download('punkt')

def summarize_pdf(file_path):
    # pdf_reader = PyPDF2.PdfReader(file_path)
    # text = ""
    # for page_num in range(len(pdf_reader.pages)):
    #     page = pdf_reader.pages[page_num]
    #     text += page.extractText()
    text = ""

    # Open the PDF file
    pdf_document = fitz.open(file_path)

    # Iterate over pages and extract text
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    # Close the PDF file
    pdf_document.close()
    sentences = nltk.sent_tokenize(text)

    # summarizer = pipeline("summarization")
    # summary = summarizer(sentences, max_length=100, min_length=50, do_sample=False)[0]

    # return summary['summary_text']
    document = " ".join(sentences)
    text = summarizer(document, max_length=130,min_length=60,do_sample=False)[0]['summary_text']

    return text
    # api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    
    # api_headers = {
    #     "Authorization": "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",  # Replace with your actual API token
    #     "Content-Type": "application/json"
    # }

    # # Set up the data payload
    # data = {
    #     "inputs": document,
    #     "options": {
    #         "max_length": 100,
    #         "min_length": 50,
    #         "do_sample": False
    #     }
    # }
    # response = requests.post(api_url, headers=api_headers, json=data)
    # if response.status_code == 200:
    #     summary = response.json()
    #     return summary['summary_text']
    # else:
    #     # Handle error response
    #     print(f"API request failed with status code {response.status_code}")
    #     return None

def pdf_summary_view(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('file-input')

        # Save the uploaded PDF temporarily
        temp_path =os.path.join(settings.MEDIA_ROOT, pdf_file.name)

        with open(temp_path, 'wb') as destination:
            for chunk in pdf_file.chunks():
                destination.write(chunk)

        # Summarize the PDF
        summary_text = summarize_pdf(temp_path)

        # Clean up the temporary PDF file
        # os.remove(temp_path)
        
        # Return the summary as JSON response
        # return JsonResponse({'result': summary_text})
        return render(request,'pdf1.html',{"result": summary_text,"input":pdf_file})
    else:
        # Handle GET requests (if needed)
        return render(request, 'pdf1.html')


from transformers import pipeline

summarizer = pipeline('summarization',model='facebook/bart-large-cnn')

text=""
def output(request):
    
    data = request.POST.get('data')
    text = summarizer(data, max_length=130,min_length=60,do_sample=False)[0]['summary_text']
    request.session['text_for_speech'] = text
    request.session['summarized_text'] = text
    return render(request,'summarease.html',{'result':text,'input':data})


def texttospeech(request):
    rate = 150
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    text = request.session.get('text_for_speech', '')
    # Use the engine to speak the given text audio
    engine.say(text)
    # Wait for the speech to finish
    engine.runAndWait()
    return render(request, 'summarease.html', {"result": text})


def language_translator(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language, src='en')
    return translation.text

def translate_summary(request, target_language='hi'):
    # Ensure 'summarized_text' is present in the session
    summarized_text = request.session.get('summarized_text', '')

    if summarized_text:
        # If summarized_text is not None, proceed with translation
        translated_text = language_translator(summarized_text, target_language)

        # Set the translated text to a new session key
        request.session['translated_text'] = translated_text

        return render(request, 'summarease.html', {"result": translated_text})
    else:
        # If 'summarized_text' is not present, handle accordingly
        return render(request, 'summarease.html', {"result": "Summarized text not found in session"})


from django.shortcuts import render
from language_tool_python import LanguageTool
from django.http import JsonResponse

def grammar_checker(request):
    if request.method == 'POST':
        input_text = request.POST.get('text_to_check', '')

        # Check grammar in the given text
        tool = LanguageTool('en-US')
        matches = tool.check(input_text)

        # Apply the corrections
        corrected_text = tool.correct(input_text)

        # Return the results as JSON
        response_data = {
            'input_text': input_text,
            'corrections': [{'ruleId': match.ruleId, 'message': match.message, 'replacements': match.replacements} for match in matches],
            'corrected_text': corrected_text,
        }

        # return JsonResponse(response_data)
        return render(request,'grammar.html',{'result':corrected_text,'input':input_text})

    return render(request, 'grammar.html')



# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):

    return render(request,'login.html')
# result_text = ""
def summarease(request):
    
    return render(request, 'summarease.html')
    # return render(request, 'summarease.html')


def registration(request):
    
    return render(request, 'registration.html')
    

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def logout(request):
    return render(request,'welcome.html')

def pdf1(request):
    return render(request,'pdf1.html')

def grammar(request):
    return render(request,'grammar.html')

def profile(request):
    return render(request,'profile.html')

def history(request):
    return render(request,'history.html')

