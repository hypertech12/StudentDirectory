import sys
studentrecords = [
    
    [ 12345, "Jonathan", "Waters", 1850,   "Prairie City Rd", "Folsom",         "CA", 95630, 9161234567 ],
    [ 12346, "Jonah",    "Rivers", 650,    "Main Street",     "Folsom",         "CA", 95630, 9161236789 ],
    [ 12347, "Abigail",  "Mill",   1234,   "Folsom Blvd",     "Folsom",         "CA", 95630, 9161245678 ],
    [ 12348, "Bobby",   "Miller",   456789, "Mills Street",    "Rancho Cordova", "CA", 95670, 9162347890 ],
    [ 12349, "Billy",    "Harrison", 4567,   "Zinfandal Dr",    "Rancho Cordova", "CA", 95670, 9160987654 ]
]
line = "-"*40

def add_student(): #adds a student to the student records
    print(line)
    
    ID =int(input("Enter 5 digit id number:"))
    while(validate_Id(ID) == False):
        ID = int(input("Id must be 5 digits. Please enter valid ID:"))

    Name = str(input("Enter First name and Last Name with a space:"))
    while(validate_First_LastName(Name) == False):#keeps asking until the correct input is set
        Name = str(input("Enter First Name and Last Name with a space"))
    if (True): # sets the ID into studentrecords by changing the values within the list
        ID = Name.lower().split()
        x = ID[0][0].upper()
        y = ID[1][0].upper()
        z = x+ID[0][1:] + " " + y+ID[1][1:]
        ID.clear()
        ID.append(z)
        
    street = int(input("Enter street number:"))
    while(validate_streetnum(street) == False):
        street = int(input("Enter street number:"))
    if (True):
        ID.append(street)

    city = str(input("Enter city name(15 letters max):"))
    while(validate_city(city) == False):
        city = str(input("Enter city name(15 letters max):"))
    if (True):
        ID.append(city)
    state = str(input("Enter State(2 letters only):"))
    while(validate_State(state) == False):
        state = str(input("Enter State(2 letters only):"))
    if (True):
        ID.append(state)

    zip_code = int(input("Enter zip code 5 digits only:"))
    while validate_zipcode(zip_code) == False:
        zip_code = int(input("Enter zip code 5 digits only:"))
    if (True):
        ID.append(zip_code)
        
    phone_number = int(input("Enter 10 digit phone number:"))
    while(validate_phonenum(phone_number) == False):
        phone_number = int(input("Enter a 10 digit phone number:"))
    if (True):
        ID.append(phone_number)
    print(ID)
    user_input = input("Do you want to add this record to studentrecords?(Yes or No)")
    if user_input == "Yes" or user_input == "yes":
        studentrecords.append(ID)
        print("You have added a new record")
    elif ID in studentrecords:
        print("The record exists")
    else:
        print("You didn't add any record")

def print_menu():#prints the menu where the user can input an option
    print("1.Student_Record")
    print("2.Add")
    print("3.Update")
    print("4.Remove")
    print("5.Search")
    print("6.Print Report")
    print("7.Exit")
 #Validations of functions   
def validate_Id(ID):
    if len(str(ID)) == 5:
        return True
    else:
        return False

def validate_First_LastName(Name):
    if len(Name) <= 15 and " " in Name:
        return True
    else:
        return False

def validate_State(state):
    if len(state) > 2 or len(state) < 2:
        return False
    else:
        return True
        ID.append(state)

def validate_streetnum(street):
    if len(str(street)) <= 6:
        return True
        ID.append(street)
    else:
        return False
def validate_city(city):
    if len(city) > 15:
        return False
    else:
        return True
        ID.append(city)
def validate_zipcode(zip_code):
    if len(str(zip_code)) == 5:
        return True
        ID.append(zip_code)
    else:
        return False

def validate_phonenum(phone_number):
    if len(str(phone_number)) == 10:
        return True
        ID.append(phone_number)
    else:
        return False
       
def update_student_byId():#updates the student ID 
    print(line)
    print("U1.Update by ID")
    i = 0
    ID = int(input("Enter 5 digit id"))
    while(validate_Id(ID) == False):
        ID = int(input("Enter new id(5 digit):"))
    
    Name = input("Enter First name and Last name with a space:")
    while(validate_First_LastName(Name) == False):
        Name = input("Enter First name and lastname with a space:")
        
    if (True):
        ID = Name.lower().split()
        x = ID[0][0].upper()
        y = ID[1][0].upper()
        z = x+ID[0][1:] + " " + y+ID[1][1:]
        ID.clear()
        ID.append(z)
                                                    
    street = int(input("Enter street number:"))
    while(validate_streetnum(street) == False):
        street = int(input("Enter street number:"))
    if (True):
        ID.append(street)

    city = str(input("Enter city name(15 letters max):"))
    while(validate_city(city) == False):
        city = str(input("Enter city name(15 letters max):"))
    if (True):
        ID.append(city)
    state = str(input("Enter State(2 letters only):"))
    while(validate_State(state) == False):
        state = str(input("Enter State(2 letters only):"))
    if (True):
        ID.append(state)

    zip_code = int(input("Enter zip code 5 digits only:"))
    while validate_zipcode(zip_code) == False:
        zip_code = int(input("Enter zip code 5 digits only:"))
    if (True):
        ID.append(zip_code)
        
    phone_number = int(input("Enter 10 digit phone number:"))
    while(validate_phonenum(phone_number) == False):
        phone_number = int(input("Enter a 10 digit phone number:"))
    if (True):
        ID.append(phone_number)
        print("You have updated the studentrecords")
        studentrecords.append(ID)
        print(studentrecords)
        i = 1      
    if(i == 0):
        print("The id you entered isn't in the list")

