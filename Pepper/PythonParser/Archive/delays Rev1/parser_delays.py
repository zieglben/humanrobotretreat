from __future__ import print_function
import fileinput
import csv
from mutagen.wave import WAVE
from Archive.speechFiler import speech_file
from gesturesConfig import *
import execnet

# import urllib3.contrib.pyopenssl
# import certifi
# import urllib3
# http = urllib3.PoolManager(
#     cert_reqs='CERT_REQUIRED',
#     ca_certs=certifi.where()
# )
# urllib3.contrib.pyopenssl.inject_into_urllib3()


INPUT_FILE = '../inputs/InputScript2.txt'


# RETURNS called function in module of python version
def call_python_version(Version, Module, Function, ArgumentList):
    gw = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()

# CLASS that holds the characteristics of a script line
class ScriptLine:
    def __init__(self, line="1) Hello #wave World", line_num=1):
        # Sets almost all class variables
        self.line = line
        self.text = self.extract_text()
        self.voice = self.extract_voice()
        self.gesture_arr = self.extract_gesture()
        self.gesture_pos_arr = self.extract_gesture_pos()
        self.line_no = line_num

        # Outputs sound file
        self.output_file = 'outputs/' + 'line' + str(line_num) + '.wav'
        speech_file(self.text, self.output_file)
        audio = WAVE(self.output_file)
        self.audio_time = audio.info.length

        # Sets gesture_time class variable
        self.gesture_time = 0
        for i in range(len(self.gesture_arr)):
            self.gesture_time += get_gesture_length(self.gesture_arr[i])

        #selects the longest time
        self.gestures_are_longer = True if self.gesture_time > self.audio_time else False
        self.total_time = self.gesture_time if self.gestures_are_longer else self.audio_time
        self.help_csv()

    def __str__(self):
        string = ('\033[94mPlaytime / Gesturetime: {} / {} \033[0m| \033[91mVoice: {} \033[0m|'
                  ' \033[92mText: "{}" \033[0m| \033[93mGestures: '
                  .format(self.audio_time, self.gesture_time, self.voice, self.text))
        for i in range(len(self.gesture_arr)):
            if i < len(self.gesture_arr) - 1:
                string += self.gesture_arr[i]
                string += ', '
            else:
                string += self.gesture_arr[i]
        string += "\033[0m"
        return string

    # RETURNS the text element string from script line
    def extract_text(self):
        # get rid of the "person" syntax
        liner = self.line
        liner = liner.partition(')')[2]
        gesture_count = liner.count('#')
        # initialize empty line to build
        text = ""
        for i in range(gesture_count + 1):
            # adds the text to the left of the leftmost gesture
            text += liner.partition('#')[0]
            # updates the running line to remove up to the leftmost gesture
            liner = liner.partition('#')[2]
            # updates the running line to remove the leftmost gesture
            liner = liner.partition(' ')[2]
        text = text.rstrip('\n ')
        text = text.lstrip('\n ')
        return text

    # RETURNS an int of the voice
    def extract_voice(self):
        return self.line.partition(')')[0]

    # RETURNS an array of gestures in the form: "BLAH #gesture1 BLAH #gesture2 BLAH" -> arr = [gesture1, gesture 2]
    def extract_gesture(self):
        liner = self.line
        gesture_count = liner.count('#')
        gestures = [''] * gesture_count
        for i in range(gesture_count):
            # removes all to the left of the first '#'
            gestures[i] = liner.partition('#')[2]
            # copies the removal to the running line string
            liner = gestures[i]
            # removes all after the gesture
            gestures[i] = gestures[i].partition(' ')[0]
            gestures[i] = gestures[i].rstrip('\n ')
            gestures[i] = gestures[i].lstrip('\n ')
        return gestures

    # RETURNS an array gesture position from the line
    def extract_gesture_pos(self):
        pos_arr = [-1] * len(self.gesture_arr)
        for i in range(len(self.gesture_arr)):
            pos_arr[i] = self.line.find(self.gesture_arr[i]) - 4   # remove 3 positions
                                                                    # for the voice spacer
                                                                    # and 1 for the '#' sign
            # print (pos_arr[i])      # TEMP
        return pos_arr

    # OUTPUTS two csv files in the /output folder with the timings for the voices and gestures
    def help_csv(self):
        with open("../outputs/voices.csv", 'a+') as vf, open("../outputs/gestures.csv", 'a+') as gf:
            voice_writer = csv.writer(vf)
            gesture_writer = csv.writer(gf)
            if self.gestures_are_longer:
                #commits voice csv
                delay_v = str((self.gesture_time - self.audio_time) / 2)
                file_v = self.output_file.partition('/')[2]      # removes 'outputs/'
                string_v = [delay_v, file_v]
                voice_writer.writerow(string_v)
                #commits gesture csv
                # for i in range(len(self.gesture_arr)):
                gesture_writer.writerow(self.gesture_arr)
            elif not self.gestures_are_longer:
                #commits voice csv
                file_v = self.output_file.partition('/')[2]      # removes 'outputs/'
                string_v = [file_v]
                voice_writer.writerow(string_v)
                #commits gesture csv
                # MAYBE TODO remake the division of the gestures according to gesture length NOT gesture script position
                string_g = []
                last_pos_ratio = 0.0
                for i in range(len(self.gesture_arr)):
                    position_ratio = float(self.gesture_pos_arr[i]) / len(self.line)   # gets the fractional position
                    delay_g = str((position_ratio - last_pos_ratio) * self.audio_time)
                    string_g += [delay_g, self.gesture_arr[i]]
                    last_pos_ratio = position_ratio     # saves last position ratio
                gesture_writer.writerow(string_g)


