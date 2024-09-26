try:
    # Open the file in write mode and write to it
    file = open("my_file.txt", "w")
    file.write("Hello, this is a test file.\n")
    file.write("Here's a second line with a number: 42.\n")
    file.write("The third line contains a mix of text and numbers: 123 and ABC.\n")
    file.close()  # Close the file after writing

    # Open the file in read mode and display its contents
    file = open("my_file.txt", "r")
    contents = file.read()  # Read the entire file
    print("File Contents:\n")
    print(contents)
    file.close()  # Close the file after reading

    # Open the file in append mode and add more content
    file = open("my_file.txt", "a")
    file.write("Appending a fourth line.\n")
    file.write("This is the fifth line with a number: 99.\n")
    file.write("The sixth line contains more text and numbers: XYZ and 456.\n")

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have the necessary permissions to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()  # Ensure the file is closed
    print("File operations completed.")
