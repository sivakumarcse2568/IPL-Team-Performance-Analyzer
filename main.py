import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import webbrowser
import matplotlib.image as mpimg

data = pd.read_csv("ipl_2026_teams.csv") 

def display_data(): #1
    print(data)

def most_runs():  #2
    highest=data["Total_Runs"].max() #3094

    for i in range(len(data)):
        if(data["Total_Runs"][i] == highest):           #table[col][index]= value
            print("Most Runs by a Team: ", data["Team"][i])
            print("Total Runs: ",highest)
            print()
            
def most_sixes():  #3
    highest=data["Total_Sixes"].max()

    for i in range(len(data)):
        if(data["Total_Sixes"][i] == highest):
            print("Most Sixes by a Team: ", data["Team"][i])
            print("Total Sixes: ",highest)
            print()

def most_fours():  #4
    highest=data["Total_Fours"].max()

    for i in range(len(data)):
        if(data["Total_Fours"][i] == highest):
            print("Most Fours by a Team: ", data["Team"][i])
            print("Total Fours: ",highest)
            print()

def most_wickets(): #5
    highest=data["Total_Wickets"].max()

    for i in range(len(data)):
        if(data["Total_Wickets"][i] == highest):
            print("Most Wickets taken by a Team: ", data["Team"][i])
            print("Total Wickets: ",highest)
            print()

def high_avg_Score():  #6
    highest=data["Avg_Team_Score"].max()

    for i in range(len(data)):
        if(data["Avg_Team_Score"][i] == highest):
            print("Highest Innings Average by a Team: ", data["Team"][i])
            print("Average: ",highest)
            print()

def most_victories():  #7
    highest=data["Wins"].max()

    for i in range(len(data)):
        if(data["Wins"][i] == highest):
            matches = data["Matches"][i]
            print("Most Wins in the Season: ", data["Team"][i])
            print("Total Wins: ",highest,"/",matches)
            print()

def high_win_percentage():  #8
    highest=data["Win_Percentage"].max()

    for i in range(len(data)):
        if(data["Win_Percentage"][i] == highest):
            print("Highest Win Percentage by a Team: ", data["Team"][i])
            print("Win Percentage: ",highest)
            print()

def highest_team_score():  #9
    highest=data["Highest_Team_Score"].max()

    for i in range(len(data)):
        if(data["Highest_Team_Score"][i] == highest):
            print("Highest Score by a Team(in Innings): ", data["Team"][i])
            print("Team Score: ",highest)
            print()
            
def lowest_team_score():  #10
    lowest=data["Lowest_Team_Score"].min()

    for i in range(len(data)):
        if(data["Lowest_Team_Score"][i] == lowest):
            print("Lowest Score by a Team(in Innings): ", data["Team"][i])
            print("Team Score: ",lowest) 
            print()
            
def top_performer():  #11
    for i in range(len(data)):
        print("*** Team : ",data["Team"][i],"***")
        
        print("Top Batter: ",data["Highest_Run_Player"][i])
        print("Top Bowler: ",data["Highest_Wicket_Player"][i])
        print()

def avg_team_runs():  #12
    runs=np.array(data["Total_Runs"])  #stored as numPy array [.....]
    average = np.mean(runs)   
    print("Average Total Runs of all Teams: ",round(average,2))
    print()

def open_ipl_logo():  #14
    webbrowser.open("https://www.iplt20.com/")

def show_logo():
    image = mpimg.imread("ipl_logo.jpg")

    plt.imshow(image)
    plt.axis("off")
    plt.title("IPL 2026 Team Performance Analyzer")
    plt.show()

#****************************************************************************************************
    
def total_runs_graph():  #1
    plt.bar(data["Team"],data["Total_Runs"])  #plt.bar(x-axis,y-axis)
    plt.title("Total Runs by IPL Teams")    
    plt.xlabel("Team")
    plt.ylabel("Total Runs")

    for i in range(len(data)):
        plt.text(i, data["Total_Runs"][i], data["Total_Runs"][i]) #At X = 0 and Y = 3057, write "3057" ...
    plt.show()

def total_sixes_graph():  #2
    plt.bar(data["Team"],data["Total_Sixes"])
    plt.title("Total Sixes by IPL Teams")
    plt.xlabel("Team")
    plt.ylabel("Total Sixe")

    for i in range(len(data)):
        plt.text(i, data["Total_Sixes"][i], data["Total_Sixes"][i]) 
    plt.show()

