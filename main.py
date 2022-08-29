import json
from random import randint,random

class Questions(object):
    def __init__(self):
        self.questions_file = "questions.json"
        self.traits = {
    "Mind": [{"Trait":"Mind"}, {"Property": [{"INTROVERTED": 0}, {"EXTRAVERTED": 0}]}, {"Descrition": "This trait determines how we interact with our environment."} ],  # Range 1 to 10
    "Energy": [{"Trait":"Energy"}, {"Property": [{"INTUITIVE": 0}, {"OBSERVANT": 0}]} , {"Descrition": "This trait shows where we direct our mental energy."} ],  # Range 1 to 10
    "Nature": [{"Trait":"Nature"}, {"Property": [{"THINKING": 0}, {"FEELING": 0}]} , {"Descrition": "This trait determines how we make decisions and cope with emotions."} ],  # Range 1 to 10
    "Tactics": [{"Trait":"Tactics"}, {"Property": [{"JUDGING": 0}, {"PROSPECTING": 0}]} , {"Descrition": "This trait reflects our approach to work, planning and decision-making."} ],  # Range 1 to 10
    "Identity": [{"Trait":"Identity"}, {"Property": [{"ASSERTIVE": 0}, {"TURBULENT": 0}]} , {"Descrition": "This trait underpins all others, showing how confident we are in our abilities and decisions."} ],  # Range 1 to 10
}
        self.trait_labels = [
            ["Mind", ["INTROVERTED", "EXTRAVERTED"]],
            ["Energy", ["INTUITIVE", "OBSERVANT"]],
            ["Nature", ["THINKING", "FEELING"]],
            ["Tactics", ["JUDGING", "PROSPECTING"]],
            ["Identity", ["ASSERTIVE", "TURBULENT"]],

        ]
        self.load_questions()
        self.answers=[]
        self.answer_range = ["Most Likely","Likely","Neither","Unlikely","Least Likely"]
    def completeQuestionsFormat(self,questions):
        i = 0
        for question in questions:
            if len(question) == 1:
                question.append({"Answer": None})
                i += 1
            if len(question) == 2:
                question.append({"Traits": []})
                i += 1
        if i > 0:
            self.saveToJson(questions)
        self.questions = questions
    def load_questions(self):
        questions = self.load_questions_from_file()
        self.completeQuestionsFormat(questions)
    def isvalid(self, selection):
        if selection == "Most Likely" or "Likely" or "Neither" or "Unlikely" or "Least Likely":
            return True
        else:
            return False
    def doSurvey(self):
        for question in self.questions:
            print(question[0])
            answer = input("5 - Most Likely 4 - Likely 3 - Neither 2 - Unlikely 1 - Least Likely")
            answer = int(answer)
            question[1]["Answer"] = answer
            self.answers.append(self.getAnswers(answer))
        return
    def doRandomSurvey(self):
        for question in self.questions:
            answer = randint(1, 5)
            question[1]["Answer"] = answer
            self.answers.append(self.getAnswers(answer))
    def getAnswers(self, answer):
        if answer == 5:
            return "Most Likely"
        elif answer == 3:
            return "Likely"
        elif answer == 3:
            return "Neither"
        elif answer == 2:
            return "Unlikely"
        elif answer == 1:
            return "Least Likely"
        else:
            return None
    def checkAndUpdateTraitAnswer(self, question):
        answer = question[1]["Answer"]
        if answer is None:
            answer = 0
        mul = 1 * answer
        for trait in question[2]["Traits"]:
            if "Mind" in trait:
                if trait["Mind"]["Property"] == "INTROVERTED":
                    self.traits["Mind"][1]["Property"][0]["INTROVERTED"] += mul
                elif trait["Mind"]["Property"] == "EXTRAVERTED":
                    self.traits["Mind"][1]["Property"][1]["EXTRAVERTED"] += mul

            if "Energy" in trait:
                if trait["Energy"]["Property"] == "INTUITIVE":
                    self.traits["Energy"][1]["Property"][0]["INTUITIVE"] += mul
                elif trait["Energy"]["Property"] == "OBSERVANT":
                    self.traits["Energy"][1]["Property"][1]["OBSERVANT"] += mul
            if "Nature" in trait:
                if trait["Nature"]["Property"] == "THINKING":
                    self.traits["Nature"][1]["Property"][0]["THINKING"] += mul
                elif trait["Nature"]["Property"] == "FEELING":
                    self.traits["Nature"][1]["Property"][1]["FEELING"] += mul
            if "Tactics" in trait:
                if trait["Tactics"]["Property"] == "JUDGING":
                    self.traits["Tactics"][1]["Property"][0]["JUDGING"] += mul
                elif trait["Tactics"]["Property"] == "PROSPECTING":
                    self.traits["Tactics"][1]["Property"][1]["PROSPECTING"] += mul
            if "Identity" in trait:
                if trait["Identity"]["Property"] == "ASSERTIVE":
                    self.traits["Identity"][1]["Property"][0]["ASSERTIVE"] += mul
                elif trait["Identity"]["Property"] == "TURBULENT":
                    self.traits["Identity"][1]["Property"][1]["TURBULENT"] += mul
    def load_questions_from_file(self):
        json_file_data = open(self.questions_file, "r")
        questions = json.load(json_file_data)
        return questions["Questions"]
    def traitsAdder(self,questions):
        for question in questions:
            if "Traits" not in question:
                question.append({"Traits": []})
            ch = "y"
            i = 0
            tkn_path1 = False
            tkn_path2 = False
            tkn_path3 = False
            tkn_path4 = False
            tkn_path5 = False
            while ch != "n":
                print("Choose traits for question...")
                print("================================")
                print(question[0])
                print("================================")
                print("1 - Mind 2 - Energy 3 - Nature 4 - Tactics 5 - Identity")
                ch = input("Choose the trait: ")
                if ch == "n" or i > 4:
                    break
                else:
                    ch = int(ch)
                if ch == 1 and not tkn_path1:
                    tkn_path1 = True
                    question[2]["Traits"].append({"Mind": {}})
                    print("Choose traits property...")
                    print("================================")
                    ch1 = 0
                    while ch1 != "1" and ch1 != "2":
                        ch1 = input("1 - INTROVERTED 2 - EXTROVERTED\n")
                        print(ch1)
                        if ch1 == "1":
                            question[2]["Traits"][i]["Mind"] = {"Property": "INTROVERTED"}
                        elif ch1 == "2":
                            question[2]["Traits"][i]["Mind"] = {"Property": "EXTROVERTED"}
                        else:
                            print("Wrong entry given")

                elif ch == 2 and not tkn_path2:
                    tkn_path2 = True
                    question[2]["Traits"].append({"Energy": {}})
                    print("Choose traits property...")
                    print("================================")
                    ch1 = 0
                    while ch1 != "1" and ch1 != "2":
                        ch1 = input("1 - INTUITIVE 2 - OBSERVANT\n")
                        if ch1 == "1":
                            question[2]["Traits"][i]["Energy"] = {"Property": "INTUITIVE"}
                        elif ch1 == "2":
                            question[2]["Traits"][i]["Energy"] = {"Property": "OBSERVANT"}
                        else:
                            print("Wrong entry given")
                elif ch == 3 and not tkn_path3:
                    tkn_path3 = True
                    question[2]["Traits"].append({"Nature": {}})
                    print("Choose traits property...")
                    print("================================")
                    ch1 = 0
                    while ch1 != "1" and ch1 != "2":
                        ch1 = input("1 - THINKING 2 - FEELING\n")
                        if ch1 == "1":
                            question[2]["Traits"][i]["Nature"] = {"Property": "THINKING"}
                        elif ch1 == "2":
                            question[2]["Traits"][i]["Nature"] = {"Property": "FEELING"}
                        else:
                            print("Wrong entry given")

                elif ch == 4 and not tkn_path4:
                    tkn_path4 = True
                    question[2]["Traits"].append({"Tactics": {}})
                    print("Choose traits property...")
                    print("================================")
                    ch1 = 0
                    while ch1 != "1" and ch1 != "2":
                        ch1 = input("1 - JUDGING 2 - PROSPECTING\n")
                        if ch1 == "1":
                            question[2]["Traits"][i]["Tactics"] = {"Property": "JUDGING"}
                        elif ch1 == "2":
                            question[2]["Traits"][i]["Tactics"] = {"Property": "PROSPECTING"}
                        else:
                            print("Wrong entry given")

                elif ch == 5 and not tkn_path5:
                    tkn_path5 = True
                    question[2]["Traits"].append({"Identity": {}})
                    print("Choose traits property...")
                    print("================================")
                    ch1 = 0
                    while ch1 != "1" and ch1 != "2":
                        ch1 = input("1 - ASSERTIVE 2 - TURBULENT\n")
                        if ch1 == "1":
                            question[2]["Traits"][i]["Identity"] = {"Property": "ASSERTIVE"}
                        elif ch1 == "2":
                            question[2]["Traits"][i]["Identity"] = {"Property": "TURBULENT"}
                        else:
                            print("Wrong entry given")
                else:
                    print("Already added this attribute!")
                    print("================================")

                    i -= 1

                i += 1
            print(question)
            chc = input("Enter anymore question (y/n): ")
            if chc == "n":
                break
        self.saveToJson(question)
    def add_traits(self, question):
        ch = "y"
        i = 0
        tkn_path1 = False
        tkn_path2 = False
        tkn_path3 = False
        tkn_path4 = False
        tkn_path5 = False
        while ch != "n":
            print("Choose traits for question...")
            print("================================")
            print(question[0])
            print("================================")
            print("1 - Mind 2 - Energy 3 - Nature 4 - Tactics 5 - Identity")
            ch = input("Choose the trait: ")
            if ch == "n" or i > 4:
                break
            else:
                ch = int(ch)
            if ch == 1 and not tkn_path1:
                tkn_path1 = True
                question[2]["Traits"].append({"Mind": {}})
                print("Choose traits property...")
                print("================================")
                ch1 = 0
                while ch1 != "1" and ch1 != "2":
                    ch1 = input("1 - INTROVERTED 2 - EXTROVERTED\n")
                    print(ch1)
                    if ch1 == "1":
                        question[2]["Traits"][i]["Mind"] = {"Property": "INTROVERTED"}
                    elif ch1 == "2":
                        question[2]["Traits"][i]["Mind"] = {"Property": "EXTROVERTED"}
                    elif ch1 == "n":
                        del question[2]["Traits"][-1]
                        break
                        i -= 1
                    else:
                        print("Wrong entry given")

            elif ch == 2 and not tkn_path2:
                tkn_path2 = True
                question[2]["Traits"].append({"Energy": {}})
                print("Choose traits property...")
                print("================================")
                ch1 = 0
                while ch1 != "1" and ch1 != "2":
                    ch1 = input("1 - INTUITIVE 2 - OBSERVANT\n")
                    if ch1 == "1":
                        question[2]["Traits"][i]["Energy"] = {"Property": "INTUITIVE"}
                    elif ch1 == "2":
                        question[2]["Traits"][i]["Energy"] = {"Property": "OBSERVANT"}
                    elif ch1 == "n":
                        del question[2]["Traits"][-1]
                        break
                        i -= 1
                    else:
                        print("Wrong entry given")
            elif ch == 3 and not tkn_path3:
                tkn_path3 = True
                question[2]["Traits"].append({"Nature": {}})
                print("Choose traits property...")
                print("================================")
                ch1 = 0
                while ch1 != "1" and ch1 != "2":
                    ch1 = input("1 - THINKING 2 - FEELING\n")
                    if ch1 == "1":
                        question[2]["Traits"][i]["Nature"] = {"Property": "THINKING"}
                    elif ch1 == "2":
                        question[2]["Traits"][i]["Nature"] = {"Property": "FEELING"}
                    elif ch1 == "n":
                        del question[2]["Traits"][-1]
                        break
                        i -= 1
                    else:
                        print("Wrong entry given")

            elif ch == 4 and not tkn_path4:
                tkn_path4 = True
                question[2]["Traits"].append({"Tactics": {}})
                print("Choose traits property...")
                print("================================")
                ch1 = 0
                while ch1 != "1" and ch1 != "2":
                    ch1 = input("1 - JUDGING 2 - PROSPECTING\n")
                    if ch1 == "1":
                        question[2]["Traits"][i]["Tactics"] = {"Property": "JUDGING"}
                    elif ch1 == "2":
                        question[2]["Traits"][i]["Tactics"] = {"Property": "PROSPECTING"}
                    elif ch1 == "n":
                        del question[2]["Traits"][-1]
                        break
                        i -= 1
                    else:
                        print("Wrong entry given")

            elif ch == 5 and not tkn_path5:
                tkn_path5 = True
                question[2]["Traits"].append({"Identity": {}})
                print("Choose traits property...")
                print("================================")
                ch1 = 0
                while ch1 != "1" and ch1 != "2":
                    ch1 = input("1 - ASSERTIVE 2 - TURBULENT\n")
                    if ch1 == "1":
                        question[2]["Traits"][i]["Identity"] = {"Property": "ASSERTIVE"}
                    elif ch1 == "2":
                        question[2]["Traits"][i]["Identity"] = {"Property": "TURBULENT"}
                    elif ch1 == "n":
                        del question[2]["Traits"][-1]
                        break
                        i -= 1
                    else:
                        print("Wrong entry given")
            else:
                print("Already added this attribute!")
                print("================================")

                i -= 1

            i += 1
        print(question)
        return question
    def saveToJson(self,questions):
        print("================================================================================================")
        print("Changes have been made!!!")
        if input("Overwrite existing questions: ") == "y":
            with open('questions.json', 'w') as outfile:
                json_string = {"Questions": questions}
                json.dump(json_string, outfile)
            # Allocate each questions with specific points
    def show_all_questions_with_traits(self):
        # Check that questions have traits defined,
        # if no traits are defined then Show Add traits by question,
        # else show trait count
        # print all questions with traits count
        i = 0
        for question in self.questions:
            if len(question[2]["Traits"]) > 0:
                trait_count = str(len(question[2]["Traits"]))
            else:
                trait_count = str(0)
            print("Q"+ str(i+1) + " -> "+ question[0], " Traits added: " + trait_count)
            i += 1
    def show_traits_of_questions(self,question):
        traits = question[2]["Traits"]
        print("Current Traits...",traits)
        if len(traits) == 0:
            print("No Traits")
        else:
            i = 0
            for trait in traits:
                print("Trait "+ str(i+1) + " -> " + str(trait))
                i += 1

    def show_all_available_traits_for_questions(self):
        i = 0
        for trait in self.traits:
            print("Trait "+ str(i+1) + " " + str(trait) + " -> " + self.traits[trait]["Property"])
            i += 1

    def traitEditer(self):
        # Add and remove and edit traits from the list of questions
        # select question and apply the three methods (Add, Remove, Edit) Traits
        # Add: Add Trait || No more than total number of traits available || No Existing traits
        # Remove: remove selected traits
        # Edit: Edit the selected traits by swapping the property
        # After the operations save the questions to the file
        ch = "y"
        while ch != "n":
            self.show_all_questions_with_traits()
            ch = input("Select the question to show Traits: ")
            if ch != "n":
                ch = int(ch) - 1
            else:
                break
            selected_question = self.questions[ch]
            selected_question_traits_count = len(selected_question[2]["Traits"])
            print("================================================================")
            print("Selected Question: "+ str(selected_question[0]), "Traits: "+ str(selected_question_traits_count))
            print("================================================================")
            if selected_question_traits_count > 0:
                # If traits found add or remove or edit traits
                chra = input("Add, Remove or Edit (enter a/r/e): ")
                if chra != "a" and chra != "n":
                    self.show_traits_of_questions(selected_question)
                    cht = input("Select the Traits: ")
                    if cht != "n" or isinstance(cht,int):
                        cht = int(cht) - 1
                        if chra == "r":
                            del selected_question[2]["Traits"][cht]
                            self.questions[ch] = selected_question
                        if chra == "e":
                            selected_question[2]["Traits"][cht] = self.swap_traits_property(selected_question[2]["Traits"][cht])
                            self.questions[ch] = selected_question

                else:
                    if chra != "n":
                        selected_question = self.add_traits(selected_question)
                        self.questions[ch] = selected_question

            else:
                # if No traits found, add traits
                chra = input("Add Traits (enter y/n): ")
                if chra == "y":
                    selected_question = self.add_traits(selected_question)
                    self.questions[ch] = selected_question
        self.saveToJson(self.questions)

    def swap_traits_property(self, curr_trait):
        #  Check if current trait matches with available traits
        #  After finding the match shift the value to the opposite
        #  Return the current trait
        print("Selected trait: ",curr_trait)
        for trait in self.trait_labels:
            print(trait[1])
            if trait[0] in curr_trait:
                if trait[1][0] in curr_trait[trait[0]]["Property"]:
                    print("Swapped with",trait[1][1])
                    curr_trait[trait[0]]["Property"] = trait[1][1]
                    return curr_trait

                elif trait[1][1] in curr_trait[trait[0]]["Property"]:
                    print("Swapped with", trait[1][0])
                    curr_trait[trait[0]]["Property"] = trait[1][0]
                    return curr_trait


