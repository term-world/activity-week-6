from typing import List


def grab_votes(filename: str) -> List[List[str]]:
    votes = []
    data = open(filename, "r")
    for line in data.readlines():
        line = line.strip()
        line = line.split(",")
        votes.append(line)
    return votes


def main():
    # TO-DO: CALL grab_votes FUNCTION TO COLLECT VOTE DATA


    # TO-DO: CONSTRUCT A results DICTIONARY THAT HAS EACH CANDIDATE REPRESENTED AS A KEY
    # WITH EACH KEY ALSO HAVING A CORRESPONDING VALUE OF 0


    # TO-DO: ITERATE THROUGH THE OUTPUT OF grab_votes AND:
    # IF THE CANDIDATE IS IN THE FIRST POSITION OF A GIVEN VOTE, ADD 3 TO THEIR KEY IN THE results DICTIONARY
    # IF THE CANDIDATE IS IN THE SECOND POSITION OF A GIVEN VOTE, ADD 2 TO THEIR KEY IN THE results DICTIONARY
    # IF THE CANDIDATE IS IN THE THIRD POSITION OF A GIVEN VOTE, ADD 1 TO THEIR KEY IN THE results DICTIONARY

    # HINT: RECALL THAT THE OUTPUT OF grab_votes IS A LIST OF LISTS, WITH EACH INNER LIST HAVING SEVERAL STRINGS
    # THIS MEANS YOU MAY NEED MORE THAN ONE FOR LOOP TO COMPLETE THIS TASK


    # DO NOT TOUCH ANYTHING BELOW THIS LINE
    print()
    for candidate in results:
        print(f"{candidate} received a score of {results[candidate]}.")
    winner = max(results, key=results.get)
    print()
    print(f"{winner} is the winner of the election!")
    print()

if __name__ == "__main__":
    main()