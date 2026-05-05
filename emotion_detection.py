import requests
import json

def emotion_detector(text_to_analyze):
    # URL to the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # create dictionary of text to be anaylyzed
    myobj = {"raw_document": {"text": text_to_analyze}}
    # set the headers needed for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # send the POST request to the API with the header and text & return response.
    response = requests.post(url, json = myobj, headers = header)
    # handle the response
    # convert to json and extract the emotion dictionary
    response_data = json.loads(response.text)
    emotion_dict = response_data["emotionPredictions"][0]["emotion"]
    # find the dominant emotion
    highest_score = 0.0
    highest_emotion = ""
    for emotion in emotion_dict:
        if emotion_dict[emotion] > highest_score:
            highest_emotion = emotion
            highest_score = emotion_dict[emotion]
    # build the response
    res = {
        'anger': emotion_dict['anger'],
        'disgust': emotion_dict['disgust'],
        'fear': emotion_dict['fear'],
        'joy': emotion_dict['joy'],
        'sadness': emotion_dict['sadness'],
        'dominant_emotion': highest_emotion,
    }
    return res