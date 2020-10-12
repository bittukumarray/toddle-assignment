# Toddle-Backend-Assignment

## Dependencies requirements:

These all commands are for Ubuntu 18.04

- Install Django - type below command in a terminal of your ubuntu

  - ```bash
    pip3 install Django
    ```

- Install Django Rest Framework - type the below command to install it into your terminal

  - ```bash
    pip3 install djangorestframework
    ```

- Install PIL and PILLOW - type the below command to install it into your terminal

  - ```bash
    pip3 install Pillow==2.2.1
    ```

- install resizeimage - type the below command to install it into your terminal

  - ```bash
    pip3 install python-resize-image
    ```

- Install boto3 - type the below command to install it into your terminal

  - ```bash
    pip3 install boto3
    ```

## APIs, parameters and output format

All the request and response input output will be in json format

- Signup API

  API url: This is a POST method

  - ```
    http://localhost:8000/auth/signup/
    ```

  Body Parameters : in JSON format, below is the body structure

  - ```json
    {
        "username":"username",
        "password":"123456"
    }
    ```

  Output :

  - ```json
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMjU2Njg5NywianRpIjoiZjM1ZmY2NzI3YmI2NDUxZTkzNzBjNGY3M2E3OTIzZmEiLCJ1c2VyX2lkIjoxMH0.nz5ipqYJq2_NrUDtX4OaEUwBivxCpd7NbMAehAMYOcs",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyNDgwNzk3LCJqdGkiOiI0NWNiODVkOWExOWY0YjAzYTFhYzJiZjlhNmQ4YWRmOSIsInVzZXJfaWQiOjEwfQ.amm5otbHLN95YSxBydkzrCDNjPf41H1D-FJ2lN4imF0"
    }
    ```

    There will be an access token which will be used to verify whether the user is authenticated or not. and there will be an refresh token too, which can be use to get access token again if the access token has expired.

    The access token expires after 5 minutes every time it gets renew, so whenever it gets expired, we can make another request with below details to get the access token

- Getting access Token from Refresh token API:

  API url : POST request:

  - ```
    http://localhost:8000/auth/login/refresh/
    ```

    

  Body Parameters:

  - ```json
    {  "refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMjU2Njg5NywianRpIjoiZjM1ZmY2NzI3YmI2NDUxZTkzNzBjNGY3M2E3OTIzZmEiLCJ1c2VyX2lkIjoxMH0.nz5ipqYJq2_NrUDtX4OaEUwBivxCpd7NbMAehAMYOcs"
    }
    ```

  Output:

  - ```json
    {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyNDgxNTQ1LCJqdGkiOiJkMDMyNTQ1ODBmMWY0NTcwYTAwMzIxMzdlZmMzMzY2OSIsInVzZXJfaWQiOjEwfQ.0c645IIZVV3rh4dA0A-oB8YCD8o-5aJl7Bp-6p5QQYc"
    }
    ```

    We get access token which can be used to make requests for protected resources.

- Login API: 

  API url: POST request

  - ​	

    ```
    http://localhost:8000/auth/login/
    ```

    

  Body parameters:

  - ​	

    ```json
    {
        "username":"username",
        "password":"123456"
    }
    ```

  Output:

  - ​	

    ```json
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMjU2Nzg0NywianRpIjoiMGIyNDY0NmE5MWQwNDNjMjkwZGYxZGQ1NDU5MjNiZTYiLCJ1c2VyX2lkIjo5fQ.exD5ivt6z510yIZx1gHixGKyLkLNw-85z0nNgbLNkps",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyNDgxNzQ3LCJqdGkiOiJiMDMzYmI4NmI5Yzc0ZDg4ODU0ZGE1MjY5MjdlNGRlMyIsInVzZXJfaWQiOjl9.TTeI_m6h36E_0rCsX08_7FMoF7wN9ZUuwF2j1o-N91Y"
    }
    ```

