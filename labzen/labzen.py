from nbformat import read, NO_CONVERT
import os
from pathlib import Path
import re
import glob


def parse_lab(notebook = 'no input'):
    
    """Parse MDS lab files to return the markdown content
    Args:
        file_name (str): A path or list of paths to MDS lab files (either
            .ipynb or .Rmd). If left blank, the function will recursively
            search for all labs in the working directory based on the file
            extension.
    Returns:
        list: Each element of list is a content of one markdown cell.
    Example:
        parse_lab()
    """
    
    # If the user did not defined the specific file, recursively 
    # search for rmd and ipynb files in the working directory
    if notebook == 'no input':
        directory = os.getcwd()
        types = ["*.ipynb", "*.Rmd"]
        files = []
        for type in types:
            pathname = directory + "/**/*" + type
            type_files = glob.glob(pathname, recursive=True)
            files += type_files
        names = [str(n+1) + '.' + os.path.basename(file)  for n, file in enumerate(files)]
        print("The existing files are:")
        for item in names:
            print(item)
        notebook = input(f'Enter your file number from the above list: ')
        notebook = files[int(notebook) -1]
    path = Path(notebook)
    name, extension = os.path.splitext(notebook)


    # defensive tests
    if extension != ".Rmd" and extension != ".ipynb":
        raise Exception("Sorry, you have not provided Rmarkdown or jupyter notebook file")

    if isinstance(notebook,str) != True:
        raise Exception("The file path should be string")

    # Parse the markdown contents of rmd or ipynb file
    source = []
    if extension == ".Rmd":
        text_and_code = path.read_text()
        text_and_code = text_and_code.split("```")

        code_blocks = []
        for string in text_and_code:
            if string.startswith("{r"):
                code_blocks.append(string)
            elif string.startswith("{python"):
                code_blocks.append(string)
            else:
                source.append(string)
    else:
        with open(notebook, encoding="utf8") as file:
            notebook = read(file, NO_CONVERT)
            cells = notebook["cells"]
            code_cells = [c for c in cells if c["cell_type"] == "markdown"]
            for cell in code_cells:
                source.append(cell["source"])

    return source



def count_points(file_name: str = None) -> pd.DataFrame:
    """Tally Available Points in Lab

    Args:
        file_name (str): A path or list of paths to MDS lab files (either
            .ipynb or .Rmd). If left blank, the function will recursively
            search for all labs in the working directory based on the file
            extension.

    Returns:
        pd.DataFrame: A cross table summarising the number of optional,
            required, and total points per lab.

    Example:
        count_points()
    """
    return None


def check_repo_link(file_name: str) -> bool:
    """ Check whether the user has included the github repo link in his/her 
        repository

    Args:
        file_name (str): A path or list of paths to MDS lab files (either
            .ipynb or .Rmd). If left blank, the function will recursively
            search for all labs in the working directory based on the file
            extension.

    Returns:
        bool: a boolean output 

    Example:
        check_repo_link()    
    """
    return None


def check_lat_version(file_name: str) -> bool:
    """ Check whether the user has pushed the latest version in his/her 
        repository

    Args:
        file_name (str): A path or list of paths to MDS lab files (either
            .ipynb or .Rmd). If left blank, the function will recursively
            search for all labs in the working directory based on the file
            extension.

    Returns:
        bool: a boolean output

    Example:
        check_lat_version() 
    """
    return None


def check_commits(file_name: str) -> bool:
    """ Check whether the user has at least three commits

    Args:
        file_name (str): A path or list of paths to MDS lab files (either
            .ipynb or .Rmd). If left blank, the function will recursively
            search for all labs in the working directory based on the file
            extension.

    Returns:
        bool: a boolean output

    Example:
        check_commits()      
    """
    return None


def check_mechanics(file_name: str) -> NoneType:
    """Performs Mechanics Checks on a MDS Lab
       This function check that you have a Github repo link, that you have 
       pushed your latest commit, and that you have at least three commit 
       messages authored by you in your history.

    Args:
        file_name (str): A path or list of paths to MDS lab files (either
            .ipynb or .Rmd). If left blank, the function will recursively
            search for all labs in the working directory based on the file
            extension.

    Returns:
        NoneType: The function prints the results of the mechanics checks to screen

    Example:
        check_mechanics()      
    
    """
    return None

  
