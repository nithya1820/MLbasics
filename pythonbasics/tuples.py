subjects=("hindi","english","math")
print(type(subjects))
print(subjects[0])
# subjects.insert("malayalam")
subjects+=("malayalam",)
subjects=list(subjects)
subjects[1]="English"
subjects=tuple(subjects)
print(subjects)