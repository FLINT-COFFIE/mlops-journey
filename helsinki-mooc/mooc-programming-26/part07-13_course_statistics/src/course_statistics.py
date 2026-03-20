# Write your solution here
# reading json files
"""import urllib.request

my_request = urllib.request.urlopen("https://helsinki.fi")
print(my_request.read())
"""

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
    print(enabled_courses)

    for course in enabled_courses:
        course_info = (
            course["fullName"],
            course["name"],
            course["year"],
            sum(course["exercises"]),
        )
        final_list.append(course_info)
    print(final_list)


retrieve_all()
