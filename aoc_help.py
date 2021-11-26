def read_file(path: str) -> list:
    """
    Reads a txt file and returns a list containing all lines of the file, stripped from newline characters
    :param path: filename & location
    :return: list of which each element contains a line of the file, stripped from newline character
    """
    with open(path, 'r') as my_file:
        lines = my_file.readlines()
        return [x.strip('\n') for x in lines]

