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

## 3. How Django Interacts with Databases

### Introduction to ORMs

So far, you've gotten familiarized with the user models, which were completely defined by Django. Now it's time to understand how to create your own models and how the structure of creating models work. Django uses an object relational mapping system or ORM to handle database communication and changes. What you need is to write class models that will then be transformed by migrations into database tables. Each class known as a model is a database table and each class attribute is a column. The way we transform a model into a database table is by the creation of migrations. Migrations will have the step-by-step transformation that a database must do to apply the changes made in the code. You've seen that we use the command migrate to apply migrations to a database. Similarly we can use the command, make migrations to create migration space on the current code, the process of using a class, defining a model, creating a migration, and applying the immigration and the changes to the database is the ORM's job. And Django's ORM, is known for being one of the best ORM's for Python and SQL databases.

Django uses an object relational mapping system or ORM to handle database communication and changes. Class models can be transformed by migrations into database tables. Each class known as a model is a database table and each class attribute is a column.

### Creating your first model

It is time for us to learn how to create a new model using Django ORM. Let's create a new app specifically for our notes. So Django-admin startapp notes. Okay. Remember, now we have to go to the settings and make sure that our new app is added in the installed apps variable. Okay. Now we can go back to this new app and open the models.py file. Here is the file where we can create the models that we'll use in this app. So let's create a new class called notes that we'll inherit from models.Model. This way, Django knows that this is a model that will have effect on the database, et cetera. Its time for us to think what attributes we want in our note. Well first, we can add a title. A title is a short text, so we can use the type Charfield, which is a limited text view. Charfield has a parameter called max length, and we should set it to a value, let's say 200. This means that our title can't be over 200 characters. Okay, we also need the notes itself, right? And the notes shouldn't have a limit, so instead of using Charfield, we can use the type TextField. As you can see, TextField doesn't require a max length differently from Charfield. We also want to know when this note was created, so we can add a field called created, that is going to be a DateTimeField. Because we don't really want to worry about this field being correctly populated, we can add a parameter called auto_now_add equals to true. This means that every time a note is created, this field will be correctly populated with the time that this note was created, so we don't really have to worry about it. There. Our notes model is done. Every note we create, we'll have at least a title, a text, and a date. Amazing. So what do we need to do now? I hope you guessed it right. We need to create migrations. Luckily, this is super easy to do. Let's type python manage.py makemigrations. Let's see what happened here. There is a new folder called migrations, and inside of it, there's a new file called 001_initial. Every first migration of an app will be named like this. If you open this, you can see that this is just a list of operations that instructs the database what needs to be done. So far, we haven't changed anything in the database, we just created the set of instructions, so everything continues as it is. What we need to do now is apply the migrations so we can run python manage.py migrate. And we're done. The changes were applied to the database and we have a shiny new table.

Create migrations after modifing [models.py](./notes/models.py)
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Using admin for data creation and manipulation

We've already created a table for notes, but if you're curious enough to go to the Django admin interface, you'll notice that nothing really changed. Why is that? The same way we didn't have to create a user model, it was just there. We didn't have to configure it to appear on the Django interface. When we are creating a new model, we need to do it ourselves. So let's go back to the notes app and open a file called admin.py. This is where we go into add which models can be displayed, and thus, modified via the Django admin interface. First, let's create a class and call it NotesAdmin. This class should inherit from admin.ModelAdmin. Let's add pass here because we don't want any additional configuration on this admin model. Now what we need to do is import from this folder. Let's import models, and on the bottom of the file, we're going to register that that model is attached to this admin model. So let's write admin.site.register, then models.Notes, and NotesAdmin. Okay, that's it. Let's go back to the admin and refresh it. There you go. Now we can see that the notes model is available on the admin interface. Let's use the add button here to create a new note. Let's title, My First Note, and then, Django is so amazing. Let's save this. Okay, we have our first note created. One thing that isn't really nice is that it is listed as this Notes Object One. This is fine for now, but if we have a long list of notes, how can we tell which one is which? Let's go back to the admin class. Instead of pass here, we can pass list_display, which is going to be a tuple, and let's pass title here. Let's save this. It restarted. And now, if we refresh here, there, instead of having this ugly name, we have the title of the note being displayed here. The default configuration of admin also allows that all fields can be changed by all users. However, we can edit the admin model class and start adding some specialized logic. We can remove some fields from being edited. We can allow only staff users to write notes. There's a lot we can do, the sky's the limit. Django admin is highly configurable.

### Using Django shell for creating and querying data

