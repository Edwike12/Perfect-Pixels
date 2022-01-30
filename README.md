#  project name:
PERFECT-PIXELS  gallery app


# AUTHOR
EDWIKE NYAUNCHO


## Project description
Perfect-Pxels is a photo gallery web application to showcase beautiful pictures. Users get can view photos uploaded by admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories.


## USER STORY
-The user is able to view images in the home page

-User can view the categories,location and description of the image

-User can also search images based on categories

-can also add image from the website

-Admin can upload images from a django dashboard


## Setup Instructions and Installation
For the application to run, you have to install:

- python3.8

- Django framework

- virtual environment

- Postgres

Setup and Installation
- open terminal

- git clone this repository https://github.com/Edwike12/Perfect-Pixels

- use a code editor

- Actvate the virtual env 

        -$ source venv/bin/activate

- Install dependancies 

        -$ pip install -r requirements.txt

- Create a database

        -psql

        -CREATE DATABASE gallery;

- .env file- create  .env file and hve the following filling where appropriate:

            -SECRET_KEY = '<Secret_key>'

            -DBNAME = 'gallery'

            -USER = '<Username>'

            -PASSWORD = '<password>'

            -DEBUG = True

- Run initial migration

        -$ python3.8 manage.py makemigrations gallery

        -$ python3.8 manage.py migrate

- Run the app

        -$ python3.8 manage.py runserver


## Technologies used
- python3.8

- Django

- Html, Css and Bootstrap

- postgres sql

- Heroku


## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug


## Development 
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


### Testing Application
-To run the tests for the class files:

    -$ python3.6 manage.py test




### contact information
Feel free to reach out:

Email: nyaunchoedwike@gmail.com


### License

*MIT*
Copyright (c) 2022 **EDWIKE NYAUNCHO**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

