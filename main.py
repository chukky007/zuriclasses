class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, newName):
        self.name = newName
        print('My name is ', self.name)

    def change_age(self, newAge):
        self.age = newAge
        print('And my age is ', self.age)

    def add_track(self, tracks):
        self.tracks.append(tracks)
        print('I am offering tracks ', self.tracks)

    def get_score(self):
        print('I got the following score ', self.score)
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Kamsi")
Bob.change_age(16)
Bob.add_track("UI/UX, Julia")
Bob.get_score()
