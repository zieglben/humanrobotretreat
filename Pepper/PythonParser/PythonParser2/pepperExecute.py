import time
# from pepper_robot.robot import *
# import pepper_robot.config
import qi
import sys
import csv
import execnet
import os
# import playsound

# This makes "import ..." commands search in the upper directory
sys.path.insert(1, os.path.realpath(os.path.pardir))

# calls a python module and function with a specific version
def call_python_version(Version, Module, Function, ArgumentList):
    gw = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()

from gesturesConfig import *
# from playFile import *

# to find PEPPER_IP & PEPPER_PORT
from config import *

# unused useful reference from http://doc.aldebaran.com/2-5/index_dev_guide.html
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


# unused useful reference from http://doc.aldebaran.com/2-5/index_dev_guide.html
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


# unused useful reference from http://doc.aldebaran.com/2-5/index_dev_guide.html
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


# unused useful reference from http://doc.aldebaran.com/2-5/index_dev_guide.html
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
    # Start a session
    behavior_service = session.service("ALBehaviorManager")
    audio_player_service = session.service("ALAudioPlayer")

    # Start background audio
    if BACKGROUND_SOUND != None:
        call_python_version("3.9", "playFile", "play", [BACKGROUND_SOUND, False])

    time.sleep(1)

    # Sets runtime unix time reference
    init_time = time.time()
    # Open commandFile.csv to read commands line by line
    with open("../outputs/commandFile.csv", 'r') as file:
        file_reader = csv.reader(file)
        # line number incrementer for file name
        line_number = 0
        # to track current time to align actions with time
        current_time = 0.0
        # calls first "init" during the start of the routine
        behavior_service.runBehavior(get_behavior_name('init'),_async=False)
        # for each script line
        for row in file_reader:
            # skips the header row of csv
            if line_number == 0:
                line_number += 1
                continue
            # waits until the time from runtime start matches the timeline command time
            while current_time < float(row[0]):
                current_time = time.time() - init_time

            # if current row is a voice file, play sound
            if row[1].find('.wav') != -1:
                # behavior_service.runBehavior(get_behavior_name('init'), _async=False)
                # find target .wav file
                file_name = '../outputs/' + row[1]
                # plays the file in newer python version (for library reason)
                call_python_version("3.9", "playFile", "play", [file_name, False])
            # if current row is a gesture, play gesture
            else:
                behavior_service.runBehavior(get_behavior_name(row[1]), _async=False)  # _async is False = wait for finish
            # line number increment for .csv reading
            line_number += 1
            # calls the "init" behavior at the end of the line to reset between speakers or such
            behavior_service.runBehavior(get_behavior_name('init'), _async=False)  #    _async is False = wait for finish


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create pepper session connection with error handling
    session = qi.Session()
    try:
        session.connect("tcp://" + PEPPER_IP + ":" + str(PEPPER_PORT))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + PEPPER_IP +
               "\" on port " + str(PEPPER_PORT) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)