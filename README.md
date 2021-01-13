# Intro to API at Hack the North

Workshop recording [here](https://www.youtube.com/watch?v=Fpc7Lp5oEkU&feature=youtu.be&ab_channel=HacktheNorth)

Workshop resources, such as powerpoint slides and additional links, [here](https://drive.google.com/drive/folders/1wET21sxRq5IKgV6X_ln8H2rmP81aZqXk?usp=sharing)

### Before beginning this workshop, please ensure that you have installed Python3 and an IDE that supports Python development, such as Visual Studio Code or PyCharm. 

You can check whether you have Python3 installed by starting a terminal session and typing
```
python3 -v
```

* [Python3](https://realpython.com/installing-python/)

* [Visual Studio Code](https://code.visualstudio.com/)

* [PyCharm](https://www.jetbrains.com/pycharm/)

### Preparation

1. Clone this repo by copying https://github.com/yccgabby/htn-api-workshop.git into your clipboard and set up your local copy of the repository

* [Visual studio code](https://code.visualstudio.com/docs/editor/versioncontrol)

* [PyCharm](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html)

2. Once you've opened up the repository on your IDE, download all necessary packages by starting a terminal session and typing
```
pip install -r requirements.txt
```
3. Open up http://swapi.py4e.com/ and start working through part 1 of the workshop! You will work on playground.py and can run it by typing in the terminal session 
```
python3 playground.py
```
4. For part 2 of the workshop, you will be interfacing with api.py and the templates folder to build out a simple web app with a server-side api. To start the Flask server and launch the app in your browser, type in the terminal 
```
python3 api.py
```
5. You can use the files in the completed folder to work through challenging parts of the workshop and check over your work. 




## FAQ

**Question:** What is the difference between backend and database?

**Answer:** Database management is a part of building a backend system for your application! In order to store data, you need a database that your system can communicate with to send and retreive information on behalf of the end user. Another part of a backend system would be constructing the API that your client device, such as a computer or mobile device, uses to connect to the database.

##
**Question:** What is the difference between a REST API and an API?

**Answer:** API, otherwise known as Application Program Interface, is a general term for constructing an intermediary layer that acts as a set of rules that a client application must follow to access data and files stored remotely. REST is a design methodology, by far the most popular one, that expands on the concept of an API and employs additional design patterns such as CRUD operations and HTTP protocols to abstract the process and make data transferrable across different technology stacks. 

##
**Question:** How is an API different from a library?

**Answer:** A library in itself is not necessary an API, and merely consists of useful functions that can further abstract the coding process in the perspective of a developer using the library. An API can be made of several libraries, although it is usually a 1:1 relationship, and specifically acts as an interface between applications to enable communication. 

##
**Question:** HTTP vs HTTPS

**Answer:** HTTP is unsecured, while HTTPS is secured. HTTPS uses SSL (secure socket layer), requires domain validation, and encrypts data before sending it over the interweb. HTTPS is almost always preferred for a production-ready application since it is safer for the end user. 

##
**Question:** What does an API endpoint mean?

**Answer:** In the context of a REST API, an endpoint represents the url of which a resource is stored on, for example, http://swapi.py4e.com/api/people/. This is an endpoint that retrieves all the people resources from the Star Wars API. 

##
**Question:** Do APIs always return JSONs?

**Answer:** An API does not have to return JSONs. APIs have long existed before the creation of JSON; however, JSON is a preferred data type for many modern applications because of its parsability to other computer languages. REST APIs standardizes the usage of JSON, however APIs can also send resources of other types such as HTML files and videos. 

##
**Question:** What's the point of using a virtualenv?

**Answer:** A virtualenv is a virtual environment where you can run code within. It is used to tailor an environment to your project's needs. If you have multiple projects on your computer that require, for example, different versions of Python, configuring a virtualenv is the best way to contain each project's package dependencies.

##
**Question:** Error: git not recognized

**Answer:** Make sure you have git installed on your computer: [here's](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) an awesome link to install git and ensure your installation is in the right path.

##
**Question:** Error: python/ python3/ pip not recognized

**Answer:** This means that you've either not installed Python yet, or your computer can't find the installation. [Here's](https://realpython.com/installing-python/) an awesome link to help you debug!

##
**Question:** ModuleNotFoundError: No module named 'requests' or unable to import flask

**Answer:** This means you've either not installed using 'pip install -r requirements.txt' in your project folder on the terminal, or the packages were installed elsewhere. This [link](https://stackoverflow.com/questions/7225900/how-to-install-packages-using-pip-according-to-the-requirements-txt-file-from-a) may help!

##
**Question:** SSLModule is not available

**Answer:** This [link](https://stackoverflow.com/questions/41328451/ssl-module-in-python-is-not-available-when-installing-package-with-pip3) may help!

