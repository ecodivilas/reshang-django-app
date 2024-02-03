## Guide
# Python->Django Setup in Windows:

### Step 1:
#### Install python 3.8
#### Install WSL (If windows) / Dual Boot
#### Install VS Code
- python (IntelliSense) Microsoft

### Step 2:
#### Add python path to environment variable

### Step 3: 
#### Verify Python: python -v

### Step4:
### In CMD:
#### mkdir \<project>
#### cd \<project>
#### code .

### Step5:
Create virtual environment
- Use WSL terminal inside the vscode
- virtualenv .
- source bin/activate (to enter the virtual environment)
- pip install "django>=3.2, <3.3"
- pip freeze (to show the installed/related packages)

### Step 6:
#### Create a new django project
``` python3 -m django startproject trydjango .```

### Step 7:
#### Put the installed packages in the file for future installation
#### echo "django>=3.2, <3.3" > requirements.txt
#### or
#### pip freeze > requirements.txt

### Future use:
#### (try-django) ecodivilas@000D202425:/mnt/c/Users/User_local/development/try
-django$
#### pip install -r requirements.txt

### Step 8:
python manage.py runserver

### Step 9:
Create views.py inside the project folder (to add route and view)
# views.py
```
from django.http import HttpResponse

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response(We pict to return the response)
    """
    HTML_STRING = f"""
    <h1>Hello {name}</h1>
    """
    return HttpResponse(HTML_STRING)
```

# urls.py

``` from .views import home_view
from .views import login_view

urlpatterns = [
    path('', home_view), # index / home /root 
    path('login/', login_view),
    path('admin/', admin.site.urls),
]
```

Step 10:
Create app/component in django:
python manage.py startapp articles