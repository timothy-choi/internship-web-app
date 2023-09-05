# Internship Website

## Steps to host
* This assumes that you have python3 and pip and venv and setuptools etc. installed. 
### Clone this repository
```
git clone git@github.com:andli28/eecs497-internship-website.git
cd eecs497-internship-website
```
### Create a virtual environment
```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip setuptools wheel
```
* IMPORTANT: Make sure you are in your virtual environment for any pip install command!
### Install utilities
`sudo apt-get install sqlite3 curl` or `brew install sqlite3 curl`, for Linux and WSL, or MacOS respectively
### Install the Internship app
```
pip install -r requirements.txt
pip install -e .
```
### Create the database and host the website
```
./bin/497db create
./bin/497run
```
# internship-web-app
