# set file or path
path = "./source.csv"

# make dict
teachers = {}

# open file
with open(path) as source:
    for line in source:
        line = line.strip().split(";")
        marks = []
        teacher = ""
        subject = ""
        sumOfMarks = 0
        countOfMarks = 0
        finalMark = 0
        if line[0] == "Семестр":
            newLine = source.readline()
            newLine = source.readline().strip().split(";")
            if newLine[0] == "Оцените качество преподавания курса по шкале от 1 до 5:":
                teacher = newLine[1]
                subject = newLine[2]
                marks = source.readline().strip().split(";")
                for mark in marks:
                    sumOfMarks += int(mark)
                    countOfMarks += 1
                if countOfMarks > 0:
                    finalMark = sumOfMarks / countOfMarks
                if teacher in teachers:
                    if subject in teachers[teacher]:
                        teachers[teacher][subject]["teacher"] = finalMark
                    else:
                        teachers[teacher][subject] = {"teacher":finalMark}
                else:
                    teachers[teacher] = {subject: {"teacher": finalMark}}
            elif newLine[0] == "Оцените предмет по шкале от 1 до 5:":
                teacher = newLine[1]
                subject = newLine[2]
                marks = source.readline().strip().split(";")
                for mark in marks:
                    sumOfMarks += int(mark)
                    countOfMarks += 1
                if countOfMarks > 0:
                    finalMark = sumOfMarks / countOfMarks
                if teacher in teachers:
                    if subject in teachers[teacher]:
                        teachers[teacher][subject]["subject"] = finalMark
                    else:
                        teachers[teacher][subject] = {"subject":finalMark}

                else:
                    teachers[teacher] = {subject: {"subject": finalMark}}
            else:
                continue
print(teachers)
# write results
with open("result.csv","w") as out:
    out.write("Преподаватель;Предмет;Средняя оценка за предмет;Средняя оценка преподавателя\n")
    for teacher in teachers:
        for sub in teachers[teacher]:
            out.write(teacher + ";" + sub + ";" + str(teachers[teacher][sub]["subject"])
                                                      + ";" + str(teachers[teacher][sub]["teacher"] ) + "\n")

