"""practicing for a quiz."""
__author__ = "730321206"


def ayeee(x: str) -> int:
    """counts number of a's written."""
    i: int = 0
    a_counter: int = 0
    while len(x) > i:
        if x[i] == "a":
            a_counter += 1
        i = i + 1
    return a_counter


def ayooo1(a: str, b: str, c: str) -> bool:
    aye_a: int = ayeee(a)
    aye_b: int = ayeee(b)
    aye_c: int = ayeee(c)
    if aye_a > 10:
        return True
    if aye_b > 10:
        return True
    if aye_c > 10:
        return True
    else:
        return False


def ayooo2(a: str, b: str, c: str) -> bool:
    return ayeee(a) > 10 or ayeee(b) > 10 or ayeee(c) > 10


def yay_pass_fail(course_grade: float, major: str) -> float:
    pass_grade: int = 60
    final_weight: float
    target_exam_grade: float

    if major == "computer science":
        final_weight = .2
    else:
        if major == "chemistry" or major == "biology":
            final_weight = .4
        else:
            final_weight = .3
    rest_weight: float = 1 - final_weight
    target_exam_grade = (pass_grade - (course_grade + rest_weight)) / final_weight
    return target_exam_grade


def time_loop(password: str) -> int:
    count: int = 0
    user_input: str
    continue_loop: bool = True

    while continue_loop:
        count += 1
        user_input = input("You are in a time loop, enter the password to get out!")
        if user_input == password:
            continue_loop = False

    return count




