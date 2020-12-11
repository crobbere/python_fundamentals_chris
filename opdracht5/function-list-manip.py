def list_manipulation(list, command, location, *arg):
    if command == "remove" and location == "end":
        return list.pop(len(list) -1)
    if command == "remove" and location =="beginning":
        return list.pop(0)
    if command =="add" and location=="beginning":
        list.insert(0, arg)
        return list
    if command =="add" and location=="end":
        list.append(arg)
        return list

my_list = [1,2,3,4,5]
print(list_manipulation(my_list, "add", "beginning", 69))
