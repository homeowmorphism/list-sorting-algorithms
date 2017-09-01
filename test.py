from hypothesis import given
import hypothesis.strategies as st 
from quicksort import quicksort 

def sorted(l):
    if len(l) <= 1: 
        return True
    i = 0
    n = len(l)
    while i < (n-1):
        if l[i+1] < l[i]:
            return False
        i += 1
    return True

@given(st.lists(st.integers()))
def test(l):
    ls = quicksort(l)
    assert sorted(ls) == True
    assert len(l) == len(ls)

   
