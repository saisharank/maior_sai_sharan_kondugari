# Joke API

## Overview
This project is a FastAPI-based application that fetches jokes from an external API (JokeAPI), processes the data, and stores it in a MySQL database.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/saisharank/maior_sai_sharan_kondugari.git
cd jokesapi
```
2. Python Installation:

&nbsp;&nbsp;&nbsp;&nbsp;Go to the official [Python download page for Windows](https://www.python.org/downloads/).  
&nbsp;&nbsp;&nbsp;&nbsp;Find a stable Python 3 release. This tutorial was tested with Python version 3.13.0.  
&nbsp;&nbsp;&nbsp;&nbsp;Click the appropriate link for your system to download the executable file: Windows installer (64 bit) or Windows installer (32-bit).  
&nbsp;&nbsp;&nbsp;&nbsp;After the installer is downloaded, double-click the .exe file, for example python-3.13.0-amd64.exe, to run the Python installer.  
&nbsp;&nbsp;&nbsp;&nbsp;Select the Install launcher for all users checkbox, which enables all users of the computer to access the Python launcher application.  
&nbsp;&nbsp;&nbsp;&nbsp;Select the Add python.exe to PATH checkbox, which enables users to launch Python from the command line.  
&nbsp;&nbsp;&nbsp;&nbsp;Click Next.  
&nbsp;&nbsp;&nbsp;&nbsp;The Advanced Options dialog displays.  
&nbsp;&nbsp;&nbsp;&nbsp;Select the options that suit your requirements:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Install for all users: recommended if you’re not the only user on this computer  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Associate files with Python: recommended, because this option associates all the Python file types with the launcher or editor  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Create shortcuts for installed applications: recommended to enable shortcuts for Python applications  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Add Python to environment variables: recommended to enable launching Python  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Precompile standard library: not required, it might down the installation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-Download debugging symbols and Download debug binaries: recommended only if you plan to create C or C++ extensions  
&nbsp;&nbsp;&nbsp;&nbsp;Click Install to start the installation.  
&nbsp;&nbsp;&nbsp;&nbsp;After the installation is complete, a Setup was successful message displays.  
&nbsp;&nbsp;&nbsp;&nbsp;Verify installation by going into command prompt
```bash
python --version
```
3. MySQL Installation:

&nbsp;&nbsp;&nbsp;&nbsp;Download the [MySQL Installer 8.0.40](https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.40.0.msi).  
&nbsp;&nbsp;&nbsp;&nbsp;After downloaading; double click the MSI installer .exe file.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Choosing a Setup Type" screen: Choose "Full" setup type. This installs all MySQL products and features. Then click the "Next" button to continue.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Check Requirements" screen: The installer checks if your pc has the requirements needed. If there is some failing requirements, click on each item to try to resolve them by clicking on the Execute button that will install all requirements automatically. Click "Next"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Installation" screen: See what products that will be installed. Click "Execute" to download and install the Products. After finishing the installation, click "Next".  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Product Configuration" screen: See what products that will be configured. Click the "MySQL Server 8.0.23" option to configure the MySQL Server. Click the "Next" button. Choose the "Standalone MySQL Server/Classic MySQL Replication" option and click on the "Next" button. In page  "Type and Networking" set Config Type to "Development Computer" and "Connectivity" to "TCP/IP" and "Port" to "3006". Then, click the "Next" button.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Authentication Method" screen: Choose "Use Strong Password Encryption for Authentication". Click "Next".  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Accounts and Roles" screen: Set a password for the root account. Click "Next". While giving password, it is advisable not to have any special character  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Apply Configuration" screen: Click the "Execute" button to apply the Server configuration. After finishing, click the "Finish" button  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Product Configuration" screen: See that the Product Configuration is completed. Keep the default setting and click on the "Next" and "Finish" button to complete the MySQL package installation.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-In the next screen, you can choose to configure the Router. Click on "Next", "Finish" and then click the "Next" button.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Connect To Server" screen: Type in the root password. Click the "Check" button to check if the connection is successful or not. Click on the "Next" button.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Apply Configuration" screen: Select the options and click the "Execute" button. After finishing, click the "Finish" button.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-"Installation Complete" screen: The installation is complete. Click the "Finish" button. 
&nbsp;&nbsp;&nbsp;&nbsp;Verify the installation as below.
```bash
mysql -u "root" -p
Enter password:
```
&nbsp;&nbsp;&nbsp;&nbsp;After login create a database "jokedb".
```bash
create database jokedb
```
4. Run the FastAPI server:

&nbsp;&nbsp;&nbsp;&nbsp;Spin up the FASTAPI using the below command.
```bash
uvicorn app:app --reload
```
5. Testing the API
&nbsp;&nbsp;&nbsp;&nbsp;You can navigate to http://127.0.0.1:8000/docs to access the automatically generated Swagger UI and test the /fetch-jokes/ endpoint.

7. Checking at the DB end
In your MySQL shell, check the data as below
```bash
use jokedb
select * from jokedb;
```

This will list out all the data loaded to the table
