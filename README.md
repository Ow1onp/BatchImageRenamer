# BatchImageRenamer

BatchImageRenamer is a simple script tool for batch renaming image files in the current directory. It uses the Tkinter library to get the starting number entered by the user and renames all eligible image files (.jpg and .png formats are supported).

## Function

- Scan all .jpg and .png images in the current directory
- Batch rename image files with user-supplied starting numbers
- Handle file name sorting and formatting

## How to use

1. Clone or download the repository and make sure you have a Python environment.
2. Place the script in the desired directory (or move the script into the directory containing the images).
3. Run the script:
    ```bash
    python revise.py
    ```
4. A dialog box will pop up asking for a starting number. Enter an integer and press OK. 5.
5. The script will automatically rename all .jpg and .png files in the directory in order and output the rename information in the terminal.

## Example

Assume the following image files are in the current directory:
image1.jpg
image2.png
anotherImage.jpg

You set the starting number to 1, then the script will rename them to:
001.jpg
002.png
003.jpg

### Caution

Make sure there are no files in the directory with the same name as the renamed images to prevent overwriting when renaming.
Running this script will modify the file names in the current directory, so it is recommended to use it in a test environment or backup the files.
