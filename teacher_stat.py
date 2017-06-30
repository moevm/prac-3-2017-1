def read_statics_from_file(path):
    statistics = []
    with open(path) as source:
        for line in source:
            line = line.strip().split(";")
            if line[0] == "Семестр":
                new_line = source.readline().strip().split(";")
                semester = new_line[0]
                course = new_line[1]
                new_line = source.readline().strip().split(";")
                if new_line[0] == "Оцените качество преподавания курса по шкале от 1 до 5:":
                    second_line = source.readline()
                    teacher,subject,final_mark = extract_name_and_marks(new_line, second_line)
                    is_find = False
                    for stat in statistics:
                        if stat["semester"] == semester and \
                                        stat["course"] == course and \
                                        stat["subject"] == subject and \
                                        stat["teacher"] == teacher:
                            stat["teacher_mark"] = final_mark
                            is_find = True
                    if not is_find:
                        statistics.append({"semester": semester,
                                           "course": course,
                                           "teacher": teacher,
                                           "subject": subject,
                                           "subject_mark": 0,
                                           "teacher_mark": final_mark})
                elif new_line[0] == "Оцените предмет по шкале от 1 до 5:":
                    second_line = source.readline()
                    teacher,subject,final_mark = extract_name_and_marks(new_line, second_line)
                    is_find = False
                    for stat in statistics:
                        if stat["semester"] == semester and \
                                        stat["course"] == course and \
                                        stat["subject"] == subject and \
                                        stat["teacher"] == teacher:
                            stat["subject_mark"] = final_mark
                            is_find = True
                    if not is_find:
                        statistics.append({"semester": semester,
                                           "course": course,
                                           "teacher": teacher,
                                           "subject": subject,
                                           "subject_mark": final_mark,
                                           "teacher_mark": 0})
                else:
                    continue
    return statistics


def extract_name_and_marks(new_line, second_line):
    teacher = new_line[1]
    subject = new_line[2]
    marks = second_line.strip().split(";")
    count_of_marks = len(marks)
    sum_of_marks = 0
    final_mark = 0
    for mark in marks:
        sum_of_marks += int(mark)
    if count_of_marks > 0:
        final_mark = sum_of_marks / count_of_marks
    return teacher,subject,final_mark


def write_statistics_to_file(statistics, path="result.csv"):
    with open(path, "w") as out:
        head = "Преподаватель;Предмет;Средняя оценка за предмет;Средняя оценка преподавателя\n"
        out.write(head)
        for stat in statistics:
            out.write(stat["teacher"] + ";"
                      + stat["subject"] + ";"
                      + str(stat["subject_mark"]) + ";"
                      + str(stat["teacher_mark"]) + "\n")

def main():
    local_path = "./source.csv"
    local_path_write = "result.csv"
    statistics = read_statics_from_file(local_path)
    write_statistics_to_file(statistics,local_path_write)




if __name__ == "__main__":
    main()