class SurveyResult:
    pass


class Survey():
    def __init__(self):
        self.survey_questions = Questions()
        self.survey_output = None
        self.done_survey = False
    def start(self):
        print("Survey Manager...")
        print("1 - Add/Edit/Remove traits on survey questions")
        print("2 - Do a Survey")
        print("3 - Do random Survey")
        print("4 - Show Survey Output")
        ch = input("Select what you want to do... ")
        if ch == "1":
            self.survey_questions.traitEditer()
        if ch == "2":
            self.survey_output = SurveyResult(self.survey_questions.doSurvey())
        if ch == "3":
            self.survey_output = SurveyResult(self.survey_questions.doRandomSurvey())
        if ch == "4":
            self.show_survey_result()

    def show_survey_result(self):

        pass

# traits = {
#     "Mind": [{"Trait":"Mind"},{"INTROVERTED":0}, {"EXTRAVERTED":0}, {"Descrition": "This trait determines how we interact with our environment."} ],  # Range 1 to 10
#     "Energy": [{"Trait":"Energy"},{"INTUITIVE":0}, {"OBSERVANT":0} , {"Descrition": "This trait shows where we direct our mental energy."} ],  # Range 1 to 10
#     "Nature": [{"Trait":"Nature"},{"THINKING":0}, {"FEELING":0} , {"Descrition": "This trait determines how we make decisions and cope with emotions."} ],  # Range 1 to 10
#     "Tactics": [{"Trait":"Tactics"},{"JUDGING":0}, {"PROSPECTING":0} , {"Descrition": "This trait reflects our approach to work, planning and decision-making."} ],  # Range 1 to 10
#     "Identity": [{"Trait":"Identity"},{"ASSERTIVE":0}, {"TURBULENT":0} , {"Descrition": "This trait underpins all others, showing how confident we are in our abilities and decisions."} ],  # Range 1 to 10
# }
#
# total_traits_points = {"Mind": [{"Trait":"Mind"},{"INTROVERTED": 0}, {"EXTRAVERTED": 0}],
#                         "Energy": [{"Trait":"Energy"},{"INTUITIVE": 0}, {"OBSERVANT": 0}],
#                         "Nature": [{"Trait":"Nature"},{"THINKING": 0}, {"FEELING": 0}],
#                         "Tactics": [{"Trait":"Tactics"},{"JUDGING": 0}, {"PROSPECTING": 0}],
#                         "Identity": [{"Trait":"Identity"},{"ASSERTIVE": 0}, {"TURBULENT": 0}]
#                       ,}
#
# def addPoints(self, to, of):
#     if of == "Most Likely":
#         total_traits_points[to][of] += 1

