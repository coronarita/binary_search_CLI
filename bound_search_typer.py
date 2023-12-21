import typer
from typing import List, Optional
from typing_extensions import Annotated

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
                 lst: Annotated[Optional[List[int]], typer.Option(help="The list what you guess the target exists, for example : 1 2 2 2 3 5")],
                 ):
    """ 
    Find the first index of target in list.
    """
    lower = lambda x, elem: x <= elem
    lo = bound_search(target, lst, lower)
    print(lo)
    
@app.command()
def upper_bound(target: Annotated[int, typer.Option(help="The number want to find in list. For example, 2")],
                 lst: Annotated[list, typer.Option(help="The list what you guess the target exists, for example : 1 2 2 2 3 5")],
                 ):
    """ 
    Find the last index of target in list.
    """
    upper = lambda x, elem: x < elem
    lo = bound_search(target, lst, upper)
    print(lo+1)

if __name__ == "__main__":
    app()