import os

def dump_chatgpt_data():
    # Assuming ChatGPT data is stored in a directory called "chatgpt_data"
    data_directory = "chatgpt_data"
    
    # Check if the directory exists
    if os.path.exists(data_directory):
        # List all files in the directory
        files = os.listdir(data_directory)
        
        # Print header for the table
        print("| File Name | Data |")
        print("|-----------|------|")
        
        # Dump data from each file
        for file in files:
            with open(os.path.join(data_directory, file), "r") as f:
                data = f.read()
                # Print or process the data as needed
                print(f"| {file} | {data} |")
    else:
        print("ChatGPT data directory not found.")

# Call the function to dump ChatGPT data
dump_chatgpt_data()
