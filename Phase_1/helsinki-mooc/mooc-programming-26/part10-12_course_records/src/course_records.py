# tee ratkaisusi tänne
# what a single course looks like
class Course:
    def __init__(self, name: str, credits: int, grade: int):
        self.__name = name
        self.__credits = credits
        self.__grade = grade

    @property
    def name(self):
        return self.__name

    @property
    def credits(self):
        return self.__credits

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, new_grade: int):
        if new_grade > self.grade:
            self.__grade = new_grade


# Managing the data
class StudyTracker:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, credits, grade)
        else:
            self.__courses[name].grade = grade

    def get_course(self, name: str):
        # if not found return none
        return self.__courses.get(name, None)

    def get_all(self):
        return self.__courses.values()


# The user interface
class StudyApplication:
    def __init__(self):
        self.__tracker = StudyTracker()

    def add_entry(self):
        name = input("Course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__tracker.add_course(name, grade, credits)

    def get_data(self):
        name = input("Course: ")
        course = self.__tracker.get_course(name)

        if course is None:
            print("no entry for this course")
        else:
            print(f"{course.name} ({course.credits} cr) grade {course.grade}")

    def statistics(self):
        courses = list(self.__tracker.get_all())
        count = len(courses)
        if count == 0:
            return

        total_credits = sum(credit.credits for credit in courses)
        mean = sum(credit.grade for credit in courses) / count

        print(f"{count} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")

        # Drawing the distribution

        for grades in range(5, 0, -1):
            stars = "x" * sum(1 for credit in courses if credit.grade == grades)
            print(f"{grades}: {stars}")

    def execute(self):
        print("1 add course\n2 get course date\n3 statistics\n0 exit")
        while True:
            cmd = input("command: ")
            if cmd == "0":
                break
            elif cmd == "1":
                self.add_entry()
            elif cmd == "2":
                self.get_data()
            elif cmd == "3":
                self.statistics()


# Final execution - NO indentation!
app = StudyApplication()
app.execute()
