from django.shortcuts import render
import requests
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
result_text = ""
def summarease(request):
    if request.method == 'POST'and request.is_ajax():
        data = request.POST.get("data")
        line_length = request.POST.get("line_length", "")

        if not all([data, line_length]):
            return JsonResponse({'status': 'error', 'message': 'Invalid request'})

        api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        api_token = "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"
        headers = {"Authorization": f"Bearer {api_token}"}

        def query(payload):
            response = requests.post(api_url, headers=headers, json=payload)
            return response.json()

        try:
            output = query({
                "inputs": data,
                "parameters": {"max_length": line_length},
            })[0]

            result_text = output["summary_text"]

            return JsonResponse({'status': 'success', 'result': result_text})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return render(request, 'summarease.html')


def registration(request):
    return render(request,'registration.html')
    

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

