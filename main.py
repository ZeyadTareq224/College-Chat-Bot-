import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def load_data(json_file_path: str) -> dict:
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def train_model() -> ChatBot:
    bot = ChatBot('Norman', logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
    ])
    trainer = ListTrainer(bot)
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
    return bot

def get_response(bot:ChatBot, question:str) -> str:
    
    answer = bot.get_response(question)
    return answer

