''' Executing this function initiates the application of emotion 
    detection to be executed over the Flask channel and deployed on
    localhost:5000
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emo_detector():
    ''' This code recieves the text from the HTML interface and
        runs emotion detection over it using emotion_detection()
        function.  The output returned shows the dominant emotion 
        and the scores for the individual emotion key value pairs
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    anger = "'anger': " + str(res['anger'])
    disgust = "'disgust': " + str(res['disgust'])
    fear = "'fear': " + str(res['fear'])
    joy = "'joy': " + str(res['joy'])
    sadness = "'sadness': " + str(res['sadness'])
    dominant_emotion = res['dominant_emotion']
    formatted_output = "For the given statement, the system response is" + \
        f"{anger}, {disgust}, {fear}, {joy}, and {sadness}. " + \
        "The dominant emotion is " + dominant_emotion + "."
    return formatted_output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000)
