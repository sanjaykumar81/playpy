class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    average_score = 0

    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        average_score = sum(self.scores) / len(self.scores)

        if 90 <= average_score <= 100:
            return 'O'
        if 80 <= average_score < 90:
            return 'E'
        if 70 <= average_score < 80:
            return 'A'
        if 55 <= average_score < 70:
            return 'P'
        if 40 <= average_score < 55:
            return 'D'
        if average_score < 40:
            return 'T'


if __name__ == "__main__":
    line = "Heraldo Memelli 8135627".split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = "100 80 40"  # not needed for Python
    scores = list(map(int, numScores.split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
