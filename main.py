import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response = False, required_words = []):
    message_certainity = 0
    has_required_words = True;

    # count how many word are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainity += 1
    
    # calculating percentage of recognized words in user message
    percentage = float(message_certainity)/ float(len(recognised_words))

    # checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words or have a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # simplifies response creating and adds into the dictionary
    def response(bot_responce, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_responce] = message_probability(message, list_of_words, single_response, required_words)

    # response -------------------------------------------------------
    response('Hello', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you', ['how', 'are', 'you'], required_words=['how'])
    response('Thank You!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # longer responces
    response(long.eating, ['what', 'do', 'you', 'eat'], required_words=['what','you', 'eat'])
    response('You\'re welcome!', ['thank', 'thanks', 'thank you'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get) # type: ignore
    # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_massage = re.split(r'\s +|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_massage)
    return response

while True :
    print('Bot :', get_response(input('You : ')))