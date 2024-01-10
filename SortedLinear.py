# This program is meant to read the keyLinear, keyBinary, sortedLinearInput, and sortedBinaryInput in order to find the
# numbers of steps it takes to find the numbers in keyLinear and keyBinary with their respective methods as well as find
# the average of the number of steps it took for binary search and linear search.

def read_sort_lin():  # This function reads the numbers from the file sortedLinearInput and returns them as an array
    file = open("sortedLinearInput.txt", "r")  # Opens the file with read permissions
    lines = file.readlines()  # Reads each line of the file and sets it equal to lines
    linesNew = [int(x) for x in lines]  # Fills the array with the contents of each line and sets it equal to linesNew
    return linesNew  # Returns the array containing the numbers of the file


def read_key_lin():  # This function reads the numbers from the file keyLinear and returns them as an array
    file = open("keyLinear.txt", "r")  # Opens the file with read permissions
    line = file.readline()  # Reads each line of the file and sets it equal to line
    values = []  # Creates the values array

    for value in line.split(' '):  # For loop to iterate through the file
        values.append(int(value))  # Appends the values in the file to the array as integers

    return values  # Returns the array containing the numbers of the file


def read_sort_bin():  # This function reads the numbers from the file sortedBinaryInput and returns them as an array
    file = open("sortedBinaryInput.txt", "r")  # Opens the file with read permissions
    lines = file.readlines()  # Reads each line of the file and sets it equal to lines
    linesNew = [int(x) for x in lines]  # Fills the array with the numbers in each line set to the linesNew variable
    return linesNew  # Returns the array containing the numbers of the file


def read_key_bin():  # This function reads the numbers from the file keyBinary and returns them as an array
    file = open("keyBinary.txt", "r")  # Opens the file with the read permission
    line = file.readline()  # Reads the file line by line and sets it to line
    values = []  # Establishes the array values

    for value in line.split(' '):  # For loop to iterate through the file
        values.append(int(value))  # Appends the elements as int to the the array

    return values  # Returns the array of the file


def linear_search(lin_arr, x):  # This function does the linear_search of an array with integer and array parameters
    lin_steps = 0  # Establishes the steps the linear function takes
    for i in range(len(lin_arr)):  # Iterates through the length of the array
        lin_steps = lin_steps + 1  # Increases the amount of steps by 1 per each iteration
        if lin_arr[i] == x:  # If statement to check if the index of the array is the same as the number parameter
            return lin_steps  # Returns the amount of steps taken if x is found
    return lin_steps  # Returns the amount of steps taken to check if x is in array


def binary_search(bin_arr, y):  # This function does the binary_search of an array with integer and array parameters
    low = 0  # Establishes the lowest part of the array
    mid = len(bin_arr) // 2  # Establishes the middle of the array
    high = len(bin_arr) - 1  # Establishes the highest point of the array
    bin_steps = 0  # Establishes the numbers of steps needed to do binary_search

    while high >= low:  # Loops while the comparison is true
        bin_steps = bin_steps + 1  # Increases the steps needed for binary steps by 1 per each iteration
        mid = (high + low) // 2  # Sets mid equal to high + low // 2

        if bin_arr[mid] < y:  # If comparison to see if the element at the mid is less than the integer parameter
            low = mid + 1  # Sets low equal to mid + 1 if above is true
        elif bin_arr[mid] > y:  # Else if another comparison of integer parameter being less than mid element
            high = mid - 1  # Sets high equal to mid - 1 if above else if is true

        else:  # If none of the above cases are met do the statement below
            return bin_steps  # Returns the number of steps if no comparisons were met
    return bin_steps  # Returns the number of steps if the comparisons are met


def main():  # Start of main function
    sort_lin = read_sort_lin()  # Sets sort_lin equal to the call read_sort_lin function
    key_lin = read_key_lin()  # Sets key_lin equal to the call of read_key_lin function
    sort_bin = read_sort_bin()  # Sets sort_bin equal to the call of read_sort_bin function
    key_bin = read_key_bin()  # Sets key_bin equal to the call of read_key_bin function

    for i in range(len(key_lin)):  # Iterates through the range of the len of the array
        print("Number of steps for linear_search to find number at index", i, ":", linear_search(sort_lin, key_lin[i]))
        # Above print statement prints the call to the Linear_search function at each element in the keyLinear array

    avg_linear = 0.0  # Establishes the avg_linear as a float
    for e in range(len(key_lin)):  # Iterates through the range of the length of the array
        avg_linear += linear_search(sort_lin, key_lin[e])  # Increases the avg_linear by the call to linear_search of
        # the element in key_lin by looking through the sort_lin array

    avg_linear = avg_linear / len(key_lin)  # Sets the avg_linear equal to avg_linear divided by the length of key_lin
    print("Average number of steps for linear_search:", avg_linear, "\n")  # Prints the average numbers of steps

    for r in range(len(key_bin)):  # Iterates the range of the length of the key_bin array
        print("Number of steps for binary_search to find number at index", r, ":", binary_search(sort_bin, key_bin[r]))
        # The above statement prints the call to the binary_search function with the specified parameters

    avg_binary = 0.0  # Establishes the avg_binary as a float

    for w in range(len(key_bin)):  # Iterates through the range of the length of the key_bin array
        avg_binary += binary_search(sort_bin, key_bin[w])  # Increases avg_binary equal to the call of binary_search
        # with the specified parameters

    avg_binary = avg_binary / len(key_bin)  # Sets the avg_binary equal to avg_binary divided by the length of key_bin
    print("Average number of steps for binary_search:", avg_binary)  # Prints the average number of steps for
    # binary_search


main()  # Calls the main function
