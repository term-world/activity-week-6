import json


def grab_data(filename: str) -> dict[str, dict[str, int]]:
    file = open(filename, "r")
    data = json.load(file)
    return data


# TO-DO: CREATE A FUNCTION THAT EVALUATES A SPECIFIC CITIZEN AGAINST ONE OF THE FOUR SPECIFIC METRICS


# TO-DO: CREATE A FUNCTION THAT CALLS THE ABOVE FUNCTION TO EVALUATE A SPECIFIC CITIZEN AGAINST *ALL* FOUR METRICS


def main():
    # DO NOT TOUCH CODE BLOCK BELOW
    citizen_data = grab_data("data/citizen-data.json")
    minimum_specs = grab_data("data/minimum-specs.json")
    print()
    citizen_num = input("Select a two-digit citizen ID# [00-47] to determine rank for: ")
    citizen_full_id = "ID#" + citizen_num
    print()
    print("The metrics for the citizen you have selected are:")
    print(citizen_data[citizen_full_id])
    print()
    # DO NOT TOUCH CODE BLOCK ABOVE
    
    # TO-DO: CALL THE FUNCTION TO EVALUATE THE CHOSEN CITIZEN AGAINST ALL FOUR METRICS AND DETERMINE THEIR RANK
    

    # DO NOT TOUCH BELOW PRINT STATEMENTS
    print(f"Citizen {citizen_num} has been assigned rank {rank}.")
    print()

if __name__ == "__main__":
    main()