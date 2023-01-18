def letter_count(file):
    count_map = {}
    char = file.read(1)
    while char:
        process(char)
        char = file.read(1)

    file.close()
            