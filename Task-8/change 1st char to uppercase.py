import pandas as pd
series = pd.Series(['he', 'is', 'a', 'good', 'boy'])
newSeries = series.str.title()
print("Resulting Series : ")
print(newSeries)


