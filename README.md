# npp-installer-script
Silently install npp v7.7 on windows

## Installing pip

- Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
- Open a command prompt and navigate to the folder containing get-pip.py.
- Run the following command:
  `python get-pip.py`
- Pip is now installed!

You can verify that Pip was installed correctly by opening a command prompt and entering the following command:
- `$ pip -V`

## How to use the script
- Make sure you have python 3.7.* installed in you windows machine.
- Open the command line `CMD` as an administrator
- Clone the repo to your preffered location
- `cd` into the cloned folder
- Run the following commands one after the another:
  ```cmd
  $ pip install pywinauto
  $ python npp-installer.py
  ```

## To run the script in an environment

- To create an environment, open the Command Line as an Administrator
- Navigate to where the script folder is
- Run the following command to activate the environment
  ```cmd
  $ python -m venv env
  ```
- This creates an environment folder where the python installations will reside.
- To activate the environment run
  ```cmd
  $ env/Scritpts/activate
  ```
 - You should see the commandline formatted as follows:
   ```cmd
   $ (env) C:/path/to/current/working/directory
   ```
 
 - Now you can install the packages required to run the script by running
   ```cmd
   $ pip install pywinauto
   ```
