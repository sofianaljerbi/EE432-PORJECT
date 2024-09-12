# Import necessary libraries
import json

# Initialize data structures
registrar_user = {'username': 'dr.salah', 'password': '1234'}
students = {}
faculty_members = {}
schedules = {'lectures': [], 'exams': []}
courses = {}


# Load data from JSON files
def load_data():
    global students, faculty_members, schedules, courses
    try:
        with open('students.json', 'r', encoding='utf-8') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = {}
    except UnicodeDecodeError as e:
        print(f"Error reading students.json: {e}")
        students = {}

    try:
        with open('faculty_members.json', 'r', encoding='utf-8') as file:
            faculty_members = json.load(file)
    except FileNotFoundError:
        faculty_members = {}
    except UnicodeDecodeError as e:
        print(f"Error reading faculty_members.json: {e}")
        faculty_members = {}

    try:
        with open('schedules.json', 'r', encoding='utf-8') as file:
            schedules = json.load(file)
    except FileNotFoundError:
        schedules = {'lectures': [], 'exams': []}
    except UnicodeDecodeError as e:
        print(f"Error reading schedules.json: {e}")
        schedules = {'lectures': [], 'exams': []}

    try:
        with open('courses.json', 'r', encoding='utf-8') as file:
            courses = json.load(file)
    except FileNotFoundError:
        courses = {}
    except UnicodeDecodeError as e:
        print(f"Error reading courses.json: {e}")
        courses = {}


# Save data to JSON files
def save_data():
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=4)
    with open('faculty_members.json', 'w') as file:
        json.dump(faculty_members, file, indent=4)
    with open('schedules.json', 'w') as file:
        json.dump(schedules, file, indent=4)
    with open('courses.json', 'w') as file:
        json.dump(courses, file, indent=4)

# دالة تسجيل الدخول
def login():
    print("\nأهلاً بكم في المشروع المصغر المماثل لمنظومة تنزيل مواد في جامعة طرابلس")
    print("1. مسجل")
    print("2. طالب")
    print("3. عضو هيئة التدريس")
    print("4. خروج")
    choice = input("اختر خياراً: ")

    if choice == '1':
        registrar_login()  # تسجيل دخول المسجل
    elif choice == '2':
        student_menu()  # قائمة الطالب
    elif choice == '3':
        faculty_menu()  # قائمة عضو هيئة التدريس
    elif choice == '4':
        exit()
    else:
        print("خيار غير صحيح!")
        login()


# Registrar login function
def registrar_login():
    print("\nالرجاء تسجيل الدخول كمسجل.")
    username = input("أدخل اسم المستخدم: ")
    password = input("أدخل الرمز: ")

    if username == registrar_user['username'] and password == registrar_user['password']:
        print(f"مرحباً بك، {username}!")
        registrar_menu()
    else:
        print("اسم المستخدم أو الرمز غير صحيح. حاول مرة أخرى.")
        login()

# Registrar menu
def registrar_menu():
    print("\nقائمة المسجل:")
    print("1. إدارة طالب")
    print("2. إدارة أعضاء هيئة التدريس")
    print("3. عرض قوائم الطلبة المسجلين في مقرر")
    print("4. تعيين درجات مقررات")
    print("5. عرض جدول المحاضرات والامتحانات")
    print("6. خروج")

    choice = input("اختر خياراً: ")
    if choice == '1':
        manage_student()
    elif choice == '2':
        manage_faculty()
    elif choice == '3':
        display_registered_students()
    elif choice == '4':
        assign_grades()
    elif choice == '5':
        display_schedule_for_registrar()
    elif choice == '6':
        login()
    else:
        print("خيار غير صحيح!")
        registrar_menu()

# Function to display schedule for the registrar
def display_schedule_for_registrar():
    print("\nجدول المحاضرات:")
    for lecture in schedules['lectures']:
        print(
            f"المقرر: {lecture['course']}, اليوم: {lecture['day']}, الساعة: {lecture['time']}, القاعة: {lecture['room']}")

    print("\nجدول الامتحانات:")
    for exam in schedules['exams']:
        print(
            f"المقرر: {exam['course']}, النوع: {exam['type']}, الفترة: {exam['period']}, اليوم: {exam['day']}, الساعة: {exam['time']}, القاعة: {exam['room']}")

    input("\nاضغط Enter للعودة.")
    registrar_menu()

