import numpy as np
import time
from src.IMU import IMU
from src.Controller import Controller
from src.State import State
from MangDang.mini_pupper.HardwareInterface import HardwareInterface
from MangDang.mini_pupper.Config import Configuration
from pupper.Kinematics import four_legs_inverse_kinematics
from MangDang.mini_pupper.display import Display
from src.MovementScheme import MovementScheme
# from src.createYogaActionList import MovementLib
from src.Command import Command
from src.MovementGroup import MovementGroups

def main_downward_dog(hold = 0.5, accel = 4, interval = 1, num_times = 1):
    Move = MovementGroups()
    Move.stop()
    for _ in range(num_times):
        Move.downward_dog_first(hold,accel)
        time.sleep(interval)
        Move.downward_dog_second(hold,accel)

    Move.stop()
    
    MovementLib = Move.MovementLib
    movement_config(MovementLib)

def main_cat_cow(num_times = 1, interval = 3):
    Move = MovementGroups()
    Move.stop()
    
    for _ in range(num_times):
        Move.height_move(0.03)
        time.sleep(interval)
        Move.height_move(-0.03)
        time.sleep(interval)
    Move.stop()
    
    MovementLib = Move.MovementLib
    movement_config(MovementLib)
    
def main_backleg(side = ""):
    Move = MovementGroups()

    if (side == "left"):
        Move.backleg_lift("left", 0.03, 3, 1)
    elif (side == "right"):
        Move.backleg_lift("right", 0.03, 3, 1)

    Move.stop()
    MovementLib = Move.MovementLib
    movement_config(MovementLib)


def main_cobra(hold = 0.5, accel = 4, interval = 1, num_times = 1):
    Move = MovementGroups()
    
    for _ in range(num_times):
        Move.cobra_first(0.5,4)
        time.sleep(interval)
        Move.cobra_second(0.5, 4)
        time.sleep(interval)
        
    Move.stop()

    MovementLib = Move.MovementLib
    movement_config(MovementLib, False)

def main_frontleg(side = ""):
    Move = MovementGroups()
    
    if (side == "left"):
        Move.foreleg_lift("left", 0.03, 3, 1)
    elif (side == "right"):
        Move.foreleg_lift("right", 0.03, 3, 1)

    Move.stop()
    MovementLib = Move.MovementLib
    movement_config(MovementLib)

def main_leg_lifts(hold = 3, accel = 1, num_times = 1, interval = 3):
    Move = MovementGroups()
    
    for _ in range(num_times):
        Move.foreleg_lift("left", 0.03, hold, accel)
        Move.stop()
        time.sleep(interval)
        Move.foreleg_lift("right", 0.03, hold, accel)
        Move.stop()
        time.sleep(interval)
        Move.backleg_lift("left", 0.03, hold, accel)
        Move.stop()
        time.sleep(interval)
        Move.backleg_lift("right", 0.03, hold, accel)
        Move.stop()
        time.sleep(interval)
    
    MovementLib = Move.MovementLib
    movement_config(MovementLib)


def main_walk(direction="", num_times = 1):
    Move = MovementGroups()
    
    if (direction == "left"):
        Move.move_left()
    elif (direction == "right"):
        Move.move_right()
    elif (direction == "forward"):
        Move.move_forward()
    elif (direction == "backward"):
        Move.move_backward()
    elif (direction == "fonda"):  # Jane Fonda routine
        for _ in range(num_times):
            
            ##### Forward then backward #####
            for _ in range(1):
                Move.stay_in_place()
            # Move.move_forward()
            Move.gait_uni(0.15, 0, 1, 1)

            for _ in range(1):
                Move.stay_in_place()
            # Move.move_backward()
            Move.gait_uni(-0.05, 0, 1.5, 1)
            #################################

            ###### Left then right ######
            for _ in range(1):
                Move.stay_in_place()
            # Move.move_forward()
            Move.gait_uni(0, 0.1, 0.75, 1)

            for _ in range(1):
                Move.stay_in_place()
            # Move.move_backward()
            Move.gait_uni(0, -0.1, 1.75, 1)
            #############################
            
            ###### Backward then forward ######
            for _ in range(1):
                Move.stay_in_place()
            Move.gait_uni(-0.05, 0, 1.5, 1)

            for _ in range(1):
                Move.stay_in_place()
            Move.gait_uni(0.15, 0, 1, 1)
            ###################################
            
            ###### Right then left #######
            for _ in range(1):
                Move.stay_in_place()
            Move.gait_uni(0, -0.1, 1.75, 1)

            for _ in range(1):
                Move.stay_in_place()
            Move.gait_uni(0, 0.1, 0.75, 1)
            ##############################

            # Reset
            for _ in range(1):
                Move.stay_in_place()

    Move.stop()
    
    MovementLib = Move.MovementLib
    movement_config(MovementLib)

