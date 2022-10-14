import pyautogui;
import time;
import random;

time.sleep(3);

for z in range(1,5):
    x = random.randint(0, 500);
    y = random.randint(0, 500);
    pyautogui.moveTo(x, y);

    localtime = time.localtime();
    result = time.strftime("%I:%M:%S %p", localtime);

    print('Moved to ' + str(result) + ' (' + str(x) + ', ' + str(y) + ')');
    time.sleep(1);

print('End...');

#pyautogui.click(x, y, button='left');
#pyautogui.doubleClick(x, y, button='left');
#pyautogui.dragTo(x, y, button='left');

#print(pyautogui.position());
