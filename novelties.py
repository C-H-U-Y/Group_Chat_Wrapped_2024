import json

data = json.loads(open("data.json").read())

smallest_contribution_length = 9999999999
smallest_contribution = None
contributor_of_smallest = None

for key in data:
    contributor = key
    contributions = data[key]['contributions']

    for contribution in contributions:
        words = contribution.split(" ")
        word_sum = 0

        breaking = False
        for word in words:
            if(word == "[IMAGE/VIDEO]"):
                breaking  = True
                break
            else:
                word_sum += 1

        if(breaking):
            break
        
        if(word_sum < smallest_contribution_length):
            smallest_contribution = contribution
            smallest_contribution_length = word_sum
            contributor_of_smallest = contributor
            continue
    
    
largest_contribution_length = 0
largest_contribution = None
contributor_of_largest = None

for key in data:
    contributor = key
    contributions = data[key]['contributions']

    for contribution in contributions:
        words = contribution.split(" ")
        word_sum = 0

        breaking = False
        for word in words:
            word_sum += 10
        
        if(word_sum > largest_contribution_length):
            largest_contribution = contribution
            largest_contribution_length = word_sum
            contributor_of_largest = contributor
            continue
    
print("-------")
print(largest_contribution_length)
print(largest_contribution)
print(contributor_of_largest)

maximum_yap = None
maximum_yapper = None

# Biggest yapper = most reactive words per proactive post
for key in data:
    contributor = key
    contributions = data[key]['contributions']

    reactive_words = data[key]['totals'][4] - data[key]['totals'][5]
    proactive_posts = data[key]['totals'][2]

    yap_ratio = reactive_words/proactive_posts

    if(maximum_yap == None):
        maximum_yap = yap_ratio
        maximum_yapper = contributor

    elif(yap_ratio > maximum_yap):
        maximum_yap = yap_ratio
        maximum_yapper = contributor

print('------')
print(maximum_yap)
print(maximum_yapper)






