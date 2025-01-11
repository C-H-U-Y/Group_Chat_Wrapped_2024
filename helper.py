def map_contact_name(name):
    chat_sender = str(name)
    if(chat_sender == "Tracka ✏️📓"):
        chat_sender = "Tracka"
    elif(chat_sender == "Toni Lenon"):
        chat_sender = "Toni"
    elif(chat_sender == "Mum"):
        chat_sender = "Lisa"
    elif(chat_sender == "Andrew Wilson"):
        chat_sender = "Andrew"
    elif(chat_sender == "Kylie Mills"):
        chat_sender = "Kylie"
    elif(chat_sender == "Koozee Doozey🌟💫"):
        chat_sender = "Koozee"
    elif(chat_sender == "Ally Wilson 🍺"):
        chat_sender = "Ally"
    elif(chat_sender == "Rose Wilson 🌹"):
        chat_sender = "Rose"
    elif(chat_sender == "Anthony Lemon"):
        chat_sender = "Anthony"
    elif(chat_sender == "ava lennon"):
        chat_sender = "Ava"
    elif(chat_sender == "Oscar Lennon"):
        chat_sender = "Oscar"
    elif(chat_sender == "James Lennon"):
        chat_sender = "Jay"
    return chat_sender


contributions = {
    "Jay":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] # number_contributions, number_reactive, number_proactive, total_images, total_words, total_words_proactive, total_stickers 
    },
    "Toni":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Tracka":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Andrew":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Ally":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Rose":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Kylie":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Anthony":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Oscar":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Ava":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Lisa":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Koozee":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
    "Archie":{
        "contributions" : [],
        "totals" : [0, 0, 0, 0, 0, 0, 0] 
    },
}
