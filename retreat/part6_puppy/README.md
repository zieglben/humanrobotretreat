<!-- README for Mini-Pupper portion of retreat -->
<!-- NOT FINAL, NEEDS TO BE UPDATED -->

# Puppy Mindfulness with Mini Pupper

## Code/File Structure

Our implementation of the Mini-Pupper code builds off of the open-source repository from MangDang robotics club, the manufacturers of the robot. Relying heavily on their implementation of the [**Stanford Pupper**](https://github.com/mangdangroboticsclub/StanfordQuadruped), and building upon the CHARISMA lab's implementation, we added more movements to the [movement library](./MovementGroup.py) and created modular, application-level programs for each of the Mini-Pupper-led activities. 

> **Important:**   
> In this repository, we have only included files with changes implemented by our team for this project. The actual repository loaded onto the robot is private, as it is used internally by the CHARISMA Lab at Oregon State University. 

## Design

The Mini-Pupper portion of the retreat is broken down into three sections that are detailed below. The chart below illustrates the modular design of each section, focusing on repeatability and time for instruction before and between each exercise. Each section follows a similar flow, with minor changes depending on the implementation requirements. With the goal of leading a group of people, this flow maximizes participant engagement and understanding to deliver a meaningful routine. This portion of the retreat was intended to transition the audience out of the silent, breath-focused mindfulness back into the faster-paced world and get blood pumping after being seated for an extended period of time. 

![image](https://github.com/user-attachments/assets/c7d09e39-4c90-4e40-9ffa-bf7f3015f854)

_Each application is broken into repeatable sub-sections, with time for rest in between each exercise and each iteration_

### Warmup 

Outlined in [```run_warmup.py```](./run_warmup.py), the Pupper uses its body to simulate human head movement to guide the audience to stretch their neck in sync with the robot. While the robot does not have a movable head like humans do, this movement pattern is easily recognizable for participants, as it changes the direction the robot is looking, which is easily translatable to the human body. The routine starts with simple up, down, left, right head movements, follows up with head circles, and ends with body tilts. The body tilts roughly translate to leaning from the torso for a human. 

[![image](https://github.com/user-attachments/assets/1830ae3d-86af-4cef-befc-3e728b72c2d8)](https://drive.google.com/file/d/1VzFStg97seyi-XyV0rHtgXfohvdv4fbD/view?usp=sharing)

### Yoga 

In this section outlined in [```run_yoga.py```](./run_yoga.py), the Pupper gets more involved, guiding the audience through a simple yoga routine starting with cat/cow, then moving into leg/arm lifts. We experimented with a dead-bug-style leg movement with the robot laying on its back, but it proved to be more confusing than intended during our second deployment. This is included in the file, however. 

[![image](https://github.com/user-attachments/assets/3dd6404b-0f9c-4d7f-a415-58f0817f9430)](https://drive.google.com/file/d/1owneABwLLBjfkyJkTjHvSGnI9rx2hryC/view?usp=sharing)

### Exercise Routine

In this section as shown in [```run_exercise.py```](./run_exercise.py), the Pupper loops through a simple cartesian plane movement scheme, focusing on keeping the leg movement constant. Modeled after a video exercise class, think Jane Fonda, our goal was to get blood pumping and break up the tense, silent atmosphere that was created by the meditation routines. We looped through this routine twice, for about 6 minutes, with Blinding Lights - Instrumental playing as background music. This simple forward, backward, left, right in-place jogging routine was effective to re-acclimate the audience and doubled as entertaining, comedic relief. 

The human facilitator experimented with variations to jogging in place, including high knees and buttkickers, which kept participants engaged in the activity. The facilitator also guided participants to find a spot on the floor to anchor to and perform the directional changes in reference to that point. Using this exocentric instruction assisted in keeping the group aligned, minimized space concerns between participants, and made it easier to align the Mini-Pupper. During this section, the robot had difficulties with alignment and would often drift in one direction or another, requiring frequent adjustments by the facilitator. This drifting problem did not happen when testing prior to deployment, but changes in the floor material likely exacerbated this issue.

[![image](https://github.com/user-attachments/assets/86dadf86-941c-4fd2-bb8d-5b185d9bac6a)](https://drive.google.com/file/d/12dz-YiktTt3nsVUQ5ciGeKS042_1v0Dy/view?usp=sharing)

## Set Up Instructions

> **Important:**   
> Since the implementation of the Mini-Pupper 2 that we used was stored locally on the CHARISMA Lab's robot, please refer to the [Stanford Quadruped implementation on the MangDang Robotics Club Github](https://github.com/mangdangroboticsclub/StanfordQuadruped) for instructions on how to setup the robot.

Once you have set up the robot according to the [Stanford Quadruped setup instructions](https://github.com/mangdangroboticsclub/StanfordQuadruped/?tab=readme-ov-file#mini-pupper), replace the default ```MovementGroup.py``` file in the ```src/``` folder with [our implementation](./MovementGroup.py), and put [```run_warmup.py```](./run_warmup.py), [```run_yoga.py```](./run_yoga.py), and [```run_exercise.py```](./run_exercise.py) in the top-level folder.

To run the program, connect to your robot through ```ssh```, open the terminal, and run ```python3 ./run_(program_here).py```.