# إدارة الطلاب
def manage_student():
    print("\nإدارة الطلاب:")
    print("1. بحث عن طالب")
    print("2. إضافة طالب جديد")
    print("3. العودة")

    choice = input("اختر خياراً: ")
    if choice == '1':
        search_student()
    elif choice == '2':
        add_new_student()
    elif choice == '3':
        registrar_menu()
    else:
        print("خيار غير صحيح!")
        manage_student()

def search_student():
    student_id = input("أدخل رقم القيد للبحث عن الطالب: ")
    if student_id in students:
        print(f"\nمعلومات الطالب: {students[student_id]}")
        manage_student_courses(student_id)
    else:
        print("الطالب غير موجود.")
        manage_student()

def add_new_student():
    student_id = input("أدخل رقم القيد: ")
    if student_id in students:
        print("الطالب موجود مسبقاً.")
    else:
        name = input("أدخل اسم الطالب: ")
        password = input("أدخل الرمز: ")
        num_semesters = int(input("أدخل عدد الفصول المنجزة: "))

        # إدخال المواد المنجزة لكل فصل مع درجاتها
        completed_courses = {}
        for semester in range(1, num_semesters + 1):
            print(f"\nإدخال المواد للفصل {semester}:")
            semester_courses = []
            total_credits = 0  # مجموع الوحدات الدراسية لكل فصل

            while True:
                course = input(f"أدخل كود المادة للفصل {semester} (أو اكتب 'خروج' لإنهاء): ")
                if course.lower() == 'خروج':
                    break

                if course not in courses:
                    print("المقرر غير موجود. الرجاء إدخال كود صحيح.")
                    continue

                # التحقق من مجموع الوحدات الدراسية
                course_credits = courses[course]['credits']
                if total_credits + course_credits > 18:
                    print(f"تجاوزت الحد الأقصى للوحدات (18 وحدة) للفصل {semester}. الرجاء إدخال مواد للفصل القادم.")
                    break

                grade = input(f"أدخل درجة المادة {course} (أو اكتب 'رجوع' للعودة): ")
                if grade.lower() == 'رجوع':
                    continue  # العودة لإعادة إدخال كود المادة

                # التحقق من صحة إدخال الدرجة
                if not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
                    print("الرجاء إدخال درجة صحيحة بين 0 و 100.")
                    continue

                semester_courses.append((course, grade))
                total_credits += course_credits  # إضافة الوحدات للمجموع

            completed_courses[f'فصل {semester}'] = semester_courses

        # حفظ بيانات الطالب
        students[student_id] = {
            'name': name,
            'password': password,
            'completed_courses': completed_courses,
            'grades': {},
            'enrolled_courses': []
        }
        save_data()
        print("تم إضافة الطالب بنجاح.")
    manage_student()

def open_new_semester_for_student(student_id):
    """فتح فصل دراسي جديد للطالب مع التحقق من الشروط."""
    if not students[student_id]['completed_courses']:
        print("يجب أن تكون مسجلاً ولديك فصل دراسي منجز لفتح فصل جديد.")
        return manage_student_courses(student_id)  # إعادة المستخدم إلى قائمة إدارة المقررات

    num_semesters = len(students[student_id]['completed_courses']) + 1
    semester_name = f'فصل {num_semesters}'
    if semester_name in students[student_id]['completed_courses']:
        print("الفصل الدراسي الجديد مفتوح بالفعل. سيتم نقلك إلى إضافة المواد.")
        delete_and_add_courses_for_student(student_id)
        return
    else:
        students[student_id]['completed_courses'][semester_name] = []
        save_data()
        print(f"تم فتح {semester_name} بنجاح.")

    manage_student_courses(student_id)  # العودة إلى قائمة إدارة المقررات بعد فتح الفصل الجديد

