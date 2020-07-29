Setup on local machine 

fork the repo.(make sure its develop branch you are forking)
within terminal navigate to your desired folder where you would want to store project

git clone the repo 
```
git clone <your forked repo url>
```
-------------now set up git remote & upstream-------------

(I would advice you carry out git tasks on git bash instead of cmd prompt if using windows)

with your forked repo now present on your  local machine cd into project folder 

you should see which branch you are actively in in brackets at the end of the terminal prompt 

for example : Jordan Rob@DESKTOP-IE0C0TE MINGW64 /e/projects/SDG-Team-272-SMES/team-272-SMES-Server (master)
$
master is the active branch in this case

so once verified what branch you are in create a new branch for your work run the command below
```
git checkout -b <add-your-new-branch-name>
```
now check whether you have origin urls for both fetch and push set by running
```
git remote -v
```
on seeing them present set up upstream url for your repo 
```
git remote add upstream <url of original project repo (not your forked repo but the one you forked from)>
```
to fetch current state of original repo run
```
git fetch upstream
```
now merge code in develop branch(original repo) to your own branch by running
```
git merge upstream/develop
```

use the usual git add,git status,git commit -m to add and commit changes to push note that since you are not in master push is like 
```
 git push origin <your branch name>
```


----------now to run project-----------------

still within project directory

install pipenv 
```
pip install pipenv
```
now run command below to create a virtual env and install dependencies

```
pipenv install
```
once complete activate the virtual environment 

```
pipenv shell
```
you will tell its activated by seeing () with characters in it preceeding the terminal prompt

fire up development server
```
py manage.py runserver
```

-----------Project Navigation------------
css, js, img, fonts, plugins files are in static folder 

template files:
i have a main base.html file that extends styling and layout to the rest of the html files to manipulate links to static resources note that the format here is as follows 
eg : <link rel="stylesheet" href="{% static  'css/market-place-1.css'  %}">

to adjust path write it within quotes as seen above

all images for slider promos, categories and products and their info is now all dynamic coming from database as created by admin not like normal html through links

restart server every after you make changes to effect them 

avoid any python code , files please 

Note: 
   
   - I would encourage you upon running development server to first navigate through the site before making your changes to know how things work

   - make sure your changes are mostly with colours and visuals , I managed to unify the layout and form factor should not be tampered with for example as we wanted a header for all pages i managed to do that now I would expect you to just add logo and adjust css properties to match colors to how you would want them but not changing navbar structure.