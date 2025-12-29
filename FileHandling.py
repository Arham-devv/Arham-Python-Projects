# File: studentsrecord.txt
# Example content:
# 101,Ali,Present
# 102,Sara,Absent
# 103,Omar,Present

# Open the file in read mode
with open("studentsrecord.txt", "r") as file:

    total_stu = 0
    total_present = 0
    total_absent = 0

    # Loop through each line in the file
    for line in file:
        line = line.strip()  # Remove newline characters and extra spaces
        if line:  # Process only if the line is not empty
            total_stu += 1  # Count total students
            parts = line.split(",")  # Split line into [EmployeeID, Name, Status]
            status = parts[2].strip().lower()  # Extract status and convert to lowercase

            # Count present and absent students
            if status == "present":
                total_present += 1
            elif status == "absent":
                total_absent += 1

# Print the final counts
print("Total Absent:", total_absent)
print("Total Present:", total_present)
print("Total Students:", total_stu)

    


    