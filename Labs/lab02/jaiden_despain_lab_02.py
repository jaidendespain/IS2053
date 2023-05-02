# Scanning the file for numbers.
def file_scanner():
    text = open("Numbers_in_text.txt", "r")
    processed_list = []

    # Seperating individual strings text.
    for element in text:
        string = element.split()

        # Adding any numbers into 'processed_list[]'.
        for character in string:
            if character.isnumeric():
                processed_list.append(character)
    
    # Passing the numbers to be sorted.
    data_processor(processed_list)

# Finding the median number.
def data_processor(unsorted_list):
    # Converting the list to int values and sorting.
    unsorted_list = [int(i) for i in unsorted_list]
    sorted_list = (sorted(unsorted_list))

    # Finding the index of the median.
    median = int((len(sorted_list)) * 0.5)

    # Printing the median number.
    print(f"The median number is {sorted_list[median:median+1]}")

def main():
    file_scanner()

main()
