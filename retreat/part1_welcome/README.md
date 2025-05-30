<!-- README for Mini-Pupper portion of retreat -->
<!-- NOT FINAL, NEEDS TO BE UPDATED -->

## Pepper

We created visual behavior flows using **Choregraphe**, Aldebaran's official visual programming IDE for the Pepper robot. These behaviors were used to introduce participants to the retreat, establish an embodied presence, and transition them smoothly into the mindfulness portion of the experience.

### Demo Video

[![Image](https://github.com/user-attachments/assets/7e4054ba-1306-4098-870b-7194af78a018)](https://drive.google.com/file/d/1aADD2FAXFfMwwHZv9yNaRM3gFjm_T4b8/view?usp=sharing)

### Design

![Image](https://github.com/user-attachments/assets/7ac53606-d26e-4ad6-bb74-faefed2d34bc)

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

### Set Up Instructions

> **Important:**  
> Please use **Choregraphe version 2.5.10.7** to ensure full compatibility with the NAOqi SDK and Pepper robot.  
> Other versions may cause compatibility issues or failed deployments.

To explore or run this behavior in Choregraphe:
1. Download the [```Meditation Retreat```](Meditation Retreat/) folder in this repository.
2. Open the [```Meditation Retreat.pml```](./Meditation Retreat.pml) file using Choregraphe 2.5.10.7.
3. Connect to Pepper and deploy the behavior directly from Choregraphe.

> Make sure your computer and Pepper are on the same network before launching the project.