def manage_student_courses(student_id):
    print(f"\nإدارة المقررات للطالب: {student_id}")

    # تحقق مما إذا كان هناك فصل دراسي مفتوح بالفعل
    num_semesters = len(students[student_id]['completed_courses'])
    semester_name = f'فصل {num_semesters + 1}'

    # إذا كان الفصل الجديد مفتوح بالفعل، انقل المستخدم مباشرة لإضافة أو حذف المواد
    if semester_name in students[student_id]['completed_courses']:
        print("الفصل الدراسي الجديد مفتوح بالفعل. سيتم نقلك إلى إضافة المواد.")
        delete_and_add_courses_for_student(student_id)
        return  # الخروج من الدالة بعد الإضافة أو الحذف

    print("1. فتح فصل دراسي جديد")
    print("2. إضافة أو حذف مادة")
    print("3. رجوع")

    choice = input("اختر خياراً: ")
    if choice == '1':
        # تحقق مما إذا كان هناك فصل دراسي مفتوح بالفعل
        if any(len(courses) == 0 for semester, courses in students[student_id]['completed_courses'].items()):
            print("يوجد فصل دراسي مفتوح بالفعل. عليك بتنزيل مواد أولاً.")
            delete_and_add_courses_for_student(student_id)
        else:
            open_new_semester_for_student(student_id)  # سيتم فتح فصل دراسي جديد
    elif choice == '2':
        delete_and_add_courses_for_student(student_id)  # إضافة أو حذف المواد
    elif choice == '3':
        registrar_menu()  # العودة إلى قائمة المسجل
    else:
        print("خيار غير صحيح!")
        manage_student_courses(student_id)


def delete_and_add_courses_for_student(student_id):
    """إضافة أو حذف مادة للطالب بعد التحقق من الشروط."""
    while True:
        print("\nالمقررات الحالية للطالب:", student_id)
        print(f"المقررات المسجلة: {', '.join(students[student_id]['enrolled_courses'])}")
        action = input("أدخل 'حذف' لإزالة مقرر، 'إضافة' لإضافة مقرر جديد، أو 'رجوع' للعودة: ").lower()

        if action == 'حذف':
            course_code = input("أدخل رمز المقرر لحذفه (أو اكتب 'رجوع' للعودة): ")
            if course_code.lower() == 'رجوع':
                continue
            if course_code in students[student_id]['enrolled_courses']:
                # تحقق من شروط co-requisites
                if any(course_code in courses[c]['corequisites'] for c in students[student_id]['enrolled_courses']):
                    print(f"لا يمكن حذف المقرر {course_code} لأنه مرتبط بمقرر آخر.")
                else:
                    students[student_id]['enrolled_courses'].remove(course_code)
                    save_data()
                    print(f"تم إزالة المقرر {course_code} بنجاح للطالب {student_id}.")
            else:
                print(f"الطالب {student_id} غير مسجل في المقرر {course_code}.")
        elif action == 'إضافة':
            course_codes = input("أدخل رموز المقررات لإضافتها (مفصولة بفواصل) (أو اكتب 'رجوع' للعودة): ").split(',')
            if 'رجوع' in course_codes:
                continue
            course_codes = [course.strip() for course in course_codes if course.strip()]
            for course_code in course_codes:
                if enroll_student_with_conditions(student_id, course_code):
                    save_data()
                    print(f"تم إضافة المقرر {course_code} بنجاح للطالب {student_id}.")
        elif action == 'رجوع':
            manage_student_courses(student_id)
            break
        else:
            print("إجراء غير صالح. الرجاء إدخال 'حذف'، 'إضافة'، أو 'رجوع'.")

def check_prerequisites(student_id, course_code):
    """تتحقق من أن الطالب استوفى جميع المتطلبات السابقة للمادة ونجح فيها."""
    if course_code not in courses:
        print(f"المادة {course_code} غير موجودة في قائمة المقررات.")
        return False

    prerequisites = courses[course_code]['prerequisites']  # قائمة المتطلبات السابقة للمادة
    completed_courses = {course: grade for semester_courses in students[student_id]['completed_courses'].values() for
                         course, grade in semester_courses}
    missing_prerequisites = []
    for prereq in prerequisites:
        if prereq not in completed_courses or int(completed_courses[prereq]) < 50:
            missing_prerequisites.append(prereq + " (راسب)")

    if missing_prerequisites:
        print(
            f"لا يمكن تسجيل المادة {course_code}. المتطلبات التالية غير مكتملة أو الطالب راسب فيها: {', '.join(missing_prerequisites)}")
        return False
    return True

