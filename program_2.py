def average_age():
    # Get User Input
    age_1 = int(input("Age of Person #1:"))
    age_2 = int(input("Age of Person #2:"))
    age_3 = int(input("Age of Person #3:"))
    age_4 = int(input("Age of Person #4:"))
    age_5 = int(input("Age of Person #5:"))

    # Sum ages
    combined_ages = age_1 + age_2 + age_3 + age_4 + age_5

    # Average the ages
    average_age_of_5_people = combined_ages / 5

    # Print the results
    print(average_age_of_5_people)

#Line which calls the above function.
average_age()