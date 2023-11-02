# AZKAR-translation-and-Transliteration
 AZKAR-translation-and-Transliteration thai and english

![Project Logo]("logo1.png") 

## Table of Contents
- [About](#about)
- [Features](#features)
- [Usage](#usage)
- [Setting Up Django Project](#setting-up-django-project)

## About
AZKAR is a web application that provides translations, and transliterations,  for various Islamic supplications (Adhkar) in english and thai languages. It offers a user-friendly interface to access morning and evening Adhkar in two languages, fostering spiritual growth and understanding. (This wep app is not yet complete as intended. Inshallah will continue to improve.)

## Features
- Access morning and evening Adhkar (supplications) in Arabic, transliteration, and translation.
- Explore Adhkar in two languages to cater to a diverse user base.
- Connect with the project creators through social media links.

## Setting Up Django Project
To set up your Django project, follow these steps:
1. Install Django using pip:
    ```bash
    pip install django
    ```
2. Create a new Django project named "myweb":
    ```bash
    django-admin startproject myweb
    ```
3. Navigate into the "myweb" directory:
    ```bash
    cd myweb
    ```
4. Create a new app within the project named "myweb":
    ```bash
    django-admin startapp myweb
    ```
5. Create the database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```
7. Information provided through the login and contact forms will be stored in the database.

Please make sure to replace `myweb` with your preferred project and app names.

## Usage

1. Visit the AZKAR web application at http://localhost:8000/ (or your hosted domain).

2. Choose your preferred language to access morning and evening Adhkar.

3. Explore the supplications, translations, and transliterations provided.

4. Connect with the project creators through social media links for any inquiries or feedback.

rovides an overview of your project, how to get started, usage instructions, contribution guidelines, and licensing information. You can further customize it to suit your project's specific needs.

