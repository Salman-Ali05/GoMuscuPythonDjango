# GoMuscuPythonDjango
4th year full stack project

when pull project :
1. create your env : python -m venv GoMuscuYourName
2. installations : pip install django, pip install djangorestframework
3. to run the server (be at the root) : python manage.py runserver

If updates on database : 
=> python manage.py makemigrations
=> python manage.py migrate

To test C(R)UD methods in POSTMAN :
create a super user : (you can try with this user :
{
    "username": "user"
    ,
    "password": "user"
}
and this url in POST mehtod : http://127.0.0.1:8000/token/
,
retrieve the "access" value)
python manage.py createsuperuser

Testing methods : 
- set in "Authorization", Bearer token, put the access value in it
- then make a simple query such as :
  - POST Example :http://127.0.0.1:8000/muscle/ ; Body : {"muscleName" : "MuscleNameYouWannaAdd"}