import ast
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Quiz_Application import main
from Quiz_data.models import questions

Ques_Answers = []

def login(request):
    try:
        if(request.method == "POST"):
            main.Info["FullName"] = request.POST.get("FullName")
            main.Info["RollNumber"] = request.POST.get("RollNumber")
            main.Info["UserId"] = request.POST.get("UserId")
            main.Info["Password"] = request.POST.get("Password")
            return redirect("/quiz_app/")
        pass
    except:
        pass
    return render(request,"index2.html")

def GetQues(request):
    if(request.method == "POST"):
        dict_str = request.body.decode("UTF-8")
        body = ast.literal_eval(dict_str)
        Ques_no = body["Ques_no"]
    try:
        return HttpResponse(json.dumps(Ques_Answers[Ques_no-1]), content_type='application/json')
    except:
        pass

def SaveQues(request):
    try:
        if(request.method == "POST"):
            dict_str = request.body.decode("UTF-8")
            body = ast.literal_eval(dict_str)
            checked_option = body["checked_option"]
            Ques_time = body["Ques_time"]
            ques_no = body["ques_no"]
            main.SaveButton(checked_option,Ques_time,ques_no)
            return HttpResponse(json.dumps(body), content_type='application/json')
    except Exception:
        print(Exception)
    return HttpResponse(json.dumps(body), content_type='application/json')

def GetInfo(request):
    Send_Info = main.Info
    password = Send_Info.pop("Password", Send_Info)
    try:
        return HttpResponse(json.dumps(Send_Info), content_type='application/json')
    except:
        pass

def quiz_app(request):
    all_ques = questions.objects.all()
    for count, question in enumerate(all_ques):
        Ques_Ans = {
                "question": str(question),
                "optionA": str(question.get_ans().get(id=count*4+1)).split(";")[1],
                "optionB": str(question.get_ans().get(id=count*4+2)).split(";")[1],
                "optionC": str(question.get_ans().get(id=count*4+3)).split(";")[1],
                "optionD": str(question.get_ans().get(id=count*4+4)).split(";")[1],
            }
        Ques_Answers.append(Ques_Ans)
    return render(request,"index.html")

def result(request):
    main.Write_TO_CSv()
    main.Draw_Graph()
    return render(request,"index1.html")