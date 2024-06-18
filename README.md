# Task X - Project Repository

This repository provides the structure necessary to approve your assignment. Please refer to the contents of this file for all necessary information. 

Link to task description on the: [dedicated page](https://eventornado.com/)

# Prerequisites

### Important Notice
Do not delete any directories/files created after cloning the repository. Removing these files will result in your task solution not being validated.

Ensure that you have Python 3.10 or higher installed on your system. You can verify your Python version by running the following command in your terminal:

```bash
python --version
```

If Python is not installed, download and install it from the official Python website.

## Cloning the Repository
To get started with the task, you first need to clone the repository to your local machine. Use the following command:
```bash
git clone https://github.com/procter-gamble/codeaithon-challenge-x.git
```

### Repository Structure
The repository is structured as follows to maintain an organized and standardized environment:

```
.
├── 📂 codeaithon-challenge-x            <- Main repository folder.
│   ├── 📂 .github                       <- This directory contains YAML files for Continuous Integration and Continuous Deployment (CI/CD).
│   ├── 📂 data                          <- The place where the data files are stored (if required)
│   ├── 📂 docs                          <- Instructions, guidelines, resources markdown files.
│   ├── 📂 src
|        └── 📂 bash                     <- Setup script
│   │    └── requirements.txt             <- Python packages required for local development
│   ├── 📂 submissions                   <- Folder which contains example output for a specific task (code, screenshot).
|        └── 📂 template                 <- A template which is used to create a directory for posting the solution to the task
│   ├── 📂 tests                         <- Pytest tests.
│   ├── .gitignore                        <- .gitignore file
│   ├── README.md                         <- This document
│   └── sonar-project.properties          <- This file is used by SonarQube to manage the code quality checks.
```

## Setup Script
Before you start working on the project, run the setup script to prepare your development environment. This script organizes the necessary files into the appropriate directories based on your coder ID.

### Preparing the Setup Script
To ensure the script can be executed, you need to grant it executable permissions. Navigate to the script's directory and run the following command:
```bash
chmod +x src/bash/./create_submission_folder.sh
```

### Running the Setup Script
From the main folder of the project, execute the setup script by running:
```bash
./src/bash/create_submission_folder.sh <your_coder_id>
```
Replace `<your_coder_id>` with your unique coder ID. This script creates a new folder within the `submissions` directory where you should place your solution to the task.

### Post-Script Structure
After running the setup script, the following structure will be created in the `submissions` folder:
```
.
├── 📂 coder-<your_coder_id>             <- This folder is your designated workspace.
│   ├── 📂 results                       <- Place your solution to the task in this folder.
│   ├── 📂 tests                         <- Write tests for the code you have created in this folder.
│   ├── README.md                        <- This file contains instructions on how to run the code you have created.
```

## Setting Up the Environment
To avoid conflicts with other Python projects or system-wide packages, it's recommended to use a virtual environment. Here's how to set it up:

## Creating a Virtual Environment
Navigate to the project's root directory and run the following command to create a virtual environment:
```bash
python -m venv env
```
This command creates a new directory env in your project directory, containing the virtual environment.

## Activating the Virtual Environment
Before working on the project, you need to activate the virtual environment. Depending on your operating system, run one of the following commands:

On Windows:
```bash
env\Scripts\activate
```

On macOS and Linux:
```bash
source env/bin/activate
```

## Installing Dependencies
The task dependencies are listed in a file named requirements.txt located in the 'code' folder. To install these dependencies, make sure your virtual environment is activated, and run:
```bash
pip install -r src/requirements.txt
```
# Working on a solution for a task

## Working with Git
To contribute to the project or update any part of the project, you should work on a separate branch and submit your changes via a pull request.

## Creating a New Branch
Ensure you are in your project directory and your Git workspace is clean. Create a new branch using the following command:
```bash
git checkout -b <branch_name>
```
Replace <branch_name> with a coder-x, where x is your assigned participant number.
## Making Changes and Committing
After making your changes, you can see them by running:
```bash
git status
```
Add your changes to the branch you created:
```bash
git add .
```
Then commit your changes:
```bash
git commit -m "A descriptive message about your changes"
```
## Pushing Changes
To push your new branch to the remote repository, use:
```bash
git push origin <branch_name>
```
## Submitting a solution
Validation of the solution involves the creation of a pull request from the branch on which the code has been placed to the main branch.

Go to the repository on GitHub. You should see a prompt to create a pull request for your recently pushed branch. Click 'Compare & pull request', add a title and description to your pull request, and then select 'Create pull request'.

### Important Notice
Please, do not merge pull request, leave is as open