def check_corequisites(student_id, course_code):
    """تتحقق من أن الطالب مسجل في جميع المواد المتزامنة المطلوبة للمادة."""
    corequisites = courses[course_code]['corequisites']  # قائمة المواد المتزامنة للمادة
    for coreq in corequisites:
        if coreq not in students[student_id]['enrolled_courses']:  # يجب أن يكون مسجلاً في المادة
            print(f"لا يمكن تسجيل المادة {course_code}. يجب تسجيل المادة المتزامنة {coreq} أولاً.")
            return False
    return True

def enroll_student_with_conditions(student_id, course_code):
    """إضافة مقرر للطالب بعد التحقق من جميع الشروط."""
    current_credits = sum(courses[course]['credits'] for course in students[student_id]['enrolled_courses'])

    # تحقق من الوحدات
    if current_credits + courses[course_code]['credits'] > 18:
        print(f"لا يمكن إضافة المقرر {course_code}. تجاوز الحد الأقصى للوحدات (18 وحدة).")
        return False

    # تحقق من المتطلبات السابقة
    if not check_prerequisites(student_id, course_code):
        return False

    # تحقق من المتطلبات المتزامنة
    if not check_corequisites(student_id, course_code):
        return False

    students[student_id]['enrolled_courses'].append(course_code)
    return True

def display_registered_students():
    """عرض قوائم الطلبة المسجلين في مقرر معين."""
    course_code = input("أدخل كود المقرر: ")
    if course_code not in courses:
        print("المقرر غير موجود.")
        return registrar_menu()

    print(f"\nقائمة الطلبة المسجلين في المقرر {course_code}:")
    students_found = False
    for student_id, info in students.items():
        if course_code in info['enrolled_courses']:
            print(f"الطالب: {student_id}, الاسم: {info['name']}")
            students_found = True

    if not students_found:
        print("لا يوجد طلبة مسجلين في هذا المقرر.")

    registrar_menu()

def assign_grades():
    """تعيين درجات مقررات للطلاب."""
    while True:
        student_id = input("أدخل رقم القيد (أو اكتب 'رجوع' للعودة): ")
        if student_id.lower() == 'رجوع':
            registrar_menu()  # العودة إلى القائمة السابقة
            break

        if student_id not in students:
            print("الطالب غير موجود.")
            continue

        course_code = input("أدخل كود المقرر: ")

        # تحقق مما إذا كانت المادة مسجلة لدى الطالب
        if course_code not in students[student_id]['enrolled_courses']:
            print(f"المادة {course_code} غير مسجلة لدى الطالب {student_id}. لا يمكن رصد درجة.")
            continue

        # تحقق مما إذا كان للطالب درجة مسجلة من قبل أستاذ المادة
        if course_code in students[student_id]['grades']:
            recorded_info = students[student_id]['grades'][course_code]
            if isinstance(recorded_info, dict) and recorded_info.get('recorded_by') == 'faculty':
                print(
                    f"تم رصد درجة الطالب {student_id} للمقرر {course_code} من قبل أستاذ المادة. الدرجة المرصودة: {recorded_info['grade']}")
                continue  # تجاوز هذا المقرر ولا تطلب إدخال درجة جديدة

        # إذا لم تكن هناك درجة مسجلة من قبل أستاذ المادة، اسمح للمسجل بإدخال درجة جديدة
        grade = input("أدخل درجة المقرر: ")
        students[student_id]['grades'][course_code] = {'grade': grade, 'recorded_by': 'registrar'}
        print(
            f"تم تعيين درجة {grade} للمقرر {course_code} للطالب {student_id} - التقدير: {calculate_grade_label(int(grade))}")

        choice = input("هل ترغب في إضافة درجة أخرى؟ (نعم/لا): ")
        if choice.lower() != 'نعم':
            break

    registrar_menu()

