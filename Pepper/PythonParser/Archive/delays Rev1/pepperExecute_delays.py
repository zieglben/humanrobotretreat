import time
from pepper_robot.robot import *
import pepper_robot.config
import qi
import naoqi
import sys
import fileinput
import csv
import execnet
from gesturesConfig import *
from threading import Thread

PEPPER_IP = '192.168.50.155'
PEPPER_PORT = 9559
# PEPPER_IP = 'localhost'
# PEPPER_PORT = 38065

# RETURNS 1 if the gestures take longer, 0 if voice takes longer
def is_gestures_longer(gestures, voice_len):
    gestures_len = 0.0
    for i in range(len(gestures)):
        gestures_len += get_gesture_length(gestures[i])
    if gestures_len > voice_len:
        return True
    else:
        return False


def call_python_version(Version, Module, Function, ArgumentList):
    gw = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()


def run_behavior(ip, port, behavior_name):
    sesh = qi.Session()
    try:
        sesh.connect("tcp://" + ip + ":" + str(port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + ip + "\" on port " + str(port) + ".\nPlease check your script "
                                                                                    "arguments. Run with -h option "
                                                                                    "for help.")
        sys.exit(1)

    behavior_mng_service = sesh.service("ALBehaviorManager")
    getBehaviors(behavior_mng_service)
    launchAndStopBehavior(behavior_mng_service, behavior_name)
    defaultBehaviors(behavior_mng_service, behavior_name)


def getBehaviors(behavior_mng_service):
    """
    Know which behaviors are on the robot.
    """
    names = behavior_mng_service.getInstalledBehaviors()
    print ("Behaviors on the robot:")
    print (names)
    names = behavior_mng_service.getRunningBehaviors()
    print ("Running behaviors:")
    print (names)


def launchAndStopBehavior(behavior_mng_service, behavior_name):
    """
    Launch and stop a behavior, if possible.
    """
    # Check that the behavior exists.
    if behavior_mng_service.isBehaviorInstalled(behavior_name):
        # Check that it is not already running.
        if not behavior_mng_service.isBehaviorRunning(behavior_name):
            # Launch behavior. This is a blocking call, use _async=True if you do not
            # want to wait for the behavior to finish.
            behavior_mng_service.runBehavior(behavior_name, _async=True)
            time.sleep(0.5)
        else:
            print ("Behavior is already running.")
    else:
        print ("Behavior not found.")

    names = behavior_mng_service.getRunningBehaviors()
    print ("Running behaviors:")
    print (names)

    # Stop the behavior.
    if behavior_mng_service.isBehaviorRunning(behavior_name):
        behavior_mng_service.stopBehavior(behavior_name)
        time.sleep(1.0)
    else:
        print ("Behavior is already stopped.")
    names = behavior_mng_service.getRunningBehaviors()
    print ("Running behaviors:")
    print (names)


def defaultBehaviors(behavior_mng_service, behavior_name):
    """
    Set a behavior as default and remove it from default behavior.
    """
    # Get default behaviors.
    names = behavior_mng_service.getDefaultBehaviors()
    print ("Default behaviors:")
    print (names)
    # Add behavior to default.
    behavior_mng_service.addDefaultBehavior(behavior_name)
    names = behavior_mng_service.getDefaultBehaviors()
    print ("Default behaviors:")
    print (names)
    # Remove behavior from default.
    behavior_mng_service.removeDefaultBehavior(behavior_name)
    names = behavior_mng_service.getDefaultBehaviors()
    print ("Default behaviors:")
    print (names)


def main(session):
    # setup CIIRC Pepper API qi wrapper
    # pepper = Pepper(PEPPER_IP, PEPPER_PORT)

    behavior_service = session.service("ALBehaviorManager")
    audio_player_service = session.service("ALAudioPlayer")

    with open("../outputs/voices.csv", 'r') as vf, open("../outputs/gestures.csv", 'r') as gf:
        voice_reader = csv.reader(vf)
        gesture_reader = csv.reader(gf)
        line_number = 1     # line number incrementer for file name
        for row_v, row_g in ((a, b) for a in voice_reader for b in gesture_reader):   # for each script line
            file_name = 'outputs/line' + str(line_number) + '.wav'
            if len(row_v) == 1:     # if voice is longer than gesture
                call_python_version("3.9", "playFile", "playFile", [file_name,False])      # play the sound before gestures
                for i in range(len(row_g)):     # determine gestures
                    if row_g[i].replace('.','').isdigit():    # if gesture column is a delay
                        # print "i: ", i, " gesture column is delay"         # temp
                        time.sleep(float(row_g[i]))
                    else:    # if gesture column is a behavior
                        behavior_service.runBehavior(get_behavior_name(row_g[i]), _async=False)  # _async is False = wait for finish
            else:    # if gesture is longer than voice
                behavior_service.runBehavior(get_behavior_name(row_g[0]), _async=True)  # play the first gesture
                if float(row_v[0]) > float(get_gesture_length(row_g[0])):     # if the first gesture is shorter than voice delay
                    delay = float(row_v[0]) - get_gesture_length(row_g[0])
                    time.sleep(delay)     # sleeps the difference in delay
                # behavior_service.stopBehavior(get_behavior_name(row_g[0]))
                print "before voice delay check"        #temp
                if row_v[i].replace('.','').isdigit():    # if voice column is a delay
                    print "inside voice delay check"        # temp
                    time.sleep(float(row_v[i]))     # sleeps the voice delay
                call_python_version("3.9", "playFile", "playFile", [file_name,False])     # play the sound now and run the next gestures
                if len(row_g) > 1:   # the next gestures
                    for i in range(len(row_g)):
                        if row_g[i].replace('.', '').isdigit():    # if is delay
                            time.sleep(float(row_g[i]))
                        else:  # if is behavior
                            behavior_service.runBehavior(get_behavior_name(row_g[i]), _async=False)
                            # behavior_service.stopBehavior(get_behavior_name(row_g[i]))
            line_number += 1    # line number increment for file name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    session = qi.Session()
    try:
        session.connect("tcp://" + PEPPER_IP + ":" + str(PEPPER_PORT))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + PEPPER_IP + "\" on port " + str(PEPPER_PORT) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)