- [Instructor] We've already learned how to do things via the Django admin, but it's time to learn how to handle models through code. Django has a tool we can use to check the content of a database, which will make our life so much easier, the Django shell. Let's go to the terminal and type python manage.py shell. You can see here that we have a Python interpreter, however, this is no ordinary interpreter, it is already tightly coupled with our project, for instance, we can type from notes.models import Notes, which is the model we just created, and with this, we can use it to query the objects in the database. Let's try to get the first note, mynote, Notes.objects.get, pk is equal to one. There, we have our note. Notes.objects is the main way of accessing data from the notes table in the database. The .get method will search for one object, which the pk private key is equal to one and returns that object. Now we can use it to access attributes of the model by simply typing mynote.title, or my note.text. We can also query for all objects in the database by using the method .all instead of the .get. Notes.objets.all, there you go, we only have one note so far. The return of this function is a query side, which is a very useful tool, but you can think of it as a list with the superpowers. We can also create a new note via the command line, let's try it out. New_note, Notes.objects.create, then title is equal to a second note, and then text is equal to this is a second note. There, the note was added to the database. If we query it again, you can see now that we have two objects being returned. If you prefer, you can open the admin interface and check it out. We can also filter notes that we want, for instance, we can query for the notes that have titles starting with the word, my. Notes.objects.filter, for the title starts with the word My, yeah. The filter also returns a query set, which in this case, returns the first object. We can also search by something that exists inside the notes, for instance, we can try to find texts that contains the word Django. So we type Notes.objects.filter, text__icontains the word Django. There you go, only the first object has the word Django in the text. We can also query for the opposite, we can actually filter notes by excluding them, so let's do the opposite notes.objects.exclude, notes that the text contains the words Django. You can see now that the filter is returning the second note instead of the first. The fun part is that query sets can also be filtered, meaning that we can add multiple filters at once, for instance, we can filter all the notes containing the word Django, but the title doesn't say anything about Django. Text contains the word Django, but exclude the ones where the title contains the word Django, there you go. As you can probably imagine, we can go on and on here with thousands of examples on how to query data. Django's ORM has a very neat interface that is very intuitive and yet highly powerful. I highly encourage you to try more queries by yourself.

```bash
(venv) victorhuerta@Victors-MacBook-Pro django-essential-training % python3 manage.py shell
Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from notes.models import Notes
>>> mynote = Notes.objects.get(pk='1')
>>> mynote.title
'My First Note'
>>> mynote.text
'Django is SO amazing!'
>>> Notes.objects.all()
<QuerySet [<Notes: Notes object (1)>]>
>>> new_note = Notes.objects.create(title="A second note", text="This is a second note")
>>> Notes.objects.all()
<QuerySet [<Notes: Notes object (1)>, <Notes: Notes object (2)>]>
>>> Notes.objects.filter(title__startswith="My")
<QuerySet [<Notes: Notes object (1)>]>
>>> Notes.objects.filter(text__icontains="Django")
<QuerySet [<Notes: Notes object (1)>]>
>>> Notes.objects.filter(text__icontains="Django").exclude(title__icontains="Django")
<QuerySet [<Notes: Notes object (1)>]>
```

## 4. Building Dynamic Webpages

### Creating a dynamic template

Now that we have our notes, how about we learn how to display them? Let's create a new view, the same way we created the other one. So notes, views.py file. And let's start with importing the models and import Notes. Okay, now let's create a function called list that receives a request, and then a variable all_notes that stores all the notes that we have in our database. Now let's return the render function again. Request, a template that we're going to create a little bit later, notes/notes_list.html, and now the brackets with notes are equal to all_notes. This is not much different from what we did in the other view, except for one thing: We are querying for all notes and sending them to the template. This way, when the template is rendered, all the information coming directly from the database will be available. Before we jump to the template, let's organize URLs. So let's create a new urls file here. And that's going to have the same format. So from django.urls import path. Then let's import the views here. And then the urlpatterns that has a list. Then here the path. Our endpoint's going to call notes because that's the list of notes. Then views.list, which is the function we just created. Amazing. The last thing is that we have to add this on the urls.py file on smartnotes. So let's add a comma here. Then path. Let's add smart here and then include notes.urls. Amazing. By doing this, all the URLs that we are adding on notes.urls will be added after the smart. So smart is going to be a part of that endpoint. This is a really nice way of organizing our project. Okay, almost there. Now we need to create the template folder. So notes, New Folder, templates. Then a new folder, notes. And now we can add our template. Notes_list.html. Okay, now we can create our template. So let's start by html. In h1, these are the notes. And now we'll start to use the powers of DTL. Bear with me just a little bit. So let's start with ul, and then curly brackets, two percentages, and in the middle, for note in notes. Okay, so in here, we're going to add a line item, two curly brackets, note-title, close the curly brackets, and now we need to do curly brackets, percentage, percentage, and in the middle, it's going to have an endfor. Okay, what's happening here? Everything that is between curly brackets is the Django template language logic. Here we're opening a list tag ul, and then saying that for each note we receive in the template, DTL should create a list item, the li. Notice that commands, such as the loop happen between curly brackets and percentages, while things that should be rendered by the template are between double brackets. So let's save this. Then run this runserver. And open it. Okay. Okay, now we can see that we have a smart here. Then let's try the smart. We're going to have the notes. And here are the notes. There it is. A web page that is dynamically getting data from the database and adding it to the HTML. If we right click here and inspect the page, we'll see here that we actually have two line items. That's because we have only two notes on the database. If we had many more, many more would be created. How easy was that? I encourage you now to go and create more notes, either via the shell or the admin and see what happens here.

