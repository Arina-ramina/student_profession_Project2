import json
def load_students():
    '''
    загрузка студентов из файла
    '''
    with open ('students.json') as f:
        students = json.load(f)
        return students

def load_professions():
    '''
    загрузка профессий из файла
    '''
    with open ('professions.json') as f:
        professions = json.load(f)
        return professions

def get_student_by_pk(pk):
    '''
    Получает словарь с данными студента по его pk
    '''
    students = load_students()
    for student in students:
        if student["pk"] == pk:
            return student
    return None

def get_profession_by_title(title):
    '''
    Получает словарь с инфо о профессии по названию
    '''
    professions = load_professions()
    for profession in professions:
        if profession['title']== title:
            return profession
    return None

echo "# student-profession" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Arina-ramina/student-profession.git
git push -u origin main
def check_fitness(student, profession):
    '''
    получив студента и профессию, возвращает словарь
    '''
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])
    has_skills = student_skills.intersection(profession_skills)
    lasc_skills = profession_skills - student_skills
    fit_percent = len(has_skills)/ len(profession_skills)*100
    return{
        'has': list(has_skills),
        "lacks": list(lasc_skills),
        "fit_percent": fit_percent
    }

def main ():
    '''
    основной код программы
    '''
    while True:
        print('Введите номер студента')
        number_student = int(input())
        student = get_student_by_pk(number_student)
        if student:
            print (f'Студент {student["full_name"]}')
            print (f"Знает {', '.join (student['skills'])}")
        else:
            print('У нас нет такого студента')
            continue

        print (f'Выберите специальность для оценки студента {student["full_name"]}')
        profession_title = input()
        profession = get_profession_by_title(profession_title)
        if profession:
            result=check_fitness(student, profession)
            print (f'Пригодность: {result["fit_percent"]}%')
            print (f'{student["full_name"]} знает {", ".join(result["has"])}')
            print (f'{student["full_name"]} не знает {", ".join(result["lacks"])}')
        else:
            print ('У нас нет такой специальности')
        break

if __name__=='__main__':
    main()