class hall:
    def __init__(self, row, cols, hall_no) -> None:
        self.row = row
        self.cols = cols
        self.hall_no = hall_no
        self.shows = []

    def add_show(self, show_id, movie_name, time):
        self.shows.append({'id': show_id, 'movie_name': movie_name, 'time': time})
        self.seats = [["0" for _ in range(self.cols)] for _ in range(self.row)]
        
    def seat_book(self, show_id, seat_to_book):
        for seat in seat_to_book:
            rw, col = seat
            if self.seats[rw-1][col-1] == "0":
                self.seats[rw-1][col-1] = "1"
            else:
                print("Seat is already booked...")

    def show_list(self):
        print(f"Shows running in the hall {self.hall_no}")
        for show in self.shows:
            print(
                f"ID: {show['id']}, Movie: {show['movie_name']}, Time: {show['time']}")

    def available_seats(self):
        print("Available seats:")
        print("   " + " ".join([chr(i) for i in range(65, 65 + self.cols)]))
        for i in range(self.row):
            print("{:2d}".format(i + 1), end=" ")
            for j in range(self.cols):
                print(self.seats[i][j], end=" ")
            print()


def main():
    hall1 = hall(5, 6, 1)
    hall1.add_show(101, "Jawan", "8.00 PM")
    hall2 = hall(5, 6, 2)
    hall2.add_show(102, "Pathan", "10.30 PM")

    while True:
        print("\nWelcome to Star Cinema!\n")
        print("1. View all shows today")
        print("2. View available seats")
        print("3. Book a ticket")
        print("4. Exit")

        choice = input("Enter the option: ")

        if choice == "1":
            hall1.show_list()
            hall2.show_list()
        elif choice == "2":
            hall_choice = input("Enter the hall number (1 or 2): ")
            if hall_choice == "1":
                hall1.available_seats()
            elif hall_choice == "2":
                hall2.available_seats()
            else:
                print("Invalid hall number. Please try again.")
        elif choice == "3":
            show_id = input("Enter the id of the movie which you want to watch: ")
            seats = input("Enter the seat number you want to book(Give seat number like: 1A,2B): ")
            seats_to_book = [(int(seat[:-1]), ord(seat[-1]) - ord('A') + 1)
                             for seat in seats.split(',')]
            hall1.seat_book(show_id, seats_to_book)
            hall2.seat_book(show_id, seats_to_book)
            print("Ticket booked success...")
        elif choice == "4":
            print("Thanks for choosing Star Cinema.Have a GOOD DAY!!!")
            break
        else:
            print("Invalid Choise.Please choice again....")


if __name__ == "__main__":
    main()
