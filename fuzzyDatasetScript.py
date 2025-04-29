import csv
from fuzzywuzzy import fuzz

def detect_action_and_ability(transcript_lines):
    actions = []
    abilities = []

    for i in range(len(transcript_lines) - 1):
        player_line = transcript_lines[i]
        dm_response = transcript_lines[i + 1]

        # You can customize this threshold based on your needs
        similarity_score = fuzz.partial_ratio(player_line.lower(), "take action")

        if similarity_score > 70:  # Adjust this threshold as needed
            actions.append(player_line)
            abilities.append(dm_response)

    return actions, abilities

def main():
    input_file_path = 'path/to/your/transcript.txt'
    output_csv_path = 'path/to/your/output.csv'

    with open(input_file_path, 'r') as file:
        transcript_lines = file.readlines()

    actions, abilities = detect_action_and_ability(transcript_lines)

    with open(output_csv_path, 'w', newline='') as csvfile:
        fieldnames = ['action', 'ability']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for action, ability in zip(actions, abilities):
            writer.writerow({'action': action.strip(), 'ability': ability.strip()})

if __name__ == "__main__":
    main()
