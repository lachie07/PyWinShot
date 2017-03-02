import os
import time
import ImageGrab

#-----OPTIONS------
SAVE_DIRECTORY = "C:\\Users\\Lachie\\Desktop\\"
TIMER_COUNTDOWN = 5
AUTOMATIC_SAVE = False
#------------------

print """Note:
When the screenshot is taken, it will display it in a low resolution.
This problem cannot be fixed, so deal with it. To view a higher
resolution image, simply open up the picture via Windows Explorer.
To change the save directory, simply open up the script and change
"Save Directory" to where ever you want it (putting a double '\'
instead of a single one)."""

time.sleep(4)

for i in range(TIMER_COUNTDOWN,-1,-1):
    print i
    time.sleep(1)

img = ImageGrab.grab()
saveas = os.path.join(SAVE_DIRECTORY,"Screenshot.jpg")
img.show()
option = raw_input("Would you like to save this screenshot(Y/N): ")
if option.lower() == "y":
    img.save(saveas)
