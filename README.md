## Web Info
The website is hosted at shnyfs.pythonanywhere.com

## Database Info
The sample database is located in /src/ and is named db.sqlite3.

## Build Process
1. Tagging - To view all tags:
- `git tag`
- To create a new tag:
- `git tag -l “<tagname>”`
2. clone the latest build from the GitHub repository:
- `git clone https://github.com/syurk738/checkShnyfer.git`
- To update an existing repository to the GitHub repository:
- `git commit –m “Pulling from remote.” && git pull`
3. (optional) To populate the database:
- Run this command: `python manage.py loaddata initialdata.json`
4. To run the project locally in debug mode:
- Navigate to `/src/`
- Run this command: `python manage.py runserver`
5.	Unit Testing

To run all tests:
- Navigate to `/src/`
- Run this command: `python manage.py test`

To run a specific test suite:
- Navigate to `/src/`
- Run this command: `python manage.py test <suitename>`
- Deploy the build to PythonAnywhere.

The website is hosted on PythonAnywhere. To deploy the build:
1.	Push to GitHub using this command: `git commit –m “pushing to remote” && git push`
2.	Go to the PythonAnywhere Bash Console at https://www.pythonanywhere.com/user/shnyfs/ and log in using these credentials:
a.	Username: Stored in DevEnvironment document
b.	Password: Stored in DevEnvironment document
c.	Note: the account is registered using my BJU email address – bstee615@students.bju.edu - and you may change it as you like.
3.	Open a console by clicking Bash Console.
4.	Run this command to navigate to the Django project: cd src
5.	Run this command: `git commit`
6.	When the commit message dialog pops up, enter a message like this: “Pulling from remote.”.
7.	Press Escape to exit INSERT mode (it’s using Vim) and press :wq to save and quit.
8.	Run this command: `git pull`
9.	Navigate to the PythonAnywhere dashboard: https://www.pythonanywhere.com/user/shnyfs/
10.	Click Open Web Tab and select the shnyfs.pythonanywhere.com app.
11.	Click Reload shnyfs.pythonanywhere.com.
12.	Done!
