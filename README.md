# Dressing-Assistant

## Inspiration

Dementia patients generally require assistance with their daily activities. The intense workload of caregivers often leads to higher stress both emotionally and physically. Even worse, it sometimes results in higher morbidity and mortality rates. On the patient's’ side, individual privacy is needed in some of their activities. Specifically, privacy is important when the patient is dressing up. Based on this consideration, we designed a dressing assistant, an automatic camera monitor, with computer vision to instruct the patient to dress up without any caregiver in presence.  

## What it does

Our dressing assistant can detect different dressing errors in details and trigger voice & text instructions in real time to advice the patient to dress correctly. For example, if the collar is not folded correctly, the assistant will recognize and instruct the patient to fold the collar until it is correct.

## How we built it

We trained our model with single dressing error and then merged them together to accomplish multi-error detection in real time. The model is based on DarkFlow (with weights from Tiny Yolo), OpenCV, and Tensorflow. The user-friendly interface is designed with Pygame. A demonstration website is built with HTML, CSS3, JavaScript, and PHP.

## How to use
#dependency package
opencv, python3.6, tensorflow, Pygame 

go to darkflow github directory:https://github.com/thtrieu/darkflow

git clone https://github.com/thtrieu/darkflow.git
cd to_directory
put voice file, inteface.py and font file into darkflow directory
python3 inteface.py

A pygame user interface will show up, press start to start dressing, press quit to quit the program.

The model will take a few seconds to load.
The program will automatically detect and instruct the user to dress up.


