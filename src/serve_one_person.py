import json

def main():
    with open("/Users/kazon/repos/TheEngineersDaily/data/ruth_requirement.json") as f:
        ruth_requirement_data = json.load(f)

    person = ruth_requirement_data["person"]
    task = ruth_requirement_data["task"]
    success = ruth_requirement_data["success"]

    return "Requirement: {p} needs to {t} so that {s}.".format(p=person, t=task,s=success)


if __name__ == "__main__":
    res_str = main()
    print(res_str)