survey = Survey()
survey.start()


# question = ["You regularly make new friends.", {"Answer": None}, {"Traits": [{"Mind": {"Property": "INTROVERTED"}}, {"Energy": {"Property": "OBSERVANT"}}, {"Nature": {"Property": "THINKING"}}, {"Tactics": {"Property": "JUDGING"}}, {"Identity": {"Property": "TURBULENT"}}]}]
# newQuestions = Questions(None)
# newQuestions.checkAndUpdateTraitAnswer(question)
# print(newQuestions.load_questions_from_file())
# print(newQuestions.traits)
# print("Mind" in question[2]["Traits"][0])
#
#
#
# questions = [["You regularly make new friends.",{"Answer":None},],
#              ["You spend a lot of your free time exploring various random topics that pique your interest.",{"Answer":None},],
#              ["Seeing other people cry can easily make you feel like you want to cry too.",{"Answer":None},],
#              ["You often make a backup plan for a backup plan.",{"Answer":None},],
#              ["You usually stay calm, even under a lot of pressure.",{"Answer":None},],
#              ["At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.",{"Answer":None},],
#              ["You prefer to completely finish one project before starting another.",{"Answer":None},],
#              ["You are very sentimental.",{"Answer":None},],
#              ["You like to use organizing tools like schedules and lists.",{"Answer":None},],
#              ["Even a small mistake can cause you to doubt your overall abilities and knowledge.",{"Answer":None},],
#              ["You feel comfortable just walking up to someone you find interesting and striking up a conversation.",{"Answer":None},],
#              ["You are not too interested in discussing various interpretations and analyses of creative works.",{"Answer":None},],
#              ["You are more inclined to follow your head than your heart.",{"Answer":None},],
#              ["You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.",{"Answer":None},],
#              ["You rarely worry about whether you make a good impression on people you meet.",{"Answer":None},],
#              ["You enjoy participating in group activities.",{"Answer":None},],
#              ["You like books and movies that make you come up with your own interpretation of the ending.",{"Answer":None},],
#              ["Your happiness comes more from helping others accomplish things than your own accomplishments.",{"Answer":None},],
#              ["You are interested in so many things that you find it difficult to choose what to try next.",{"Answer":None},],
#              ["You are prone to worrying that things will take a turn for the worse.",{"Answer":None},],
#              ["You avoid leadership roles in group settings.",{"Answer":None},],
#              ["You are definitely not an artistic type of person.",{"Answer":None},],
#              ["You think the world would be a better place if people relied more on rationality and less on their feelings.",{"Answer":None},],
#              ["You prefer to do your chores before allowing yourself to relax.",{"Answer":None},],
#              ["You enjoy watching people argue.",{"Answer":None},],
#              ["You tend to avoid drawing attention to yourself.",{"Answer":None},],
#              ["Your mood can change very quickly.",{"Answer":None},],
#              ["You lose patience with people who are not as efficient as you.",{"Answer":None},],
#              ["You often end up doing things at the last possible moment.",{"Answer":None},],
#              ["You become bored or lose interest when the discussion gets highly theoretical.",{"Answer":None},],
#              ["You find it easy to empathize with a person whose experiences are very different from yours.",{"Answer":None},],
#              ["You usually postpone finalizing decisions for as long as possible.",{"Answer":None},],
#              ["You rarely second-guess the choices that you have made.",{"Answer":None},],
#              ["After a long and exhausting week, a lively social event is just what you need.",{"Answer":None},],
#              ["You like to have a to-do list for each day.",{"Answer":None},],
#              ["You rarely feel insecure.",{"Answer":None},],
#              ["You often spend a lot of time trying to understand views that are very different from your own.",{"Answer":None},],
#              ["In your social circle, you are often the one who contacts your friends and initiates activities.",{"Answer":None},],
#              ["If your plans are interrupted, your top priority is to get back on track as soon as possible.",{"Answer":None},],
#              ["You are still bothered by mistakes that you made a long time ago.",{"Answer":None},],
#              ["You rarely contemplate the reasons for human existence or the meaning of life.",{"Answer":None},],
#              ["Your emotions control you more than you control them.",{"Answer":None},],
#              ["You take great care not to make people look bad, even when it is completely their fault.",{"Answer":None},],
#              ["Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.",{"Answer":None},],
#              ["When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.",{"Answer":None},],
#              ["You would love a job that requires you to work alone most of the time.",{"Answer":None},],
#              ["You believe that pondering abstract philosophical questions is a waste of time.",{"Answer":None},],
#              ["You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.",{"Answer":None},],
#              ["You know at first glance how someone is feeling.",{"Answer":None},],
#              ["You often feel overwhelmed.",{"Answer":None},],
#              ["You complete things methodically without skipping over any steps.",{"Answer":None},],
#              ["You are very intrigued by things labeled as controversial.",{"Answer":None},],
#              ["You would pass along a good opportunity if you thought someone else needed it more.",{"Answer":None},],
#              ["You struggle with deadlines.",{"Answer":None},],
#              ["You feel confident that things will work out for you.",{"Answer":None},],]
#
# def traitsAdder(questions):
#     for question in questions:
#         question.append({"Traits":[]})
#         ch = "y"
#         i = 0
#         tkn_path1 = False
#         tkn_path2 = False
#         tkn_path3 = False
#         tkn_path4 = False
#         tkn_path5 = False
#         while ch != "n":
#             print("Choose traits for question...")
#             print("================================")
#             print(question[0])
#             print("================================")
#             print("1 - Mind 2 - Energy 3 - Nature 4 - Tactics 5 - Identity")
#             ch = input("Choose the trait: ")
#             if ch == "n" or i > 4:
#                 break
#             else:
#                 ch = int(ch)
#             if ch == 1 and not tkn_path1:
#                 tkn_path1 = True
#                 question[2]["Traits"].append({"Mind":{}})
#                 print("Choose traits property...")
#                 print("================================")
#                 ch1 = 0
#                 while ch1 != "1" and ch1 != "2":
#                     ch1 = input("1 - INTROVERTED 2 - EXTROVERTED\n")
#                     print(ch1)
#                     if ch1 == "1":
#                         question[2]["Traits"][i]["Mind"] = {"Property":"INTROVERTED"}
#                     elif ch1 == "2":
#                         question[2]["Traits"][i]["Mind"] = {"Property":"EXTROVERTED"}
#                     else:
#                         print("Wrong entry given")
#
#             elif ch == 2 and not tkn_path2:
#                 tkn_path2 = True
#                 question[2]["Traits"].append({"Energy":{}})
#                 print("Choose traits property...")
#                 print("================================")
#                 ch1 = 0
#                 while ch1 != "1" and ch1 != "2":
#                     ch1 = input("1 - INTUITIVE 2 - OBSERVANT\n")
#                     if ch1 == "1":
#                         question[2]["Traits"][i]["Energy"] = {"Property":"INTUITIVE"}
#                     elif ch1 == "2":
#                         question[2]["Traits"][i]["Energy"] = {"Property":"OBSERVANT"}
#                     else:
#                         print("Wrong entry given")
#             elif ch == 3 and not tkn_path3:
#                 tkn_path3 = True
#                 question[2]["Traits"].append({"Nature": {}})
#                 print("Choose traits property...")
#                 print("================================")
#                 ch1 = 0
#                 while ch1 != "1" and ch1 != "2":
#                     ch1 = input("1 - THINKING 2 - FEELING\n")
#                     if ch1 == "1":
#                         question[2]["Traits"][i]["Nature"] = {"Property":"THINKING"}
#                     elif ch1 == "2":
#                         question[2]["Traits"][i]["Nature"] = {"Property":"FEELING"}
#                     else:
#                         print("Wrong entry given")
#
#             elif ch == 4 and not tkn_path4:
#                 tkn_path4 = True
#                 question[2]["Traits"].append({"Tactics": {}})
#                 print("Choose traits property...")
#                 print("================================")
#                 ch1 = 0
#                 while ch1 != "1" and ch1 != "2":
#                     ch1 = input("1 - JUDGING 2 - PROSPECTING\n")
#                     if ch1 == "1":
#                         question[2]["Traits"][i]["Tactics"] = {"Property":"JUDGING"}
#                     elif ch1 == "2":
#                         question[2]["Traits"][i]["Tactics"] = {"Property":"PROSPECTING"}
#                     else:
#                         print("Wrong entry given")
#
#             elif ch == 5 and not tkn_path5:
#                 tkn_path5 = True
#                 question[2]["Traits"].append({"Identity":{}})
#                 print("Choose traits property...")
#                 print("================================")
#                 ch1 = 0
#                 while ch1 != "1" and ch1 != "2":
#                     ch1 = input("1 - ASSERTIVE 2 - TURBULENT\n")
#                     if ch1 == "1":
#                         question[2]["Traits"][i]["Identity"] = {"Property":"ASSERTIVE"}
#                     elif ch1 == "2":
#                         question[2]["Traits"][i]["Identity"] = {"Property":"TURBULENT"}
#                     else:
#                         print("Wrong entry given")
#             else:
#                 print("Already added this attribute!")
#                 print("================================")
#
#                 i -= 1
#
#             i += 1
#         print(question)
#         chc = input("Enter anymore question (y/n): ")
#         if chc == "n":
#             break
#     with open('questions.json', 'w') as outfile:
#         json_string = {"Questions": questions}
#         json.dump(json_string, outfile)
#
#         # Allocate each questions with specific points
# if input("Add traits to questions and save file") == "y":
#     traitsAdder(questions)
# # questions = [["You regularly make new friends.",{"Answer":None},{"Traits":[["Mind",{"Property":None}]]}],
# #              ["You spend a lot of your free time exploring various random topics that pique your interest.",{"Answer":None},{"Traits":None}],
# #              ["Seeing other people cry can easily make you feel like you want to cry too.",{"Answer":None},{"Traits":None}],
# #              ["You often make a backup plan for a backup plan.",{"Answer":None},{"Traits":None}],
# #              ["You usually stay calm, even under a lot of pressure.",{"Answer":None},{"Traits":None}],
# #              ["At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know.",{"Answer":None},{"Traits":None}],
# #              ["You prefer to completely finish one project before starting another.",{"Answer":None},{"Traits":None}],
# #              ["You are very sentimental.",{"Answer":None},{"Traits":None}],
# #              ["You like to use organizing tools like schedules and lists.",{"Answer":None},{"Traits":None}],
# #              ["Even a small mistake can cause you to doubt your overall abilities and knowledge.",{"Answer":None},{"Traits":None}],
# #              ["You feel comfortable just walking up to someone you find interesting and striking up a conversation.",{"Answer":None},{"Traits":None}],
# #              ["You are not too interested in discussing various interpretations and analyses of creative works.",{"Answer":None},{"Traits":None}],
# #              ["You are more inclined to follow your head than your heart.",{"Answer":None},{"Traits":None}],
# #              ["You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.",{"Answer":None},{"Traits":None}],
# #              ["You rarely worry about whether you make a good impression on people you meet.",{"Answer":None},{"Traits":None}],
# #              ["You enjoy participating in group activities.",{"Answer":None},{"Traits":None}],
# #              ["You like books and movies that make you come up with your own interpretation of the ending.",{"Answer":None},{"Traits":None}],
# #              ["Your happiness comes more from helping others accomplish things than your own accomplishments.",{"Answer":None},{"Traits":None}],
# #              ["You are interested in so many things that you find it difficult to choose what to try next.",{"Answer":None},{"Traits":None}],
# #              ["You are prone to worrying that things will take a turn for the worse.",{"Answer":None},{"Traits":None}],
# #              ["You avoid leadership roles in group settings.",{"Answer":None},{"Traits":None}],
# #              ["You are definitely not an artistic type of person.",{"Answer":None},{"Traits":None}],
# #              ["You think the world would be a better place if people relied more on rationality and less on their feelings.",{"Answer":None},{"Traits":None}],
# #              ["You prefer to do your chores before allowing yourself to relax.",{"Answer":None},{"Traits":None}],
# #              ["You enjoy watching people argue.",{"Answer":None},{"Traits":None}],
# #              ["You tend to avoid drawing attention to yourself.",{"Answer":None},{"Traits":None}],
# #              ["Your mood can change very quickly.",{"Answer":None},{"Traits":None}],
# #              ["You lose patience with people who are not as efficient as you.",{"Answer":None},{"Traits":None}],
# #              ["You often end up doing things at the last possible moment.",{"Answer":None},{"Traits":None}],
# #              ["You become bored or lose interest when the discussion gets highly theoretical.",{"Answer":None},{"Traits":None}],
# #              ["You find it easy to empathize with a person whose experiences are very different from yours.",{"Answer":None},{"Traits":None}],
# #              ["You usually postpone finalizing decisions for as long as possible.",{"Answer":None},{"Traits":None}],
# #              ["You rarely second-guess the choices that you have made.",{"Answer":None},{"Traits":None}],
# #              ["After a long and exhausting week, a lively social event is just what you need.",{"Answer":None},{"Traits":None}],
# #              ["You like to have a to-do list for each day.",{"Answer":None},{"Traits":None}],
# #              ["You rarely feel insecure.",{"Answer":None},{"Traits":None}],
# #              ["You often spend a lot of time trying to understand views that are very different from your own.",{"Answer":None},{"Traits":None}],
# #              ["In your social circle, you are often the one who contacts your friends and initiates activities.",{"Answer":None},{"Traits":None}],
# #              ["If your plans are interrupted, your top priority is to get back on track as soon as possible.",{"Answer":None},{"Traits":None}],
# #              ["You are still bothered by mistakes that you made a long time ago.",{"Answer":None},{"Traits":None}],
# #              ["You rarely contemplate the reasons for human existence or the meaning of life.",{"Answer":None},{"Traits":None}],
# #              ["Your emotions control you more than you control them.",{"Answer":None},{"Traits":None}],
# #              ["You take great care not to make people look bad, even when it is completely their fault.",{"Answer":None},{"Traits":None}],
# #              ["Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.",{"Answer":None},{"Traits":None}],
# #              ["When someone thinks highly of you, you wonder how long it will take them to feel disappointed in you.",{"Answer":None},{"Traits":None}],
# #              ["You would love a job that requires you to work alone most of the time.",{"Answer":None},{"Traits":None}],
# #              ["You believe that pondering abstract philosophical questions is a waste of time.",{"Answer":None},{"Traits":None}],
# #              ["You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.",{"Answer":None},{"Traits":None}],
# #              ["You know at first glance how someone is feeling.",{"Answer":None},{"Traits":None}],
# #              ["You often feel overwhelmed.",{"Answer":None},{"Traits":None}],
# #              ["You complete things methodically without skipping over any steps.",{"Answer":None},{"Traits":None}],
# #              ["You are very intrigued by things labeled as controversial.",{"Answer":None},{"Traits":None}],
# #              ["You would pass along a good opportunity if you thought someone else needed it more.",{"Answer":None},{"Traits":None}],
# #              ["You struggle with deadlines.",{"Answer":None},{"Traits":None}],
# #              ["You feel confident that things will work out for you.",{"Answer":None},{"Traits":None}],]
#
#
# def fillQuestions(questions):
#     for question in questions:
#         random_ch = randint(1, 5)
#         question[1]["Answer"] = random_ch
#     return questions
#
# questions = fillQuestions(questions)
# for question in questions:
#     print(question)