# Banna README
![Logo](banna/farmer/static/farmer/img/github_logo.png)

> **ICT4D in the field**
> - Allard Oelen
> - Aron van Groningen  
> - Amir Azizi Musa
> - Deva Ramakrishnan
> - Hameedat Omoine
> - Linh Tran

## Introduction
BannaTree is an application that allows Banana Contract farmers in Malaysia to enter farm data into the system. With this data, the Malaysian agricultural department is able to provide the contract farmers with better advice. For more information about contract farming, take a look at the 'summary of use case' section. BannaTree consists of three different interface. The first interface is for the farmers, and is built for smartphone screens. The second interface is for the agricultural department, they can use this interface to review the data entered by the farmer. The final interface is for the banana factory, this interface is similar to the previous one, but the factory is able to add banana purchase data.

## Summary of use case
Contract farmers are farmers that are helped by the government in terms of getting: advice, fertilizer, seeds but more importantly: a fixed price for their bananas. With this guarantee, they do not have to worry about marketing, and selling their bananas. Right now, a dozens of farmers are already part of this contract farming program.

In order to make this program more effective, the government wants to collect basic statistical data about the harvest, planted trees, and whether fertilizer is used or not. With this information, the government can give better advice to the farmers, in order to increase their yield. This is where our application, BannaTree, comes in. BannaTree provides farmers a smartphone interface where they can enter this kind of information on a monthly basis. In the end, the government can use this data to improve the complete banana contract farmers program.


## Installation requirements
- Python 3.6 or higher
- Django 2
- Postgresql


## Installation instructions
Local installation (make sure to have Python and Django installed first, optionally work in a virtual environment)
- `$ git clone https://github.com/aoelen/banna`
 - (Optionally create a virtual environment using: `$ virtualenv venv`)
 - (Optionally activate the environment: `$ source venv/bin/activate`)
- Install the required packages: `$ pip install -r requirements.txt`
- Change the database settings in: `banna/banna/settings.py`
- (Import sample data: `python manage.py loaddata db.json`)
- Run the server: `$ python banna/manage.py runserver`
- Visit Banna at: `http://localhost:8000`