### Display content of a single note

Now that we have a list of notes, how about we create a way to visualize details of a particular note? Let's go back to the notes app, views.py and let's create a new function here. Now, this function should receive a second parameter called pk for private key. So let's go def detail request, pk. Okay, now we can use this pk to go in the database and get that particular note. So note is equal to Notes.objects.get. Pk is equal to pk. Okay, and the common response. Return render the request. Let's keep the pattern here. So notes/notes_detail.html. And then let's pass note inside the brackets. Okay, now what we need to do is create the template. So let's go back here. New file, notes_detail.html. And let's create a simple HTML that has the title as note.title is an h1. And then let's go a text here, note.text. And there you go. Okay, so there's one thing still missing, which is the URL. This needs to be a slightly different URL because we need to be able to pass down the second parameter to that function. So let's do this by adding a new path here. So we're going to have notes, then slash, the minor and greater sign, and pk. Great, and now the views.detail. Okay, so what we're telling here is that URL will receive a new value named pk that will be an integer number. Now, the only thing left to do is start the runserver again. And test this out. So here we have the notes, and if we pass now the pk for our first note, we can see the template displaying the details of the first note. Okay, so this works fine but we still have a problem. The get method that we're using to get the note from the database will actually throw an error if you pass down a private key that doesn't exist. So if we try the same URL but with I don't know, 11 or something, unless you have created 11 notes, this will raise an error. So let's try it out. Notice here that this is returning an exception of the type does not exist. We can also see here that there is a message with the exception saying notes matching query does not exist. Django has an amazing traceback for us to understand where exactly the error happened. You can see right here that the problem started in line 11 on the notes, views.py file, which is exactly where we define the query. We only have this page explaining the error again because we continue to have the debug equals true in the settings file. In a production environment, the user would see a 500 error, which means an internal error. When an object is not found, the correct response is a 404 status code saying that that object does not exist. So let's change our code to make sure that we get the correct status code. Let's go back to the views file. And in here, let's import from django.http. Let's import Http404. Okay, and now we can wrap this query in a try and except block. So try and except if the Notes.DoesNotExist equals true, we're going to raise an Http404 with the message Note doesn't exist. Okay, so if you go back now to the previous link, and refresh, we're going to see here that this page is now returning a 404 with a message that we define. This is a much nicer flow than the error we had before because we're controlling the message to the user. If you can, we can actually create another template, specifically for a 404 and return it with a nice message. It is completely up to you.

### Introduction to Django class-based views

So far, you've learned how to create views using functions. However, Django has a couple more features that we can leverage to get things even simpler. Welcome to class-based views. Most views have similar patterns, and reinventing the wheel is something nobody really wants. Class-based views are extensive classes that implement typical view behavior, and you just need to override a few things to make it do what you want. This will allow us to avoid the boring work and focus on the things that are unique to our project. Let's go back to our code and change our views that are function-based to the ones that are class-based and see in detail how class-based views work. The first view we made was in the home app, so let's go back and change it. The only thing we need to do here is display a template, so we can do that by using the class-based view TemplateView class. So let's in here import from django.views.generic import TemplateView. Okay, so now we can create a new class called HomeView that inherits from TemplateView, and the only thing we need to pass here is the template name. So we can copy here and paste it here, and that's it. We still need one more thing because our template requires some extra information, so we can add a variable called extra_context and now pass this dictionary here in it. We can delete this now. Oops, it's missing something, okay. So now we can delete this function here, and we have our first class-based views. The last thing missing is that we need to change the way the URLs are defined, so let's go to the URLs, and in here, instead of passing the home function, we're going to pass the HomeView class and we need to call a method called as_view. You can see here now that the server is working just fine, so we can go back here, and it's still working. So we can quickly do the same with the second function here, the authorized view. So let's create a class called AuthorizedView that also inherits from TemplateView. Then the template_name. We're going to have this here. Oops, there's an extra space here, okay. Okay, because we don't have the extra attributes required here, we can just not pass the extra_content. Okay, but we're still missing authentication. How do we handle authentication on class-based views? Well, to do that, we're going to need a mixin class. *Mixins are helper classes that can be used along with other classes to provide additional features.* For this case, we'll use the LoginRequiredMixin. So let's go back here, and we can remove this now and use the from django.contrib.auth.mixins. We can import LoginRequiredMixin. The only thing we need to do here now is make sure that this class, which is a mixin, is added before the TemplateView, okay? The last thing missing is the login_url. So we can actually go here, add the login_url. Let's still pass the admin, and that's it. So we can remove this now, fix the URLs to be AuthorizedView.as_view, and that's it. As you can see here, things are quite nice and well-organized, and you also don't have to remember the requests coming in and out of the function. Class-based views might not seem like the amazing features they are, but that's because we are still handling simple views. As the views increase in complexity, they become more and more amazing allies.

