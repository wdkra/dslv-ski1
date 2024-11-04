import json
import time


# load file
def load_json_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# show Question and Anwsers
def show_Q_and_A(json_list, query):
    for item in json_list:
        if item["id"] == query or item["question"] == query:
            # show the question (F is Frage)
            print(f"F: {item['question']}")
            for answer in item["answers"]:
                # show options and their trueness
                # X is right (cross), O is false (do not cross)
                correctness = "X" if answer["is_correct"] else "O"
                print(f"- W: ({correctness}) {answer['answer']}")
            return
    print("main.py: Not fund")
    print('Jetzt ist NUR die Suchung mit FRAGEN-Nr. moeglich!!!')


if __name__ == "__main__":
    # fuer Levi sodass er mich nicht fragt
    print('Die Reihenfolge der Optionen ist RANDOM, waehl also bitte die Option fuer sich und NICHT nach ihrer Position aus!!!')
    time.sleep(3)
        
    while True:
        # load answer list
        json_list = load_json_list("resource.json")
    
        show_Q_and_A(json_list, input('Gib Fragen-Nummer ein...\n'))
