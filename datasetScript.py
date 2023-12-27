import csv
import re

def extract_lines(input_file, output_csv):
    with open(input_file, 'r', encoding='utf-8') as file:
        transcript = file.readlines()

    # Define a regular expression to capture Brennan's lines with the word "roll"
    pattern = r'^Brennan:.*\broll\b.*$'

    brennan_lines_with_roll = [line.strip() for line in transcript if re.search(pattern, line, re.IGNORECASE)]

    # Write the data to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['line']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for line in brennan_lines_with_roll:
            writer.writerow({'line': line})

if __name__ == "__main__":
    input_file = "shortTestScript.txt"
    output_csv = "lines_with_roll.csv"

    extract_lines(input_file, output_csv)


