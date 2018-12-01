# Web Info

The website is hosted at [shnyfs.pythonanywhere.com](http://shnyfs.pythonanywhere.com/)

# Database Info

The sample database is located in /src/ and is named db.sqlite3.

# Build Process

- Tagging

To view all tags:

`git tag`

To create a new tag:

`git tag -l '<tagname>'`

- Check out the project to a workstation

To clone the latest build from the GitHub repository:

`git clone [https://github.com/syurk738/checkShnyfer.git](https://github.com/syurk738/checkShnyfer.git)`

To update an existing repository to the GitHub repository:

`git commit –m 'Pulling from remote.' && git pull`

- Populate the database

Run this command: `python manage.py loaddata initialdata.json`

- Rebuild the database

Run this command: `python manage.py makemigrations && python manage.py migrate`

- Run the project locally

1. Navigate to /src/
2. Run this command: `python manage.py runserver`

- Unit Testing

To run all tests:

1. Navigate to /src/
2. Run this command: `python manage.py test`

To run a specific test suite:

1. Navigate to /src/
2. Run this command: `python manage.py test <suitename>`

- Deploy the build to PythonAnywhere

The website is hosted on [PythonAnywhere](http://shnyfs.pythonanywhere.com/). To deploy the build:

1. Push to GitHub using this command: `git commit –m 'Pushing to remote' && git push`
2. Go to the PythonAnywhere Bash Console at [https://www.pythonanywhere.com/user/shnyfs/](https://www.pythonanywhere.com/user/shnyfs/consoles/10887859/) and log in using these credentials:
  1. Username: See Dev Environment document
  2. Password: See Dev Environment document
  3. Note: the account is registered using my BJU email address – [bstee615@students.bju.edu](mailto:bstee615@students.bju.edu) - and you may change it as you like.
3. Open a console by clicking Bash Console.
4. Run this command to navigate to the Django project: cd checkShnyfer
5. Run this command: `git commit-m 'Pulling from remote.'`
6. Run this command: `git pull`
7. Run this command: `cd src`
8. Run this command: `pip3 install –-user django-crispy-forms`
9. Run this command: `python3 manage.py makemigrations && python3 manage.py migrate`
10. Navigate to the PythonAnywhere dashboard:[https://www.pythonanywhere.com/user/shnyfs/](https://www.pythonanywhere.com/user/shnyfs/consoles/10887859/)
11. Click Open Web Tab and select the shnyfs.pythonanywhere.com app.
12. Click Reload shnyfs.pythonanywhere.com.
13. Done!