def grep(file, text):
    """
    Raises FileNotFoundError if file does not exist
    :param file: name of the file where text is searched
    :param text: search term
    :return:
    """
    lines_matching = []
    with open(file, "r") as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


if __name__ == "__main__":
    filename = input("Insert filename: ")
    search_term = input("Insert search term: ")

    try:
        lines = grep(filename, search_term)
        if lines:
            print("Found matching lines:")
        for line in lines:
            print(line, end="")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    finally:
        print("Finally executed!")
