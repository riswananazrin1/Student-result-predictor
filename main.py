import pandas as pd
df = pd.read_csv("students.csv")
print(df)
print("number of students:",len(df))
print("average study hours:",df["hours_studied"].mean())
print("highest study hours:",df["hours_studied"].max())
print("lowest study hours:",df["hours_studied"].min())
passed_students=df[df["result"]=="Pass"]
failed_students=df[df["result"]=="Fail"]
print("number of passed students:",len(passed_students))
print("number of failed students:",len(failed_students))
pass_percentage = (len(passed_students)/len(df)*100)
print("pass percentage :", pass_percentage)