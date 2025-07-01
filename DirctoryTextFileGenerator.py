import os
import argparse

parser = argparse.ArgumentParser(description='Dataset Text List Formatting')

parser.add_argument("--data_path", type=str, default = r'./input_images', help='Data path of your dataset')
parser.add_argument("--output_path", type=str, default = r'./data_list', help='Output path of MST format TXT file')
args = parser.parse_args()

def textFileGenerator(data_path, output_path):
    """
    Generates a text file listing all files in the given directory.
    
    Args:
        data_path (str): The path to the directory containing the dataset.
        output_path (str): The path where the output text file will be saved.
    
    """

    # Get the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Extract last folder name from path
    folder_name = os.path.basename(os.path.normpath(data_path))
    output_path = f"{output_path}/{folder_name}_list.txt"

    print(f"Creating image list: {output_path}")

    with open(output_path, 'w') as f:
        for root, dirs, files in os.walk(data_path):
            for file in files:
                if file.lower().endswith(('.jpg', '.png')): # Check if image file
                    
                    file_path = os.path.join(root, file) # Full file path
                    # relative_path = os.path.relpath(file_path, data_path)
                    relative_path = os.path.relpath(file_path, project_root) # Get relative path
                    relative_path = relative_path.replace('\\', '/')
                    
                    f.write(f"./{relative_path}\n") # Write path to file

    print(f"Image list created: {os.path.abspath(output_path)}")
    print(f"Total folders processed: {folder_name}")
    
    


if __name__ == '__main__':

    textFileGenerator(args.data_path, args.output_path)