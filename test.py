from hypothesis import given
import hypothesis.strategies as st 

from insertion_sort import insertion_sort
from mergesort import mergesort
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
def test_insertion_sort(l):
    n = len(l)
    insertion_sort(l)
    assert sorted(l) == True
    assert n == len(l)

@given(st.lists(st.integers()))
def test_mergesort(l):
    n = len(l)
    mergesort(l)
    assert sorted(l) == True
    assert n == len(l)

@given(st.lists(st.integers()))
def test_quicksort(l):
    ls = quicksort(l)
    assert sorted(ls) == True
    assert len(l) == len(ls)
