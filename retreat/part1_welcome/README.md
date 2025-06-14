# Welcome & Setting Intention

The exercise was developed by KweonHo Park of the Capstone team to start Pepper, it focuses participants' eyes to help them start our retreat stably. Initiates the 3 hours retreat by welcoming on the participants and appreciate their time to participation. Starting off with introducing the team, the project, and the two robots, sharing our aim and the flow of the retreat with the participants. We also suggested participants to stay with us till the end to maximize the experience but they can leave on will.

## Overview

Time: 0:00-0:10 

Activity: Introduce the project group members, and using AI generated voice to introduce both robots.

### Pepper

We created visual behavior flows using **Choregraphe**, Aldebaran's official visual programming IDE for the Pepper robot. These behaviors were used to introduce participants to the retreat, establish an embodied presence, and transition them smoothly into the mindfulness portion of the experience.

#### Demo Videos

##### Live Demo
[![image](https://github.com/user-attachments/assets/8c2ef940-af9b-4a05-8178-0c20b115f372)](https://drive.google.com/file/d/1XQg6iXJKm2g9FYTju6RaRnLxWfT6AOuD/view?usp=sharing)

##### Development Demo (for clarity)
[![image](https://github.com/user-attachments/assets/8e5cbc5d-68ae-40fc-84d8-cb3734b6683b)](https://drive.google.com/file/d/1aADD2FAXFfMwwHZv9yNaRM3gFjm_T4b8/view?usp=sharing)

#### Design

![image](https://github.com/user-attachments/assets/b3c9be40-29cb-4177-a4df-80937b5242e3)

**Flow Summary:**  
Pepper begins by greeting the audience with a wave and introducing the day’s intention.  
Then it previews each upcoming activity in order:
- Robot Cowboy Folies, Silent Nature Witnessing, RAIN Meditation, Puppy Robot Movement, and the Closing Circle, etc.
  
The entire intro is designed to be ~5 minutes long with pauses and gestures for emphasis.

**Each behavior was structured using a combination of:**
- **Timeline animations** for predefined arm and head movements.
- **Animated Speech** boxes for voice output with synchronized facial expressions.
- **Programming Script** boxes for simple logic (e.g., timing transitions).

This segment was designed to align with the human MC's pacing and create a welcoming, low-pressure start to the retreat.

> Note: This segment does **not** rely on external Python scripts or audio parsers. All logic is fully embedded within the Choregraphe project.

#### Set Up Instructions

If this is your first time using the Pepper, please refer to our [first-time setup guide](../../moreInfo/setup/README.md#Pepper-Quick-Start-Guide).

To explore or run this behavior in Choregraphe:
1. Download the [```Meditation Retreat```](Meditation%20Retreat/) folder in this repository.
2. Open the [```Meditation Retreat.pml```](Meditation%20Retreat/Meditation%20Retreat.pml) file using Choregraphe 2.5.10.7.
3. Connect to Pepper and deploy the behavior directly from Choregraphe.

> Make sure your computer and Pepper are on the same network before launching the project.


### Pupper

#### Flow

After Pepper greets everyone, we intorduces Mini-Pupper and the team working on it with entertaining AI-generated audio. The idea is to attract interest while provide as many information about the quadraped robot. 
- Simply run the audio on your computer connecting to a speaker (.wav file located in sub folder named pupper_intro1_final.wav)

**[Text to speech AI tool - Elevenlabs](https://elevenlabs.io/app/speech-synthesis/text-to-speech)**

- Possible Extension: implement the audio into Mini-Pupper with action

Note: the script can be modified using online AI audio generate service based on preferences or needs
