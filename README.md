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
- Consistent delivery: Both robots were run with scripts that were revised and tested over multiple iterations of the retreat
- Increased accessibility: Robots can be more accessible for anyone who purchased or participated the retreat
- Higher engagement: Curiosity leads people to experience new way of meditation and explore the inner-workings of robotics at the same time
- Customizable interactions: The scripts we developed can be changed based on the needs of the sessions or groups
- Scalable deployment: Once refined, the robots can lead the exercises by themselves with little human-in-the-loop intervention

# Retreat Structure

The structure for our deployments was modeled after a certain style of group mindfulness, retreats. Retreats are commonly in remote areas, away from distraction and the busyness of life. Our goal was to create an entirely encapsulated experience and limit distractions from the outside world. The two retreats we held were in a large lecture room in the Kelley Engineering Center on the Oregon State University campus. The room we selected had floor to ceiling windows to view the outside world, but offered an enclosed experience for the participants. The presence of these windows aided in the nature portions of the retreat, as detailed below. 

While many retreats are designed as weekend getaways, the schedule we developed fits within a 3-hour window and went through two iterations to reach its final form below. The 3-hour session balances participant engagement and robot operational limits, while allowing enough time for transition and individual, silent reflection. While a longer session would give participants more time to interact with the robots, it is also important to consider the robot battery life, audience attention span, and effectiveness of a longer session. With our time developing the robot programs, we found that longer sessions without human intervention often lost the attention of the participants, which helped us reach the timing in our schedule below. 

Importantly, the retreat structure is modular, allowing facilitators to modify the experience as needed. Each segment can be used independently, which supports future template development and broader adoption by non-technical audiences. The retreat schedule is as follows:

##  Retreat Schedule (3 Hours)

<details>

**<summary>0:00–0:10 — Welcome & Setting Intention</summary>**

- Pepper and Mini-Pupper welcome participants and introduce the retreat experience.
- Icebreaker activity led by the MC to build rapport and set a group intention.
- Emphasis on openness, curiosity, and grounding before mindfulness activities begin.

</details>

<details>

**<summary>0:10–0:30 — Robot Cowboy Folies: An Exercise in Cacophony and Noticing</summary>**

- Audience reads a Hero’s Journey script alongside LLM-generated sound cues.
- Focus on the emotional impact of sound and storytelling.
- Encourages playfulness and awareness of collective rhythm and participation.

</details>

</details>

<details>

**<summary> 0:30–1:00 — Mindful Breathing with Robot: An Exercise in Silence and Noticing</summary>**

- Guided breath meditation with soft, calming voice.
- Transitions into the silent portion of the retreat.
- Focused on grounding participants in the present and preparing for deeper reflection.

</details>

</details>

<details>

**<summary> 1:00–1:15 — Silent Nature Witnessing: Reflection and Collection</summary>**

- Participants walk silently outside, observing the natural world mindfully.
- Tasked with bringing back a found object for robotic VLM (Vision-Language Model) analysis.
- Encourages solo reflection and deep environmental noticing.


</details>

</details>

<details>

**<summary> 1:15–1:45 —  RAIN Guided Meditation: Technology & Nature</summary>**

- A guided meditation inspired by Tara Brach’s R.A.I.N. technique.
- Combination of Pepper’s custom intro and human-guided audio.
- Offers emotional grounding and emphasizes mindfulness of thoughts and feelings.

</details>

</details>

<details>

**<summary> 1:45–2:15 — Puppy Robot Facilitated Mindful Movement</summary>**

- Quadruped-human movement mirroring activities.
- Includes yoga-inspired stretching followed by upbeat, exercise-based movement (e.g., Jane Fonda-style cardio).
- Highlights differences in human and robot body systems while promoting playful physical awareness.


</details>

</details>

<details>

**<summary> 2:15–2:45 — Almost Closing Circle: Group Sharing & End of Silence</summary>**

- Participants engage in partner-based feedback with a therapy-style chatbot.
- Practice active listening and reflection using robot-human dialogue.
- Marks the closing of the silent portion of the retreat.

</details>

</details>

<details>

**<summary> 2:45–3:00 — Meditation & Integration</summary>**

- Guided relaxation session with ocean sounds and robotic drum rhythms.
- Encourages participants to let go of tension and integrate their experience.
- Gentle close to the retreat, fostering inner calm and closure.

</details>

## Project Timeline & Milestones

