import json

INPUT_FILE = "input.csv"


def csv_to_list_dict() -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    with open(filename, "r") as f:
        splitted_list = [line.replace(new_line, '').split(delimiter) for line in f]
        row_numbers = len(splitted_list)
        headers_index = 0  # пусть заголовки были в первой строке csv файла
        list_dict = []
        for i in range(headers_index + 1, row_numbers):  # после строки с заголовками идут строки со значениями
            list_dict.append(dict(zip(splitted_list[0], splitted_list[i])))
        return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE, delimiter=",", new_line="\n"), indent=4))

