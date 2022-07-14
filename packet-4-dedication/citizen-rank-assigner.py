import json


def grab_file(filename: str) -> dict[str, dict[str, int]]:
    file = open(filename, "r")
    contents = json.load(file)
    return contents


def evaluate_one(citizen_id: str, metric: str, citizen_data: dict[str, dict[str, int]], minimum_specs: dict[str, dict[str, int]]) -> int:
    
    # TO-DO: IMPLEMENT FUNCTION THAT EVALUATES A SPECIFIC CITIZEN AGAINST ONE OF THE FOUR SPECIFIC METRICS


    return rank
    

def evaluate_all(citizen_id: str, citizen_data: dict[str, dict[str, int]], minimum_specs: dict[str, dict[str, int]]) -> int:
    
    # TO-DO: IMPLEMENT FUNCTION THAT EVALUATES A SPECIFIC CITIZEN AGAINST *ALL* FOUR METRICS


    return final_rank


def main():
    citizen_data = grab_file("data/citizen-data.json")
    minimum_specs = grab_file("data/minimum-specs.json")
    print()
    citizen_num = input("Select a two-digit citizen ID# [00-47] to determine rank for: ")
    citizen_full_id = "ID#" + citizen_num
    rank = evaluate_all(citizen_full_id, citizen_data, minimum_specs)
    print()
    print(f"Citizen {citizen_num} has been assigned rank {rank}.")
    print()

if __name__ == "__main__":
    main()