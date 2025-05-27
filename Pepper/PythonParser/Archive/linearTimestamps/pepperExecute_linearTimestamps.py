import time
# from pepper_robot.robot import *
# import pepper_robot.config
import qi
import sys
import csv
import execnet
import os

sys.path.insert(1, os.path.realpath(os.path.pardir))
from gesturesConfig import *

# PEPPER_IP = '192.168.50.155'
# PEPPER_PORT = 9559
PEPPER_IP = 'localhost'
PEPPER_PORT = 37689     #45285

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
    behavior_service.runBehavior(get_behavior_name('init'), _async=False)  # _async is False = wait for finish

    print "in main"  #TEMP
    with open("../outputs/commandFile.csv", 'r') as file:
        file_reader = csv.reader(file)
        line_number = 0     # line number incrementer for file name
        current_time = 0.0
        print "before file reader" #TEMP
        behavior_service.runBehavior(get_behavior_name('init'),
                                     _async=False)  # _async is False = wait for finish
        for row in file_reader:   # for each script line
            if line_number == 0: #skips the header row of csv
                print "hitting line_num=0" #TEMP
                line_number += 1
                continue
            print "hitting line_num in loop" #TEMP
            print "current_time: %f" % current_time #TEMP
            print "float(row[0]): %f" % float(row[0]) #TEMP
            file_name = '../outputs/line' + str(line_number) + '.wav'
            time.sleep(float(row[0]) - current_time)   #delays until the next command
            if row[1].find('.wav') != -1: #if current row is a voice file
                call_python_version("3.9", "playFile", "playFile",
                                    ['../outputs/' + row[1], False])      # play the sound before gestures, (True means wait)
            else:   #if current row is a gesture
                behavior_service.runBehavior(get_behavior_name('init'),
                                             _async=False)  # _async is False = wait for finish
                behavior_service.runBehavior(get_behavior_name(row[1]), _async=False)  # _async is False = wait for finish
            line_number += 1    # line number increment for file name
            current_time += float(row[0])
    behavior_service.runBehavior(get_behavior_name('init'), _async=False)  #    _async is False = wait for finish


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