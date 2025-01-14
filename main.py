from tkinter import *
# from tkinter import ttk
from PIL import Image, ImageTk
from student import Student

class FaceRecSys:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition Student Attendance System')
        root.resizable(0, 0)
        # root.attributes('-alpha', 0.95)

        # Background Image
        imgBg = Image.open(
            r"images\colorBg.png")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg) #set image

        BgImg = Label(self.root, image=self.PhoImgBg) # shows in window
        BgImg.place(x=0, y=0, width=1530, height=790) # place image

        titleLabel = Label(text="STUDENT ATTENDANCE SYSTEM",
                           font=("Calibri Light", 30,),
                           bg='#E8F0F2', fg='black')

        titleLabel.place(x=0, y=120, width=1530, height=50)

        # Making  buttons for 'Student Details', 'Face Detector', 'Train Data', 'Attendance', 'Photos', 'Exit'

        # Student detail button
        studenButton = Image.open(r"images\StudentButton.jpg")
        studenButton = studenButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgStdBtn = ImageTk.PhotoImage(studenButton)

        Btn1 = Button(BgImg, image=self.PhoImgStdBtn,command=self.student_details,cursor='hand2')
        Btn1.place(x=250, y=270, width=130, height=130)

        Btn1 = Button(BgImg, text='STUDENT DETAILS',command=self.student_details,cursor='hand2',font=("Calibri", 12, 'bold',),bg='black', fg='white')
        Btn1.place(x=250, y=370, width=130, height=30)

        # Face Detect Button
        faceDetectButton = Image.open(r"images\facedetect.PNG")
        faceDetectButton = faceDetectButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgFacDetBtn = ImageTk.PhotoImage(faceDetectButton)

        Btn2 = Button(BgImg, image=self.PhoImgFacDetBtn, cursor='hand2')
        Btn2.place(x=550, y=270, width=130, height=130)

        Btn2 = Button(BgImg, text='DETECT FACE', cursor='hand2',
                      font=("Calibri", 12, 'bold',),
                      bg='black', fg='white')
        Btn2.place(x=550, y=370, width=130, height=30)

        # Attendance Button
        attendanceButton = Image.open(r"images\attendance1.PNG")
        attendanceButton = attendanceButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgAttendBtn = ImageTk.PhotoImage(attendanceButton)

        Btn3 = Button(BgImg, image=self.PhoImgAttendBtn, cursor='hand2')
        Btn3.place(x=850, y=270, width=130, height=130)

        Btn3 = Button(BgImg, text='ATTENDANCE', cursor='hand2',
                      font=("Calibri", 12, 'bold',),
                      bg='black', fg='white')
        Btn3.place(x=850, y=370, width=130, height=30)

        # Help desk button
        helpDskButton = Image.open(r"images\helpdesk.PNG")
        helpDskButton = helpDskButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgHelpdskBtn = ImageTk.PhotoImage(helpDskButton)

        Btn4 = Button(BgImg, image=self.PhoImgHelpdskBtn, cursor='hand2')
        Btn4.place(x=1150, y=270, width=130, height=130)

        Btn4 = Button(BgImg, text='HELP DESK', cursor='hand2',
                      font=("Calibri", 12, 'bold',),
                      bg='black', fg='white')
        Btn4.place(x=1150, y=370, width=130, height=30)

        # Train data Button
        trainFaceButton = Image.open(r"images\train data.PNG")
        trainFaceButton = trainFaceButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgTrainFacBtn = ImageTk.PhotoImage(trainFaceButton)

        Btn5 = Button(BgImg, image=self.PhoImgTrainFacBtn, cursor='hand2')
        Btn5.place(x=400, y=510, width=130, height=130)

        Btn5 = Button(BgImg, text='TRAIN DATA', cursor='hand2',
                      font=("Calibri", 12, 'bold',),
                      bg='black', fg='white')
        Btn5.place(x=400, y=610, width=130, height=30)

        # Photos button
        photosButton = Image.open(r"images\gallery.png")
        photosButton = photosButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgPhoBtn = ImageTk.PhotoImage(photosButton)

        Btn6 = Button(BgImg, image=self.PhoImgPhoBtn, cursor='hand2')
        Btn6.place(x=700, y=510, width=130, height=130)

        Btn6 = Button(BgImg, text='PHOTOS', cursor='hand2',
                      font=("Calibri", 12, 'bold',),
                      bg='black', fg='white')
        Btn6.place(x=700, y=610, width=130, height=30)

        # Developer Button
        contactDeveloper = Image.open(r"images\contact.png")
        contactDeveloper = contactDeveloper.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgContBtn = ImageTk.PhotoImage(contactDeveloper)

        Btn7 = Button(BgImg, image=self.PhoImgContBtn, cursor='hand2')
        Btn7.place(x=1000, y=510, width=130, height=130)

        Btn7 = Button(BgImg, text='DEVELOPER', cursor='hand2',
                      font=("Calibri", 12, 'bold',),
                      bg='black', fg='white')
        Btn7.place(x=1000, y=610, width=130, height=30)

    # Making Function for student details Button activate from main window

    def student_details(self):
        self.student_details_window=Toplevel(self.root)
        self.app = Student (self.student_details_window)






if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = FaceRecSys(root)
    root.mainloop()


