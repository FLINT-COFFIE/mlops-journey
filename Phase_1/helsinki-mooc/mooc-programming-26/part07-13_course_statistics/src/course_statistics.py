# Write your solution here
# reading json files
# import urllib.request
# my_request = urllib.request.urlopen("https://helsinki.fi")
# print(my_request.read())

### Part 1

# importing json
import json
import urllib.request


def retrieve_all():
    # making the request
    site_info = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    my_request = urllib.request.urlopen(site_info)
    data = my_request.read()

    courses = json.loads(data)
    enabled_courses = []

    final_list = []

    for course in courses:
        if course["enabled"]:
            enabled_courses.append(course)
    # print(enabled_courses)

    for course in enabled_courses:
        course_info = (
            course["fullName"],
            course["name"],
            course["year"],
            sum(course["exercises"]),
        )
        final_list.append(course_info)
    return final_list


### Part 2


def retrieve_course(course_name: str):
    site_info = (
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    )
    my_request = urllib.request.urlopen(site_info)
    data = my_request.read()

    course_info = json.loads(data)

    # print(course_info)
    final_info = {}

    # defining variables
    weeks = len(course_info)

    students = []
    hours = []
    exercises = []

    # updating dictionary
    final_info["weeks"] = weeks

    for week in course_info:
        students.append(course_info[week]["students"])
        hours.append(course_info[week]["hour_total"])
        exercises.append(course_info[week]["exercise_total"])

    # final values
    max_students = max(students)
    hours_average = sum(hours) // max_students
    exercises_average = sum(exercises) // max_students

    # updating final_info
    final_info["students"] = max_students
    final_info["hours"] = sum(hours)
    final_info["hours_average"] = hours_average
    final_info["exercises"] = sum(exercises)
    final_info["exercises_average"] = exercises_average

    # returning final info
    return final_info
    # print(final_info)


# testing
if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")