def faculty_menu():
    print("\nمرحباً بك في قائمة عضو هيئة التدريس. الرجاء تسجيل الدخول.")
    faculty_id = input("أدخل رمز العضو: ")

    if faculty_id in faculty_members:
        # التحقق مما إذا كان الرمز الشخصي غير معين
        if faculty_members[faculty_id]['password'] is None:
            print("هذا هو الدخول الأول. يرجى تعيين رمزك الشخصي.")
            new_password = input("أدخل الرمز الجديد: ")
            faculty_members[faculty_id]['password'] = new_password
            save_data()
            print("تم تعيين الرمز بنجاح.")
            faculty_options(faculty_id)  # استدعاء دالة الخيارات بعد تعيين الرمز
        else:
            # إذا كان للعضو رمز مسبق، يتحقق من صحة الرمز
            password = input("أدخل الرمز: ")
            if faculty_members[faculty_id]['password'] == password:
                print(f"مرحباً أستاذ {faculty_members[faculty_id]['name']}!")
                print(f"المواد التي تدرسها: {', '.join(faculty_members[faculty_id]['assigned_courses'])}")
                # عرض الخيارات للعضو
                faculty_options(faculty_id)
            else:
                print("بيانات الدخول غير صحيحة.")
                faculty_menu()
    else:
        print("العضو غير موجود.")
        login()

def faculty_options(faculty_id):
    """خيارات أعضاء هيئة التدريس بعد تسجيل الدخول بنجاح."""
    while True:
        print("\nخيارات عضو هيئة التدريس:")
        print("1. عرض قائمة الطلبة في مادة")
        print("2. إضافة درجات للطلبة في مادة")
        print("3. عرض جدول المحاضرات والامتحانات")  # الخيار الجديد
        print("4. خروج")

        choice = input("اختر خياراً: ")

        if choice == '1':
            display_students_in_course(faculty_id)
        elif choice == '2':
            add_grades_for_course(faculty_id)
        elif choice == '3':
            display_schedule(faculty_id, 'faculty')  # عرض الجدول لعضو هيئة التدريس
        elif choice == '4':
            login()
        else:
            print("خيار غير صحيح! الرجاء المحاولة مرة أخرى.")

def display_students_in_course(faculty_id):
    """عرض قائمة الطلبة المسجلين في مادة معينة يدرسها عضو هيئة التدريس."""
    print(f"\nالمواد التي تدرسها: {', '.join(faculty_members[faculty_id]['assigned_courses'])}")
    course_code = input("أدخل رمز المادة لعرض الطلبة المسجلين: ")

    if course_code not in faculty_members[faculty_id]['assigned_courses']:
        print("المادة غير معطاة لهذا العضو.")
        return

    print(f"\nقائمة الطلبة المسجلين في المادة {course_code}:")
    students_found = False
    for student_id, info in students.items():
        if course_code in info['enrolled_courses']:
            print(f"الطالب: {student_id}, الاسم: {info['name']}")
            students_found = True

    if not students_found:
        print("لا يوجد طلبة مسجلين في هذه المادة.")

def add_grades_for_course(faculty_id):
    """إضافة درجات للطلبة في مادة معينة يدرسها عضو هيئة التدريس."""
    print(f"\nالمواد التي تدرسها: {', '.join(faculty_members[faculty_id]['assigned_courses'])}")
    course_code = input("أدخل رمز المادة لإضافة الدرجات: ")

    if course_code not in faculty_members[faculty_id]['assigned_courses']:
        print("المادة غير معطاة لهذا العضو.")
        return

    for student_id, info in students.items():
        if course_code in info['enrolled_courses']:
            # تحقق مما إذا كان للطالب درجة مسجلة بالفعل
            if course_code in info['grades']:
                current_grade = info['grades'][course_code]
                print(
                    f"الطالب {student_id} ({info['name']}) تم رصد درجته من قبل أستاذ المقرر. الدرجة المرصودة: {current_grade}")
                continue  # تجاوز هذا الطالب ولا تطلب إدخال درجة جديدة

            # إذا لم تكن هناك درجة مسجلة، اسمح للأستاذ بإدخال درجة جديدة
            grade = input(f"أدخل درجة الطالب {student_id} ({info['name']}): ")
            students[student_id]['grades'][course_code] = {'grade': grade, 'recorded_by': 'faculty'}
            save_data()
            print(f"تم تعيين درجة {grade} للمادة {course_code} للطالب {student_id}.")

    print("تم تحديث الدرجات بنجاح.")

