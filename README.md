# django-essential-training

[LinkedIn Learning Course - Django Essential Training](https://www.linkedin.com/learning/django-essential-training)

https://github.com/LinkedInLearning/django-esst-2894047

## Introduction

### What is Django?

Who doesn't want to build applications super fast with a great structure and simple framework? We also need phenomenal security and user authentication built in to make sure we have a reliable system. One of the best frameworks for doing this is Django. Django is an open source framework for building web apps quickly, and with very little code. In this course, we'll cover the essentials and we'll build a working application from start to finish. We go through a signup, login, creation and deletion of content. The whole full. I'm Leticia Portella, I'm an oceanographer that fell in love with programming and after teaching myself how to program, I've been working as a software engineer for many years. Join me in this LinkedIn learning course. As we dive into Django, and start building your first application.

### What you will need to start a Django project

There are a few things you need to get the most out of this course. You will need a Python 3.8 virtualenv and you must install Django 3.2, but should also work with later versions of Django. This is a simple stall. You'll just beep install Django and you'll get the latest version. We also need an editor, I'll use VS Code, and a browser, I'll use Chrome, but feel free to choose the tools you think are best for you. You might want to have at least some familiarity with HTTP and an idea of its methods. This will help you have a solid foundation and understand everything even better. And finally, we're going to host our exercises on GitHub, so you can check it out. If you need a refresher on any of this, check out some courses here in the library.

- Python 3.8 virtualenv

```bash
brew install python
python3 -m venv venv
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Django 3.2

```pip requirements
Django~=3.2.10
```

## 1. Starting Your Django Project

Building your Django Project

1. Start your project
2. Create your first view
3. Use templates

### Creating a new Django project - `django-admin startproject`
With Django, we can have a whole project working in a matter of minutes. We can start our project by using a Django command, called Django-admin, and then a sub-command, startproject, then, the name of our project, smartnotes, and then dot to indicate we want to create the project in this folder. Okay, so this command creates two things: a managed.py file and a folder called smartnotes, the same name we gave our project. The managed.py file will be the entry point of your project. With it, you'll be able to run your project server, manually work with the database, and much more. If you look inside the smartnotes folder, you'll notice that all of the files here are related to the configuration of your project. The two main files you'll use here are the urls.py file, where you're going to configure, well, the URLs of your project, and the settings.py. Let's take a quick look into the settings.py. You can see here that there is a lot of global variables being defined. For instance, the debug equals true here tells Django that we are working in a development environment. Because we're in this safe development environment, it can return much more information when something goes wrong than it would in a production environment. You don't really have to understand everything it has right now, we'll get to it eventually, the only thing you need to know is that this is where you have the base of your project. As magic as this sounds, you already have everything you need to run your project. You can use Python, then the file, manage.py, and the command runserver to create a server using the default configurations we have right here. We can see here that there is some warnings in red, but you don't have to worry about it for now. You can also see that we're using Django Version 3.2, and that the configuration file being used is the smartnotes.settings. This means that this server is using this settings.py inside the smartnotes folder as the basis of it. You can also see that it gives a link to a web page hosted in the port 8000 of your local host. This means that your project is up and running on your computer and you can access it by using your browser. Let's click here and see what happens. Yes, you can see here that it will open a web page with the default layout. This means that you have successfully created and ran your first Django project, congratulations.

[manage.py](./manage.py) will be your entrypoint of your Django project. With it, you'll be able to run your project server, manually work with the database, and much more.

Your generated Django project folder, in this case [smartnotes](./smartnotes/), will contain all of the files related to the configuration of your project such as settings and urls, etc.

```bash
python3 manage.py runserver
```

### Minimum working page - `django-admin startapp`

When dealing with big software projects, we need to make sure we are not creating a mess. The way we do this is to compartmentalize our project into smaller sections that have clear boundaries from day one. That's why Django created the concept of apps. Let's create one to understand it better. We'll use again the django-admin command to create a new app called home. You can see now that we have two folders: smartnotes, which is our settings folder, and home, which is the Django app we just created. Every time we create an app, we need to add it to the settings file so that it knows that that folder is part of the project we're running. Let's open the settings.py file. And add the name of our app in the INSTALLED_APPS variable. In order to make things a bit more organized, I always leave a small comment separating this app, created by us, from those that were already installed by default. Okay. Now that we have our project started, our app configured, it's time to create our first view. Let's go to the home, then go to the views file, and write our first function. As you can see, this is a pre-configured file. So we need to create our functions here. Let's import from django.http import HttpResponse. We can delete this, and now we create def home. It receives a request. And it return an HttpResponse with a simple message. Hello, world! As you can see, this function is saying that every time it receives a request, it will return a response with the text Hello, world! Okay, but how does it know when to send a request to this function? Well, that's why we have the urls.py file. We can go back now to the smartnotes, urls.py, and import this file there so we can have access to this function. So from home, let's import views, and now here inside the urlpatterns, we're going to add a new path. Let's call it home. And let's say views.home. Okay, so let's run our server again, and see what happens if we go to the localhost:8000. Yeah, so now instead of that beautiful page we had, because we have something implemented and not just the default configuration, we start to receive a 404, which makes sense because we never implemented anything here. However, because we have the debug equals true on the settings file, Django will list the endpoints that this project has available. And guess who is there. Yes, our home endpoint we just created. Now if we go to localhost home, we can see that we have the Hello, world! being displayed. Amazing, right? Let's take a moment here to understand what's happening. When a person goes to the home endpoint, they're making a request to that path. Django will go to the urls.py file to see if it's ready to receive a request at this path. Since it is, it will go to the views file, finally arriving to the function we defined. Since the function received the request, it can then respond with a message Hello, world! Django uses a common pattern as the way of structuring its project called Model View Template framework, or MVT. Views are responsible for handling requests and responses. In this video, you have learned that views can be as simple as functions, and can respond with something as simple as pure text. There are yet two additional layers for us to get familiarized with, right? These additional layers will allow us to increase our project's complexity, while being simple tools to work with. The model layer handles the data and how it's stored, and we'll see more about it in chapter three. The template layer allow us to render the information coming from the database into lovely HTML pages.

Every time we create an app, we need to add it to the settings file so that it knows that that folder is part of the project we're running. Let's open the [settings.py](./smartnotes/settings.py) file. And add the name of our app in the `INSTALLED_APPS` variable. In order to make things a bit more organized, I always leave a small comment separating this app, created by us, from those that were already installed by default. Okay. Now that we have our project started, our app configured, it's time to create our first view.

```bash
python3 manage.py runserver
```

http://127.0.0.1:8000 does not return anything since config is not setup (modified from the default config)

http://127.0.0.1:8000/home returns `Hello, World!` as expected


Django uses the Model View Template (MVT) Framework

Views are responsible for handling requests and responses.

Model Layer - handles the data and how it's stored

Template Layer - allow us to render the information coming from the database into lovely HTML pages

### Creating your first Django Template

Okay, it's time to learn how to return HTML pages by using the amazing Django template language. Let's start by creating a folder called templates inside our app folder. And inside of this folder, we'll also create another folder with the same name as our app, so let's call it home. This might seem weird, but it will allow us to quickly identify where a template is located, even if we don't know in which app we are on. This is a typical organization pattern for Django templates. Inside this folder, let's create a file called welcome.html. And inside it, we're going to add a basic HTML page. So a html tag, let's add a header with a title, so SmartNotes, and then a body with just one Welcome to SmartNotes. Okay, so now we can go back to the views file and change our base function. Instead of using the HttpResponse, we'll use the function render from the Django shortcuts that's already imported here. To use this function, we need to pass three parameters, the original request, the name of the template, and empty brackets. I know there is a warning here in the terminal that sounds a bit scary, but don't worry, this is normal, and we'll get to it later. Let's save this file and check the home end point again. And voila, our beautiful HTML is now being rendered. You might be wondering why we left the empty brackets behind, right? Although we are writing an HTML page, Django is actually using a template framework to create the final HTML page that we see in the browser. We can use the brackets at the end of the function as a way of passing down information from the view to the template. So let's import the datetime model and pass today's date into the dictionary with a key called today, datetime.today. We can then modify our template to receive a variable called today by defining it between double brackets. Today is today. Let's save it and try it again. There it is. This is why we're not using pure HTML, but actually a backend framework for defining templates called Django template language, or DTL. The HTML file we wrote will pass through the detail mechanism and it will insert the variables passed on the dictionary of the render function down to the template. This looks simple now, but DTL allows us to use sophisticated programming logic for creating dynamic HTML pages with very little effort.

```bash
python3 manage.py runserver
```

Django template language (DTL) - backend framework for defining templates
DTL allows us to use sophisticated programming logic for creating dynamic HTML pages with very little effort.