def main_jog(direction=""):
    Move = MovementGroups()
     
    if (direction == "forward"):
        ##### Forward then backward #####
        for _ in range(1):
            Move.stay_in_place()
        # Move.move_forward()
        Move.gait_uni(0.15, 0, 1, 1)

        for _ in range(1):
            Move.stay_in_place()
        # Move.move_backward()
        Move.gait_uni(-0.05, 0, 1, 1)
        #################################
    elif (direction == "left"):
        ###### Left then right ######
        for _ in range(1):
            Move.stay_in_place()
        # Move.move_forward()
        Move.gait_uni(0, 0.1, 1, 1)

        for _ in range(1):
            Move.stay_in_place()
        # Move.move_backward()
        Move.gait_uni(0, -0.1, 1, 1)
        ##############################
    elif (direction == "right"):
        ###### Right then left #######
        for _ in range(1):
            Move.stay_in_place()
        Move.gait_uni(0, -0.1, 1, 1)

        for _ in range(1):
            Move.stay_in_place()
        Move.gait_uni(0, 0.1, 1, 1)
        ##############################
        
    elif (direction == "back"):
        ###### Backward then forward ######
        for _ in range(1):
            Move.stay_in_place()
        Move.gait_uni(-0.05, 0, 1, 1)

        for _ in range(1):
            Move.stay_in_place()
        Move.gait_uni(0.15, 0, 1, 1)
        ###################################
    
    MovementLib = Move.MovementLib
    movement_config(MovementLib)

def main_twist(degree = 0, hold = 0, accel = 0, num_times = 1):
    Move = MovementGroups()
    
    for i in range(0, num_times):
        Move.body_row(degree, hold, accel)
        Move.body_row(-degree, hold, accel)
        Move.body_row(degree, hold, accel)
        Move.body_row(-degree, hold, accel)
        
    Move.stop()
    
    MovementLib = Move.MovementLib
    movement_config(MovementLib)
    
def main_head_move(pitch_deg = 0, yaw_deg = 0, hold = 0, accel = 0, num_times = 1):
    Move = MovementGroups()
    
    for i in range(0, num_times):
        Move.head_move(pitch_deg, 0, hold, accel)
        Move.head_move(-pitch_deg+5, 0, hold, accel)
        Move.head_move(0, yaw_deg, hold, accel)
        Move.head_move(0, -yaw_deg, hold, accel)

    Move.stop()
    
    MovementLib = Move.MovementLib
    movement_config(MovementLib)
    
def main_head_circle(speed = 15, num_times = 1):
    Move = MovementGroups()
    
    for i in range(0, num_times):
        Move.head_ellipse(speed)
        
    Move.stop()
    
    MovementLib = Move.MovementLib
    movement_config(MovementLib)
    
def main_body_circle():
    Move = MovementGroups()
    Move.body_cycle()
    MovementLib = Move.MovementLib
    movement_config(MovementLib)

def main_stop():
    Move = MovementGroups()
    Move.stop()
    MovementLib = Move.MovementLib
    movement_config(MovementLib)
    

def movement_config(MovementLib, use_imu=False):
    # Create config
    config = Configuration()
    hardware_interface = HardwareInterface()
    disp = Display()

    disp.show_image("/home/ubuntu/apps-md-robots/cartoons/Trot.jpg")
     
            

    # Create imu handle
    if use_imu:
        imu = IMU(port="/dev/ttyACM0")
        imu.flush_buffer()

    # Create controller and user input handles
    controller = Controller(
        config,
        four_legs_inverse_kinematics,
    )
    state = State()

    #Create movement group scheme instance and set a default True state
    movementCtl = MovementScheme(MovementLib)
    dance_active_state = True
    lib_length = len(MovementLib)
    # print(f"lib_length: {lib_length}")

    last_loop = time.time()

    command = Command()
    command.pseudo_dance_event = True

    while True:
        now = time.time()
        if now - last_loop < config.dt:
            continue
        last_loop = time.time()

        # Read imu data. Orientation will be None if no data was available
        quat_orientation = (
            imu.read_orientation() if use_imu else np.array([1, 0, 0, 0])
        )
        state.quat_orientation = quat_orientation

        # Step the controller forward by dt
        if dance_active_state == True:
            # Caculate legsLocation, attitudes and speed using custom movement script
            movementCtl.runMovementScheme()
            command.legslocation        = movementCtl.getMovemenLegsLocation()
            command.horizontal_velocity = movementCtl.getMovemenSpeed()
            command.roll                = movementCtl.attitude_now[0]
            command.pitch               = movementCtl.attitude_now[1]
            command.yaw                 = movementCtl.attitude_now[2]
            command.yaw_rate            = movementCtl.getMovemenTurn()
            controller.run(state, command, disp)
        else:
            controller.run(state, command, disp)
        if movementCtl.movement_now_number >= lib_length - 1 and movementCtl.tick >= movementCtl.now_ticks:
            print("exit the process")
            break


        # Update the pwm widths going to the servos
        hardware_interface.set_actuator_postions(state.joint_angles)


def jane_fonda():
    while(1):
        main_walk("fonda", 8) # ~6.4 min routine, loop until we are done

jane_fonda()