from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        #test for joy
        #arrange
        test_text = "I am glad this happened"
        #act
        result = emotion_detector(test_text)
        #assert
        self.assertEqual(result['dominant_emotion'], 'joy')
        
        #test for anger
        #arrange
        test_text = "I am really mad about this"
        #act
        result = emotion_detector(test_text)
        #assert
        self.assertEqual(result['dominant_emotion'], 'anger')
        
        #test for disgust
        #arrange
        test_text = "I feel disgusted just hearing about this"
        #act
        result = emotion_detector(test_text)
        #assert
        self.assertEqual(result['dominant_emotion'], 'disgust')
                
        #test for sadness
        #arrange
        test_text = "I am so sad about this"
        #act
        result = emotion_detector(test_text)
        #assert
        self.assertEqual(result['dominant_emotion'], 'sadness')
                
        #test for fear
        #arrange
        test_text = "I am really afraid that this will happen"
        #act
        result = emotion_detector(test_text)
        #assert
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()