### A bit more on class-based views

We worked with templates, but now it's time for more complex views. Let's start with our list endpoint. On the notes, let's go to views.py file. And in here let's import from django.views.generic import ListView. Okay, now I can start our class-based view. Let's go to create a class. So let's call it NotesListView, that inherits from ListView. And we need to add here, which model we're listing objects from. So let's add here a model equals to notes, okay. And because our template is expecting to receive a list called notes, we should also add here that the context object name is different from the default. The default is objects, but we call it notes. That's it, that's our whole end point. The only thing we need to do now is change the end point URL. So let's go back here, then change lists to NotesListView.as_view and that's it. We can go back here and also delete our old endpoint. We don't need it anymore. Okay, it restarted. So let's try it out. Instead of homes, we're going to go to smart notes. There you go. You may be thinking what's happening here? Where is the query? The list view is already making the query for us. We also don't need to define the template name because we created a template name that follows the standard of that class based view. But if we enter a different name, it might not work. So instead we can pass here an attribute called template name, you guessed correctly. So we can say here, notes/notes_list.html. Yeah, that's all we have to do for the list end point. Now we can go to the detail view. Can you guess what we need? Not much else. Just import here, detail view, and then let's create the class. So class notes, detail view that inherits from detail view here, we need model equal to notes and context object name is equal to note, to note and that's it. Wait, just that? You might be thinking like, what about the exception with row when the object can't be found, there is no need. The detail class-based view already take care of that for us. There is no need for us to handle any of that complexity. Let's change the URL and give it a try. So in here, let's change detail for NotesDetailView.as_view. Let's go back, then that one, and it works. And if we go to something that doesn't exist, yep. It's still returning a 404. Hopefully at this point, you can already see how class-based views are an amazing feature of Django. And we've only scratched the surface. There are very few case scenarios where you will prefer to create a function-based view as the ones you just replaced. In the vast majority of cases, a class-based view will be the ideal tool for you.

By default, the `ListView`/`DetailView` generic view uses a template called `<app name>/<model name>_detail.html`

## 5. Building a Robust Front End in Django

### Static files in Django

It is time to think about our project's front end. Our templates are too simple with just HTML on them, so let's add some colors. The first thing we need to do is create a folder where we're going to store all the static files, such as the CSS and JavaScript files, images, videos, et cetera. So let's go here and create new folder, static. Now we need to tell Django that this is the folder it needs to look into when searching for static files. To do that, let's go to the smartnotes, then settings. Then in here, we can scroll down a little bit, and we're going to see here that there is a STATIC_URL already. Now we're also going to add STATICFILES_DIRS. This should be a list. And in here, we're going to say BASE_DIR / 'static' which will lead Django to the folder we just created. Okay, now we can go back to the static and create a new folder just for the CSS files and one CSS file. Let's call it style.css. Okay, so in here we can create a simple CSS file. Let's create a class called note-li, color equals red. Really simple. What we need to do now is make sure that our template and Django per se recognizes this file. So let's go to the notes and let's try the notes_list file. Okay, in here, the first thing we need to do is actually tell Django that this HTML is going to use the static files. So let's go curly brackets, percentages, and load static. Okay, now what we need here is to add a CSS file as we would in any HTML file, so let's create a head then a link, so the rel is going to be stylesheet, the type is going to be text/css, and on the href, we're going to use the Django template language to add our URL. So let's call static, then css/style.css. That's it. That's all we need to do to have the CSS being rendered on this file. So let's go here on the li and add a class which is going to to be our class name, note-li. And let's save it. Okay, let's try it out. I'm going to refresh this, and there you go. Now the notes are red because the CSS is being rendered and used in this file. If we open the inspector here, we can see here that the head is appearing. We have the href here being correctly rendered, and then each notes here has the class that has the attribute of color red. If you hover this href, you'll notice that this is actually a link, so let's go here. Let's copy this, and then we can replace it here, and there you go. As you can see here, this is the file we just created. So actually Django is locating the file and loading it automatically into the templates. There you go. Now you can use CSS in all your templates.

### How to set up a base HTML for every Django template

