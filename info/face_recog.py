import face_recognition
import cv2
import numpy as np
import os
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Contact, Student, Take_attendence
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date
import pyttsx3

speech = pyttsx3.init()
speech.setProperty("rate",140)

def face(request):
    if request.method == "POST":
        nam = request.POST.get('Face_Recognition', '')
        if nam=="Face_Recognition":
            path = "media/images"
            images = []
            classNames = []
            mylist = os.listdir(path)

            for cl in mylist:
                curImg = cv2.imread(f'{path}/{cl}')
                images.append(curImg)
                classNames.append(os.path.splitext(cl)[0])

            # print(classNames)

            def findEncodings(images):
                encodeList = []
                for img in images:
                    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                    encode = face_recognition.face_encodings(img)[0]
                    encodeList.append(encode)
                return encodeList

            encodeListKnown = findEncodings(images)

            cap = cv2.VideoCapture(0)
            p=0
            while nam=="Face_Recognition":
                success, img = cap.read()
                imgS = cv2.resize(img,(0,0),None,1,1)
                imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

                facesCurFrame = face_recognition.face_locations(imgS)
                encodesCurFrame = face_recognition.face_encodings(img, facesCurFrame)

                for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                    # print(faceDis)
                    matchIndex = np.argmin(faceDis)
                    # print(matchIndex)
                    # print(matches)
                    if matches[matchIndex]:
                        name = classNames[matchIndex].upper()
                        # print(name)
                        if Student.objects.filter(university_roll_no=name).exists():
                            data = Student.objects.get(university_roll_no=name)
                            student_name = data.name
                            # print(student_name)
                            y1,x2,y2,x1 = faceLoc
                            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                            cv2.putText(img,student_name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                            now = date.today()
                            # print(now)
                            if not Take_attendence.objects.filter(attendence_date=now, university_roll=data.university_roll_no).exists():
                                attendance_report = Take_attendence(name=student_name, status="Present",university_roll=data.university_roll_no, attendence_date=now, section=data.post, employe=data)
                                attendance_report.save()
                    else:
                        y1,x2,y2,x1 = faceLoc
                        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                        cv2.putText(img,"Not Present",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                        
                cv2.imshow('Webcam',img)
                if cv2.waitKey(1) & 0XFF == ord('q'):
                    break       
            cap.release()
            cv2.destroyWindow("Webcam")
        return render(request, "info/attendence_new.html")