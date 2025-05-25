# Human-Robot Meditation Retreat: Development, Deployment, and Assessment
### Exploring the effectiveness of delivering mindfulness exercises through robots.
![Pepper and Pupper (1)](https://github.com/user-attachments/assets/49448785-82ee-4e6e-9d2b-cd35934d44fe)


_Mini-Pupper 2 (left) and Pepper (right) robots were the main systems used for this project as pictured above._

This repository and its contents were developed as part of a Senior Capstone project at Oregon State University from September 2024 - June 2025, in collaboration with the CHARISMA Lab on campus. The project followed up on a 6-month robot-led meditation series from January – June 2024 by the CHARISMA Lab at OSU.

# Why Robots?

Meditation and mindfulness practices have gained popularity in recent years, especially after the COVID-19 pandemic, which increased isolation and stress. While many automated meditation resources, such as apps or scripted videos, offer accessible guidance, they lack the dynamic and embodied interaction that is offered by in-person guided meditation. This project explored how leveraging the physical presence of robots can enhance meditation experiences beyond static, pre-recorded scripts.

# Retreat Structure

The retreat is designed to be an approximately 3-hour session, balancing participant engagement and robot operational limits. The flow maximizes interaction with multiple robot/system deployments while incorporating natural transitions between activities. While a longer session would give participants more time to interact with the robots, it is also important to consider the robot battery life, audience attention span, and effectiveness of a longer session. 

# Findings



# Codebase

## Pepper

### Pepper Python SDK Integration & Parser

We used the Python SDK (NAOqi) to create custom scripts for the Pepper robot without relying solely on Choregraphe.

#### Project Structure

```
humanrobotretreat/
├── pynaoqi-python2.7-2.8.6.23... # Official Python SDK for Pepper
├── PythonParser/
│ ├── inputs/ # Input text scripts (InputScript.txt)
│ ├── outputs/ # Generated files (.wav, .csv)
│ └── parser.py # Parses script into audio + command timeline
├── PythonParser2/
│ └── pepperExecute.py # Executes gestures & audio on Pepper using NAOqi
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

# Next Steps


# Acknowledgements

