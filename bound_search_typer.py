import typer
from typing import List

app = typer.Typer()

def bound_search(target: int,
                 lst: List[int],
                 compare,):
    
    lo, hi = 0, len(lst)
    while lo < hi : 
        mid = (lo + hi) // 2
        
        if compare(target, lst[mid]): 
            hi = mid
        else : 
            lo = mid + 1
    print(lo)
    return lo

@app.command()
def lower_bound(target: int=typer.Argument(...),
                 lst: List[int]=typer.Argument(...),
                 ):
    lower = lambda x, elem: x <= elem
    bound_search(target, lst, lower)
    
    
@app.command()
def upper_bound(target: int=typer.Argument(...),
                 lst: List[int]=typer.Argument(...),
                 ):
    upper = lambda x, elem: x < elem
    bound_search(target, lst, upper)


if __name__ == "__main__":
    app()