- Create Survey API:

  API url: POST request and user needs to be authenticated for it, they will have to pass the JWT token in header

  - ​	

    ```
    http://localhost:8000/survey/create/
    ```

  Body Parameters:

  - ```json
    {
        "survey_name":"surveyName",
        "questions":[
            {
                "title":"are you good?"
            },
            {
                "title":"Do you play cricket?"
            },
            {
                "title":"are you good at math?"
            },
            {
                "title":"Do you play cricket?"
            }
        ]
    }
    ```

    While requesting, there will be a survey_name field and then there will be a list of questions and in each questions there will be a field title which holds the question

  Headers parameters:

  - ```
    
    Authorization = Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyNDgzMzY2LCJqdGkiOiJkMWI5NjQ4MmQ2NjQ0NTUzOWVkYTdmNWRhNzU1ZWZjYyIsInVzZXJfaWQiOjl9.tS3l-415WkDsFWb1j0pvfsXnrnAcsaRExIUBT2wbYMY
    
    ```

    That is, in  header pass, Authorization equal to Bearer token

  

  Output:

  - ```json
    {
        "survey_id": 10,
        "questions": [
            {
                "Q_id": 24,
                "Q_title": "are you good?"
            },
            {
                "Q_id": 25,
                "Q_title": "Do you play cricket?"
            },
            {
                "Q_id": 26,
                "Q_title": "are you good at math?"
            },
            {
                "Q_id": 27,
                "Q_title": "Do you play cricket?"
            }
        ]
    }
    ```

    And the survey gets created in database.

- Take Survey API:

  API url: POST request and user needs to be authenticated for it, they will have to pass the JWT token in header

  - ```
    http://localhost:8000/survey/take/
    ```

  Body Parameters:

  - ```json
    {
        "survey_id":"1",
        "questions":[
            {
                "question_id":1,
                "ans_given":true
            },
            {
                "question_id":2,
                "ans_given":false
            }
            
        ]
    }
    ```

    We will have to pass survey id and then a list of all the questions which user answered with question id and answer given(true/false)

    

  Headers parameters:

  - ```
    Authorization = Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyNDgzMzY2LCJqdGkiOiJkMWI5NjQ4MmQ2NjQ0NTUzOWVkYTdmNWRhNzU1ZWZjYyIsInVzZXJfaWQiOjl9.tS3l-415WkDsFWb1j0pvfsXnrnAcsaRExIUBT2wbYMY
    
    ```

    That is, in  header pass, Authorization equal to Bearer token

  Output:

  - ```json
    {
        "msg": "You took survey successfully"
    }
    ```

    and the database gets updated with all the given answers.

- Show survey result API:

  API url: GET request and user needs to be authenticated for it, they will have to pass the JWT token in header

  - ```json
    http://localhost:8000/survey/get-result/<survey_id>
    i.e http://localhost:8000/survey/get-result/4
    ```

  Headers Parameters:

  - ```
    Authorization = Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyNDgzMzY2LCJqdGkiOiJkMWI5NjQ4MmQ2NjQ0NTUzOWVkYTdmNWRhNzU1ZWZjYyIsInVzZXJfaWQiOjl9.tS3l-415WkDsFWb1j0pvfsXnrnAcsaRExIUBT2wbYMY
    ```

    That is, in  header pass, Authorization equal to Bearer token

  Output:

  - ```json
    {
        "survey_id": 1,
        "questions": [
            {
                "Q_id": 1,
                "Q_title": "Ravana was a coward",
                "true_resp": 2,
                "false_resp": 1
            },
            {
                "Q_id": 2,
                "Q_title": "Ravana was a brave man",
                "true_resp": 0,
                "false_resp": 3
            }
        ]
    }
    ```

    As a output we will get survey id and the list of all questions along with the no. of people chose true response and the number of people chose False response.



- Image Resized API(Bonus):

  API url: POST request

  - ```
    http://localhost:8000/auth/thumbnail/
    ```

  Body parameters:

  - ```json
    {
        "url":"https://ccbucket-12345.s3.ap-south-1.amazonaws.com/onions.jpeg"
    }
    ```

    That is, in body the user should pass url of an image and also it does not require user to be authenticated

  Output:

  - ```json
    {
        "resized_url": "https://toddle-bucket-resized.s3.ap-south-1.amazonaws.com/onions.jpeg"
    }
    ```

    In response, we will get resized image url, I am putting resized images to AWS

​			