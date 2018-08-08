
# Routes

Routes connect URLs to views. The routes are stored in a **urls.py** file, which can be found in both the project folder and in each of the apps' folders. URLs are matched in a way similar to **regular expressions** with a little more flexibility (in Django 1.X, routes were handled explicitly with regex). You can read more about routes [here](https://docs.djangoproject.com/en/2.0/topics/http/urls/).


```python
from django.urls import path

# import your views module, so you can tell Django about the view functions
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
]
```

You can specify a parameter in your path using `<type:var_name>`, where `type` is the data type of the parameter (e.g. `str` (default), `int`, `slug`, etc.)

Routes are evaluated **in order**: whichever route matches first is the one used.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('base/<int:id>/', views.base_capture),
    path('base/wont_match/', views.base_wont_match),  # this will never match because of _both_ of above routes.
]
```

## include()

The `include` function allows you to combine the routes of multiple `urls.py` files into one. This is used to connect the project's 'main' `urls.py` to the `urls.py` in each of the apps.

```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('path/', include('<appname>.urls'))
]
```

## Parameters in the Path

See the [views.md](02%20-%20Views.md#path-parameters) file.
