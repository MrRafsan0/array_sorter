user_array = []
while True:
    user_input = input("Enter Numbers to sort (or 'q' to quit): ") #taking input here.
    if user_input == "q": #checking if the user wants to quit
        print("taking input finished") #just for debugging
        break
    user_array.append(int(user_input)) #adding input into the user_array. if you don't use int func then the input will be stored as a string and the script will no longer sort.
    print(user_array)
def bubble_sort(arr):
    n = len(arr) #to get how long the for loop needs to run. for ex: if user_array = [2, 3] the len(arr) will be 2 and the for loop will run accourdingly
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
sorted_array = bubble_sort(user_array)
print(sorted_array)
print("script completed")
#tried to learn while loop and buuble sorting
