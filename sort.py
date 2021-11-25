# allows for arguemnt input from the cli
import sys
# allows for file validation by accessing the directory
import os.path as path
# allows for readable data display
import yaml
# allows for reading csv files and sorting
import pandas as manageFile



def sortFile(fileName):

    csvFile = manageFile.read_csv(fileName)

    # Checking if the file contents has the appropriate headings
    csvFileHeaderValues = list(csvFile) # retriving just the column names for error checking
    expectedHeaderValues = ['firstname', 'lastname', 'date', 'division', 'points', 'summary']

    # Exit program if coloumn names are not the same
    if set(csvFileHeaderValues) != set(expectedHeaderValues):
        return "Invalid column names, please reformat the contents of the file and try again"

    # sorting the data by division and points, we want to sort the points by highest
    csvFile.sort_values(["division", "points"], ascending=[True, False], inplace=True)
  
    # taking the first three entries from the sorted file
    finalData = csvFile.head(3) 

    # initialising empty dictionary to store the extracted data
    results = {'records':[]}

    # looping through the three entries, formatting them and appending them to array inside the dictionary
    for key,value in finalData.iterrows():
        results['records'].append({"name":f"{value['firstname']} {value['lastname']}", 
        'details': f"In division {value['division']} from {value['date']} performing {value['summary']}"})

    #using yaml to display the data in a readable manner
    return yaml.dump(results)
    


if __name__ == '__main__':
    if path.isfile(f"{sys.argv[1]}"):
        print(sortFile(sys.argv[1]))
    else: print("the file does not exist, exiting appication")