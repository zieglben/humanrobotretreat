<!-- README for Mini-Pupper portion of retreat -->
<!-- NOT FINAL, NEEDS TO BE UPDATED -->

## Pepper

We created visual behavior flows using **Choregraphe**, Aldebaran's official visual programming IDE for the Pepper robot. These behaviors were used for guided meditation and interaction segments of the retreat.

### Design

![Image](https://github.com/user-attachments/assets/7ac53606-d26e-4ad6-bb74-faefed2d34bc)

The Pepper interaction flow was designed to introduce participants to the retreat, establish an embodied presence, and transition them into the first mindfulness activity. The design emphasizes clear gestures, synchronized speech, and smooth pacing to create a calming and welcoming atmosphere.

> **Flow Summary:**  
> Pepper begins by greeting the audience with a wave and introducing the day’s intention.
> Then it previews each upcoming activity in order: Robot Cowboy Folies, Silent Nature Witnessing, RAIN Meditation, Puppy Robot Movement, and the Closing Circle.
> The entire intro is designed to be ~5 minutes long with pauses and gestures for emphasis.

Each behavior was structured using a combination of:
- **Timeline animations** for predefined arm and head movements.
- **Animated Speech** boxes for voice output with synchronized facial expressions.
- **Programming Script** boxes for simple logic (e.g., timing transitions).

The Choregraphe behavior begins with a **wave gesture and a welcoming message**, followed by **expressive animations** like raising arms and reacting to participant presence. This sequence was carefully timed and tested to align with human facilitator introductions.

> Unlike other portions of the retreat, this segment does not rely on external Python scripts or audio parsing systems. All behavior is embedded within the Choregraphe project.

#### Demo Video

[![Image](https://github.com/user-attachments/assets/7e4054ba-1306-4098-870b-7194af78a018)](https://drive.google.com/file/d/1aADD2FAXFfMwwHZv9yNaRM3gFjm_T4b8/view?usp=sharing)

#### Description

- Timeline animations, animated speech, and script boxes were used to construct this behavior in Choregraphe.
- Gestures like `#wave` and `#raise_up` were tested and synced with voice segments.

### Set Up Instructions

> **Important:**  
> Please use **Choregraphe version 2.5.10.7** to ensure full compatibility with the NAOqi SDK and Pepper robot.  
> Other versions may cause compatibility issues or failed deployments.