def update_student_byFirstName_LastName():
    print(line)
    print("U2/U3. Update by First and Last Name")
    i = 0
    filtered_list=[]
    p = str(input("Enter first name or lastname"))
    while len(filtered_list) < 1:       #updates the student records for the first and last name
        for x in (studentrecords):
            if p in x[1] or p in x[2]:
                filtered_list.append(x)
                i += 1
                print(i,x)
        if len(filtered_list) < 1:
            p = str(input("The name you inputed isn't inside student records. Enter again"))
            
                
    a = int(input("Select a number to update that list:"))

    
    y = filtered_list[a-1] #removes the previous value within the list
    if y in studentrecords:
        studentrecords.remove(y)

    ID = int(input("Enter 5 digit id:"))
    while(validate_Id(ID) == False):
        ID = int(input("Enter new id(5 digit):"))
                
    Name = input("Enter First name and Last name with a space:")
    while(validate_First_LastName(Name) == False):
        Name = input("Enter First name and lastname with a space:")
                            
    if (True):
        ID = Name.lower().split()
        x = ID[0][0].upper()
        y = ID[1][0].upper()
        z = x+ID[0][1:] + " " + y+ID[1][1:]
        ID.clear()
        ID.append(z)
                            
    street = int(input("Enter 6 digit street number:"))
    while(validate_streetnum(street) == False):
        street = int(input("Enter 6 digit street number:"))
    if (True):
        ID.append(street)

    city = str(input("Enter city name(15 letters max):"))
    while(validate_city(city) == False):
        city = str(input("Enter city name(15 letters max):"))
    if (True):
        ID.append(city)
    state = str(input("Enter State(2 letters only):"))
    while(validate_State(state) == False):
        state = str(input("Enter State(2 letters only):"))
    if (True):
        ID.append(state)

    zip_code = int(input("Enter zip code 5 digits only:"))
    while validate_zipcode(zip_code) == False:
        zip_code = int(input("Enter zip code 5 digits only:"))
    if (True):
        ID.append(zip_code)
        
    phone_number = int(input("Enter 10 digit phone number:"))
    while(validate_phonenum(phone_number) == False):
        phone_number = int(input("Enter a 10 digit phone number:"))
    if (True):
        ID.append(phone_number)
                            
    print("You have updated the studentrecords")
    studentrecords.append(ID)
    print(studentrecords)      
    
             
def search_student(): #Searches the student in the records
    print(line)
    print("Search Student")
    name = str(input("Input to search the database:"))
    for row in studentrecords:
        if name in row:
            print(name, " is found in the student records")
            break
    else:
        print("No record has been found")

def remove_student_byID(): #Removes the student by ID
    print(line)
    print("D1.Remove by Id")
    i = 0
    z = int(input("Enter id:"))
    a ='no'   
    for x in studentrecords:
        if z in x:
            print(x)
            i = 1
            a = input("Do you want to delete that record(yes or no)?")
            break
        
    if(i == 0):
        print("No record found")
        
    if(a == "Yes" or a == "yes"):
        studentrecords.remove(x)
        print(studentrecords)
        print("You have deleted the record")
    elif(a == "No" or a == "no"):
        print("No record has been deleted")
#Sorts by ID, First Name, LastName, or City
def Sort_by_Id():
    print(line)
    print("Sort by Id")
    studentrecords.sort()
    print(studentrecords)
def Sort_by_FirstName():
    print(line)
    print("Sort by First Name")
    for x in studentrecords:
        studentrecords.sort()
    print(studentrecords)

def Sort_by_LastName():
    print(line)
    print("Sort by Last Name")
    studentrecords.sort()
    print(studentrecords)

def Sort_by_City():
    print(line)
    print("Sort by City")
    studentrecords.sort()
    print(studentrecords)
    

def Print_Report():#Takes a user input which can sort by ID, First and Last name, and by city
    print(line)
    a = str(input("Choose 1.Sort by Id / 2.Sort by First Name / 3.Sort by Last Name / 4.Sort by city (Choose 1-4)"))
    if (a == "1"):
        Sort_by_Id()
    elif a == "2":
        Sort_by_FirstName()
    elif a == "3":
        Sort_by_LastName()
    elif a == "4":
        Sort_by_City()
        
        
while (True): # Functions are called and user can make a selection from 1-7 to use the function
    print_menu()
    choice = input("Make a selection from the above menu(1-7):")
    print(choice)
    if(choice == "7"):
        sys.exit()
    elif (choice == "2"):
        add_student()
    elif (choice == "3"):
        update_student_byId()
        #update_student_byFirstName_LastName()
    elif (choice == "4"):
        remove_student_byID()
    elif (choice == "5"):
        search_student()
    elif (choice == "1"):
        print(studentrecords)
    elif (choice == "6"):
        Print_Report()
