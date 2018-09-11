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

 ### to the Code
 If you make changes to the code in a python file that already exists and the server is running, you do not need to restart the server.

 ## GIT
**Please do not commit to the master branch.** Instead, follow the instructions [here](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches) to create branches, commit, and create pull requests. 

 ## More Questions
 > Django: Go to [this django project](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) for a full tutorial on how to use Django. 
 > Project: Email [mailto](syurk738@students.bju.edu)
 