import re
import typer
from  typing import List

def parse_list(_: typer.Context, value: str) -> List[int]:
    try:
        # By using regex, find number and change to integer
        numbers = map(int, re.findall(r'\d+', value))
        return list(numbers)
    except ValueError:
        raise typer.BadParameter("List must include integers")
    
if __name__ == "__main__" :
    
    parsed = parse_list(typer.Context, "[1, 2, 3, 4, 5, 6]")
    print(parsed, type(parsed))  # To check the type and format
    
    test_cases = ["1, 2, 3, 4, 5", "1 2 3 4 5", "[1,2,3,4,5]", "[1, 2, 3, 4, 5]"]
    for test_case in test_cases : 
        print(f"{test_case} to switch {parse_list(typer.Context, test_case)}")
    print("Successfully transformed, all of the cases")