As we've seen, it's pretty easy to add CSS files into Django template. But it would be quite exhaustive to need to always remember to add the CSS link to all templates we have in all our apps. If you're thinking that there must be a better way of doing this, you're absolutely right. What we need now is a base template. Let's create a templates folder in the static folder, and a base.html template in it. Okay, so in here, we can create a normal HTML file. So html. Then head. Then in here, we can have link. Type's going to be text/css. Then href, it's going to be the same loading of a static file that we had. Css/style.css. Okay? Now we have to remember to load static on the top of the file. Load static. And now we can create a body. Perfect. Now what we need to do here is add the following command. So curly brackets and percentage. Block content. And then similarly, we're going to do another one but now it's endblock. Okay, so I called this content, but you can call it whatever you like. The important thing here is to know that this is a block area where we can inject things. Let's try it out. Let's go back to the notes, and open the notes_list template. So in here, what we can do is extends base.html. Now, what we can do is get rid of all this basic HTML stuff here and use this block content here. So block content, and in here, we can endblock. Okay, so what we're doing here, we're taking only the important part of our template, and wrapping it on the block content command so this can be injected on the base template. Let's try it out. Okay, so we have a problem here. The template is showing us non-existent. What happens here? So you can see here where Django was trying to search for a base.html template. So you can see that it tried in multiple places, including the two templates folder in home and notes app. But as you can see, the static folder template is not being looked for. So what we need to do is tell Django what to look for. So let's go back. Then in here, let's go to settings file, and down below, we're going to find out that there is a templates, and there is a list of directories that we can add here. So similar to what we did on the static files, we're going to add that particular folder in here. So let's do BASE_DIR and then slash, and then static/templates. Okay, so it reloaded. Let's try it again. And there you go. So let's take a minute to understand what's going on here. What's happening here is that with this syntax, we can define the basics of our HTML in our base.html template, and then we create each web page as a separate template that extends the base. So we will build each template separately and just the small parts but we'll then inject it to the base template where we can have all our default configurations, such as the CSS files and the JavaScript. This will allow us to keep each web page template as simple as we can while keeping all the configuration in a single place. That's another power of the Django template language. Now that you know exactly how to use a base template, I encourage you to go back and try it out in all the templates we have so far.

### Let's add some style

Okay, so instead of defining all the CSS, we want to speed up our front end a little bit, so let's use the CSS framework. We're going to use Bootstrap for now, so what we need to do is on the static, base.html, I'm going to change this CSS we just created with the link to the Bootstrap framework version five. So we can go back, delete this line, and that's it. I know it's a pretty big link, so you can find it on the notes of this class. Okay, once we define this, we can start using it. So the first thing we can do here is on top of the block content, let's add a div and then on this div, let's add a class equals to my-5 text-center and container. Okay, so now we can go to the home page and check the changes that the Bootstrap's already made. So let's go here. You can see here now that the style's a little bit better. We have more spacing, the text is on center, et cetera. So let's add a button on the home page that will lead us to the list of notes. So let's go to home. Welcome. Perfect. Here we can add, so it's going to be an a href. Let's leave it empty for now. Then in here, we're going to use two classes. Btn for button and btn-primary for the style. Then check out these smart notes. Okay, so if we go back, we can see now that we have a button but it doesn't do anything. So how do we deal with links here? We could hard code the link to our localhost but imagine that when we deploy our website, we need to remember to come back and change everything. Not so good. Thankfully, the Django template language has a function for that. What we need to do is the following. Let's open curly brackets and percentage, and then use url, and then in here we're going to say notes.list. Okay, you might be wondering, okay, how Django knows which endpoint to link? It doesn't, and we need to tell it. So let's go back to notes, urls, and in here, what we're going to do is add a name. So we can give a name notes.list. That's all we need for Django dynamically define each endpoint we are pointing to, no matter if you're on localhost or production. Let's test it out. Let's click here, and there you go. We're being redirected to this template. That also needs some styling. We'll get there. So let's go back to this page and try to style it up a little bit. So let's go to notes_list, and in here, we need a couple of things. So first, we can add some vertical styling here. So we're going to use my-5 here. Okay. And let's use a couple of divs here to have some cards. So bear with me just a little longer. So in here, instead of the ul, we're going to use a div, and this div's going to have class is equal row row-cols3 and g-2. Then we're going to have another div here, and this div is going to have a class equals to col. Okay, and finally, we're going to have another div that is going to have a class equals p-3 border. Okay, so this here is going to be a row, and we're going to have each card to be a column. So what we can do here now is say that for note in notes, we're going to have in here, let's add a title. So it's going to have here note.title. And then let's end the for here. And let's leave it for now like this. So we can remove this. Okay, let's check out. Amazing. This would look a little bit better if we could display some of the text of a note but not all of it. We can use the truncatechars function to do this. Let's try it out. So in here, let's add note.text, and then with the pipe, truncatechars. Let's just leave it at 10. So this is going to display 10 characters. So let's try it out. And there you go. So what's happening here is that Django is taking the text and just displaying the first 10 characters plus the three dots. It looks a little bit better, doesn't it? Okay, so it's still missing a couple of things, so we can't really access all the details of that particular note. So we're almost there. First, let's give a name to the detail URLs as well. So let's go back. Urls.py and then in here, let's add name is equal to notes.detail. Okay, so now we can go back, and in the title, we can add the link. So it's going to be an a with href is equal to the url, and then notes.detail. Let's pass this to here. It's still missing something. So we also need to pass here the pk. So the pk is going to be the note.id. Pretty simple. We can also add some classes here just to make it a little bit prettier. So let's pass class is equals to text-dark, and text-decoration-non. Okay. Reorganizing, that's it. Let's try it out. Let's go back, refresh, and you can see here that now we have a link to the specific note. But now we're still missing some details style here. So let's go back. Notes_details, and let's just add here a div. This should be in here. And on this div, let's add a class border. Let's make it round. And just add some style on the h1, so my equals 5. Okay, I think we're done here. Let's go back. Yeah, so all done. Now you have style and dynamically generated links. How amazing was that?