def manage_faculty():
    print("\nإدارة أعضاء هيئة التدريس:")
    print("1. بحث عن عضو هيئة تدريس")
    print("2. إضافة عضو هيئة تدريس جديد")
    print("3. إنشاء جداول الامتحانات والمحاضرات")
    print("4. العودة")

    choice = input("اختر خياراً: ")
    if choice == '1':
        search_faculty_member()
    elif choice == '2':
        add_new_faculty_member()
    elif choice == '3':
        create_schedule()
    elif choice == '4':
        registrar_menu()
    else:
        print("خيار غير صحيح!")
        manage_faculty()

def search_faculty_member():
    faculty_id = input("أدخل رمز العضو: ")
    if faculty_id in faculty_members:
        print(f"\nمعلومات العضو: {faculty_members[faculty_id]}")
        print("1. تعيين مادة")
        print("2. تغيير رمز العضو")
        print("3. حذف مادة")
        print("4. العودة")
        choice = input("اختر خياراً: ")
        if choice == '1':
            assign_course_to_faculty(faculty_id)
        elif choice == '2':
            change_faculty_password(faculty_id)
        elif choice == '3':
            remove_course_from_faculty(faculty_id)
        elif choice == '4':
            manage_faculty()
        else:
            print("خيار غير صحيح!")
            search_faculty_member()
    else:
        print("العضو غير موجود.")
        manage_faculty()

def add_new_faculty_member():
    faculty_id = input("أدخل رمز العضو: ")
    if faculty_id in faculty_members:
        print("العضو موجود مسبقاً.")
    else:
        name = input("أدخل اسم العضو: ")
        # لا نطلب الرمز هنا، سيُطلب من العضو عند دخوله لأول مرة
        faculty_members[faculty_id] = {'name': name, 'password': None, 'assigned_courses': []}
        save_data()
        print("تم إضافة عضو هيئة التدريس بنجاح.")
    manage_faculty()

def assign_course_to_faculty(faculty_id):
    """تعيين مادة جديدة لعضو هيئة التدريس."""
    print(f"\nالمواد الحالية للعضو {faculty_id}: {', '.join(faculty_members[faculty_id]['assigned_courses'])}")
    course_code = input("أدخل رمز المادة لتعيينها: ")

    if course_code not in faculty_members[faculty_id]['assigned_courses']:
        faculty_members[faculty_id]['assigned_courses'].append(course_code)
        save_data()
        print(f"تم تعيين المادة {course_code} للعضو {faculty_id}.")
    else:
        print(f"العضو {faculty_id} مُعين بالفعل لتدريس المادة {course_code}.")

    search_faculty_member()

def remove_course_from_faculty(faculty_id):
    """حذف مادة من قائمة المواد لعضو هيئة التدريس."""
    print(f"\nالمواد الحالية للعضو {faculty_id}: {', '.join(faculty_members[faculty_id]['assigned_courses'])}")
    course_code = input("أدخل رمز المادة لحذفها: ")

    if course_code in faculty_members[faculty_id]['assigned_courses']:
        faculty_members[faculty_id]['assigned_courses'].remove(course_code)
        save_data()
        print(f"تم حذف المادة {course_code} من العضو {faculty_id}.")
    else:
        print(f"المادة {course_code} غير موجودة في قائمة المواد المقررة للعضو {faculty_id}.")

    search_faculty_member()

def change_faculty_password(faculty_id):
    new_password = input("أدخل الرمز الجديد: ")
    faculty_members[faculty_id]['password'] = new_password
    save_data()
    print("تم تغيير الرمز بنجاح.")
    search_faculty_member()

# إنشاء جداول المحاضرات والامتحانات
def create_schedule():
    print("\nإنشاء جداول:")
    print("1. جدول محاضرات")
    print("2. جدول امتحانات")
    print("3. رجوع")
    choice = input("اختر نوع الجدول: ")

    if choice == '1':
        create_lecture_schedule()
    elif choice == '2':
        create_exam_schedule()
    elif choice == '3':
        manage_faculty()  # العودة إلى قائمة إدارة أعضاء هيئة التدريس
    else:
        print("خيار غير صحيح!")
        create_schedule()

