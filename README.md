# applause_btn
python 3 code to make a button play an applause sound


To use this code your raspberry pi must have 
1. rpi.gpio
Install this library with pip:
pip install rpi.gpio
 
2. pygame
sudo apt-get update
sudo apt-get install python3-pygame

3. flite
sudo apt-get install flite

4. applause-1.wav
wget http://www.pacdv.com/sounds/people_sound_effects/applause-1.wav

Some special Raspberry pi configurations also need to be set

You must set the Rpi output audio to 3.5mm (headphone) jack
to access this configuration use command: 
sudo rasp-config  

Make sure you can hear audio play back with the following terminal commands:
amixer set PCM unmute
amixer set PCM 100%
Test that these commands worked with the following command:
amixer
