# About The project
  This is simple blog web application which includes feature to add multiple blog post 

#How to run this project
1. Create a virtual environment and
  Linux- python3 -m env yourenvname
  
2. Activatng Virtual environment and install the project dependecies
   #source projectenv/bin/activate.
   
   #intall the following required dependencies to run the project
   pip install django pillow 

3. How to run the project

  Once in project directory, please use the following commands.
  
  python manage.py collectstatic 
  python manage.py makemigrations #This will make all models fields and attributes ready to be moved to the database
  python manage.py migrate #Actual migration to the database
  
  finally run, 
  python manage.py runserver
  
  
  
   
  
