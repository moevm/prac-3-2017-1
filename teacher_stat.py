def read_statics_from_file(path):
    # make dict
    teachers = {}
    with open(path) as source:
        for line in source:
            line = line.strip().split(";")
            sum_of_marks = 0
            count_of_marks = 0
            final_mark = 0
            if line[0] == "Семестр":
                source.readline()
                new_line = source.readline().strip().split(";")
                if new_line[0] == "Оцените качество преподавания курса по шкале от 1 до 5:":
                    teacher = new_line[1]
                    subject = new_line[2]
                    marks = source.readline().strip().split(";")
                    for mark in marks:
                        sum_of_marks += int(mark)
                        count_of_marks += 1
                    if count_of_marks > 0:
                        final_mark = sum_of_marks / count_of_marks
                    if teacher in teachers:
                        if subject in teachers[teacher]:
                            teachers[teacher][subject]["teacher"] = final_mark
                        else:
                            teachers[teacher][subject] = {"teacher": final_mark}
                    else:
                        teachers[teacher] = {subject: {"teacher": final_mark}}
                elif new_line[0] == "Оцените предмет по шкале от 1 до 5:":
                    teacher = new_line[1]
                    subject = new_line[2]
                    marks = source.readline().strip().split(";")
                    for mark in marks:
                        sum_of_marks += int(mark)
                        count_of_marks += 1
                    if count_of_marks > 0:
                        final_mark = sum_of_marks / count_of_marks
                    if teacher in teachers:
                        if subject in teachers[teacher]:
                            teachers[teacher][subject]["subject"] = final_mark
                        else:
                            teachers[teacher][subject] = {"subject": final_mark}

                    else:
                        teachers[teacher] = {subject: {"subject": final_mark}}
                else:
                    continue
    return teachers


def write_statistics_to_file(teachers):
    with open("result.csv", "w") as out:
        out.write("Преподаватель;Предмет;Средняя оценка за предмет;Средняя оценка преподавателя\n")
        for teacher in teachers:
            for sub in teachers[teacher]:
                out.write(teacher + ";" + sub + ";" + str(teachers[teacher][sub]["subject"])
                          + ";" + str(teachers[teacher][sub]["teacher"]) + "\n")


def main():
    local_path = "./source.csv"
    teachers = read_statics_from_file(local_path)
    write_statistics_to_file(teachers)


if __name__ == "__main__":
    main()




