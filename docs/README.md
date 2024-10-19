# Documentation for DCALC
### Installation
Installation steps for Windows:
1. First make sure you have Python (version 3, preferably above 3.9) by typing `python --version` in command prompt
2. if you get something like `Python 3.12.5` then you are good to go to the next step, otherwise go to https://www.python.org/downloads/ then click the Download Python 3.12.5 button and follow the installation steps to install the latest version of Python on your machine.
3. Scroll down to the dropdown saying "Assets"
4. click on "Source code (zip)"
5. The package will come up in downloads.
6. Go to file explorer.
7. Navigate to Downloads.
8. click on `dcalc-0.11-beta.3.zip`
9. click "Extract All". (Or you can use command-line with the `unzip dcalc-0.11-beta.3.zip` command.)
10. Open command prompt.
11. Type `cd Downloads/dcalc-0.11-beta.3/dcalc-0.11-beta.3/`
12. Type `dir` or `ls`
13. Make sure that there is a file called `main.py`
14. Type `python main.py`
15. You have launched the console calculator.
# Calculators
## November prereleases
### v0.11 b3 preview
added Modulo and Floor Division (currently at the highest precedence)<br>
[###v0.11b2](https://github.com/GreatCoder1000/dcalc/releases/tag/v0.11-beta.2)
Added install steps. 
Fixed minor bugs from last beta.
second of five planned beta releases
<br><br><br>

## October 2024
### v0.1019.0 - Ported to github
### v0.1018.4 - Main part of "main.py" in "evaluate0.py" for the evaluation method.
### v0.1018.3 - Added Docs
The docs are the thing you are reading right now!
### v0.1018.2 - Error Handling
Handles errors by storing answer as string, and formatter helper function `format_out()` 
formats string as a human-readable error string.
### v0.1018.1 - Root Functionality
Added root. eg.<br>
```
>>> 2 rt 5
2.23606797749979
```
### v0.1018.0 - Main release
Removed decimal to fraction.
### v0.1018.0b - Decimal to fraction.
Beta release.
Tested decimal to fraction functionality.
Removed in later release.
