import json

def main(data_file_path = "/Users/kazon/repos/TheEngineersDaily/data/ruth_requirement.json"):
    with open(data_file_path) as f:
        ruth_requirement_data = json.load(f)

    person = ruth_requirement_data.get("person")
    task = ruth_requirement_data.get("task")
    success = ruth_requirement_data.get("success")

    validate_field(person, "person")
    validate_field(task, "task")
    validate_field(success, "success")

    return "Requirement: {p} needs to {t} so that {s}.".format(p=person, t=task,s=success)

def validate_field(field, field_name):
    """
    Each value is a string, and each value contains at least one non-whitespace character.
    """

    error_message = "Saved requirement is incomplete: {f} is required. Add a non-empty {f} value to the saved requirement file."

    if field is None:
        raise ValueError(error_message.format(f=field_name))
    if not isinstance(field, str):
        raise ValueError(error_message.format(f=field_name))
    if not field.strip():
        raise ValueError(error_message.format(f=field_name))    

if __name__ == "__main__":
    res_str = main()
    print(res_str)