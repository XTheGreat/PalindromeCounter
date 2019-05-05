# Program to count the number of palindromes in a file.

# parallel arrays for sorting.
list_palindromes = []
list_length = []

# returns true if word is palindrome
def is_Palindrome(word):
    val = False
    reverse = word[::-1]
    if(word==reverse):
        list_palindromes.append(word) # adds word to list of palindromes
        list_length.append(len(word))
        val = True
    return val
    
# returns count of palindrome
def  count_Palindromes(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            # remove new line character found in files
            if(is_Palindrome(line.rstrip('\n'))):
                count = count+1
    return count

# sorts values in the list of palindromes
# using the parallel array list_length values
def sort_Lists():
    list_Sorted = [x for _,x in sorted(zip(list_length,list_palindromes))]
    return list_Sorted

def writetoFile(filename):
    list_Sorted = sort_Lists()
    with open(filename, 'w') as f:
        for item in list_Sorted:
            f.write("%s\n" % item)

def main():
    filename = raw_input("Provide file path to read from: ")
    count = count_Palindromes(filename)
    print("There are "  + str(count) + " palindrome(s).")
    filename = raw_input("Provide file path to write to: ")
    writetoFile(filename)
    print("Saved!")

    
if __name__ == '__main__':
    main()
    
