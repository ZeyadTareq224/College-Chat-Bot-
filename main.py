import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def load_data(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def train_model(trainer):

    data = load_data('intents.json')
    for sample in data.get("intents"):
        dialogue = []
        questions = sample.get("text", [])
        responses = sample.get("responses", [])
        
        for question in questions:
            for response in responses:
                
                dialogue.append(question)
                dialogue.append(response)
        trainer.train(dialogue)

def get_response(question):
    bot = ChatBot('Norman', logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
    ])
    trainer = ListTrainer(bot)
    train_model(trainer=trainer)

    answer = bot.get_response(question)
    return answer
