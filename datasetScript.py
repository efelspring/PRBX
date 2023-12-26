import csv
import re

def extract_actions_and_stats(input_file, output_csv):
    with open(input_file, 'r', encoding='utf-8') as file:
        transcript = file.read()

    # Define a regular expression to capture player actions and associated stats
    pattern = r'Brennan: (.+roll.+)'

    matches = re.findall(pattern, transcript, re.DOTALL)
    #print(matches)
    # Create a list of tuples with (action, stat)
    data = [(action.strip(), stat.strip()) for action, stat in matches]

    # Write the data to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['action', 'stat']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for action, stat in data:
            writer.writerow({'action': action, 'stat': stat})

if __name__ == "__main__":
    input_file = "D20ScriptTest.txt"
    output_csv = "output_actions_and_stats.csv"
    
    extract_actions_and_stats(input_file, output_csv)
