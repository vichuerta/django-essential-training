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

### Creating a new Django project - `django-admin startproject`
With Django, we can have a whole project working in a matter of minutes. We can start our project by using a Django command, called Django-admin, and then a sub-command, startproject, then, the name of our project, smartnotes, and then dot to indicate we want to create the project in this folder. Okay, so this command creates two things: a managed.py file and a folder called smartnotes, the same name we gave our project. The managed.py file will be the entry point of your project. With it, you'll be able to run your project server, manually work with the database, and much more. If you look inside the smartnotes folder, you'll notice that all of the files here are related to the configuration of your project. The two main files you'll use here are the urls.py file, where you're going to configure, well, the URLs of your project, and the settings.py. Let's take a quick look into the settings.py. You can see here that there is a lot of global variables being defined. For instance, the debug equals true here tells Django that we are working in a development environment. Because we're in this safe development environment, it can return much more information when something goes wrong than it would in a production environment. You don't really have to understand everything it has right now, we'll get to it eventually, the only thing you need to know is that this is where you have the base of your project. As magic as this sounds, you already have everything you need to run your project. You can use Python, then the file, manage.py, and the command runserver to create a server using the default configurations we have right here. We can see here that there is some warnings in red, but you don't have to worry about it for now. You can also see that we're using Django Version 3.2, and that the configuration file being used is the smartnotes.settings. This means that this server is using this settings.py inside the smartnotes folder as the basis of it. You can also see that it gives a link to a web page hosted in the port 8000 of your local host. This means that your project is up and running on your computer and you can access it by using your browser. Let's click here and see what happens. Yes, you can see here that it will open a web page with the default layout. This means that you have successfully created and ran your first Django project, congratulations.

[manage.py](./manage.py) will be your entrypoint of your Django project. With it, you'll be able to run your project server, manually work with the database, and much more.

Your generated Django project folder, in this case [smartnotes](./smartnotes/), will contain all of the files related to the configuration of your project such as settings and urls, etc.

```bash
python3 manage.py runserver
```
