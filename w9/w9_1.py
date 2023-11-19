
def employees(dict_list):
    count = int(input("How many employees do you want to add?:\n"))
    while count != 0:
        count -= 1
        name = input("Enter worker's name:\n")
        workplace = input("Enter worker's workplace:\n")
        age = int(input("Enter worker's age:\n"))

        dict_list.append({"Name" : name, "Workplace" : workplace, "Age" : age})

def print_work_info(dict_list):
    print("List of Employees:")
    for line in dict_list:
        print(f"Name: {line.get('Name')}", end=", ")
        print(f"Workplace: {line.get('Workplace')}", end=", ")
        print(f"Age: {line.get('Age')}")

dict_list = []

employees(dict_list)
print_work_info(dict_list)
