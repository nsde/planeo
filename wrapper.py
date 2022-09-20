import api
import datetime

def get_student_id(first_name: str=None, last_name: str=None) -> int:
    if not (first_name and last_name): # no parameters set
        # set name to the default one 
        my_name = api.env('FULL_NAME')
        first_name = ' '.join(my_name.split()[:-1])
        last_name = my_name.split()[-1]
        
    query = last_name + '_' + first_name

    for student in api.untis.students():
        student_code = '_'.join(student.name.split('_')[:2]) # remove date of birth, e.g. "Mustermann_Max Bernd_20031224" → ""Mustermann_Max Bernd"
        if student_code == query:
            return student.id

today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

tt = api.untis.timetable(student=api.get_student_id(), start=monday, end=friday)

print(tt[0].subjects)

# IMPORTANT
api.untis.logout()
