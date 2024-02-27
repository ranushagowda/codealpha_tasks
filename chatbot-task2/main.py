import json
from difflib import get_close_matches
# Load the queries from json file
def load_queries(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data:dict=json.load(file)
    return data
def save_queries(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches:list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None
def get_answer_for_question(question: str, knowledge: dict) -> str | None:
    for q in knowledge["questions"]:
        if q["question"] == question:
            return q["answer"]
def chat_bot():
    knowledge:dict=load_queries('queries.json')
    while True:
        user_input:str=input('You: ').lower()
        if user_input.lower()=='quit':
            break
        best_match:str|None=find_best_match(user_input, [q["question"] for q in knowledge["questions"]])

        if best_match:
            answer: str=get_answer_for_question(best_match, knowledge)
            print(f'Bot:{answer}')
        else:
            print('Bot:i don\'t know the answer.Can you teach me?')
            new_answer:str=input('Type the answer or "skip" to skip:')

            if new_answer.lower()!='skip':
                knowledge["questions"].append({"question": user_input, "answer": new_answer})
                save_queries('queries.json', knowledge)
                print('Bot:Thank you for sharing your knowledge! I learnt a new response:)')
        if user_input=='Bye':
            exit(0)


if __name__=='__main__':
    chat_bot()
