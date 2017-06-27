def read_statics_from_file(path):
    # make dictionary
    statistics = {}
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
                    if semester in statistics:
                        if course in statistics[semester]:
                            if teacher in statistics[semester][course]:
                                if subject in statistics[semester][course][teacher]:
                                    statistics[semester][course][teacher][subject]["teacher"] = final_mark
                                else:
                                    statistics[semester][course][teacher][subject] = {"teacher": final_mark,"subject": 0}
                            else:
                                statistics[semester][course][teacher] = {subject: {"teacher": final_mark, "subject": 0}}
                        else:
                            statistics[semester][course] = {teacher: {subject: {"teacher": final_mark, "subject": 0}}}
                    else:
                        statistics[semester] = {course: {teacher: {subject: {"teacher": final_mark, "subject": 0}}}}

                elif new_line[0] == "Оцените предмет по шкале от 1 до 5:":
                    second_line = source.readline()
                    teacher,subject,final_mark = extract_name_and_marks(new_line, second_line)
                    if semester in statistics:
                        if course in statistics[semester]:
                            if teacher in statistics[semester][course]:
                                if subject in statistics[semester][course][teacher]:
                                    statistics[semester][course][teacher][subject]["subject"] = final_mark
                                else:
                                    statistics[semester][course][teacher][subject] = {"teacher": 0, "subject": final_mark}
                            else:
                                statistics[semester][course][teacher] = {subject: {"teacher": 0, "subject": final_mark}}
                        else:
                            statistics[semester][course] = {teacher: {subject: {"teacher": 0, "subject": final_mark}}}
                    else:
                        statistics[semester] = {course: {teacher: {subject: {"teacher": 0, "subject": final_mark}}}}
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
        for semester in statistics:
            for course in statistics[semester]:
                for teacher in statistics[semester][course]:
                    for sub in statistics[semester][course][teacher]:
                        out.write(teacher + ";"
                                  + sub + ";"
                                  + str(statistics[semester][course][teacher][sub]["subject"]) + ";"
                                  + str(statistics[semester][course][teacher][sub]["teacher"]) + "\n")



def main():
    local_path = "./source.csv"
    local_path_write = "result.csv"
    statistics = read_statics_from_file(local_path)
    write_statistics_to_file(statistics,local_path_write)


if __name__ == "__main__":
    main()
