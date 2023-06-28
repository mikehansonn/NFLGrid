def recommend_names(user_input, names_list):
    matches = []
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching
    
    for name in names_list:
        if user_input in name.lower():
            matches.append(name)

    return matches


def main():
    # Read the names from the text file
    with open("players.txt", "r") as file:
        names_list = file.read().splitlines()

    while True:
        user_input = input("Enter a name or part of a name: ")
        recommendations = recommend_names(user_input, names_list)

        if recommendations:
            print("Recommendations:")
            print("\n".join(recommendations))
        else:
            print("No recommendations found.")

        # Exit the loop if the user enters an empty string
        if not user_input:
            break


if __name__ == '__main__':
    main()
