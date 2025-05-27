from __future__ import print_function
import sys
import fileinput
import decimal
import fileinput
import csv
import os
import inspect
from mutagen.wave import WAVE
import time
from contextlib import closing
import execnet

# This makes "import ..." commands search in the upper directory
sys.path.insert(1, os.path.realpath(os.path.pardir))

from gesturesConfig import *
# to find INPUT_FILE
from config import *


def speech_file(mytext="Hello World", output_file="output", voice= "tts_models/en/jenny/jenny", chosen_language = None, chosen_speaker = None):
    import torch
    from TTS.api import TTS
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # List available 🐸TTS models
    print(TTS().list_models())
    # Init TTS with the target model name
    tts = TTS(model_name = voice, progress_bar=False).to(device)
    # Run TTS
    tts.tts_to_file(text=mytext, file_path=output_file, language=chosen_language, speaker_wav=chosen_speaker, split_sentences=False)


# CLASS that holds the characteristics of a script line
class ScriptLine:
    def __init__(self, current_timestamp, line="1) Hello #wave World", line_num=1, ):
        # Sets almost all class variables
        self.line_no = line_num
        self.current_timestamp = current_timestamp
        self.line = line
        self.text = self.extract_text()
        self.voice = self.extract_voice()
        self.gesture_arr = self.extract_gesture()
        self.gesture_pos_arr = self.extract_gesture_pos()

        # Outputs sound file if NOT '0' (if is robot)
        if self.voice != '0':
            self.output_file = '../outputs/' + 'line' + str(line_num) + '.wav'
            # if no voice for this line
            if self.text:
                speech_file(self.text, self.output_file, get_voice_name(int(self.voice)), get_voice_language(int(self.voice)), SPEAKER_WAV)
                # Get audio length
                audio = WAVE(self.output_file)
                self.voice_time = round(audio.info.length, 3)
            else:
                # Creates an empty file
                with open(self.output_file, 'w') as fp:
                    pass
                self.voice_time = 0.0

            # Sets gesture_time class variable
            self.gesture_time = 0.0
            for i in range(len(self.gesture_arr)):
                # Error handling for non-gesture
                if get_gesture_length(self.gesture_arr[i]) == 0.0:
                    print("\033[91mUnknown gesture \"" + self.gesture_arr[i] + "\" in Line " + str(self.line_no) + "\033[0m")
                    exit(1)
                self.gesture_time = round(float(get_gesture_length(self.gesture_arr[i])) + self.gesture_time, 3)

            # Fills human text output
            # put file with spacers
            with open('../outputs/' + 'lines(human).txt', "a") as myfile:
                myfile.write('\trobot: ' + self.line)
        # If '0' (if human)
        else:
            self.output_file = '../outputs/' + 'lines(human).txt'
            with open(self.output_file, "a") as myfile:
                myfile.write('line' + str(self.line_no) + ': ' + self.line)
            # based on 130 WPM speech
            self.voice_time = round(float(self.text.count(' ')) * 60.00 / 130.00, 3)
            # gesture length assumed to exactly fit in the length of speech
            self.gesture_time = self.voice_time
        # Initializes the total running time of this line
        self.total_time = 0.0
        # Heavy lifting of the parsing
        self.help_csv()

    # Formats the printing output of this class
    def __str__(self):
        string = ('\033[94mPlaytime / Gesturetime: {} / {} \033[0m| \033[91mVoice: {} \033[0m|'
                  ' \033[92mText: "{}" \033[0m| \033[93mGestures: '
                  .format(self.voice_time, self.gesture_time, self.voice, self.text))
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
        # Get rid of the "person" syntax
        liner = self.line
        liner = liner.partition(')')[2]
        gesture_count = liner.count('#')
        # Initialize empty line to build
        text = ""
        for i in range(gesture_count + 1):
            # Adds the text to the left of the leftmost gesture
            text += liner.partition('#')[0]
            # Updates the running line to remove up to the leftmost gesture
            liner = liner.partition('#')[2]
            # Updates the running line to remove the leftmost gesture
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
            # Error handling for non_valid chars
            if not gestures[i].isalnum() and gestures[i].count("_") == 0:
                print("\033[91mSYNTAX ERROR: Gesture \"" + gestures[i] + "\" in Line " + str(self.line_no) + " contains a non-valid character\033[0m")
                exit(1)
        return gestures

    # RETURNS an array gesture position from the line
    def extract_gesture_pos(self):
        pos_arr = [-1] * len(self.gesture_arr)
        for i in range(len(self.gesture_arr)):
            # remove 3 positions for the voice spacer and 1 for the '#' sign
            pos_arr[i] = self.line.find(self.gesture_arr[i]) - 4 - i
        return pos_arr

    # OUTPUTS one csv file in the /output folder with the timestamps for the voices and gestures
    def help_csv(self):
        with open("../outputs/commandFile.csv", 'a+') as file:
            file_writer = csv.writer(file)

            # adds the voice at current time stamp
            file_writer.writerow([self.current_timestamp, self.output_file.partition('/')[2].partition('/')[2]])    #removes 'outputs/' and adds voice timeline

            # adds the gesture positions in at correct times
            total_delay = 0.0
            last_pos_ratio = 0.0
            last_gesture_timestamp = 0.0
            last_gesture_delay = 0.0
            last_gesture_length = 0.0
            last_delay_from_timestamp = 0.0
            for i in range(len(self.gesture_arr)):
                # gets the fractional position
                position_ratio = float(self.gesture_pos_arr[i]) / len(self.line)
                # finds the time delay from the references timestamp of the line
                delay_from_timestamp = round((position_ratio - last_pos_ratio) * self.voice_time, 3)
                # sets the relative time at which to play the gesture
                timestamp = round(self.current_timestamp + delay_from_timestamp, 3)
                # sets the time the gesture takes to execute
                gesture_length = round(get_gesture_length(self.gesture_arr[i]), 3)
                # compares to see if relative sentence position is too close to previous gesture (overlapping)
                if timestamp < last_gesture_timestamp + last_gesture_length:
                    # then play at the timestamp directly after previous gesture finishes
                    timestamp = round(last_gesture_timestamp + last_gesture_length, 3)
                # write this time and this gesture to the ,csv
                file_writer.writerow([timestamp, self.gesture_arr[i]])
                delay_between_gestures = last_gesture_delay + last_delay_from_timestamp
                # prevent negative delay to contributing to total delay
                if delay_between_gestures > 0:
                    total_delay = round(delay_between_gestures + total_delay, 3)
                # print("\033[95m-------Gesture---\"" + self.gesture_arr[i] + "\"------------------------")   # TEMP
                # print("gesture length:" + str(gesture_length))                                  # TEMP
                # print("gesture delay:" + str(delay_between_gestures))                           # TEMP
                # print("timestamp:" + str(timestamp))                                            # TEMP
                # print("---")                                                                    # TEMP
                # print("last length:" + str(last_gesture_length))                                # TEMP
                # print("last delay:" + str(last_gesture_delay))                                  # TEMP
                # print("last timestamp:" + str(last_gesture_timestamp))                          # TEMP
                # print("---")                                                                    # TEMP
                # print("total delay:" + str(total_delay))                                        # TEMP
                # print("total gesture time:" + str(self.gesture_time))                           # TEMP
                # print("-----------------------------------------------")                        # TEMP
                # saves last gesture values
                last_pos_ratio = position_ratio
                last_gesture_timestamp = timestamp
                last_gesture_delay = delay_between_gestures
                last_gesture_length = gesture_length
                last_delay_from_timestamp = delay_from_timestamp
            # adds to the ongoing current timestamp for the next line
            if self.gesture_time + total_delay > self.voice_time:
                # adds gesture time and delays to total line time if gesture time is longer than voice
                self.total_time = round(self.gesture_time + total_delay, 3)
            else:
                # adds voice time to total line time if voice time is longer than gesture and delays
                self.total_time = round(self.voice_time + self.total_time, 3)
            # updates current_timestamp for the sake of the next line's reference
            self.current_timestamp = round(self.total_time, 3)

