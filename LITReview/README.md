# P9_bchir_solayman

Summaries
---------

* General description
* Requirements
* Installation
* Run the script

General description
-------------

This application is an MVP for the website LITReview who allows registered users to ask a review on a book / article by creating a ticket.
Members of the site could respond to the ticket by giving a notation and remarks, called a review.
They can follow people of their choices to read their posts. The application was developed with Django framework 3.


Requirements
---------

This application uses the following packets:

* asgiref==3.4.1
* attrs==21.2.0
* coverage==6.2
* Django==3.2.7
* iniconfig==1.1.1
* packaging==21.3
* pluggy==1.0.0
* py==1.11.0
* pyparsing==3.0.6
* pytest==6.2.5
* pytest-cov==3.0.0
* pytest-splinter==3.3.1
* pytz==2021.1
* selenium==3.141.0
* six==1.16.0
* splinter==0.16.0
* sqlparse==0.4.2
* toml==0.10.2
* tomli==1.2.2
* urllib3==1.26.7


Installation
------------

First, you can download this project by :

clicking on « code » then « download ZIP »

or [click here to download it directly](https://github.com/Solayman-B/P4_bchir_solayman/archive/refs/heads/main.zip)

Unzip the file when the download is completed

You can also install [Git via this link](https://git-scm.com/downloads) and use :

    gh repo clone Solayman-B/P9_bchir_solayman


To use this application properly, you need to use [python3](https://www.python.org/downloads/)

Then you can create a virtual environment:

    python3 -m venv env # env is the name of the directory, but you can choose another one if you want

On Windows, run:

    env\Scripts\activate.bat

On Unix or macOS, run:

    source env/bin/activate

And to deactivate, simply use:

    deactivate

You can install all the required paquets with:

    pip install -r requirements.txt


Run
---

Go to the folder containing the project and use `python3 main.py runserver` then open your internet browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/
). You can now subscribe and log you in to use the website.


