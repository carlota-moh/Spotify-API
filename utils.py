import json

def write_json(dic, file_path):
    """
    Function used to write data to JSON in a specified file_path

    Params:
    -dic: dictionary
        Python dictionary to be written to file

    -file_path: string
        final location of the file

    """
    import json
    with open(file_path, "w") as f:
        json.dump(dic, f)

def write_textfile(string, file_path):
    with open(file_path, "w") as f:
        f.write(string)