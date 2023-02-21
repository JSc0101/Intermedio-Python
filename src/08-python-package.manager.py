## python package manager ##

## pip
import numpy
import pandas
import requests
from package import arimethics

print(numpy.version.version)

arr = numpy.array([20,30,40,50,60,70])
print(arr * 2)

print(pandas.api.types)
response = requests.get("https://rickandmortyapi.com/api/character")
print(response.status_code)
data = response.json()
print(data)

# pip list
# pip unistall pandas
# pip show numpy

result = arimethics.sum(20,20)
print(result)
