import glob
import csv
from typing import List




def generate_folder_names(start_year: int, start_month: int, end_year: int, end_month: int) -> List[str]:
    """
    Generate folder names from start_year-start_month to end_year-end_month.
    :param start_year: The starting year.
    :param start_month: The starting month.
    :param end_year: The ending year.
    :param end_month: The ending month.
    :return: A list of folder names.
    """
    folder_names = []
    current_year = start_year
    current_month = start_month

    while current_year < end_year or (current_year == end_year and current_month <= end_month):
        folder_name = f"{current_year}-{current_month:02d}"
        folder_path = f'data\{folder_name}'
        folder_names.append(folder_path)
        current_month += 1
        if current_month > 12:
            current_year += 1
            current_month = 1

    return folder_names


folders = generate_folder_names(2010, 12, 2024, 2)
print(folders)

def merge_crime_street_into(output_file: str, folders: List[str]) -> None:
    try:
        with open(output_file, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            for folder in folders:
                csv_files = glob.glob(folder + '/*-metropolitan-street.csv')
                print("CSV files found in folder:", csv_files)  # Debugging output
                for csv_file in csv_files:
                    try:
                        with open(csv_file, 'r', newline='') as infile:
                            csv_reader = csv.reader(infile)
                            for row in csv_reader:
                                csv_writer.writerow(row)
                        print(f"Concatenated CSV file: {csv_file}")
                    except Exception as e:
                        print(f"Error reading file '{csv_file}': {e}")
    except Exception as e:
        print(f"Error writing to file '{output_file}': {e}")


def merge_crime_outcomes_into(output_file: str, folders: List[str]) -> None:
    try:
        with open(output_file, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            for folder in folders:
                csv_files = glob.glob(folder + '/*-metropolitan-outcomes.csv')
                print("CSV files found in folder:", csv_files)  # Debugging output
                for csv_file in csv_files:
                    try:
                        with open(csv_file, 'r', newline='') as infile:
                            csv_reader = csv.reader(infile)
                            for row in csv_reader:
                                csv_writer.writerow(row)
                        print(f"Concatenated CSV file: {csv_file}")
                    except Exception as e:
                        print(f"Error reading file '{csv_file}': {e}")
    except Exception as e:
        print(f"Error writing to file '{output_file}': {e}")





def merge_crime_ss_into(output_file: str, folders: List[str]) -> None:
   try:
       with open(output_file, 'w', newline='') as outfile:
           csv_writer = csv.writer(outfile)
           for folder in folders:
               csv_files = glob.glob(folder + '/*-metropolitan-stop-and-search.csv')
               print("CSV files found in folder:", csv_files)  # Debugging output
               for csv_file in csv_files:
                   try:
                       with open(csv_file, 'r', newline='') as infile:
                           csv_reader = csv.reader(infile)
                           for row in csv_reader:
                               csv_writer.writerow(row)
                       print(f"Concatenated CSV file: {csv_file}")
                   except Exception as e:
                       print(f"Error reading file '{csv_file}': {e}")
   except Exception as e:
       print(f"Error writing to file '{output_file}': {e}")


def merge_crime_general(output_file: str, folders: List[str], file_type: str) -> None:
   try:
       with open(output_file, 'w', newline='') as outfile:
           csv_writer = csv.writer(outfile)
           for folder in folders:
               csv_files = glob.glob(folder + f'/*{file_type}.csv')
               print("CSV files found in folder:", csv_files)  # Debugging output
               for csv_file in csv_files:
                   try:
                       with open(csv_file, 'r', newline='') as infile:
                           csv_reader = csv.reader(infile)
                           for row in csv_reader:
                               csv_writer.writerow(row)
                       print(f"Concatenated CSV file: {csv_file}")
                   except Exception as e:
                       print(f"Error reading file '{csv_file}': {e}")
   except Exception as e:
       print(f"Error writing to file '{output_file}': {e}")

def merge_pas_general(output_file: str, folders: List[str]) -> None:
   try:
       with open(output_file, 'w', newline='') as outfile:
           csv_writer = csv.writer(outfile)
           for folder in folders:
               csv_files = glob.glob(folder + f'/*.csv')
               print("CSV files found in folder:", csv_files)  # Debugging output
               for csv_file in csv_files:
                   try:
                       with open(csv_file, 'r', newline='') as infile:
                           csv_reader = csv.reader(infile)
                           for row in csv_reader:
                               csv_writer.writerow(row)
                       print(f"Concatenated CSV file: {csv_file}")
                   except Exception as e:
                       print(f"Error reading file '{csv_file}': {e}")
   except Exception as e:
       print(f"Error writing to file '{output_file}': {e}")

# Function calls
#merge_crime_street_into(output_file="project_data/combined_crime.csv", folders= folders)
#merge_crime_outcomes_into(output_file="project_data/combined_crime_outcomes.csv", folders= folders)
#merge_crime_ss_into(output_file="project_data/combined_crime_stop_and_search.csv", folders= folders)
#merge_crime_general(output_file="project_data/combined_street.csv", folders= folders, file_type='-street')
#merge_crime_general(output_file="project_data/combined_outcomes.csv", folders= folders, file_type='-outcomes')
#merge_crime_general(output_file="project_data/combined_stop_and_search.csv", folders= folders, file_type='-stop-and-search')
merge_pas_general(output_file='project_data/pas_granular.csv', folders=['data'])