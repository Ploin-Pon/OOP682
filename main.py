class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Dog's Name: {self.name}, Age: {self.age}")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

def main():
    my_dog = Dog("Buddy", 3)
    my_dog.info()
    your_dog = Dog("Max", 5)
    your_dog.info()
    print(my_dog)

if __name__ == "__main__":
    main()
