"""
To render html web pages
"""
import random
from datetime import date

from django.http import HttpResponse

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response(We pict to return the response)
    """
    name = "Ely"
    number = random.randint(10, 1232323) # API call to some rest API with python & python requests
    today =  date.today()
    HTML_STRING = f"""
    <h1>Hello {name}</h1>
    <h2>Random Number: {number}</h2>
    <h2>Date Today: {today}</h2>
    """

    print(3434*744737)
    return HttpResponse(HTML_STRING)

def login_view(request):
    HTML_STRING = """
    <h1>Login</h1>
    <label>Username</label>
    <label>Password</label>
    """
    return HttpResponse(HTML_STRING)