import wiringpi2 as odroid
import time
import os
import glob
import sys

odroid.wiringPiSetup()

Button = 3

odroid.pinMode(Button,0)
odroid.pullUpDnControl(Button,1)


#loop
print("Program Running")
while True:#loops forever till keyboard interupt (ctr + C) 
  if odroid.digitalRead(Button) == False: #when button not pressed:
    sys.stderr.write(".")
    time.sleep(1)
  else:
    print("Button Pressed")
    #    ------|    photo & Bell    |------ #
    #Get FileName
    now = time.strftime("Date%m-%d-%yTime%H-%M-%S")
    #Make command to run odroidC2.sh
    command = "bash odroidC2.sh " +  str(now)
    
    # -- odroidC2.sh is an Shell script that
    # -- is responsible for taking the photo and
    # -- making the Doorbell Noise
    
    # --- We insert the "Now" argument so the python
    # --- script knows what the file name of the
    # --- picture will be so it can pass it on into the
    # --- email script (so it knows what file to email
    
    #run command
    os.system(command)
    #diagnostics
    print("Filename:", now)
    
  
    # ----| Email     |---- #
    print("Email")#email
    emailcommand = 'sudo python IoTOdroid.py "Someone is ringing the doorbell"' + ' "photos/' + now + '.jpg"'
    os.system(emailcommand) #running the Email script with:
    #-- the subject as "Someone is ringing the doorebell" and the filename
    #-- We made before at the -Photo & Bell- section
    
    # -- End Diagnostic Info
    print("Done Process")
    #-space out for next "Press of Button"
    print("")
    print("")

