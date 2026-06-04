import pandas as pd

data = {
    "Name": ["Joe", "Jacob", "Alice"],
    "Age": [32, 25, 40]
}

df = pd.DataFrame(data)




def showLessThan(age):
    print(df.query('Age < @age'))
    

           

showLessThan(31)
