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

### Django apps and the concept of modularization

- [Instructor] Earlier, we talked why apps are a good way to organize our project. Let's take a minute to understand a bit more why this type of modularization is such an important concept. As you've seen, an app is a small library that is contained inside your Django project. We can have as many apps as we want, however, as the project grows, if we don't take care of it, things can start to get messy and things will fly between the apps. That's why we need to understand what we need to do to make good Django apps. Good software projects should be well modularize, and your Django project should be no different. That's why each app should be self-contained, which means that everything you need for that app should live inside it. That's why we created the folder template inside it. The ideal app is one where you can delete the folder and do nothing else, the Django project just continued to work perfectly. So far, we're almost there, but there's still one thing that we need to do to clean things up. When we created our first endpoint, we had to import the fuse file from home into the URLs file in the smart notes folder. This creates a dependency that wouldn't allow us to quickly delete the home app. Let's make things a bit more organized. Okay, so first thing is to create another URL file inside the home app. In here, we're going to create a file, very similar to the one we have on the smart notes app. And let's add the same endpoint that we had in the previous file, views.home using the home function. Okay, so now comes the fun part, in the smart notes, let's get the URLs file. We can delete the dependencies that we implemented here, and now from the jungle URLs, we're also going to import the include function. Now, what we need to do is add an import path, but instead of using a function, we're going to use the include function here to pass that file as a string. So path, let's leave it open for now, and then let's include the home.urls file. Let's save this, and if we go back to browser, yes, as you can see here, nothing changed except the fact that now, if we delete the whole app, these won't give any errors because the app is not being important on this smart notes URLs file. There, with just a couple of tweaks, we eliminated a dependency and your project is following good standards of Django applications.

Good software projects should be well modularize, and your Django project should be no different. That's why each app should be self-contained, which means that everything you need for that app should live inside it. That's why we created the folder template inside it. The ideal app is one where you can delete the folder and do nothing else, the Django project just continued to work perfectly.

## 2. Django Built-In User Management

### Creating users in Django

Even though Django is typically known for the ease in which we can create endpoints. One of the most powerful features is the Django Admin Interface. It provides an interface. So that site administrators like you and me can easily view and manipulate data. Let's check out how that works. Are you wondering what you need to get it? Nothing, the system comes by default. When you open the local host 8000, you can see that besides the home endpoint we created, the admin endpoint is also available. Let's open it. As you can see, this is a login interface, but what now we didn't create any authentication system right, wrong. Django has the entire authentication system ready to go. The only thing we need to do is to make sure our database is properly configured. Let's go back. And remember when we had this red message while running the run server, this message is letting us know that our project has some database changes that weren't applied yet. The way Django knows if the database is behind the system, changes is through a couple of files called migrations. Migrations, explain what kind of changes a database need to perform such as create a new table, establish a new relationship, et cetera. Django already has the migrations for the authentication system ready. So what you need to do is apply them to the database and we do this by using the command migrate that will actually change the database. So what we can do now is run the command migrate. Okay, you can see here that the changes made are all regarding the admin and the auth apps. We don't see these apps because they come from Django by default, but they are there and they're ready to be used. You shouldn't worry too much about migrations now. We'll learn a lot about them in future classes. Since now, our database is up to speed with Django. What we need is to create a super user that will have all the powers that can in this Django project. We do this by running the command, create super user. It's pretty straightforward. Let's make the username admin. I'm going to leave the email address empty, and I'll add admin as a password. As you can see, Django already has a couple of checks to guarantee we are creating secure passwords. You can bypass it for now as I will just because this is while we are developing this project locally, never bypass it in production environments. Security must always be your number one priority, and Django is here to help you. Okay, now we can go back to the local host 8000 admin. Well, first let's run the server again. Okay, now we can go back to the admin interface, Admin, admin, login, and there you go. Now you have full access to the Django Admin Interface. And as you can see, we don't have any red messages now, while we run the run server, because our database is completely up to speed with the project. There you go.


Migrations, explain what kind of changes a database need to perform such as create a new table, establish a new relationship, et cetera. Django already has the migrations for the authentication system ready. So what you need to do is apply them to the database and we do this by using the command migrate that will actually change the database.

```bash
python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver
```

### Django admin: Easily visualizing and creating data

The Django admin interface allow us to quickly and easily access data that exists in the database. This means that users and groups, you can see here, are actually tables in our database. If we open the users table, we can see that we already have one record, the admin user we created using the create super user command. This is the one you're logged with right now. The interface also allow us to quickly filter the data by some of the characteristics of users. We can search for a user by staff status, super user status, et cetera. You can also search by a characteristic on the search bar here. Let's create a new user, shall we? We have to go here on add user, then add a username, and let's add a password. adminadmin. Save. As you can see here, we can't bypass the password check on the interface, so we actually need a really good password here. And let's click save. Perfect. Now we have the user created. As you can see, to create a user, we just need the username and password, but there is more to it, such as personal information, permissions, et cetera. All of this complex authentication user was created by Django by default. We just need to use it. One thing that I would like you to notice is that the password is encrypted. And that's why you're seeing a bunch of random characters here. By using Django's authentication system, you're also guaranteeing that your system is correctly and safely storing passwords. If we go back to the list of users, you can see now that we have the user recreated. We can also select it and delete the selected user. As you are deleting data, Django prompts a second screen with the data you're deleting so you can confirm that you want to perform the section. So let's click Yes, I'm sure, and there, we successfully deleted that user. If we go back to the homepage, we can also see that the interface lists the actions we made in the system, such as the creation and deletion of a user. As you can see, the admin interface is a nice and safe space to directly access data in the database. If your system doesn't require inputs from users, like a blog, for instance, you can use this interface to create all the data you want and use the views to display it. It's simple and powerful.

### User authentication in two simple steps

So far, you've learned that Django comes with a powerful authentication system, already ready to be used. Now, let's learn how to use it. First, let's go back to our home app and create a second template. Let's call it "Authorized." And in here, let's create a simple HTML that has a title, You are in a restricted area. Now we can go back to the views file and create a very similar function to home. But this time we're going to display the authorized template, def authorized request. And it's going to return render request. Now let's add the home authorized dot HTML and empty square brackets. Yeah, so now we have exactly the same thing, and here comes the wonderful Django simplicity. In here, let's import from Django dot contrib dot auth dot decorators. Let's import login required. So now I can add this function as a decorator to our authorized function. That's it. That's all we need to do to block the access of this webpage if a user is not logged in. To finalize, let's go to the urls dot py and add this as a path. So let's call it authorized and views dot authorized. Now we can go back and try to access the authorized endpoint. There you go. We can see the template we created. This is only possible because we're logged in via the Django admin interface. If we go back to the admin and log out and try to re-access the authorized area, you see here that we get a 404, meaning that this page was not found. Why is that? Because we're not logged in. The complex authentication system just required a single line of code. However, a 404 is really not a nice flow, right? We want the user to know that they need to be logged in to access this page. The ideal flow is that we redirect them to the login page. To do this, we need to go back to the views file and add a parameter called login url. And let's pass this as slash admin. If we go back and try to access it again, and there it is. Since we are not logged in, Django understand that it needs to redirect me to the login url, which for now was defined as the admin end point. How amazingly simple was to add authentication to this endpoint?

