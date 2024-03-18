from applicationFunctions import getAllStudents
from applicationFunctions import addStudent
from applicationFunctions import updateStudentEmail
from applicationFunctions import deleteStudent

def main():
    #Testing of script
    print("Initial Database")
    getAllStudents.getAllStudents()

    print("Adding student William Zhu")
    addStudent.addStudent("William","Zhu","williamzhu2@cmail.carleton.ca","2021-09-01")
    getAllStudents.getAllStudents()

    print("Updating Jim beam's email")
    updateStudentEmail.updateStudentEmail(3,"jbb@cmail.carleton.ca")
    getAllStudents.getAllStudents()

    print("Deleting Jane Smith with student id 2")
    deleteStudent.deleteStudent(2)
    getAllStudents.getAllStudents()

if __name__ == "__main__":
    #Direct execution of script
    main()