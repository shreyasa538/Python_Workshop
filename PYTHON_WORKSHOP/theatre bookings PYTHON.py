sections = {'a': [["🟩"]*10 for _ in range(10)],
            'b': [["🟩"]*10 for _ in range(10)],
            'c': [["🟩"]*10 for _ in range(10)]}

number_of_seats = int(input("Enter number of seats to book: "))
if number_of_seats > 10:
    print("Cannot book more than 10 seats in a row.")
    exit()
s=[[],[],[]]
for i in range(number_of_seats):
    print(f"{i+1} Booking:")
    section = input("Enter section (a, b, c): ").lower()
    if section not in sections:
        print("Invalid section. Please try again.")
        break
    else:
        s.append(sections[section])
        row = int(input("Enter row number (0-9): "))
        col = int(input("Enter column number (0-9): "))
        if 0 <= row < 10 and 0 <= col < 10:
            if sections[section][row][col] == "🟩":
                sections[section][row][col] = "😁"
                print(f"Seat booked: {section.upper()} Row {row} Seat {col}")
            else:
                print("Seat already booked!")
        else:
            print("Invalid seat number. Please try again.")
            break   

print("\nCurrent seating arrangement:")
for row in range(10):
    row_display = []
    for sec in 'abc':
        row_display.append(' '.join(sections[sec][row]))
    print('   '.join(row_display))