# RETURNS 1 if the gestures take longer, 0 if voice takes longer
def is_gestures_longer(gestures, voice_len):
    gestures_len = 0.0
    for i in range(len(gestures)):
        gestures_len += get_gesture_length(gestures[i])
    if gestures_len > voice_len:
        return True
    else:
        return False


# CLEARS out the output files from previous run
def clear_csv():
    with open("../outputs/voices.csv", "w") as t:
        t.truncate()
    with open("../outputs/gestures.csv", "w") as y:
        y.truncate()


def main():
    clear_csv()
    # receive text input from script file
    input_script = fileinput.input(files=INPUT_FILE)
    # # open file
    # fp = open(INPUT_FILE, 'r')
    # lines = len(fp.readlines())
    # line_results = [lines]
    # fp.close()

    for line in input_script:
        # Extract line to class
        line_number = fileinput.lineno()


        testing_class = ScriptLine(line, line_number)
        print(testing_class)


        # #
        # gestures_take_longer = is_gestures_longer(gestures_arr, playtime)
        # csv_handling(gestures_arr, gestures_take_longer, playtime)


    fileinput.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # speech_file("yoooo hooooo bababooie", "outputs/bababooie.wav")
    # audio = WAVE("outputs/bababooie.wav")
    # playtime = audio.info.length
    # print("playtime: ", playtime)
    main()


# def check_speed(line_number, line):
#    # extracts the speed number (1-5) before the '#'
#    line_speed = line.partition('#')[0]
#    # checks if the speed number is valid, else error
#    if not line_speed.isdigit():
#        print(f"\033[1:91mIn Script line({line_number}): speed (prior to '#') is snot a positive integer\033[0m")
#        exit(1)
#    else:
#        line_speed = int(line_speed)
#    if line_speed < 1 or line_speed > 5:
#        print(f"\033[1:91mIn Script line({line_number}): speed out of range: {line_speed}\033[0m")
#        exit(1)
#    return line_speed


# Press Shiffor line in fileinput.input(encoding="utf-8"):
# t+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import torch
#from transformers import pipeline, DistilBertTokenizer, DistilBertForSequenceClassification, TextClassificationPipeline


#model_id = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"


#def analyze_sentiment(text):
#    sentiment_analyzer = pipeline("sentiment-analysis", model=model_id, top_k=None)
#    result = sentiment_analyzer(text)
#    return result[0]['label'], result[0]['score']

#def print_line_sentiments(line_number, sentiment_file_results):
#    # prints out these line-sentiments
#    for i in range(3):
#        current_sentiment_label = sentiment_file_results[line_number][0][i]['label'].upper()
#        # labels the color to the sentiment
#        if current_sentiment_label == 'POSITIVE':
#            print('\033[92m', )
#        elif current_sentiment_label == 'NEGATIVE':
#            print('\033[91m')
#        elif current_sentiment_label == 'NEUTRAL':
#            print('\033[93m')
#        print('\t',current_sentiment_label,)
#        print('\033[0m \t', round(sentiment_file_results[line_number][0][i]['score'] * 100, 2), '%')
#    return