| Feature                        | Description                                                                                      | Date                                 | Dependency                                | Assigned to |
|-------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------|-------------------------------------------|-------------|
| Demo Design                   | Structure for demonstrating retreat functions of Pepper and Pupper                              | Fall Term Week 7                     | None                                      | Everyone    |
| Project development, iteration 1 | Time dedicated to developing the Winter retreat                                                  | Fall Term Weeks 7–10<br>Winter Term Weeks 1–5 | Use design documentation                   | Everyone    |
| Winter mini retreat 1         | Full meditation retreat with CHARISMA Labs                                                      | 2025.Feb.2nd                          | All prepared robots we have               | Everyone    |
| Project development, iteration 2 | Time to modify production for Winter retreat 2                                                  | Winter Term Weeks 5–6                | Feedback from Winter retreat 1            | Everyone    |
| Winter mini retreat 2         | Second retreat with CHARISMA Labs, based on iteration 2                                         | 2025.Feb.22nd                         | All prepared robots we have               | Everyone    |
| Spring documentation          | Document findings and design in publishable form for CHARISMA                                  | Post-retreat Spring Term             | Feedback from each iteration              | Everyone    |
| Engineering Expo              | Final project presentation and showcase                                                         | Friday, June 6                        | Final poster for the expo                 | Everyone    |

# Core Findings: HRI with Meditation

Through the design, development, and facilitation of this meditation retreat, we gained insight into how humans perceive and interact with robots in wellness contexts. Participants often approached the robots with both **interest and confusion**. While many were eager to engage and see what the robots could do, unfamiliarity with meditation practices—or with robots themselves—often made initial interaction challenging. This highlighted the importance of **clear guidance**, **gentle onboarding**, and **bridging unfamiliar environments** to make robot-assisted meditation more accessible and effective.

The natural solution, a human-in-the-loop approach, was often reached with our robot deployments, especially with the coordinate system stretching using the Mini-Pupper 2. The Mini-Pupper has a very rigid body, with not much room for expression, so while it may have seemed very clear what the intended movements were for the development team, the audience often found it difficult to understand what they were to do without a human demonstration alongside the robot. This human-in-the-loop approach bridged the gap between the robot coordinate system and the human coordinate system in a way that made sense for participants who had no prior knowledge of the activities during that portion of the retreat. 

Social setup, room layout, and egocentric vs exocentric instructions also impacted the delivery of the Mini-Pupper exercise and stretching routines. With more people in the room at our first iteration, it was more difficult to find space and settle on a placement of participants that didn't limit anyone's view of the robot or overall experience. As pictured below, the layout we decided on was the robot and human facilitator up front, and everyone else spaced evenly behind the robot. Modeling after a yoga or exercise class, the human facilitator faced the audience and provided mostly egocentric instructions from the perspective of the audience, which made it much easier for participants to understand their instructions. While this approach likely removes the need for a robot instructor, as the human is much more expressive and instructive, we found that the robot served as a necessary and interesting distraction. 

![Retreat social layout (1)](https://github.com/user-attachments/assets/1a2a8b6d-2e30-4a5d-ac52-6d64657128d6) 

_Mini-Pupper activity social diagram_

Drawing from their time developing the program and knowledge of programming, the human facilitator often revealed behind-the-scenes information about the development process in the form of instructions. For example, the exercise routine is mostly coded using a looping structure, so when participants asked how long the routine was, the instructor hinted at it being a simple loop, offering both comedic relief and a better understanding of the inner-workings of the Mini-Pupper's programming. We found that while the retreat was intended to be a quiet, relaxing experience, humor often found its way in and enhanced the experience for everyone involved. Therefore, for the second retreat, the Mini-Pupper team iterated upon that to create funny vocal scripts for the robot to use when introducing the team and itself that referenced the audience to deliver some of its comedy. 

## Development Challenges
- **Robot connectivity**: Ensuring stable Wi-Fi in varied locations
- **Gesture/audio sync**: Timing issues resolved with human intervention
- **Battery life**: Retreat schedule adjusted to include rest intervals
- **Room booking**: Ensure a room big enough for 10-20 people for 3 hours few weeks before deployments


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

### Retreat Tour

The human robot retreat may host the retreat with other universities due to interest generated at ICRA.

**Tentative Tour Stops (Aug 2025 – Jan 2026):**
- University of Iowa
- University of California Santa Cruz
- University of California Los Angeles
- University of Texas at Austin
- Simon Fraser University
- University of Washington

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

![retreat team](https://github.com/user-attachments/assets/77d1fb80-701d-434a-aa41-ea6c2ea10378)



