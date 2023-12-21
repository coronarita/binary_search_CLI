import typer
from typing import List, Optional
from typing_extensions import Annotated

from parse import parse_list  # 리스트 파싱을 위해 정의했던 함수를 가져옵니다.

app = typer.Typer()

def bound_search(target: int,
                 lst: Optional[List[int]],
                 compare,):
    
    lo, hi = 0, len(lst)
    while lo < hi : 
        mid = (lo + hi) // 2
        
        if compare(target, lst[mid]): 
            hi = mid
        else : 
            lo = mid + 1
    return lo

@app.command()
def lower_bound(target: Annotated[int, typer.Option(help="The number want to find in list. For example, 2")],
                 lst: Annotated[str, 
                                typer.Option(..., help="The list what you guess the target exists, for example : \"1 2 2 2 3 5\", \"[1, 2, 2, 2, 3, 5]\"",
                                             callback=parse_list)],
                 print_result: bool = True
                 ):
    """ 
    Find the first index of target in list.
    """
    lower = lambda x, elem: x <= elem
    lo = bound_search(target, lst, lower)
    if print_result :
        print(lo)
    return lo
    
@app.command()
def upper_bound(target: Annotated[int, typer.Option(help="The number want to find in list. For example, 2")],
                 lst: Annotated[str,
                                typer.Option(..., help="The list what you guess the target exists, for example : \"1 2 2 2 3 5\", \"[1, 2, 2, 2, 3, 5]\"",
                                             callback=parse_list)],
                 print_result: bool = True
                 ):
    """ 
    Find the last index + 1 of target in list.
    """
    upper = lambda x, elem: x < elem
    lo = bound_search(target, lst, upper)
    if print_result :
        print(lo)
    return lo

@app.command()
def count_num(target: Annotated[int, typer.Option(help="The number want to find in list. For example, 2")],
                 lst: Annotated[str,
                                typer.Option(..., help="The list what you guess the target exists, for example : \"1 2 2 2 3 5\", \"[1, 2, 2, 2, 3, 5]\"",
                                             callback=parse_list)],):
    """
    Return the number of target in the list.
    """
    cnt = upper_bound(target, lst, False) - lower_bound(target, lst, False)
    print(cnt)
    return cnt
    

if __name__ == "__main__":
    app()