# regex for whitespace manipulation ):
import re

# chatgpt for message sentiment analysis
from openai import OpenAI

# json handling 
import json

client = OpenAI(
  api_key="REDACTED"
)


# 1. Read in data
# ----------
# exported into a text file because its easier to parse
data_file = open("./data/chat_dataset_txt.txt", encoding='UTF-8')
chat_log = data_file.read()
data_file.close()
# ----------

# 2. segment data for proccesing
# ----------
# Messages are delimited (and bookmarked) by these lines
# First item will be empty because of the bookmarked delimiter, so skip that as well
chat_log_split = chat_log.split("----------------------------------------------------")[1:]
# ----------

# 3. Auxillary functions for processing
# ----------
# 3.1 - map the contact name in dataset to the name in the contributions data map (see section 4)
from helper import map_contact_name
# ----------

# 4. proccess
# ----------
# GOAL = populate the below json with GROUPS of contributions (grouping messages that are sent back to back) and their metadata
# Classify contributions as pro-active or re-active, note down their length, reactions and metadata and save all this in the data structure
from helper import contributions

# variable setup for section 4.4
current_contributor = None
current_contribution = []

# variable setup for section 4.5
contribution_iteration = 1

# 4.1 - Iterate through messages
# ----------
for chat in chat_log_split:
    
    # split the content for proccessing
    chat_lines = chat.split('\n')

    # 4.2 - get metadata and also chat content
    # ----------
    # get chat info
    _,chat_name,chat_information,_ = chat_lines[0:4]
    # get chat content
    chat_content = chat_lines[4:-2]

    # proccess information into metadata
    # ignore notifications
    if("notification" in chat_information):
        continue

    # messages recieved and messages sent are formatted different
    if("from" in chat_information):
        chat_time, remaining_info = chat_information.split(" from ")
        chat_sender, _ = remaining_info.split(" (+")
    else:
        chat_time, remaining_info = chat_information.split(" to ")
        chat_sender = "Archie"

    # transfer chat sender from contact name to name recognisable by data map
    chat_sender = map_contact_name(chat_sender)    
    
    # print(chat_sender)
    # print(chat_content)    
    # ----------


    # 4.3 - detect chat type
    # ----------
    # possible types = (sticker / gif), (image / video), text
    message_type = None

    for content_section in chat_content:
        if("(Video)" in content_section or "(Image)" in content_section):
            message_type = "image_video"
            break
        if("(Sticker)" in content_section or "(Gif)" in content_section):
            message_type = "gif_sticker"
            break

    if(message_type == None):
        message_type = "text"
    
    # print(message_type)
    # ----------

    # 4.4 - group messages into strings of contributions
    # ----------
    # track the current contributor and their a list of the content of this contribution
    if(current_contributor == None):
        current_contributor = chat_sender

    # if this is from the current contributor, simply append the content and move on
    if(chat_sender == current_contributor):
        current_contribution.append([message_type, chat_content])
        continue        
    
    # else - this message is not part of the existing contirbution and we can break off for analysis
    contribution_to_proccess = current_contribution
    contributor = current_contributor

    # reset the data, appending the current message to a new string of contributions
    current_contribution = []
    current_contributor = chat_sender
    current_contribution.append([message_type, chat_content])
    # ----------

    # 4.5 - Analyse the contribution and append to data array
    # ----------
    num_images = 0
    num_stickers = 0
    num_words = 0
    contribution_text_string = ""

    for contribution_part in contribution_to_proccess:
        # unpack saved data
        part_type, part_content = contribution_part

        # analyse a replying to????

        # compress text into a concise string
        if(part_type == "text"):
            # setup to skip the whole 'replying too message"
            skipping = False
            for section in part_content:

                # strip back replies because they don't count as your contribution
                if("➜ Replying to " in section):
                    if("»" not in section):
                        skipping = True
                    continue

                if("»" in section):
                    skipping = False
                    continue
                
                if(skipping):
                    continue
                
                contribution_text_string += section

                if(section == ""):
                    contribution_text_string += ' '

        elif(part_type == "image_video"):
            contribution_text_string += " [IMAGE/VIDEO] "
            num_images += 1

            # extract any image caption as well
            if(len(part_content) > 3):
                contribution_text_string += part_content[0]

        
        elif(part_type == "gif_sticker"):
            contribution_text_string += " [GIF/STICKER] "
            num_stickers += 1
        
        contribution_text_string += " " 
        
    # process whitespace (replace all blocks of consecutive whitespace with a single space and then strip trailing and leading whitespace characters)
    contribution_text_string = re.sub(r'\s+', ' ', contribution_text_string).strip()
    num_words += len(contribution_text_string.split(" "))
    # ----------

    # 4.5 - Save the contribution data
    # ----------    
    # save the contributions
    contributions[contributor]['contributions'].append(contribution_text_string)

    # increment the totals
    contributions[contributor]['totals'][0] += 1 
    contributions[contributor]['totals'][3] += num_images
    contributions[contributor]['totals'][4] += num_words
    contributions[contributor]['totals'][6] += num_stickers

    # 4.6 - Use chatGPT wrapper to classify message
    # ----------    
    print("Classifying message from {}\n----------\n{}\n----------".format(contributor, contribution_text_string))
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {
            "role": "developer", 
            "content": "You are classifying group chat messages as either 'Proactive' or 'Reactive' on the nature of the content. Any message that seems to be providing unseen content and insights to the chat should be classified as Proactive. Some pre-processing has been done such that images and vidoes have been replaced with the text [IMAGE/VIDEO]. Images (NOT EMOJIS) should almost always be considered proactive when some other supporting content is provided (brief captions / text ). Try think about wether or not it seems as though a message is a direct response to someone's previous content (these types of messages are reactive!). Remember, proactive / reactive is not about the tone of the message or if it's 'uplifting' it's only about proactivity in terms of content generation. Reply with only 1 word."
        },
        {
            "role": "user", 
            "content": "{}".format(contribution_text_string)
        }
    ]
    )

    message_category = (str(completion.choices[0].message).split("content='")[1].split("'")[0])
    print("{}\n\n".format(message_category))

    # ----------    

    
    if(message_category == "Proactive"):
        contributions[contributor]['totals'][2] += 1
        contributions[contributor]['totals'][5] += num_words

    else:
        contributions[contributor]['totals'][1] += 1

    # ----------

    # track the current contribution index ... might be helpful later
    contribution_iteration += 1
    
# ----------


# Save JSON object to a file in a readable format
with open('data.json', 'w') as file:
    json.dump(contributions, file, indent=4)