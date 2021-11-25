
# allows for readable data display
import yaml
# allows for reading csv files and sorting
import pandas as manageFile

file = './data.csv'

def sortFile(fileName):

    csvFile = manageFile.read_csv(fileName)

    # sorting the data by division and points, we want to sort the points by highest
    csvFile.sort_values(["division", "points"], ascending=[True, False], inplace=True)
  
    #taking the first three entries from the sorted list
    finalData = csvFile.head(3) 

    #initialising empty object to store the extracted data
    results = {'records':[]}

    
    for key,value in finalData.iterrows():
        results['records'].append({"name":f"{value['firstname']} {value['lastname']}", 'details': f"In division {value['division']} from {value['date']} performing {value['summary']}"})

    #using yaml to display the data in a readable manner
    return yaml.dump(results)


print(sortFile(file))