import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Marks_data_path = "static/Marks-data.csv"

QuesAns = (
    {
        "question": "What is the average of first five multiples of 12?",
        "optionA": "24",
        "optionB": "38",
        "optionC": "40",
        "optionD": "36",
        "correctOption": "optionD"
    },

    {
        "question": "Find the speed of the train, if a train 142 m long passes a pole in 6 seconds.",
        "optionA": "77.2 km/hr",
        "optionB": "85.2 km/hr",
        "optionC": "79.6 km/hr",
        "optionD": "79.2 km/hr",
        "correctOption": "optionB"
    },

    {
        "question": "What is the simple interest on Rs. 52000 at 15/13% per annum for a period of 8 month?",
        "optionA": "350 Rs",
        "optionB": "375 Rs",
        "optionC": "425 Rs",
        "optionD": "400 Rs",
        "correctOption": "optionD"
    },

    {
        "question": "Each side of an equilateral triangle is 12cm, then its altitude is equal to",
        "optionA": "3√6 cm",
        "optionB": "3√2 cm",
        "optionC": "6√3 cm",
        "optionD": "6√2 cm",
        "correctOption": "optionC"
    },

    {
        "question": "The average of five numbers is 27. If one number is excluded, the average becomes 25. The excluded number is",
        "optionA": "25",
        "optionB": "35",
        "optionC": "45",
        "optionD": "55",
        "correctOption": "optionB"
    }
)

data = {
    "Question_1" : -1,
    "Question_2" : -1,
    "Question_3" : -1,
    "Question_4" : -1,
    "Question_5" : -1,
    "Time_1" : -2,
    "Time_2" : -2,
    "Time_3" : -2,
    "Time_4" : -2,
    "Time_5" : -2,
    "Total_Marks" : 0,
    "Total_Time" : 0,
    "Attempted_Correct" : 0,
    "Attempted_Incorrect" : 0,
    "Unattempted" : 0
}

data_list = {}

Info = {"FullName":None,
        "RollNumber":None,
        "UserId":None,
        "Password":None,
        "Total_Marks":None,
        "Total_Time":None,
        "rank":None}

def Marks(time):
    if(time<=5):
        return 10
    elif(time>=120):
        return 2
    else:
        return ((-8)*(time-5)/115)+10

def Write_TO_CSv():
    for i in range(1,6):
        if (data[f"Time_{i}"] == -2):
            data["Unattempted"] = data["Unattempted"] + 1
        elif(data[f"Question_{i}"] == -1):
            data["Attempted_Incorrect"] = data["Attempted_Incorrect"] + 1
        else:
            data["Attempted_Correct"] = data["Attempted_Correct"] + 1
    data["Total_Marks"] = data["Question_1"] + data["Question_2"] + data["Question_3"] + data["Question_4"] + data["Question_5"] + data["Attempted_Incorrect"] + data["Unattempted"]
    data["Total_Time"] = data["Time_1"] + data["Time_2"] + data["Time_3"] + data["Time_4"] + data["Time_5"] + 2*data["Unattempted"]

    Info["Total_Marks"] = data["Total_Marks"]
    Info["Total_Time"] = data["Total_Time"]

    for i in data:
        list1 = []
        list1.append(data[i])
        data_list[i] = list1
    
    Write_df = pd.DataFrame(data_list)
    Write_df.to_csv(Marks_data_path, mode='a', index=False, header=False)
    Info["rank"] = rank(Info["Total_Marks"],Info["Total_Time"])

def Calculate():
    df_read = pd.read_csv(Marks_data_path)
    arr = df_read.to_numpy()

    Average = np.average(arr, axis=0)
    Avg_marks = Average[0:5]
    Avg_time = Average[5:10]

    Correct_Solved_List = []
    for i in range(5):
        Incorrect_Solved = np.count_nonzero(arr[:,i] == -1)
        Correct_Solved_List.append(len(arr) - Incorrect_Solved)
    Correct_Solved = np.array(Correct_Solved_List)

    return Avg_marks,Avg_time,Correct_Solved

def Marks_Validator():
    df_read = pd.read_csv(Marks_data_path)
    arr = df_read.to_numpy()
    last_rec = arr[len(arr)-1]
    data_marks = []
    for Marks in last_rec[0:5]:
        if(Marks == -1):
            data_marks.append(0)
        else:
            data_marks.append(Marks)
    return data_marks