# CLEARS out the output files from previous run
def clear_csv():
    # clears commandFile.csv
    with open("../outputs/commandFile.csv", "w") as t:
        t.truncate()
    # clears lines(human).txt
    with open("../outputs/lines(human).txt", "w") as t:
        t.truncate()
    # clears line[1, 2, ...].wav
    os.system("rm ../outputs/line*")
    # adds header
    with open("../outputs/commandFile.csv", 'a+') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(['timestamp', 'action'])


def main():
    # setsup output files
    clear_csv()
    # receive text input from script file
    input_script = fileinput.input(files=INPUT_FILE)
    # running time
    ongoing_length = 0.0
    for line in input_script:
        # Extract line to class
        line_number = fileinput.lineno()

        # creates a script line class
        line_class = ScriptLine(ongoing_length, line, line_number)

        # adds the line length to the onging total length
        ongoing_length = round(line_class.total_time + ongoing_length, 3)
        # print("\033[95mongoing_length:" + str(ongoing_length) + "\033[0m")                      #TEMP
        print(line_class)

        # Adds "init" gesture at the end of the line
        with open("../outputs/commandFile.csv", 'a+') as file:
            file_writer = csv.writer(file)
            file_writer.writerow([ongoing_length, "init"])
        # adds the time for the robot to "init" behavior at the end of a line
        ongoing_length = round(ongoing_length + get_gesture_length("init"), 3)

    fileinput.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


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
