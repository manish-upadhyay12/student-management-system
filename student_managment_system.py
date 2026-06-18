
import csv
from pathlib import Path

def create_file():  # this is to create file
    try:

        path_name = input("enter name of the file:")
        path = Path(path_name)
        if not path.exists():
            with open(path, "w", newline="") as file:
                data = csv.DictWriter(file, fieldnames=["Name", "father_name", "age", "roll_number",
                                                        "college", "phone_number", "village"])
                data.writeheader()

                print("file created succfully")
        else:
            print("file already exist")

    except Exception as err:
        print(f"error occured{err}")


def read_file():  # this is to read file
    try:
        path_name = input("enter file name:")  # take file name or path
        path = Path(path_name)  # create object of path
        if path.exists():  # chekc if file exist or not
            while True:  # when write input come it stop
                try:   # chekeck is there any error
                    number = int(input(
                        " choose 1 to for roll_number to check detail of student:\n"
                        "choose 2 for name to check detail of student:\n"
                        "choose 3 to read whole data:"))  # take input numkber
                    break  # if input right then break execute
                except ValueError:
                    print("wrong input :only integer number allowed")
            with open(path, "r")as file:  # open file

                data = csv.DictReader(file)
                try:  # create reader object

                    if number == 1:
                        # condition for check data according to roll_number

                        # input roll_number
                        roll_number = input("input roll_number :")

                        for i in data:

                            # check detail according to rollnumber
                            if i["roll_number"] == roll_number:
                                print(i)  # then print detail
                                break
                            # if
                            # else:
                            #     print("RollNumber not found")

                                # this is for roll number
                except Exception as err:
                    print(f"error occured {err}")
                try:
                    if number == 2:
                        name = input("enter name of student:").lower()
                        found = False  
                        for j in data:
                            if j["Name"].lower() == name:
                                print(j)
                                found = True
                                break
                        if not found:
                            print("name not  found")
                            # else:
                            #     print("name not found")

                except Exception as err:
                    print(f"error occured {err}")
            try:
                if number == 3:  # if number is 3 so we can see whole data
                    with open(path, "r")as file:  # open file
                        data = csv.DictReader(file)
                        for i in data:
                            print(i)
            except Exception as err:
                print(f"error occured{err}")

    except Exception as err:
        print(f"error occured{err}")
# ----------------------------------------------------------------------------------------------


def update_file():

    try:

        path_name = input("enter file name:")
        path = Path(path_name)
        if path.exists():
            choice = int(input("1. choose 1 to change file name:\n"
                               "2. choose 2 to update student of data\n"
                               "3. choose 3 to add data "))
            if choice == 1:
                new_file = input("enter new name of file to change")
                path.rename(new_file)
                print("file name changes succssfully")
                # ----------------------------------------------------------
            elif choice == 2:
                print(["Name", "father_name", "age", "roll_number",
                       "college", "phone_number", "village"])

                allowed = ["Name", "father_name", "age", "roll_number",
                                                         "college", "phone_number", "village"]
                while True:
                    # this condition is for column what we want to change check input is wrong onot
                    change = input("what you want to change:")
                    if change in allowed:   # when change input is right loop break
                        break
                    print("Invailid input")

                new_data = input("enter new data:")  # new data
                # student rollnumber
                roll_number = input("enter roll_number of student")
                rows = []  # blank list
                with open(path, "r")as file:
                    data = csv.DictReader(file)  # object of dictreader
                    for row in data:
                        rows.append(row)  # add all data in list
                    found = False  # first imagine is rollnumber in data
                    for row in rows:
                        if row["roll_number"] == roll_number:
                            row[change] = new_data
                            found = True
                            print("update successfully")
                    if not found:  # when roll number not found in data
                        print("roll_number not found")
                with open(path, "w", newline="") as file:  # to overwrite when updation is complete write data one more time 
                    data = csv.DictWriter(file, fieldnames=["Name", "father_name", "age", "roll_number",
                                                            "college", "phone_number", "village"])
                    data.writeheader()  # write header
                    data.writerows(rows)  # write all rows of rows list in 
   # --------------------------------------------------------------------
            elif choice == 3:   # to add all dataof one student student 
                count = int(input("How many student data you want to add:"))
                for i in range(count):  
                    # loop to know how many student data we want to store
                    name = input("enter your name:")
                    father_name = input("enter your father_name:")
                    age = int(input("enter your age:"))
                    rollNumber = int(input("enter your roll number:"))
                    college = input("enter your college name:")
                    phone_number = input("enter  phone_number")
                    village = input("entet village name :")
                    with open(path, "a", newline="") as file:  # used to update the file use a mode to update or add data
                        data = csv.DictWriter(file,
                                              fieldnames=["Name", "father_name", "age", "roll_number", "college", "phone_number", "village"])

                        data.writerow({"Name": name, "father_name": father_name, "age": age, "roll_number": rollNumber,
                                       "college": college, "phone_number": phone_number, "village": village})
                        # ---------------------------------------------------------------

        else:
            print("file not exist")
    except Exception as err:
        print(f"error occured{err}")
# ----------------------------------------------------------------------


def delete_file():
    file_name = input("enter file name:")
    path = Path(file_name)
    if path.exists(): # check file exist or not
        while True:
            try:
                # choice show menue what you want to do delete whole file or single data of student
                choice = int(input("1. choose 1 to delete whole file "

                                   "2. choose 2 to delete student record:"))
                break
            except ValueError:
                print("integer number only")   # execute when wrong input 

        if choice == 1:  # delete whole file
            path.unlink()  # delete whole file
            print("file deleted successfully")
        else:
            print("file not deleted")  # if file not deleted else execute

        if choice == 2:   

            # delete one student data

            roll_number = input("enter roll_number of student: ")  #taking rollnumber
            with open(path, "r")as file:  # open file in readmode 
                content = csv.DictReader(file) 
                modified = [] # blak list
                for row in content: 
                    if row["roll_number"] != roll_number:  # skip iteration when rollnumber found
                        modified.append(row)   # add all rows of data 
            with open(path, "w", newline="")as file:   #rewrite the file and open file on write mode
                data = csv.DictWriter(file,
                                      fieldnames=["Name", "father_name", "age", "roll_number",
                                                  "college", "phone_number", "village"]) # creating object of dictwriter
                data.writeheader()  # write header
                data.writerows(modified) # write all rows second time

print("This is menue:")
print("enter 1 to create file")
print("enter 2 to read file")
print("enter 3 to update file")
print("enter 4 to delete file")
while True:
    try:
        choice = int(input("enter input number to perform operation: "))
        break
    except ValueError:
        print("error occured only integer number allowed")
if choice == 1:  
    create_file()  # function for creating file
elif choice == 2:
    read_file()  # function for reading  file
elif choice == 3:
    update_file()    # function for updating file
elif choice == 4:
        delete_file()
             # function for delete  file

    


# knowledgeable information
# 👉 csv.writer(file) ek writer object (tool / pen) banata hai
# 👉 Ye object directly file me kuch nahi likhta
# 👉 Ye sirf writing capability deta hai
# csv.writer()= file me structured data likhne ke liye hota hai
# writerow() =ek single row likhta hai
# newline="" =extra blank lines stop karta hai
# "w" mode= file ko overwrite karta hai
# csv module =import karna mandatory hai
# with open("student.csv","w",newline ="") as file:
#     data = csv.writer(file)
#     data.writerow(["a",10])