def bar_graph():
    df_read = pd.read_csv(Marks_data_path)
    arr = df_read.to_numpy()

    bar_fig, bar_ax = plt.subplots()

    bar_x = np.array(["Question_1", "Question_2", "Question_3", "Question_4","Question_5"])
    bar_data_marks = Marks_Validator()
    Avg_marks,Avg_time,Correct_Solved = Calculate()
    bar_Avg_marks = Avg_marks
    
    X_axis = np.arange(len(bar_x))
    width = 0.17
    plt.bar(X_axis - width, bar_data_marks, 2*width, label = 'Scored Marks', color='#023e8a')
    plt.bar(X_axis + width, bar_Avg_marks, 2*width, label = 'Average Marks', color='#0077b6')
    
    plt.xticks(X_axis, bar_x)
    plt.legend()
    plt.xlabel("Question Number",labelpad=15)
    plt.ylabel("Marks Obtained",labelpad=15)

    bar_ax.tick_params(bottom=False, left=True)
    bar_ax.set_axisbelow(True)
    bar_ax.yaxis.grid(True, color='#EEEEEE')
    bar_ax.xaxis.grid(False)

    def addlabels(x,y,dist):
        for i in range(len(x)):
            plt.text(i+dist, y[i]-1,"%0.1f"%y[i], ha = 'center',color = "white")

    addlabels(bar_x, bar_data_marks,-0.17)
    addlabels(bar_x, bar_Avg_marks,0.17)

    bar_fig.tight_layout()
    plt.savefig("static/bar-graph.jpg",dpi = 500,bbox_inches='tight')

def barh_graph():
    df_read = pd.read_csv(Marks_data_path)
    arr = df_read.to_numpy()

    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(y[i]-1,i-0.07,y[i], ha = 'center',color = "white")

    barh_fig, barh_ax = plt.subplots()

    barh_x = np.array(["Question_1", "Question_2", "Question_3", "Question_4","Question_5"])
    Avg_marks,Avg_time,Correct_Solved = Calculate()
    barh_y = np.array(Correct_Solved)
    plt.xlabel("No. of students",labelpad=15)
    plt.ylabel("Question Number",labelpad=15)
    plt.barh(barh_x,barh_y, height = 0.4,color="#40916c" )

    barh_ax.spines['top'].set_visible(False)
    barh_ax.spines['right'].set_visible(False)
    barh_ax.spines['bottom'].set_visible(False)

    barh_ax.set_axisbelow(True)
    barh_ax.yaxis.grid(False)
    barh_ax.xaxis.grid(True, color='#EEEEEE')
    barh_ax.tick_params(bottom=False, left=False)

    barh_fig.tight_layout()

    addlabels(barh_x, barh_y)

    plt.savefig("static/barh-graph.jpg",dpi=500,bbox_inches='tight')

def pie_graph():
    df_read = pd.read_csv(Marks_data_path)
    arr = df_read.to_numpy()  

    last_rec = arr[len(arr)-1]
    if (last_rec[12]==0 and last_rec[13] == 0 and last_rec[14] == 0):
        pass
    else:
        pie_fig, pie_ax = plt.subplots()
        pie_data = last_rec[12:]
        pielabels = ["Attempted_Correct","Attempted_Incorrect","Unattempted"]
        piecolors = ["C9","#ee9b00","#eb4d4b"]

        plt.pie(pie_data, startangle = 90,colors = piecolors,autopct='%1.1f%%',textprops=dict(color="w"),counterclock=False)

        plt.legend(title = "Question Summary:",labels = pielabels,bbox_to_anchor=(1,0.5),loc = "center left")
        pie_fig.tight_layout()
        plt.savefig("static/pie-graph.jpg",dpi=500,bbox_inches='tight')

def Draw_Graph():
    bar_graph()
    barh_graph()
    pie_graph()

def rank(Total_Marks,Total_Time):
    df_read = pd.read_csv(Marks_data_path)
    df_read_sort = df_read.sort_values(['Total_Marks', 'Total_Time'],  ascending=[False, True],ignore_index=True)

    rank = df_read_sort.loc[(df_read_sort['Total_Marks'] == Total_Marks) & (df_read_sort['Total_Time'] == Total_Time)].index + 1
    return rank[0].item()

def SaveButton(checked_option,Ques_time,ques_no):
    if(checked_option == None):
        pass
    elif(QuesAns[ques_no-1]["correctOption"] == checked_option):
        data[f"Question_{ques_no}"] = Marks(Ques_time)
        data[f"Time_{ques_no}"] = Ques_time
    else:
        data[f"Question_{ques_no}"] = -1
        data[f"Time_{ques_no}"] = Ques_time
