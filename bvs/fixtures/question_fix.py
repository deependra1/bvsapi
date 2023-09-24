import json
from datetime import datetime


questions_data = [
    "What is the current health status of the patient?",
    "Has the doctor scheduled any follow up visits or medical treatment?",
    "Have you beeb exercising as per the physiotherapist's advice? Do you find it beneficial?",
    "Have you faced any kind of difficulty in daily life activities of dependent on family for basic chores?",
    "Social treatment post burn support/view?",
    "How supportive is the family?",
    "What was your means of livelihood in any economic generating activity?",
    "If you are involved, have you faced any challenges? Workplace treatment?",
    "Ask if the patient is interested in any training or area of interest or support? Yes/No",
    "Is the child reluctant to go to school? or Effect on child's education after incident",
    "How well has s/he adjust with their friends?",
    "Can the child independently function or is dependent on the family of basic chores?",
    "Societal perception towards the child?",
    "If the child is disabled, what are the problems faced by the patient?",
    "What kind of changes have you noticed on your child pre/post incident or BVSN's intervention?"

]

questions = []
for index, question in enumerate(questions_data):
    question = {
        "model": "bvs_question.Question",
        "pk": index + 1,
        "fields": {
            "questionnaire": question,
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    questions.append(question)

with open("questions.json", "w") as questions_file:
    json.dump(questions, questions_file, indent=4)
