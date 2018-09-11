# checkShnyfer

## Getting Started
Clone this project into the directory of your choice.

To run this project, you will need to activate the vitrual environment that goes along with this project. Open a command line in checkShnyfer directory and type ```.\Scripts\activate```. This will activate the virtual environment. 

**Please install all packages that will be used for this project inside of this environment.**

## Deploying Development Server
To run the server, cd into 'src' (There should be a manage.py file) and type ```py manage.py runserver```. This will start a deployment server at http://127.0.0.1:8000/ unless specified otherwise (```py manage.py runserver 8080```). The server automatically reloads code changes. __You do need to manually restart the server when files are added.__
 
 **You should see a “Congratulations!” page, with a rocket taking off. IF NOT LET ME KNOW!** 

 ## Making Changes

 ### To the Database
 If changes are made to the database run ```py manage.py migrate``` to make the changes to the database.

 ### More Questions
 Go to [this django project](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) for a full tutorial on how to use Django. 