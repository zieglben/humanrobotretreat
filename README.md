# Human-Robot Meditation Retreat: Development, Deployment, and Assessment
### Exploring the effectiveness of delivering mindfulness exercises through robots.
![Pepper and Pupper (1)](https://github.com/user-attachments/assets/49448785-82ee-4e6e-9d2b-cd35934d44fe)


_Mini-Pupper 2 (left) and Pepper (right) robots were the main systems used for this project as pictured above._

This repository and its contents were developed as part of a Senior Capstone project at Oregon State University from September 2024 - June 2025, in collaboration with the CHARISMA Lab on campus. The project followed up on a 6-month robot-led meditation series from January – June 2024 by the CHARISMA Lab at OSU.

# Why Robots?

Meditation and mindfulness practices have gained popularity in recent years, especially after the COVID-19 pandemic, which increased isolation and stress. While many automated meditation resources, such as apps or scripted videos, offer accessible guidance, they lack the dynamic and embodied interaction that is offered by in-person guided meditation. This project explored how leveraging the physical presence of robots can enhance meditation experiences beyond static, pre-recorded scripts.

## Target Audience
- Mindfulness practitioners
  - Stressful students
  - Busy Faculty
  - Visistors seeking relaxation
  - People seeking for new meditation methods/media
- Wellness retreat organizers
    - CHARISMA Lab
    - Capstone team
    - (See in Acknowledgements) 
- Human-robot interaction researchers
- Robots Lover
- Yoga Enjoyers

## Core Features
- Robot-led guided meditation with gestures and voice or music
- Two robotic body with different emotional/visual feedback to participants
  - Humanoid (Pepper)
  - Quadroped (Mini-Pupper)
- Real time, in-person voice and gesture additional guidance with retreat organizer
- Customizable meditation exercise using scripts

## Benefits

- Embodied presence: Physical presence of the robots and faculty increase the realism of the meditation compared to video/audio  
- Consistent delivery: Both robots are running with scripts that were revised and tested
- Increased accessibility: Robots can be more accessible for anyone who purchased or participated the retreat
- Higher engagement: Curisoty should lead people to experience new way of meditation
- Customizable interactions: Scripts can be changed based on the needs of the sessions or groups
- Non-judgmental guidance: Robots can create a much comfortable environment for meditation as it do not judge or react 
- Scalable deployment: Once refined, the robots should lead the exercises by themselves withou any human intervention

# Retreat Structure

The retreat is designed to be an approximately 3-hour session, balancing participant engagement and robot operational limits. The flow maximizes interaction with multiple robot/system deployments while incorporating natural transitions between activities. While a longer session would give participants more time to interact with the robots, it is also important to consider the robot battery life, audience attention span, and effectiveness of a longer session. 

##  Retreat Schedule (3 Hours)

- **0:00–0:10 — Welcome & Setting Intention**  
  Pepper and Mini-Pupper introduce themselves and the team. Icebreaker + MC facilitation to begin the day.

- **0:10–0:30 — Robot Cowboy Folies**  
  LLM-Human folie script with audience sound cues. Explores emotion through story and sound.

- **0:30–1:00 — Mindful Breathing with Robot**  
  Guided breath meditation by Pepper or human. Transitions participants into silence and mindfulness.

- **1:00–1:15 — Silent Nature Witnessing**  
  Solo outdoor reflection. Participants observe nature mindfully and return with a found object for VLM analysis.

- **1:15–1:45 — RAIN Guided Meditation**  
  Jointly led by Pepper and human using Tara Brach’s R.A.I.N. meditation. Emphasizes nature-tech harmony.

- **1:45–2:15 — Puppy Robot Mindful Movement**  
  Mini-Pupper leads stretching and movement exercises comparing robot and human motion (e.g., yoga + jogging).

- **2:15–2:45 — Closing Circle: Sharing & Chatbot**  
  Group reflection. Participants share insights while engaging with a listening therapy chatbot.

- **2:45–3:00 — Meditation & Integration**  
  Final relaxation session with Octodrum robot music and ocean sounds. Guided cool-down and reflection.


## Project Timeline & Milestones

| Feature                        | Description                                                                                      | Date                                 | Dependency                                | Assigned to |
|-------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------|-------------------------------------------|-------------|
| Demo Design                   | Structure for demonstrating retreat functions of Pepper and Pupper                              | Fall Term Week 7                     | None                                      | Everyone    |
| Project development, iteration 1 | Time dedicated to developing the Winter retreat                                                  | Fall Term Weeks 7–10<br>Winter Term Weeks 1–5 | Use design documentation                   | Everyone    |
| Winter mini retreat 1         | Full meditation retreat with CHARISMA Labs                                                      | 2025.Feb.2nd                          | All prepared robots we have               | Everyone    |
| Project development, iteration 2 | Time to modify production for Winter retreat 2                                                  | Winter Term Weeks 5–6                | Feedback from Winter retreat 1            | Everyone    |
| Winter mini retreat 2         | Second retreat with CHARISMA Labs, based on iteration 2                                         | 2025.Feb.22nd                         | All prepared robots we have               | Everyone    |
| Project development, iteration 3 | Develop production for Spring retreat                                                           | Winter Term Weeks 6–10<br>Spring Term | Feedback from Winter retreat 2            | Everyone    |
| Spring documentation          | Document findings and design in publishable form for CHARISMA                                  | Post-retreat Spring Term             | Feedback from each iteration              | Everyone    |
| Engineering Expo              | Final project presentation and showcase                                                         | Friday, June 6                        | Final poster for the expo                 | Everyone    |

# Findings

## Core Findings: HRI in Meditation

Through the design, development, and facilitation of this meditation retreat, we gained insight into how humans perceive and interact with robots in wellness contexts.

Participants approached robots with both **interest and confusion**. While many were eager to engage and see what the robots could do, unfamiliarity with meditation practices—or with robots themselves—often made initial interaction challenging.

This highlighted the importance of **clear guidance**, **gentle onboarding**, and **bridging unfamiliar environments** to make robot-assisted meditation more accessible and effective.


## Development Challenges
- **Robot connectivity**: Ensuring stable Wi-Fi in varied locations
- **Gesture/audio sync**: Timing issues resolved with human intervention
- **Battery life**: Retreat schedule adjusted to include rest intervals
- **Room Booking**: Ensure a room big enough for 10-20 people for 3 hours few weeks before deployments


# Codebase

## Pepper

### Pepper Python SDK Integration & Parser

We used the Python SDK (NAOqi) to create custom scripts for the Pepper robot without relying solely on Choregraphe.

#### Project Structure

```
humanrobotretreat/
├── pynaoqi-python2.7-2.8.6.23... # Official Python SDK for Pepper
├── PythonParser/
│ ├── PythonParser1/
│ │ ├── inputs/ # Input text scripts (InputScript.txt)
│ │ ├── outputs/ # Generated files (.wav, .csv)
│ │ └── parser.py # Parses script into audio + command timeline
│ ├── PythonParser2/
│ │ └── pepperExecute.py # Executes gestures & audio on Pepper using NAOqi
```

#### Setup Instructions

1. **Install NAOqi SDK**  
   Download: `pynaoqi-python2.7-2.8.6.23-win64-vs2015-20191127_152649`
2. **Add SDK path to your Python 2.7 environment**

   - **Windows**  
     In the *Environment Variables* window:  
     - Add new user variable `PYTHONPATH`  
     - Set it to: `C:\path\to\python-sdk\lib`

   - **Mac**
     ```bash
     export PYTHONPATH=${PYTHONPATH}:/path/to/python-sdk/lib/python2.7/site-packages
     export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:/path/to/python-sdk/lib
     ```

   - **Linux**
     ```bash
     export PYTHONPATH=${PYTHONPATH}:/path/to/python-sdk/lib/python2.7/site-packages
     ```

3. Ensure **Pepper and your computer are on the same network**

#### Input Script Format

Example (`InputScript.txt`):
```
1) Hello #wave I am Pepper and I am going to speak about the garden of serenity.
2) I am #shocked also Pepper #raise_up
1) But I am curious about the next line #wave
```

- `1)` or `2)` indicates voice ID
- `#wave`, `#raise_up`, `#shocked` refer to gestures created in Choregraphe

#### Configuration

Example (`config.py`):
```
_PEPPER_IP = '192.168.xx.xxx'_
_PEPPER_PORT = 9559_
_INPUT_FILE = '../inputs/InputScript.txt' #Select the input text file you want to output_
_SPEAKER_WAV = '../inputs/female.wav'_
_BACKGROUND_SOUND = None_
```

#### How to Run

1. **Generate Output Files**
```
python3 PythonParser1/parser.py
```

2. **Execute on Pepper (Python 2.7)**
```
python PythonParser2/pepperExecute.py
```

This will:
- Parse the input test
- Generate `.wav` voice lines
- Synchronize gesture/audio actions via `commandFile.csv`
- Control Pepper via NAOqi

#### Notes

- `pepperExecute.py` **must be** run with **Python 2.7**
- `parser.py` can run with **Python 3.x**
- NAOqi SDK is required and must be sourced for execution
- Pepper must be **powered on** and reachable via the specified IP

---

### Pepper Behaviors with Choregraphe

We also created visual behavior flows using **Choregraphe**, Aldebaran's official visual programming IDE for the Pepper robot. These behaviors were used for guided meditation and interaction segments of the retreat.

> **Important:**  
> Please use **Choregraphe version 2.5.10.7** to ensure full compatibility with the NAOqi SDK and Pepper robot.  
> Other versions may cause compatibility issues or failed deployments.

#### Demo Video

[**Click to play Pepper Demo Video**](https://media.oregonstate.edu/media/t/1_j2n719d6)

#### Description

- Behaviors were built using timeline animation boxes, animated speech, and Python Script boxes in Choregraphe.
- Motion gestures like `#wave`, `#raise_up`, and `#shocked` were defined and tested inside the timeline editor.
- Custom scripts enabled more dynamic interactions and transitions during the retreat.
- These visual behaviors complement the Python-based parser system used in other parts of the project.

## Pupper

### Code/File Structure

### Design

Flow chart of the Mini-pupper

![Picture4](https://github.com/user-attachments/assets/bd767552-1a55-4124-8f67-db81d2dea9b3)

### Set Up Instructions

### How to Run

### Customizable Features

# Next Steps


# Acknowledgements

Feel free to contact us via Email or the CHARISMA Lab for more information or anwswering your questions.

Lab Manager:

Heather Knight - (heather.knight@oregonstate.edu)

Team Members:

Ben Ziegler - (zieglben@oregonstate.edu)

Eliane Wang - (wangel@oregonstate.edu) 

Jacob Strand - (strandja@oregonstate.edu)

Kweon Ho Park - (parkkweo@oregonstate.edu)

Yen-Ting Chou - (chouye@oregonstate.edu)

![retreat_team](https://github.com/user-attachments/assets/8c43c1d9-cc32-4152-83c7-59efd4589311)


