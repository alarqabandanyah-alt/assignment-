# Movie Manager App

class Movie:
    def __init__(self, name, rating, minutes):
        self.name = name
        self.rating = rating
        self.minutes = minutes

    def show_movie(self):
        print(f"{self.name} - Rating: {self.rating}/10 - {self.minutes} minutes")


movie1 = Movie("The Hunger Games", 9, 142)
movie1.show_movie()


class ActionMovie(Movie):
    def __init__(self, name, rating, minutes, has_fighting):
        super().__init__(name, rating, minutes)
        self.has_fighting = has_fighting

    def show_movie(self):
        print(f"{self.name} is an action movie!")


action1 = ActionMovie("Avengers", 9, 143, True)
action1.show_movie()


class ComedyMovie(Movie):
    def __init__(self, name, rating, minutes, is_funny):
        super().__init__(name, rating, minutes)
        self.is_funny = is_funny

    def show_movie(self):
        print(f"{self.name} is a comedy movie!")


comedy1 = ComedyMovie("The Mask", 8, 101, True)
comedy1.show_movie()


class MovieManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):
        print("\n===== MOVIES =====")

        for number, movie in enumerate(self.movies, 1):
            print(f"{number}. ", end="")
            movie.show_movie()

    def total_minutes(self):
        total = 0

        for movie in self.movies:
            total += movie.minutes

        print(f"Total movie minutes: {total}")

    def menu(self):
        while True:
            print("\n===== MOVIE MANAGER =====")
            print("1. Show movies")
            print("2. Total movie minutes")
            print("3. Add movie")
            print("4. Quit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.show_movies()

            elif choice == "2":
                self.total_minutes()

            elif choice == "3":
                name = input("Enter movie name: ")

                try:
                    rating = int(input("Enter movie rating: "))
                    minutes = int(input("Enter movie minutes: "))

                    new_movie = Movie(name, rating, minutes)
                    self.add_movie(new_movie)

                    print(f"{name} was added!")

                except ValueError:
                    print("Please enter numbers for the rating and minutes.")

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Please choose 1, 2, 3, or 4.")


manager = MovieManager()

movie2 = Movie("Titanic", 9, 195)
action2 = ActionMovie("Black Panther", 8, 134, True)

manager.add_movie(movie1)
manager.add_movie(action1)
manager.add_movie(comedy1)
manager.add_movie(movie2)
manager.add_movie(action2)

manager.menu() 