### Chapter 5 Quiz

#### Question 1 of 4
Where should you keep your static files?

- in the home folder
- in the smartnotes folder
- in their own folder
    Correct ✅

#### Question 2 of 4
How can you tell Django that the following html code will be using the static files?

```html
<html>
     <h1> These are the notes:</h1>
     <ul>
          {% for note in notes %}
               <li>{{note.title}}</li>
          {% endfor %}
     </ul>
</html>
```
- by adding {% load static %} to the top of the html code
    Correct ✅
- by adding {{ load static }} to the top of the html code
- by adding {( load static )} to the top of the html code

#### Question 3 of 4

Which function tells Django to display part of a note?

- the textfield function
- the charField function
- the truncatechars function
    Correct ✅

#### Question 4 of 4
Where are the basics of your html defined?

- in the notes_form.html template
- in the notes_detail.html template
- in the base.html template
    Correct ✅
- in the authorized.html template

## 6. Django Forms: Validation Shouldn’t Be Hard

### Create a webpage

Whenever we're building a system, there is a couple of common operations that we should support for every model we create. These are the create, read, update and delete or CRUD operations. These are the minimal operations that a system should typically support. So far regarding the notes model, we implemented the retrieve method by having an endpoint to get the details of a particular note. To fully support the notes model, we need to handle all the other three operations as well. Now we're going to learn how to implement a create method. Let's go back to notes, views.py and in here, let's import, well, I hope you guessed it, CreateView. Once we have this, we can actually start our new class. So class NotesCreateView that inherits from CreateView, and we're going to need three things here. So model equals to Notes. Fields, which is going to be title, and text. And finally, a success_url that is going to be the /smart/notes, which is our list endpoint. Let's understand what's going on here. First the model. So the endpoint understands what it's regarding to. Then the fields would be the attributes from the model that we allow a user to fill. Since we don't need to pass a created add field, we just define it as title and text. Finally, we want to redirect the user to the list of existing notes so they can see the note they just created. This is the success_url attribute here. And that's it. That's all we need to do in this class. Now we can add the endpoint to the urls.py file, the same way we did to every other endpoint so far. So in here, let's add path. Then notes/new. And then we can call view.NotesCreateView.as_view. And let's not forget to pass a name to it. So notes.new. And a comma here. Okay, so the last thing that's missing is the template. So let's create it. Let's call it notes_form.html. Okay, so let's use the default template. So extends base.html. And then the block content. And finally, the endblock. Okay, so now we can start. To send information back to the server, we'll need a form tag from the HTML. So let's add this here. Okay, so in the form, we can do action is equal to, we're going to use the method url, and then notes.new, which is the endpoint we just created. And also, the method here needs to be POST because we're sending information back to the server. Okay, so now what we need is to allow a user to pass back the information we define on our endpoint: title and text. How do we do that? Well, this can't be more simple. In here, we can do double curly brackets. Then form and that's it. Want to see what happens here? Let's go back to the browser, and try out our new endpoint. So in here, we can open the inspector element, and you can see here that in the body, we have a form. And the form is actually passed down to the HTML as two label tags and one input tag, and one text area. This is because Django already knows which type of data each attribute expects. Thus it creates an appropriate HTML tag to receive it. Well, we're still missing the Submit button, so let's add that. So in here, let's add button of type submit. The class is going to be btn btn-primary. Let's add some vertical alignment. Submit. That's it. Now we have everything we need in place. That is basically all we have to do to have an endpoint to create a new node.

### Understanding how Django handles security in POSTs

We did everything we needed to do to implement the create endpoint, but if you try to create a new note, you'll notice that it will actually return a 403 error, meaning that we are forbidden to do this action. Well, we're actually missing one less thing to our form. So if we go here, we can add curly brackets, percentage, and then a csrf_token. And that's it. So let's try again. I can go back, refresh this page, so this is a new note. It worked! Let's submit, and yes, indeed it works. You're probably wondering, what is this magic that was missing? This is a **CSRF token, that stands for cross-site request forgery**. What happens here is that every time a browser requests a webpage that has a form, Django will send a unique token to that browser. This token will be securely kept and no other website can access it. When the user sends back a form, it will also send back the token, allowing Django to know that this request is coming from a legit user. Django will then process the request and return the appropriate response. However, if for some reason, a third-party have access to the user credentials, when they try to make the request from another browser, they won't have the token, so Django understand that this request is coming from an unreliable source and will not process the request, thus, preventing this type of attack. As you can see, this is an additional layer of security that Django is adding to your website with just a small line of code. Beyond the numerous features that allow you to speed up the process of creating a website, this security features are a big part of why developers choose Django to work with.

