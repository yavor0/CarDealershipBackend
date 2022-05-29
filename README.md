# Instructions
1. Add mysql login information in the USER environment variables. There has to be one `MYSQL_USERNAME` and `MYSQL_PASSWORD` variable with the correct values respectively. 
2. Create a database called `dealership` (**lowercase**)
3. Run these commands in the folder with `Pipfile`:\
 -- `pipenv install`\
 -- `pipenv run python manage.py migrate`
4. To run the backend: `pipenv run python manage.py runserver`
 
 # Supported endpoints
 `/dealership/cars` - information for all cars\
 `/dealership/cars/<id>` - information for a specific car by its id
 # In development:
 Car evaluation endpoint
