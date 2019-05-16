def read_file(file_name):
    file = open(file_name)
    data = file.read()
    file.close()
    return data
