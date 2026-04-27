import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(mydataset)
print("---------------------")
print(myvar)
print("---------------------")
print(myvar['cars'])
print("---------------------")
print(myvar.loc[0])
print("---------------------")
print(myvar.loc[[0, 1]])

