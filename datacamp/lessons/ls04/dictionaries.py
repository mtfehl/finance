from typing import Dict

def main() -> None:
    world = {"usa":30.55, "uk":2.77, "aus":39.21}
    print(world["usa"])
    print(team)
    if 91 in team:
        print("You have Rodman!")
    
team: Dict[int, str] = {}
team[23] = "Jordan"
team[91] = "Rodman"

if __name__ == "__main__":
    main()

europe: Dict[str, str] = {}
europe["italy"] = "rome"
europe["poland"] = "warsaw"
print("italy" in europe)
 # returns "True" since Italy is found in Europe dict

countries = {'spain': { 'capital':'madrid', 'population':46.77}, 'france': {'capital':'paris', 'population':66.03}}
print(countries["spain"]["capital"])
# Returns Madrid