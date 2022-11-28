import json

INPUT_FILE = "input.csv"


def csv_to_list_dict() -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        result = []
        for index, line in enumerate(f):
            fields = line.strip(new_line).split(delimiter)
            if index == 0:
                heads = fields
                continue
            result.append({})

            for i, _ in enumerate(heads):
                result[-1][heads[i]] = fields[i]
    return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

