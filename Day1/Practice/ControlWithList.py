flag = True
names = ["Intkhab", "Mohit", "Manoj"]
while(flag):
    name = raw_input("Enter a name to add to the names list")
    if name in names:
        print("Name already exists in the list");
    else:
        names.append(name)
        print("Added the name in list, Updated list is: ", names)

    if(input("want to continue? type 1 for yes and 2 for no")==2):
        flag = False
