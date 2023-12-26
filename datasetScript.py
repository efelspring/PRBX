import csv
import re

def extract_actions_and_stats(input_file, output_csv):
    with open(input_file, 'r', encoding='utf-8') as file:
        transcript = file.read()

    # Define a regular expression to capture player actions and associated stats
    pattern = r'Brennan:([ a-zA-Z,.\d])+[rR]oll([ a-zA-Z,.\d])+\n'

    matches = re.findall(pattern, transcript)
    print(matches)

    # Write the data to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames="matches")
            
        for i in matches:
            print(i)
            #writer.writerow(i)

if __name__ == "__main__":
    input_file = "shortTestScript.txt"
    output_csv = "output_actions_and_stats.csv"
    
    extract_actions_and_stats(input_file, output_csv)