def total_wickets_graph():     #3
    labels = []
    for i in range(len(data)):
        labels.append(data["Team"][i] + " - " + str(data["Total_Wickets"][i]))   # "Team" + "-" + "Wickets"
    plt.pie(data["Total_Wickets"], labels=labels)
    plt.title("Total Wickets by IPL Teams")
    plt.show()

def wins_losses_graph():     #4
    losses = data["Matches"] - data["Wins"]
    plt.bar(data["Team"], data["Wins"], label="Wins")
    plt.bar(data["Team"], losses, bottom=data["Wins"], label="Losses")  #bottom=> start the loss bar on top of WinsBar
    plt.title("Wins vs Losses by IPL Teams")
    plt.xlabel("Team")
    plt.ylabel("Matches")
    plt.legend()
    for i in range(len(data)):
        plt.text(i, data["Wins"][i], data["Wins"][i])  #(x-pos , y-pos , Text to add)
        plt.text(i, data["Matches"][i], losses[i])  #display values at top bar

    plt.show()

def win_percentage_graph():     #5
    plt.plot(data["Team"], data["Win_Percentage"], marker="o")
    plt.title("Win Percentage by IPL Teams")
    plt.xlabel("Team")
    plt.ylabel("Win Percentage")
    for i in range(len(data)):
        plt.text(i, data["Win_Percentage"][i], data["Win_Percentage"][i])   #(x-pos , y-pos , text )
    plt.show()

#****************************************************************************************************
    
def graph_menu():   #13
    while True:
        print("***** GRAPHICAL ANALYSIS *****")
        print("1. Total Runs by Team.")
        print("2. Total Sixes by Team.")
        print("3. Total Wickets by Team.")
        print("4. Wins vs Losses.")
        print("5. Win Percentage.")
        print("6. Back to Main Menu.")
        print()

        choice = int(input("Enter your choice: "))
        print()

        if(choice == 1):
            total_runs_graph()

        elif(choice == 2):
            total_sixes_graph()

        elif(choice == 3):
            total_wickets_graph()

        elif(choice == 4):
            wins_losses_graph()

        elif(choice == 5):
            win_percentage_graph()

        elif(choice == 6):
            break

        else:
            print("Invalid choice. Please try again.")

        print()

def menu():
    while True:
        print()
        print("==========================================")
        print("     IPL 2026 TEAM PERFORMANCE ANALYZER")
        print("==========================================")
        print("1. Display Team Statistics.")
        print("2. Team with Most Runs.")
        print("3. Team with Most Sixes.")
        print("4. Team with Most Fours.")
        print("5. Team with Most Wickets.")
        print("6. Team with Highest Average Score.")
        print("7. Team with Most Victories.")
        print("8. Team with Highest Win Percentage.")
        print("9. Highest Team Score.")
        print("10. Lowest Team Score.")
        print("11. Top Performer of Each Team.")
        print("12. Average Total Runs of All Teams.")
        print("13. Graph Analysis.")
        print("14. Open IPL Website.")
        print("15. Exit.")
        print()

        choice=int(input("Enter your choice: "))
        if(choice == 1):
            display_data()

        elif(choice == 2):
            most_runs()

        elif(choice == 3):
            most_sixes()

        elif(choice == 4):
            most_fours()

        elif(choice == 5):
            most_wickets()

        elif(choice == 6):
            high_avg_Score()

        elif(choice == 7):
            most_victories()

        elif(choice == 8):
            high_win_percentage()

        elif(choice == 9):
            highest_team_score()

        elif(choice == 10):
            lowest_team_score()

        elif(choice == 11):
            top_performer()

        elif(choice == 12):
            avg_team_runs()

        elif(choice == 13):
            graph_menu()

        elif(choice == 14):
            open_ipl_logo()

        elif(choice == 15):
            print("Thank you for using IPL 2026 Team Performance Analyzer!")
            print()
            break

        else:
            print("Invalid Choice!!")
            print()

print()
print("Welcome to IPL 2026 Team Performance Analyzer!")
print("Analyze team statistics, performance and graphs.")

show_logo()

menu()



