def read_statics_from_file(path):
    statistics = []
    start_string = "Семестр"
    subject_mark_string = "Оцените предмет по шкале от 1 до 5:"
    teacher_mark_string = "Оцените качество преподавания курса по шкале от 1 до 5:"
    semester_key = "semester"
    course_key = "course"
    subject_key = "subject"
    teacher_key = "teacher"
    teacher_mark_key = "teacher_mark"
    subject_mark_key = "subject_mark"
    with open(path) as source:
        for line in source:
            line = line.strip().split(";")
            if line[0] == start_string:
                new_line = source.readline().strip().split(";")
                semester = new_line[0]
                course = new_line[1]
                new_line = source.readline().strip().split(";")
                if new_line[0] == teacher_mark_string:
                    second_line = source.readline()
                    teacher,subject,final_mark = extract_name_and_marks(new_line, second_line)
                    is_find = False
                    for stat in statistics:
                        if stat[semester_key] == semester and \
                                        stat[course_key] == course and \
                                        stat[subject_key] == subject and \
                                        stat[teacher_key] == teacher:
                            stat[teacher_mark_key] = final_mark
                            is_find = True
                    if not is_find:
                        statistics.append({semester_key: semester,
                                           course_key: course,
                                           teacher_key: teacher,
                                           subject_key: subject,
                                           subject_mark_key: 0,
                                           teacher_mark_key: final_mark})
                elif new_line[0] == subject_mark_string:
                    second_line = source.readline()
                    teacher,subject,final_mark = extract_name_and_marks(new_line, second_line)
                    is_find = False
                    for stat in statistics:
                        if stat[semester_key] == semester and \
                                        stat[course_key] == course and \
                                        stat[subject_key] == subject and \
                                        stat[teacher_key] == teacher:
                            stat[subject_mark_key] = final_mark
                            is_find = True
                    if not is_find:
                        statistics.append({semester_key: semester,
                                           course_key: course,
                                           teacher_key: teacher,
                                           subject_key: subject,
                                           subject_mark_key: final_mark,
                                           teacher_mark_key: 0})
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
    subject_key = "subject"
    teacher_key = "teacher"
    teacher_mark_key = "teacher_mark"
    subject_mark_key = "subject_mark"
    head = "Преподаватель;Предмет;Средняя оценка за предмет;Средняя оценка преподавателя\n"
    with open(path, "w") as out:
        out.write(head)
        for stat in statistics:
            out.write(stat[teacher_key] + ";"
                      + stat[subject_key] + ";"
                      + str(stat[subject_mark_key]) + ";"
                      + str(stat[teacher_mark_key]) + "\n")

def main():
    local_path = "./source.csv"
    local_path_write = "result.csv"
    statistics = read_statics_from_file(local_path)
    write_statistics_to_file(statistics,local_path_write)




if __name__ == "__main__":
    main()
