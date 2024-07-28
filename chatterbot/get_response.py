from chatterbot import ChatBot

class ENGSM:
    ISO_639_1 = "en_core_web_sm"

chatbot = ChatBot("Rogerio", tagger_language=ENGSM)

while True:
    
    mensagem = input("Você: ")
    print("")
    
    if mensagem == "sair":
        break
    
    resposta = chatbot.get_response(mensagem)
    print("Rogerio: ")
    print(resposta)
    print("")