def create_lecture_schedule():
    print("\nإنشاء جدول محاضرات:")
    while True:
        course_code = input("أدخل رمز المقرر: ")
        day = input("أدخل اليوم: ")
        time = input("أدخل الساعة (مثل 10:00-11:30): ")
        room = input("أدخل القاعة: ")

        # التحقق من وجود تعارض في اليوم، الوقت، والقاعة
        if check_schedule_conflict(day, time, room):
            print("لا يمكن إضافة المحاضرة. هناك تعارض في اليوم، الوقت، والقاعة.")
            continue  # إعادة طلب إدخال محاضرة جديدة

        schedules['lectures'].append({'course': course_code, 'day': day, 'time': time, 'room': room})
        save_data()
        print("تم إضافة المحاضرة بنجاح.")

        cont = input("هل ترغب في إضافة محاضرة أخرى؟ (نعم/لا): ")
        if cont.lower() != 'نعم':
            break

    # طباعة جدول المحاضرات
    print("\nجدول المحاضرات:")
    for lecture in schedules['lectures']:
        print(
            f"المقرر: {lecture['course']}, اليوم: {lecture['day']}, الساعة: {lecture['time']}, القاعة: {lecture['room']}")

    create_schedule()

def check_schedule_conflict(day, time, room):
    """التحقق من وجود تعارض في جدول المحاضرات."""
    for lecture in schedules['lectures']:
        if lecture['day'] == day and lecture['time'] == time and lecture['room'] == room:
            return True  # تعارض موجود
    return False  # لا يوجد تعارض

def create_exam_schedule():
    print("\nإنشاء جدول امتحانات:")
    print("1. امتحان نصفي")
    print("2. امتحان فاينل")
    exam_type = input("اختر نوع الامتحان: ")

    if exam_type not in ['1', '2']:
        print("خيار غير صحيح!")
        return create_exam_schedule()

    exam_type = "نصفي" if exam_type == '1' else "فاينل"

    while True:
        course_code = input("أدخل رمز المقرر: ")
        period = input("اختر الفترة (الأولى/الثانية): ")
        day = input("أدخل اليوم: ")
        time = input("أدخل الساعة (مثل 10:00-11:30): ")
        room = input("أدخل القاعة: ")

        # التحقق من وجود تعارض في اليوم، الفترة، الوقت، والقاعة
        if check_exam_schedule_conflict(day, period, time, room):
            print("لا يمكن إضافة الامتحان. هناك تعارض في اليوم، الفترة، الوقت، أو القاعة.")
            continue  # إعادة طلب إدخال امتحان جديد

        schedules['exams'].append(
            {'course': course_code, 'type': exam_type, 'period': period, 'day': day, 'time': time, 'room': room})
        save_data()
        print("تم إضافة الامتحان بنجاح.")

        cont = input("هل ترغب في إضافة امتحان آخر؟ (نعم/لا): ")
        if cont.lower() != 'نعم':
            break

    # طباعة جدول الامتحانات
    print("\nجدول الامتحانات:")
    for exam in schedules['exams']:
        print(
            f"المقرر: {exam['course']}, النوع: {exam['type']}, الفترة: {exam['period']}, اليوم: {exam['day']}, الساعة: {exam['time']}, القاعة: {exam['room']}")

    create_schedule()

def check_exam_schedule_conflict(day, period, time, room):
    """التحقق من وجود تعارض في جدول الامتحانات."""
    for exam in schedules['exams']:
        if exam['day'] == day and exam['period'] == period and exam['time'] == time and exam['room'] == room:
            return True  # تعارض موجود
    return False  # لا يوجد تعارض

