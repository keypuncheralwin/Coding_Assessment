# Coding Assessment
My solution to a company's coding assessment

## The Problem

Create a CLI tool which:

Takes in a CSV file containing the following columns:
firstname: String
lastname: String
date: String (format YYYY-MM-DD)
division: Integer
points: Integer
summary: String
Sorts the records by division and points.
Selects the top three records.
Prints the records to stdout in the following YAML format:
records:

```
- name: <firstname> <lastname> 
  details: In division <division> from <date> performing <summary>
- name: <firstname> <lastname>
  details: In division <division> from <date> performing <summary>
- name: <firstname> <lastname>
  details: In division <division> from <date> performing <summary>
```

### Constraints
- You must use one of the following languages to implement your solution:
    * Java
    * Groovy
    * Python
    * C#
- You must use git to manage your code.
- You must regularly push your code to Github.
- Create an account if you do not have an existing one.
- Create a new repository under your account and push your code to it.

## The Solution

I used python to solve the problem. I used a python module called pandas to aid in reading the csv file and sorting it according to the specifications. Once the file was sorted, the first three entries were stored in a variable.

I then looped through this variable and extracted the necessary information and formatted it which was then appended into a list inside a dictionary. The Pyyaml module was used to display the dictionary in a readable manner.

Since we're creating a cli tool we want to be able to just type in the file name we want to sort in the terminal itself rather than having to open up the python script and entering it in there. In order to do this, I used the python sys module which takes in arguements from the terminal. I used the python os module to check if the entered file actually exists.

Since the function is returning a dictonary with the relavnt data it made it posible to write test cases to see if we're getting the right data.

Pyhton needs to be installed on the local machine in order for this program to run. Since I used some python modules to create this tool, they will need to be installed as well. All the dependencies are listed in the requirements.txt file which can be installed by typing in the following command (adjust the command based on the file path)

<code>pip install -r /requirements.txt</code>

I recommand running the program/installing the depencies in a python virtual environment to avoid clashes with other projects/programs.

(macOS commands, commands vary depending on OS)

<code>python -m venv venv</code>

<code>source venv/bin/activate</code> 

Once the dependencies are installed, the file can be run by typing in the name of the script followed by the csv file path (adjust the command based on the file path)

<code>python sort.py ./csv_files/data.csv</code>

