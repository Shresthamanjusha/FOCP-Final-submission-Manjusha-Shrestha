import sys
# Function to analyze the log file
def analyze_log(log_file_path):
    try:
        # Attempt to open the log file for reading
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: File not found - {log_file_path}")
        return
    except Exception as e:
        # Handle other exceptions that may occur during file reading
        print(f"Error: {e}")
        return

    # Variables for analysis
    correct_entry = 0
    doused_cats = 0
    total_time_inside = 0
    correct_visits = []

    # Loop through every line in the log file
    for line in lines:
        # Check if the line indicates the end of the log
        if line.strip() == 'END':
            break

        # Split the line into parts using ',' as the delimiter
        parts = line.strip().split(',')
        if len(parts) == 3:
            cat_name, entry_time, dept = parts
            entry_time = int(entry_time)
            dept = int(dept)

            # Check if the cat is the correct cat
            if cat_name == 'OURS':
                correct_entry += 1
                time_inside = dept - entry_time
                total_time_inside += time_inside
                correct_visits.append(time_inside)
            else:
                # Count the number of times other cats were doused with water
                doused_cats += 1

    # Check if there is any data for analysis
    if correct_entry == 0:
        print("No data found")
    else:
        total_hours = total_time_inside / 60
        average = sum(correct_visits) / correct_entry
        maximum = max(correct_visits)
        minimum = min(correct_visits)

        # Print the analysis results
        print("Log File Analysis")
        print("=================")
        print("Total number of times the correct cat has entered the house is:", correct_entry)
        print("Number of times cats were doused with water:", doused_cats)
        print("Total time spent in the house by the correct cat: {:.2f} hours".format(total_hours))
        print("Average duration of each visit by the correct cat: {:.2f} minutes".format(average))
        print("Duration of the longest visit by the correct cat:", maximum, "minutes")
        print("Duration of the shortest visit by the correct cat:", minimum, "minutes")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <log_file_path>")
        sys.exit(1)

    # Get the log file path from the command-line arguments
    log_file_path = sys.argv[1]
    
    # Call the analyze_log function with the specified log file path
    analyze_log(log_file_path)
    print("=======================")