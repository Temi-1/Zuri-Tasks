class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, newname):
        self.name = newname
        return self.name

    def change_age(self, newage):
        self.age = newage
        return self.age

    def add_track(self, newtrack):
        self.tracks.append(newtrack)
        return self.tracks
        
    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(f"Initial name: {Bob.name}")
print(f"Initial age: {Bob.age}")
print(f"Initial tracks: {Bob.tracks}")
print(f"Score: {Bob.score}")

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(f"Changed name: {Bob.name}")
print(f"Changed age: {Bob.age}")
print(f"Updated tracks list: {Bob.tracks}")
print(f"Score: {Bob.get_score()}")