import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column 1","Column 2","Column 3"])

result =df
result = df["Column 1"]
result = type(df["Column 1"])
result = df[["Column 1","Column 2"]]

# loc["row","column"] => loc["row"] => loc[:,"column"]
result = df.loc["A"]
result = type(df.loc["A"])
result = df.iloc[2]

result = df.loc[:,"Column 1"]
result = df.loc[:,["Column 1","Column 2"]]
result = df.loc[:,:"Column 2"]
result = df.loc["A":"B",:"Column 2"]
result = df.loc[:"B",:"Column 2"]
result =df.loc["A","Column 1"]
result = df.loc["C","Column 3"]
result = df.loc[["A","B"],["Column 1","Column 2"]]

df["Column 4"]= pd. Series(randn(3),["A","B","C"])
df["Column 5"]= df["Column 1"]+df["Column 3"]

# print(df.drop("Column 5",axis=1))

# result=df.drop("Column 5",axis=1,inplace=True)
result=df.drop("Column 5",axis=1,inplace=False)


print(result)
print(df)