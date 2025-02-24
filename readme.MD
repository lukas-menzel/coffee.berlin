# Flask Website Starter Template 

This repository is a starter template intended to be forked and used for your own website. The focus here is on having a slim, working, full-stack website which can be (relatively) easily built, tested, and deployed on Google App Engine using GitHub actions. It is meant intended primarily for students of the Foundations of Software Engineering Course run in the spring of 2021 at CODE University of Applied Sciences, based in Berlin, Germany, but run remotely due to the pandemic. This README assume that the reader already has a basic familiarity with a broad range of topics and technologies touched on in that class, so it lacks explanation, but may occasionally make reference to something done in that class. 

## Every Time You Develop on Your Project

Every time you restart your computer or reopen VSCode, you'll have to do a few things. Instructions for macOS and Linux distributions assume you are using a Bash shell. Instructions for Windows assume you are using the Command Prompt. Instructions for other shells can be found online. 

- Activate your virtual environment for this project: 
   
    macOS/Linux: `source venv/bin/activate`
    
    Windows: `env\Scripts\activate.bat`

- Point Flask to your application: 

    macOS/Linux:  `export FLASK_APP=main.py`
    
    Windows: `set FLASK_APP=main.py`
- Enable hot reloading, debug mode, and other useful features for local development:  

     macOS/Linux: `export FLASK_ENV=development`

    Windows: `set FLASK_ENV=development`
- run your flask application: 

    `flask run`

## While You're Developing... 

Whenever you deploy your code, it will be automatically testing and linted by the GitHub Action. To have a quicker feedback loop and to make sure there are as few surprises as possible, run the same commands locally, too:

To test your app: 

> pytest --doctest-modules

To Lint your app: 
> flake8 --exclude venv 


# Installation Instructions
This will be a quick overview of steps for how to use this template on your own project, but will not be a line-for-line cookbook. You can find deeper explanations, tips, and instructions in the [Foundation's main class repository](https://github.com/DrAdamRoe/foundations-sample-website), used for homework assignments. 

## Before you start... 
You should have:
- Python 3.8.x installed on your computer 
- Visual Studio Code (or another IDE of your choosing) installed on your computer 
- A GitHub account 
- A Google Cloud Platform account (with class credits)

### Make This Your Own

Ready to go? Start by making this project your own:
- Fork this repository into your GitHub account. This is a good time to rename the repository to have the name of your project - but you can do it later, too. 
- Choose (or create) a working directory on your own computer and change directory into it
- Clone _your_ version onto your computer in that working directory.

Now you should be ready to get the starter template running on your computer!

### Get Set Up for Local Development: 
- Open Visual Studio Code, and open the folder containing your locally cloned repository. Before editing the code, make sure everything works as expected, locally at least.  
- Open a terminal in VS Code, too. This should automatically be in the same directory as your repository, if not, you should change directory to be in there. 
- In the terminal, create a new virtual environment for this project, using Python 3.8.x. The exact command will depend on your operating system and setup, but the idea is the same: call the Python executable at the command line (e.g. `python` or `python3.8` or `python3` or maybe `\Python38\python` on Windows). Normally, that will open the Python REPL interface, but we don't want that this time - we want it to create a virtual environment for us. To do that, pass the argument `-m venv`, which tells Python "run the venv module". Then, give it one more argument which is the path to a folder name where the virtual environment will live. For ease and consistency, this should be called `venv` and live in the repository root folder. This command could look like this, in the end, depending on your setup:
    
    > python3.8 -m venv venv 

- Activate your virtual environment (instructions can be found at the top of this readme)
- Download the Python modules listed in requirements.txt using pip: 

    > pip install -r requirements.txt

- Run the local development server and make sure it all works. Instructions can be found at the top of this readme for using Flask's built in development server. Alternatively, you can use the command `uwsgi` to start your development server: 

> uwsgi --http-socket 127.0.0.1:5000 --wsgi-file great_project/website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/

You should be able to run the website locally and see it in your local browser! 

### Configure Visual Studio Code 

A lot can be said here, but there are a few things that will make your life much easier, and are highly recommended: 

- Enable the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), which will immediately give you coding suggestions and show warnings. 
- Set the linter to `flake8`, the same one we are using at the command line and when we build on Google Cloud. This will give you visual feedback (yellow and red squiggly lines)
- Set the version of Python (or "interpreter") to be the virtual environment you have just created. This will help you to identify mismatches in your setup, especially when importing modules. 

#### Setup Continuous Deployment
You now have a website working locally, congratulations! And you can edit it, too. A website isn't really that useful unless it's on the web, though. A detailed explanation for how to do this can be found on our [Miro Board](https://miro.com/app/board/o9J_lTxsze4=/), in the [Foundation's main class repository](https://github.com/DrAdamRoe/foundations-sample-website), and in Google Classroom (where there is a walkthrough video). As a reminder, the main steps are: 
- Before you start, make sure you are logged into Google Cloud with your university email address, and have redeemed the voucher for free credits. 
- Create a new project on Google Cloud, and enable App Engine and Cloud Build. 
- Create a new service account, and give it the appropriate permissions.
- Create a key for your service account, and add that key as a "Secret" to your GitHub repository.  

GitHub should now be able to deploy your website to Google Cloud, and run it! To test this, you may have to trigger a build. If there is already a failed build (a red x visible on your repository's page), you can click on it and "Re-run jobs". The code itself hasn't changed, but your setup has - so we expect it to work now. Otherwise, you can push your code from your computer to GitHub, and it will trigger a build and deploy. 

At this stage, your website should be running on the internet, live! 

## Make This Repository Your Own

Now that you have verified that this setup works, it is time to make it your own. Here are a few things I suggest changing right away:   
- The repository name, if you haven't yet. 
- Change the title of the index page
- Edit the CSS a little, changing a font or color.
- Rename the folder `great_project` to be your project name. When you do this, you will have to change a few references to the directory: in `app.yaml`, `main.py`, and `test_great_project.py`. You can use the feature `Edit --> Find in Files` to find all occurrences of the name to make sure you have found them all. 

Even before you add any "features", this makes the website and code look and feel more like it is yours already! 

Once you have made some of these small changes, remember to add, commit, and push your changes - and with that, it should automatically be live on the internet! 
