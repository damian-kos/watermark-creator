## watermark-creator

A tkinter based utility which that allows to put a watermark text on top of your images.


## Features:

- Create text watermark on top of image
- Adjust text opacity
- Adjust text position on image

## Installation
- Install Python: If you haven't installed Python already, download the latest version of Python from the official website (https://www.python.org/downloads/), and install it on your system.
- Open Command Prompt: Press the Windows key + R to open the Run dialog box. Type "cmd" and press Enter to open the Command Prompt.
- Navigate to the directory containing your Python script: Use the "cd" command to navigate to the directory where your Python script is saved. For example, if your script is saved on the desktop, type "cd C:\Users<username>\Desktop" and press Enter.
- Run the Python script: Once you are in the directory where your script is saved, type "python <filename>.py" and press Enter. Replace <filename> with the name of your Python script. Your script will run, and the output will be displayed in the Command Prompt.

### Usage
As app loads first thing you may want to do is to click ``` Chose your file ``` button. You can choose multiple files.
![image](https://user-images.githubusercontent.com/106775028/226755026-c2d2afea-5a5a-4c7d-9184-ceaeaa6171ba.png)

Your loaded image(s) will appear with their names in textbox. From here you can click on an image you would like to edit first.
![image](https://user-images.githubusercontent.com/106775028/226755381-23133eb2-1a1d-44cc-a466-d50b737d3a28.png)

Test image will load on right part of an app. 
![image](https://user-images.githubusercontent.com/106775028/226755453-55fda130-ddcb-4188-8834-de218330b634.png)

Now it's time to create your watermark text.
Type in text in text box above ```Get text``` and ```Convert``` buttons
![image](https://user-images.githubusercontent.com/106775028/226755513-c9d7c140-6d1b-46e3-b9f0-10e76b19ad3a.png)

Now we need to click ```Get text``. Text won't be visible at first because it's opacity is 0. We need to use opacity slider.
![image](https://user-images.githubusercontent.com/106775028/226755680-034d4584-23e3-4cab-82ec-8c6546bcb978.png)

![image](https://user-images.githubusercontent.com/106775028/226755655-50bcc46f-80a0-494c-b549-880b6842fbc9.png)

Once you are happy with your result. Click ```Save results```.
![image](https://user-images.githubusercontent.com/106775028/226756419-d5ea50f3-96d4-433a-b982-be58901c7554.png)

#### Known limitations
Unfortunately as you will notice it saves only one image at the time. Result is saved as ```final.png``` in a directory where script is located. So to not override your changes you need to rename and move this file into other directory.
``` 
script_folder/
├─ images/
│  ├─ example_image.png
├─ main.py
├─ final.png
```



