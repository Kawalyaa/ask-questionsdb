
[![Build Status](https://travis-ci.org/Kawalyaa/ask-questionsdb.svg?branch=simple5)](https://travis-ci.org/Kawalyaa/ask-questionsdb)  [![Coverage Status](https://coveralls.io/repos/github/Kawalyaa/ask-questionsdb/badge.svg?branch=simple5)](https://coveralls.io/github/Kawalyaa/ask-questionsdb?branch=master) [![Maintainability](https://api.codeclimate.com/v1/badges/a03f4007df3278801558/maintainability)](https://codeclimate.com/github/Kawalyaa/ask-questionsdb/maintainability)

# Ask-Questions

Ask-questions is a platform which enables people to ask question and get answers

## Built with

* python 3
* flask_restful

## Features

  1. User can create an account and login
  1. User can post questions
  1. user can delete questions they post
  1. User can post answers
  1. Users can view answers to the questions

## Installing

Step 1

### Clone this repository

```
$ git clone https://github.com/Kawalyaa/ask-questionsdb.git

$ cd ask-questionsdb

```

Create and activate the virtual environment

```
$ python3 -m venv venv

$ source venv/bin/activate

```

Install project dependencies

```
pip install -r requirements.txt

```

Step 2

### Setup Databases

Go to postgres terminal and do the following

Main Database

```
# CREATE DATABASE database_name ;
```

Testing Database

```
# CREATE DATABASE test_database ;
```

Step 3

### Storing the environmental variables

```
export FLASK_APP="run.py"
export FLASK_ENV="development"
export DATABASE_URL="your database url"
export DATABASE_TEST_URL="your database url for testing"
export SECRETE="your secrete key"
```

step 4

### Running the application

```
$ flask run
```

Step 5

### Testing the application

```
$ nosetests app/tests
```

## API-ENDPOINTS

 Method | Endpoints | Functionality |
 ------ | --------- | -------------: |
 POST | api/v2/auth/signup | creat User account |
 POST | api/v2/auth/login | A user can login |
 POST | api/v2/auth/logout | A user can logout |
 |   Questions endpoints                      ||
 POST | api/v2/question | A user can post question |
 GET | api/v2/question | A user can view all the questions |
 GET | api/v2/question/<int:post_id> | A user can view a single question |
 PUT | api/v2/question/<int:post_id> | A user can edit a question
 DELETE | api/v2/question/<int:post_id> | A user can delete a question

## Author

*Kawalya Andrew*
