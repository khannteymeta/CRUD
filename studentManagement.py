import os
os.system("cls")
#list of student name
list_student_name  = [
    "meta",
    "metey",
    "yaya",
    "krita",
    "thanin",
    "teytey"
]

#list of student avrage score
list_stu_average_score  = [
    67,
    89,
    90,
    87,
    50,
]
#list of student id
list_student_id  = [
    1,2,3,4,5
]


#menu function
def menu ():
    print("-------Student management system-------")
    print("1. Display all student ")
    print("2. Add ")
    print("3. Search by name")
    print("4. Update by id ")
    print("5. Delete by id")
    print("6. Filter student by score")
    print("0. exit")
    print("-"*45)
    
    
    
def print_format_table(id, name, avg_score):
    #align header
    print(f"{id:<10} {name:<20} {avg_score:<20}")
def print_format_talbe_header():
    id = "ID"
    name = "Name"
    avg_score = "Average score"
    print(f"{id:<10} {name:<20} {avg_score:<20}")  
    print("-"*45)    
    
     
def display_student():
    print("----------Displlay all Student---------")
    #header func
    print_format_talbe_header()
    
    #loop through all info
    for i in range(len(list_student_name)):
        #print formart table from func
        print_format_table(list_student_id[i],list_student_name[i],list_stu_average_score[i])
              
def add_new_student():
    print("----------Add new Student----------")
    name = input("name : ")
    avg_score = float(input("avg_score : "))
    id = len(list_student_name)+1
    
    #append
    list_student_name.append(name)
    list_stu_average_score.append(avg_score)
    list_student_id.append(id)
    
def search_by_name():
    print("---------Search by name--------")
    search_name = input("Search name : ")
    #search index of student
    found =False
    
    #header format invoke form func
    print_format_talbe_header()
    for i in range(len(list_student_name)):
        if(search_name.lower() in list_student_name[i].lower()):
            print_format_table(list_student_id[i],list_student_name[i],list_stu_average_score[i])
            found = True 
       
    if found != True:
        print("not found")
        
        
def update_by_id():
    print("-------Update student id -------")
    #call function 
    display_student()
    id = int(input("Entet id  : "))
    try:
        index_student = list_student_id.index(id)
        name = input("name  : ")
        avg_score = float(input("Average score : "))
        list_student_name[index_student] = name
        list_stu_average_score[index_student] = avg_score
        print("Student updated")
    except Exception  as e:
        print(e)
        print("file is not found")   
         

add_new_student()
display_student()
    
    
    
    
   
        
    
    