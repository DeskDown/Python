def import_csv(file, delimiter = ","):
    """Powershell alike csv reader

    Args:
        file (string): [path to the csv file]   
        delimiter (str, optional): delimiter to parse data. Defaults to ","
            " is invalid delimiter.

    Returns:
        [tuple]: (list of labels, list of line objects with attribute named as labels)
    """

    import csv
    data_as_obj = []
    data_as_list = []
    labels = []
    try:
        """open the file and read the file just as we do in normal csv reading
        """
        with open(file, "r", newline= "") as f:
            reader = csv.reader(f, delimiter= delimiter)
            """Header is not allowed to have "
            """
            labels = [l.strip().replace("\"","") for l in reader.__next__()]
            data_as_list = [a for a in reader]
    except FileNotFoundError as fe:
        print(f"file {file} not found!")
        raise fe from None

    class line:
        """Objects of this class will be returned as data.
        All attributes are set dynamically.
        Attribute values are the labels provided by the csv Header
        """
        labels = ""
        def __init__(self, data):
            self.data = data

    line.labels = labels
    for data in data_as_list:
        NOT_VALID = data == [] or data[0].replace(" ","") == ""
        if NOT_VALID: continue
        l_obj = line(data)
        for label, value in zip(labels, data):
            setattr(l_obj, label, value.strip())
        data_as_obj.append(l_obj)
    
    return labels, data_as_obj

if __name__ == '__main__':
    labels, data = import_csv("cities.csv")
    print(labels)
    for line_number, line in enumerate(data, start= 1):
        print(line_number, " : ", end = "")
        for label in labels:
            print(getattr(line, label), end= ",")
        print("")