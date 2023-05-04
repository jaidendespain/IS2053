# close the open file.
def close_file(file):
    file.close()

# read and print the file contents.
def read_file():
    text_file = open("C:/Users/Jaiden/Desktop/FunWithFiles.txt", "r")

    line_one = text_file.readline()
    line_two = text_file.readline()
    line_three = text_file.readline()
    print(f"{line_one}{line_two}{line_three}")

    close_file(text_file)

# add the user's favorite movie to the file.
def add_movie():
    favorite_movie = input("What's your favorite movie? \n")
    text_file = open("C:/Users/Jaiden/Desktop/Movies.txt", "a")
    text_file.write(f"\n{favorite_movie}" + "")

    close_file(text_file)

# main function.
def main():
    read_file()
    add_movie()

main()
