import re

input_file = "password.txt"
output_file = "password_output.txt"

# Define the password criteria pattern
password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~])[A-Za-z\d!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~]{8,}$")

# Open the input and output files
with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
    # Iterate through each line in the input file
    for line in file_in:
        password = line.strip()
        # Check if the line meets the password criteria
        if password_pattern.match(password):
            # Line meets the criteria, so write it to the output file
            file_out.write(password + "\n")

print("Filtered passwords saved to", output_file)
