class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name= new_name
        print(self.name, "is my name ")

    def change_age(self, new_age):
        self.age= new_age
        print(self.age, "is my age ")

    def add_track(self, new_tracks):
        self.tracks= new_tracks
        print(self.tracks, "is my track ")

     def get_score(self, score):
        self.score = score
    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(85.5)