def display_completed_semesters_with_gpa(student_id):
    """تعرض المواد المنجزة لكل فصل دراسي للطالب مع درجاتها وتقديراتها وحساب المعدل التراكمي."""
    print(f"\nالفصول الدراسية المنجزة للطالب {student_id}:")
    completed_courses = students[student_id]['completed_courses']
    total_points = 0
    total_credits = 0

    for semester, courses_in_semester in completed_courses.items():
        semester_points = 0
        semester_credits = 0
        print(f"{semester}:")
        for course, grade in courses_in_semester:
            if course in courses:  # التحقق من أن رمز المادة موجود في القاموس
                course_credits = courses[course]['credits']  # جلب عدد الوحدات الدراسية للمادة
                grade_label = calculate_grade_label(int(grade))  # حساب التقدير من الدرجة
                semester_credits += course_credits
                points = int(grade) * course_credits
                semester_points += points
                print(f"  المادة: {course}, الدرجة: {grade}, التقدير: {grade_label}")
            else:
                print(f"المادة {course} غير موجودة في قائمة المقررات.")

        semester_gpa = semester_points / semester_credits if semester_credits > 0 else 0
        total_points += semester_points
        total_credits += semester_credits
        print(f"المعدل التراكمي للفصل {semester}: {semester_gpa:.2f}")

    overall_gpa = total_points / total_credits if total_credits > 0 else 0
    print(f"\nالمعدل التراكمي العام للطالب {student_id}: {overall_gpa:.2f}")

def calculate_grade_label(grade):
    """حساب التقدير بناءً على الدرجة."""
    if 85 <= grade <= 100:
        return 'ممتاز'
    elif 75 <= grade < 85:
        return 'جيد جداً'
    elif 65 <= grade < 75:
        return 'جيد'
    elif 50 <= grade < 65:
        return 'مقبول'
    else:
        return 'ضعيف'

def student_menu():
    """عرض قائمة الخيارات للطالب."""
    student_id = input("أدخل رقم القيد: ")
    if student_id in students:
        password = input("أدخل الرمز: ")
        if password == students[student_id]['password']:
            print(f"مرحباً بك، {students[student_id]['name']}!")
            while True:
                print("\nقائمة الطالب:")
                print("1. عرض الفصول الدراسية المنجزة مع المعدل التراكمي")
                print("2. إدارة المواد المسجلة")
                print("3. عرض جدول المحاضرات والامتحانات")  # الخيار الجديد
                print("4. خروج")
                choice = input("اختر خياراً: ")

                if choice == '1':
                    display_completed_semesters_with_gpa(student_id)
                elif choice == '2':
                    manage_student_courses(student_id)  # سيتم ضبط هذه الدالة للتحقق من الفصول الدراسية
                elif choice == '3':
                    display_schedule(student_id, 'student')  # عرض الجدول للطالب
                elif choice == '4':
                    login()
                    break
                else:
                    print("خيار غير صحيح!")
        else:
            print("الرمز غير صحيح.")
            student_menu()
    else:
        print("الطالب غير موجود.")

def display_schedule(user_id, user_type):
    """عرض جدول المحاضرات والامتحانات للطالب أو عضو هيئة التدريس."""
    if user_type == 'student':
        enrolled_courses = students[user_id]['enrolled_courses']
        print("\nجدول المحاضرات للمواد المسجلة:")
        for lecture in schedules['lectures']:
            if lecture['course'] in enrolled_courses:
                print(f"المقرر: {lecture['course']}, اليوم: {lecture['day']}, الساعة: {lecture['time']}, القاعة: {lecture['room']}")

        print("\nجدول الامتحانات للمواد المسجلة:")
        for exam in schedules['exams']:
            if exam['course'] in enrolled_courses:
                print(f"المقرر: {exam['course']}, النوع: {exam['type']}, الفترة: {exam['period']}, اليوم: {exam['day']}, الساعة: {exam['time']}, القاعة: {exam['room']}")

    elif user_type == 'faculty':
        assigned_courses = faculty_members[user_id]['assigned_courses']
        print("\nجدول المحاضرات للمقررات المعطاة:")
        for lecture in schedules['lectures']:
            if lecture['course'] in assigned_courses:
                print(f"المقرر: {lecture['course']}, اليوم: {lecture['day']}, الساعة: {lecture['time']}, القاعة: {lecture['room']}")

        print("\nجدول الامتحانات للمقررات المعطاة:")
        for exam in schedules['exams']:
            if exam['course'] in assigned_courses:
                print(f"المقرر: {exam['course']}, النوع: {exam['type']}, الفترة: {exam['period']}, اليوم: {exam['day']}, الساعة: {exam['time']}, القاعة: {exam['room']}")

    input("\nاضغط Enter للعودة.")

# بدء النظام
load_data()
login()
