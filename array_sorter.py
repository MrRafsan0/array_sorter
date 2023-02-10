user_array = []
while True:
    user_input = input("Enter Numbers to sort (or 'q' to quit): ")
    if user_input == "q":
        print("taking input finished")
        break
    user_array.append(int(user_input))
    print(user_array)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
sorted_array = bubble_sort(user_array)
print(sorted_array)
print("script completed")
#tried to learn while loop and buuble sorting