### Django forms: Powerful validation with minimal work

Adding a new endpoint was nice and easy but now it's time to consider more complex scenarios. Model forms are the best way of doing this in Django. Let's check it out. First, we're going to create a file called forms, and inside our notes app. Okay, so in here, let's add from django import forms. And from .models import Notes. With this, we can create a new class called NotesForm that's going to inherit from forms.ModelForm. And inside this class, we're going to create a new class Meta. Okay, that's going to receive model, which is Notes, and fields, just like we added on the class-based view for createView. So title, and text. Okay, with this, we can come back to the views.py file, and in here, instead of passing the fields, we're going to pass a form_class that's going to be our NotesForm. We also need to import it. So from .forms import NotesForm. Okay, so far what we did will result in exactly the same behavior as we have so far but the form will give us power to do much more. For instance, let's say that we want to add a specific behavior that just allow us to add notes that contains the word Django in the title. Let's go back to the forms. All we need to do here is add a new method called def clean, and the field, we want to add a validation. In this case, title. So in here, we can get the title from the cleaned_data, which is a dictionary. The cleaned_data is returned by the form, and is particularly useful for fields with strong validation. Like for instance, emails. In this scenario, it will be exactly the same value as the user passed. With this, we can actually start our validation. So if Django not in title, we're going to raise a ValidationError with a message. We only accept notes about Django. If everything goes well, we just return title. Okay, so we have here the ValidationError already imported. And we can try this out. Let's go back to our browser. Let's add a new note. A new note, which is a test. Let's submit this, and we have our error. We only accept notes about Django. Okay, so this is pretty cool. Django already injects the validation errors directly to our HTML. You can see here, we have a ul that has a class ErrorList and a list of errors. This is pretty cool but we can't really control the design. So let's change this a little bit so we have a really good validation error here. We can go back and on our style.css, we can add here that the ul.errorlist is not going to be displayed. So we're going to control this. Then on the form template, we're going to add an if block. So if our form have errors, we're going to do something. So let's close the if so we don't forget this. So endif. Then in here, we're going to add a div, which is a class of type alert, and let's make it an alert-danger. Some vertical spacing. And in here, what we can do is pass the form.errors.title, and as_text. Okay, let's go back. Let's refresh this. And if I add a new node, which is a test, try to submit this, and there you go. Now you can add validations in any field you want with just a couple of additional methods in a form class.

### Django forms are useful for layout as well!

This form we just created, it's starting to look nice, but there's work to do here. It's still missing some style. One alternative would be to build the whole form by hand with each label and each input, everything. As you can see, this is not such a fun activity once you have a form already laid out for you, right? Forms are amazing because not only they add validation, but also, because you can quickly add styles to it. First, let's say that we want to change the labels of our form. Title and texts are the words we use in the backend, but that doesn't mean that it looks so good for our users. What we can do is, on the class meta, add a field called labels, and in here, let's add text, it's going to be, write your thoughts here. Let's say this. Now if we go back and refresh this, as you can see, we are controlling the UX directly from our backend. We can also add an attribute widget to inject CSS classes directly to the form. Let's go back and add a new field code, widgets, and then, in here, let's add title, and this is going to be a forms text input, and then we're going to pass attributes. This is going to be a dictionary and the class is going to be form control and some vertical spacing as usual. We can do a similar thing with the text. So text, this on the other hand is not a text input, but a text area, and also, we're going to add, again, attributes, and let's add the same classes. Class is equal to form control, and this. Let's go back and check it out. Refresh. Yeah. You can see now that controlling the frontend in an easy and accessible way is also a main advantage of using model forms. All this without ever changing the original template. Nice and easy.

### Chapter 6 Quiz

#### Question 1 of 4

If you want to label your text box to say "Place notes here" instead of "Text", how should you modify the following code?

```python
class NotesForm(forms.ModelForm):
     class Meta:
          model = Notes
          fields = ('title', 'text')
```

```python
# Correct ✅
class NotesForm(forms.ModelForm):
     class Meta:
          model = Notes
          fields = ('title', 'text')
          labels = {
               'text': 'Place notes here:'
          }
```

```python

class NotesForm(forms.ModelForm):
     class Meta:
          model = Notes
          fields = ('title', 'text')
          labels = {
               'title': 'Place notes here:'
          }
```

```python
class NotesForm(forms.ModelForm):
     class Meta:
          model = Notes
          fields = ('title', 'text')
          labels = {
                'Place notes here:'
          }
```

#### Question 2 of 4

In the `views.py` file, what can be passed instead of the fields, as shown in the following code snippet, to allow for more powerful validation?

