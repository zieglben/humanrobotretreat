# Human-Robot Meditation Retreat: Development, Deployment, and Assessment
### Exploring the effectiveness of delivering mindfulness exercises through robots.
![Pepper and Pupper (1)](https://github.com/user-attachments/assets/49448785-82ee-4e6e-9d2b-cd35934d44fe)


_Mini-Pupper 2 (left) and Pepper (right) robots were the main systems used for this project as pictured above._

This repository and its contents were developed as part of a Senior Capstone project at Oregon State University from September 2024 - June 2025, in collaboration with the CHARISMA Lab on campus. The project followed up on a 6-month robot-led meditation series from January – June 2024 by the CHARISMA Lab at OSU.

This repository is broken down into three main sections: [```retreat/```](./retreat/) contains documentation, setup, and code for each section of the retreat, [```moreInfo/```](./moreInfo/) has configuration and other important information, and [```futureWork/```](./futureWork/) contains our findings and work-in-progress ideation for future work on this project.


<!--Update as structure is changed-->
```
humanrobotretreat/
├── retreat/
│ ├── part1_welcome/
│ │ ... # folder for each section
│ ├── part8_end/ 
├── moreInfo/
│ ├── setup/ # getting started guides and helpful resources
├── futureWork/
```

# Why Robots?

Meditation and mindfulness practices have gained popularity in recent years, especially after the COVID-19 pandemic, which increased isolation and stress. While many automated meditation resources, such as apps or scripted videos, offer accessible guidance, they lack the dynamic and embodied interaction that is offered by in-person guided meditation. This project explored how leveraging the physical presence of robots can enhance meditation experiences beyond static, pre-recorded scripts.

## Target Audience
- Mindfulness practitioners
  - Stressed students
  - Busy Faculty
  - Visistors seeking relaxation
  - People seeking for new meditation methods/media
- Wellness retreat organizers
    - CHARISMA Lab
    - Capstone team
    - (See in Acknowledgements) 
- Human-robot interaction researchers
- Robot Enthusiasts
- Yoga Enjoyers

## Core Features
- Robot-led guided meditation with gestures, voice, and music
- Two robots with different body shapes displaying emotional and visual feedback to participants
  - Humanoid (Pepper)
  - Quadroped (Mini-Pupper)
- Real time, in-person voice and gesture additional guidance from the human facilitators
- Customizable meditation exercises using scripts and modular code

## Benefits

- Embodied presence: Physical presence of the robots and faculty increase the realism of the meditation compared to video/audio  
- Consistent delivery: Both robots were run with scripts that were revised and tested over multiple iterations of the retreat
- Increased accessibility: Robots can be more accessible for anyone who purchased or participated the retreat
- Higher engagement: Curiosity leads people to experience new way of meditation and explore the inner-workings of robotics at the same time
- Customizable interactions: The scripts we developed can be changed based on the needs of the sessions or groups
- Scalable deployment: Once refined, the robots can lead the exercises by themselves with little human-in-the-loop intervention


<!--This needs to be updated to just be important milestones, maybe a Gantt chart? -->
## Project Timeline & Milestones

```mermaid
    gantt
    dateFormat  YYYY-MM-DD
    title Project Timeline
    excludes 2024-12-13, 2024-12-14, 2024-12-15, 2024-12-16, 2024-12-17, 2024-12-18, 2024-12-19, 2024-12-20, 2024-12-21, 2024-12-22, 2024-12-23, 2024-12-24, 2024-12-25, 2024-12-26, 2024-12-27, 2024-12-28, 2024-12-29, 2024-12-30, 2024-12-31, 2025-01-01, 2025-01-02, 2025-01-03, 2025-01-04, 2025-01-05, 2025-01-06, 2025-03-22, 2025-03-23, 2025-03-24, 2025-03-25, 2025-03-26, 2025-03-27, 2025-03-28, 2025-03-29, 2025-03-30

    section Fall 2024
    Ideation Phase           :ideate, 2024-10-4, 2024-11-10
    Design Phase             :design, 2024-10-20, 2024-11-17
    Dev Iteration 1          :dev1, 2024-11-8, 2024-12-13

    section Winter 2025
    Winter Break             :done, break, 2024-12-13, 2025-01-06
    Dev Iteration 1          :dev12, 2025-01-06, 2025-02-02
    Feb 2 Winter Retreat 1   :crit, milestone, retreat1, 2025-02-02, 0d
    Dev Iteration 2          :dev2, after retreat1, until retreat2
    Feb 22 Winter Retreat 2         :crit, milestone, retreat2, 2025-02-22, 0d
    Documentation            :docs0, after retreat2, 2025-03-22

    section Spring 2025
    Spring Break             :done, break2, 2025-03-22, 2025-03-31
    Documentation/Expo Prep  :docs, 2025-03-31, 2025-06-05
    June 6 Engineering Expo    :milestone, expo, 2025-06-06, 0d
```

# Acknowledgements

**Team Members:**
- Ben Ziegler – zieglben@oregonstate.edu
- KweonHo Park – parkkweo@oregonstate.edu
- Eliane Wang – wangel@oregonstate.edu
- Yen-Ting Chou – chouye@oregonstate.edu
- Jacob Strand – strandja@oregonstate.edu

**Project Partner:**
- Dr. Heather Knight - heather.knight@oregonstate.edu,
CHARISMA Robotics Lab

![retreat team](https://github.com/user-attachments/assets/77d1fb80-701d-434a-aa41-ea6c2ea10378)
