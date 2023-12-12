import json
import re


def check_string_using_regex(regular_expression: str, string: str):
    return re.match(regular_expression, string)


def parse_json(file_path):
    """
    :param file_path: file path
    :return: read file and return json
    """
    with open(file_path, encoding="utf-8") as json_data:
        json_data = json.load(json_data)
        return json_data


def to_camel(string: str) -> str:
    """
    Generate camelcase string
    input-
        string= sequence_number
    output-
        string= sequenceNumber
    """
    schema_attribute = string.split("_")
    return schema_attribute[0] + "".join(ele.title() for ele in schema_attribute[1:])
