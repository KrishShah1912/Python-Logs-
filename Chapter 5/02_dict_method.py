x = {} # it will create empty dictionary

marks = {

    "krish" : 100,
    "Rahul" : 39, 
    "Shubham" : 89,
    "Rudra" : 57
}

print(marks.items()) # here it will provide the whole dict 

print(marks.keys()) # here left hand side will be printed like krish, rahul, shubham

print(marks.values()) # here right side will be printed like 100, 39, 89

marks.update({"krish" : 97}) # here krish marks will be changed (updated)

marks. update({"Harsh" : 45}) # here we can add another list data items 

print(marks)

print(marks.get("krish")) # here it will displayed marks of krish , if we enter Rohan then it will print none beocz we don't have any person name rohan
