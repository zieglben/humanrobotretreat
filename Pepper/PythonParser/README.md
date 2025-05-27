# Text-to-Pepper-Robot PythonAnimator

Joseph Conrow's HonorsThesis (Defneded 5/30/24)

## Setup
### Linux
1. **Download Pycharm (requires JetBrains liscence)**    
When setting up the enviornment, I used Pycharm, and found that to be the easier and most straightforward IDE. It manages the python interpreters well (have not tried any other IDEs to compare, ei. VisualStudio). We also tested the simple use of command line interface (CLI).

2. **Setup Python Versions**
First, insure that you have Python versions 2.7 and 3.9. Check the current python interpreter version by entering in the terminal:
``` python --version ```

If the output is the incorrect version, to switch installed versions, try:
``` sudo update-alternatives --config python ```
![Chaning currently selected python version for local "python"](/assets/images/san-juan-mountains.jpg "San Juan Mountains")



3. **Download Program**     
This can be done by using "git clone ..." or by downloading the .zip.

4. **Open Project**     
Click "Open" in under the "File" header. Then select the downloaded folder named "PythonParser". Now we are good to run the program.

## How to Use





## FAQ

### Errors

1. **ModuleNotFoundError: No module named 'BLANK'**    
If you get this error, likely there is an issue with your python modules. That is, a library got misplaced or the wrong Python interpreter was used. 

2. **Process finished with exit code 137 (interrupted by signal 9:SIGKILL)**    
This is caused most certainly due to an over usage of RAM during the processing of your script (mainly the TTS processing occurring). This can be minimized by closing other programs on the computer (especially browsers).

