def Tower_Of_Hanoi_using_Recursion(n, source, destination, auxiliary):
    # Base condition
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return

    Tower_Of_Hanoi_using_Recursion(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    Tower_Of_Hanoi_using_Recursion(n - 1, auxiliary, destination, source)


# Driver code
print("Enter the no. of dishes")
no_of_dish = int(input())
Tower_Of_Hanoi_using_Recursion(no_of_dish, 'X', 'Y', 'Z')
# X, Y, Z are the name of rods