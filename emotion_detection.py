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
    return response.text