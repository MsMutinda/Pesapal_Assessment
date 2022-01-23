import requests, re
from collections import Counter

urls_to_scrape = [
                    'https://github.com/features',
                    'https://www.heroku.com/private-spaces',
                    # "http://127.0.0.1:4735",
                    'https://hexagonaviation.com/contact-us'
                ]

lists = []
for url in urls_to_scrape:
    # fetch text from webpage specified
    text = requests.get(url).text
    # remove html tags
    clean = re.compile('<.*?>')
    cleaned = re.sub(clean, '', text)
    # remove newline characters
    cleaned_text = cleaned.replace('\n', '')
    # extract individual words from the cleaned text
    words = cleaned_text.split()
    # append a sorted list of words from each url onto lists
    lists.append(sorted(words))


# words that exist in github.com and hexagonaviation.com
words_in_all = set(lists[0]).union(set(lists[2]))
print("Words present in the urls {} and {} are: \n {} ".format(urls_to_scrape[0], urls_to_scrape[2], words_in_all))

# words in one webpage but absent in another
# example - site 3 unique words (compared to site 2)
url3_unique = set(lists[2]).difference(set(lists[1]))
# url3_unique = set(lists[2]) - set(lists[1])
print("Words unique for {} are: \n {} ".format(urls_to_scrape[2], url3_unique))


# count number of occurences for each word
for list in lists:
    words_dict = dict()
    for word in list:
        word = word.lower()        
        word_count = 0
        if word not in words_dict:
            word_count = 1
            words_dict[word] = word_count
        else:
            words_dict[word]+=1

    words_list = words_dict.items()
    # words_tuple = [(word, count) for word, count in words_dict.items()]
    # print a sorted list of unique words on a page with the number of occurences for each
    print(sorted(words_list))

