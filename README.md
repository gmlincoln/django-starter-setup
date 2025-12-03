### Django Starter Project

This is a clean and simple Django starter project with a single app named **core**.  
It includes basic URL routing, a view, template rendering, and passing dictionary data to a template.

---

### 📁 Project Structure
```bash
|-.venv(create virtual environment)  
|myProject/  
    │── manage.py  
    │  
    ├── myProject/  
    │ ├── init.py  
    │ ├── settings.py  
    │ ├── urls.py  
    │ └── wsgi.py  
    │  
    └── core/  
    ├── init.py  
    ├── views.py  
    ├── urls.py  
    └── templates/  
    └── index.html  
    
```


---

### 🚀 How to Run the Project

#### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
# or
py -m venv .venv
```


#### 2️⃣ Activate Environment
**Windows**
```bash

.venv\Scripts\activate

```

#### 3️⃣ Install Django

```bash 

pip install django

```


#### 4️⃣ Run Server
```bash

python manage.py runserver
# or
py manage.py runserver

```


---

#### 🔗 URL Routing Overview

**Project URLs: `myProject/urls.py`**

```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

```

**App URLs: `core/urls.py`**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

```

#### 🧩 Passing Data to Template

**App Views: `views.py`**

```python

from django.shortcuts import render

def home(request):
    data = {
        "title": "Welcome to Django",
        "message": "This message is coming from views.py",
        "author": "Golam Maula Lincoln"
    }
    return render(request, "index.html", data)

```

#### 🎨 Display in Template

**In App: `templates/index.html`**

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <h3>Author: {{ author }}</h3>
</body>
</html>

```