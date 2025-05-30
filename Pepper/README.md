
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

[**Click to play Pepper Demo Video**](https://drive.google.com/file/d/1OA1LWzkkapTcMa5AKxkxwJxYH7gjEVsx/view?usp=sharing)

#### Description

- Behaviors were built using timeline animation boxes, animated speech, and Python Script boxes in Choregraphe.
- Motion gestures like `#wave`, `#raise_up`, and `#shocked` were defined and tested inside the timeline editor.
- Custom scripts enabled more dynamic interactions and transitions during the retreat.
- These visual behaviors complement the Python-based parser system used in other parts of the project.