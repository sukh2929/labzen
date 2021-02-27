import pandas as pd


def parse_lab(file_name: str) -> list:
    """[summary]

    Args:
        file_name (str): [description]

    Returns:
        list: [description]
    """
    return None


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
    """ Check whether the user has included the github repo link in his 
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
    """ Check whether the user has atleast three commits

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
    """ It is a wrapper function which calls the other functions - check_repo_link, 
        check_commits, check_lat_version 

    Args:
        file_name (str): A path or list of paths to MDS lab files (either
            .ipynb or .Rmd). If left blank, the function will recursively
            search for all labs in the working directory based on the file
            extension.

    Returns:
        NoneType: Does not return any output

    Example:
        check_mechanics()      
    
    """
    return None