```python
class NotesCreateView(CreateView):
     model = Notes
     fields = ['title', 'text']
     success_url = '/smart/notes'
```

- a context_object_name
- a form_class
    Correct ✅
- a template_name

#### Question 3 of 4

Every time a browser requests a webpage that has a form, what will Django send to that browser?

- a password
- a token
Correct ✅
- a code
- a form

#### Question 4 of 4

If you are sending information back to the server, what should your method be in the following form tag?

```html
<form action="{% url 'notes.new' %}" method= >
     {{ form}}
</form>
```

- `method='PUT'`
- `method='POST'`
    Correct ✅
- `method='DELETE'`
- `method='GET'`

## 7. Working with Existing Data

### The U in the CRUD: Updating data

Okay, so now we have the create end point, it's time to create the view update endpoint. Let's go back to the views file on notes. And on here, we're going to also add UpdateView. Now we can add a new class, NotesUpdateView that inherits from UpdateView. And we actually just need to copy these from the CreateView and paste it here. That's it, that's all we need to do. The only thing still missing are the URLs. So what we can do is go back here, we can copy and paste the details view, and then add here a /edit on the end point, change the class where is this originating to, and the name. That's it, that's all we need to do. If we go back to the notes now, get the first note, and then add a /edit at the end, you can see that we have our form here and we have the fields already filled in with the data from that particular note. So if we try something, just save and try again. Uh oh, it didn't work. Okay, so let's check it out. What is going on? If you go to our template, if you notice here, we're actually hard coding which URL the form should be sent to. We don't actually need this. The form is smart enough to know where to send this to. So let's get rid of this. Let's go back, edit, and then submit it. If we see now, our note was edited. That's it. So editing basically comes for free after you implemented the create end point. We can style this page a little bit, so let's go to the template. We can add a cancel button that will return from this page if the user changed their mind. So it can go to a href is going to be the function that have URL, and then let's go back to notes.list. We still need some class here, so let's type btn and then btn-secondary, and then Cancel. We can also go back to the details. In here we can create a new button that will take us to the edit page, so a href, then curly brackets, percentage url, notes.update, and then pk is equal to note.id. Let's add some class here as well, so btn and btn-secondary, Edit. Okay, let's try this out. If we go back here and this note, we now have the button edit. We can actually edit here and then we can actually cancel our submit. There you go. Now you have a full cycle between list, detail, and edit with just a couple lines of code.

### The D in the CRUD: Deleting data

So it's time to think about the last operation from the crude operations, deleting data. Let's start as usual. Let's go back to the views and from here, we're going to add actually from Django views generic edit, let's important delete view. The delete endpoint is even simpler than all the endpoints we created until now. We can add a new class notes delete view that inherits from delete view, and we actually just need the model and a success URL. Once more, the end point URL needs to be added to the URL's file. So let's go back here. Let's copy this and instead of edit, let's call this delete. Let's change the class here and the name. No, we need to create a template to confirm if the user wants to delete a particular note. Let's go here and add a new one called notes underline delete dot HTML. So let's start with the basics. So extends base dot HTML then block. This is also going to be a form. So let's add form and the methods going to be post. Since this is a form we can forget about the CSRF underlying token and then in here, we're going to add a message. Are you sure you want to delete? And then let's add notes dot title, let's add quotes here and then another message saying that this action actually can't be undone. And finally, an input button type is equal submit and the class is going to be BTN BTN danger. So it can be a nice red and value it's going to be confirm. Since we already have our template, we can go back to the details and add yet one more button here called that will lead us to the delete. Let's make it red as well. Okay, it's time to try it out. Let's go back to one particular note. Now we have the delete button and if we click here, oh-oh, okay. We're getting again a template does not exist. We can see here that while it was loading the template, it was looking for a template with the name notes, notes, confirm delete. So we have two alternatives here. One is to change the name of our template to match the template that Django is expecting. I prefer to usually add the template name to avoid having to remember which template is related to which endpoint. So we can come back here to the views and add a template name. This name is also very similar to the other template names that we have. So, in my opinion, this is a little bit better, but you can choose whatever you prefer. Let's try again. Let's delete this. Okay, we have our message, let's confirm and there you go, the note was deleted.

### Chapter 7 Quiz

#### Question 1 of 2
What must be removed from your template for the form to work successfully?

```html
<form action="{% url 'notes.new' %}" method='POST'>{% csrf_token %}
     {{ form.as_p }}
     <button type="submit" class="btn-primary my-5">Submit</button>
</form>
```

- `action="{% url 'notes.new' %}"`
     Correct ✅
- `method='POST'>{% csrf_token %}`
- `{{ form.as_p }}`

#### Question 2 of 2
When you add the following class to your views page, what else is needed?
class NotesDeleteView(DeleteView):

- the success url and the form class
- the model and the form class
- the model and the success url
     Correct ✅
- the model, the success url, and the form class
