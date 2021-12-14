
***
[Watch below for the English version](#epic_events-en) 
***

# Projet Epic Events services (fr)

***

Ce projet est entièrement codé en [python 3.10](https://www.python.org/downloads/release/python-3100/)

Il est réalisé dans le cadre d'une formation sur le site [OpenClassrooms](https://openclassrooms.com/fr/).
Ce projet consiste en la réalisation d'un crm sécurisé utilisant django ORM. Il dispose d'une API REST créer à l'aide de REST Framework et une interface utilisateur simple réalisé avec le site d'aministration django.

## Table des matières
1. [Informations génerales](#informations-generales)
2. [Installation/usage](#installation-usage)

***

## Informations Generales

Ce projet utilise le framework de developpement web [django](https://docs.djangoproject.com/fr/4.0/) ainsi que le framework [django-rest](https://www.django-rest-framework.org/) pour la réalisation de la partie API. Ce projet utilise une base de donnée [PostgreSQL](https://www.postgresql.org/).
L'API du projet utilise un système d'authentification basé sur les **J**son **W**eb **T**oken ([JWT](https://jwt.io/)). La mise en oeuvre de cette authentification se fait à l'aide du package [simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html). Pour utiliser l'API, [une documentation](https://documenter.getpostman.com/view/17930773/UVR5spcW) dédiée est à votre disposition.


## Installation Usage

Pour utiliser ce projet il est nécéssaire de bénéficier d'une version de python au moins égale à 3.10, car ce projet utilise le systeme de [pattern matching](https://www.python.org/dev/peps/pep-0636/) disponible à partir de python 3.10.

Il est aussi nécéssaire d'installer PostgreSQL sur votre machine et de configurer une base de donnée qui pourra être utilisée par le projet, [cliquez ici](https://www.postgresql.org/docs/) pour afficher la documentation de PostgreSQL.

Il est possible de cloner le projet depuis github grâce à la commande suivante :

```
$ git clone https://github.com/npaillasson/epic_events_services.git
```

Rendez-vous ensuite à la racine du projet. Il est ensuite recommandé de créer un environement virtuel avec venv afin d'installer tous les packages et dépendances nécéssaires au fonctionnement du projet :

```
$ python3 -m venv env
```

Utilisez ensuite la commande suivante pour activer l'environnement :
```
$ source env/bin/activate
```

ou sous Windows:
```
> env\Scripts\activate
```

Vous pouvez ensuite installer les packages nécéssaire grâce à pip et au fichier requirements.txt à votre disposition à la racine du projet:
```
$ pip install -r requirements.txt
```

Avant de lancer le server, il est nécéssaire de renseigner votre base de donnée dans le fichier src/epic_events_services/settings.py du projet:
```
...
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": <database name>,
        "USER": <user>,
        "PASSWORD": "",
        "HOST": "",
        "PORT": "5432",
    }
}
...
```

Avant la première exécution du projet il est nécéssaire d'effectuer les migrations à l'aide des commandes suivantes:
```
$ python src/manage.py makemigrations
$ python src/manage.py migrate
```

Pour lancer le serveur exécuter la commande suivante :
```
$ python src/manage.py runserver
```

Vous pouvez ensuite aller sur le [site](http://127.0.0.1:8000/EpicEvents/CRM_acces/login/) (http://127.0.0.1:8000/EpicEvents/CRM_acces/login/)

Avant votre première connexion il est nécéssaire de créer un super-utilisateur à l'aide de la commande django:

```
$ python src/manage.py createsuperuser
```

Pour désactiver l'environnement virtuel, utilisez la commande suivante :
```
$ deactivate
```

Ou sous Windows:
```
> env\Scripts\deactivate
```

***
# Epic-events (en)
***


This project is entirely coded in [python 3.10](https://www.python.org/downloads/release/python-3100/)

It is realized within the framework of a training on the site [OpenClassrooms](https://openclassrooms.com/fr/).
This project consists in the realization of a secured crm using django ORM. It has a REST API created with the REST Framework and a simple user interface realized with the django administration site.


## Table of contents
1. [General information](#general-information)
2. [Installation/usage](#installation)

***

## General Information

This project uses the web development framework [django](https://docs.djangoproject.com/en/4.0/) as well as the framework [django-rest](https://www.django-rest-framework.org/) for the realization of the API part. This project uses a [PostgreSQL](https://www.postgresql.org/) database.
The API of the project uses an authentication system based on **J**son **W**eb **T**oken ([JWT](https://jwt.io/)). The implementation of this authentication is done using the [simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html) package. To use the API, [documentation](https://documenter.getpostman.com/view/17930773/UVR5spcW) is available.


## Installation

To use this project you need a version of python at least equal to 3.10, because this project uses the [pattern matching](https://www.python.org/dev/peps/pep-0636/) system available from python 3.10.

It is also necessary to install PostgreSQL on your machine and to configure a database that can be used by the project, [click here](https://www.postgresql.org/docs/) to display the PostgreSQL documentation.

To clone the project locally use the following command :

```
$ git clone https://github.com/npaillasson/epic_events_services.git
```

Then go to the root of the project, it is recommended to create a virtual environment with venv :

```
$ python3 -m venv env
```

To activate the virtual environment use :
```
$ source env/bin/activate
```

If you are on Windows use:
```
> env\Scripts\activate
```

To install the necessary packages use pip and the file requierements.txt:
```
$ pip install -r requirements.txt
```

Before launching the server, it is necessary to fill in your database in the file src/epic_events_services/settings.py of the project:
```
...
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": <database name>,
        "USER": <user>,
        "PASSWORD": "",
        "HOST": "",
        "PORT": "5432",
    }
}
...
```

Before the first execution of the project it is necessary to perform the migrations with the following commands:
```
$ python src/manage.py makemigrations
$ python src/manage.py migrate
```

To start the server run the following command:
```
$ python src/manage.py runserver
```

You can then go to the [site](http://127.0.0.1:8000/EpicEvents/CRM_acces/login/)(http://127.0.0.1:8000/EpicEvents/CRM_acces/login/)

Before your first connection it is necessary to create a super-user with the django command:
```
$ python src/manage.py createsuperuser
```

To deactivate the virtual environement use :
```
$ deactivate
```

If you are on Windows use:
```
> env\Scripts\deactivate
```


****