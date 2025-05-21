print("Theater Seats\n")
H = int(input("Enter number of rows: "))
L, M, R = 6, 10, 6
total_cols = L + M + R
seats = [['A'] * total_cols for _ in range(H)]
print("\nInitial Theater Layout:\n")
for _ in range(H):
    print('A' * L + '  ' + 'A' * M + '  ' + 'A' * R)
def display_seats():
    for row in seats:
        print(''.join(row[:L]) + '  ' + ''.join(row[L:L+M]) + '  ' + ''.join(row[L+M:]))
print("\nCurrent Seat Status:")
display_seats()
def book_seat():
    row = int(input("Enter row number: "))
    col = int(input("Enter seat number: "))
    if 0 <= row < H and 0 <= col < total_cols:
        if seats[row][col] == 'A':
            seats[row][col] = 'B'
            print("Seat booked.")
        else:
            print("Seat already booked.")
    else:
        print("Invalid seat.")
book_seat()
print("\nCurrent Seat Status:")
display_seats()
if input("Book another? (yes/no): ").lower() == 'yes':
    book_seat()
print("\nFinal Seat Layout:")
display_seats()