import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn import tree
def train_model():
    df= pd.read_csv("students.csv")

    print(df)
    x = df[["hours_studied", "attendence", "assignment_score"]]
    y= df["result"]
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(x_train,y_train)
    return model,x,y, x_test,y_test
model, x, y, x_test, y_test = train_model()
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy * 100, "%")
cm = confusion_matrix(y_test, y_pred)
print("\nconfusion matrix:")
print(cm)
print("\nClassification Report:")
print(classification_report(y_test,y_pred ))
plt.figure(figsize=(12,8))
tree.plot_tree(model,feature_names=x.columns,class_names=model.classes_,filled=True)
plt.savefig("decision_tree.png")
plt.show()
n = int(input("enter number of students:"))
students = []
for i in range(n):
    print("\nstudent",i+1)
    hours= float(input("enter hours studied:"))
    attendence = float(input("enter attendence:"))
    assignment = float(input("enter assignment score:"))
    students.append([hours, attendence, assignment])
    students_df = pd.DataFrame(students,columns=["hours_studied","attendence","assignment_score"])
predictions = model.predict(students_df)
print("\n-----Results-----")
for i in range(len(predictions)):
    print(f"student{i+1}prediction:",predictions[i])
pass_count=0
for result in predictions:
    if result== "Pass":
        pass_count += 1
fail_count = len(predictions) - pass_count
pass_percentage = (pass_count/len(predictions)) * 100

print("\n----summary----")
print("passed students:",pass_count)
print("failed students:",fail_count)
print("pass percentage:",pass_percentage,"%" )
results_df = pd.DataFrame({"student_ID":range(1, len(students)+1),"Hours_studied":[student[0] for student in students],"Attendence":[student[1] for student in students],"Assignment_score":[student[2]for student in students], "prediction": predictions})
results_df.to_csv("predicted_results.csv",index=False)
print("Results saved to predicted_results.csv")