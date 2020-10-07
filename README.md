# Auswärtsspiel - Flask version
Here, I'm trying to do a bit more of a straightforward architecture - just a simple flask app.

To start

	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

And then

	flask run

To deploy the first time.

	az webapp up --sku S1 --name auswaerts-flask --location SwitzerlandNorth

## Azure Devops Setup
Created a project. Linked to the github sources. Created a pipeline (use Firefox). Python to Linux Web App on Azure. If all worked well you can select the Web App name, validate and configure.


