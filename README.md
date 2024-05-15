# BatchImageRenamer

BatchImageRenamer is a simple script tool for batch renaming image files in the current directory. It uses the Tkinter library to get the starting number entered by the user and renames all eligible image files (.jpg and .png formats are supported).

## Features

- Scan all .jpg and .png images in the current directory
- Batch rename image files with user-supplied starting numbers
- Handle file name sorting and formatting

## How to Use

You can use this tool in two ways:

### Using the Python Script

1. Clone or download the repository and make sure you have a Python environment.
2. Place the script in the desired directory (or move the script into the directory containing the images).
3. Run the script:
    ```bash
    python revise.py
    ```
4. A dialog box will pop up asking for a starting number. Enter an integer and press OK.
5. The script will automatically rename all .jpg and .png files in the directory and output the rename information in the terminal.

### Using the Executable File

If you have the executable file, follow these steps:

1. Ensure the executable file is in the desired directory (or move it into the directory containing the images).
2. Run the executable file by double-clicking it.
3. A dialog box will pop up asking for a starting number. Enter an integer and press OK.
4. The tool will automatically rename all .jpg and .png files in the directory and output the rename information.

## Example

Assume you have the following image files in the current directory:
image1.jpg
image2.png
anotherImage.jpg

You set the starting number to 1, then the script will rename them to:
001.jpg
002.png
003.jpg


## Caution

- Make sure there are no files in the directory with the same name as the renamed images to prevent overwriting when renaming.
- Running this tool will modify the file names in the current directory. It is **recommended to use it in a test environment or backup the files**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
