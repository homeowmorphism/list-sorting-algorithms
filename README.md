# Common list sorting algorithms 

Easy to read Python implementations with helpful print statements for a faciliatated understanding of insertion sort, mergesort and quicksort. 

Test file uses [pytest](https://docs.pytest.org/en/latest/) and [hypothesis](https://docs.pytest.org/en/latest/) to introduce the reader to use these good packages if he doesn't have them already. Test file is not crucial to usage or understanding of algorithm.

## Run

```
$ python 
from insertion_sort import insertion_sort
from mergesort import mergesort 
from quicksort import quicksort

>>> l1 = [5,4,2,3,1]
>>> l2 = [4,2,3,1,5]
>>> l3 = [1,2,3,5,4]

>>> insertion_sort(l1)
>>> mergesort(l2)
>>> quicksort(l3)

```

## Run test

You will need [pytest](https://docs.pytest.org/en/latest/) to run `test.py` as well as the [hypothesis](https://hypothesis.readthedocs.io/en/latest/) library. 

```
brew install pytest
pip install hypothesis
```

If everything works correctly you should be able to type the following command without any errors. 

```
pytest test.py
```


