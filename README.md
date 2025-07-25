# Group 4 - Robot Escape Room Project:

## This was our final project in our Elements of Computer Programming I class during the 2024 fall semester at Delaware State University, under the guidance of Professor Marwan Rasamny. During the class, we learned Python and applied what we learned, along with our studying, to code everything. We used Mbot2's as the player and enemies, using an extra CyberPi for the controller. Everything was coded using mBlock, a graphical programming platform based on Scratch and Python programming. It can be downloaded from www.mblock.com. To play the game yourself, you need at least two mBots and 3 Cyberpi's. You will also need some cardboard, colored paper, and black tape. Once you set up the maze, you can place your enemy bots on their designated paths. Then connect both the Remote Receiver and Sender to the same wifi network, and you're good to go!

### Remote Control Sender
The remote control sender is what you will use to control your mBot2. When you press any buttons or move the joystick, it sends the corresponding signal to the remote control receiver.
### Remote Control Receiver
All basic functions of the mbot are controlled by receiving the signals sent by the sender, then communicating with the mBot to move it.
### The Enemy Bot Pathing:
This code causes the enemy bots to follow a path marked by black tape until the end of the game. 
### The Score & Leaderboard System:
Controls the start and end of the game, as well as the score & time elapsed, along with which keys you've collected throughout the game.
### The Key System:
When the right color is detected, this code broadcasts a signal from the receiver to the sender and allows it to display which keys were collected

### Objective:
Our escape room consists of three robots. One is remotely controlled by the player (you), the others act as enemies. The goal of the escape room is to collect three colored keys(R.G.B) as you navigate through the maze. At the same time, you are trying to avoid enemy bots who can get in your way and cost you time. To win the game, you must collect all three keys. There is also a leaderboard, allowing you to compete with yourself or friends to see who can achieve the fastest time.

### mBot Controls
Pressing up on the joystick will move the mBot forward until the input is released.
Pressing down on the joystick will move the mBot backward until the input is released.
Pressing the left joystick button will rotate the mBot left until the input is released.
Pressing the right joystick button will rotate the mBot right until the input is released.
Double-tapping the A button will activate a speed boost, which doubles your speed until a new joystick input is pressed. 
Pressing the B button will scan the ground beneath the mbot. If it detects red, green, or blue, it will count that key as collected. 

# Created by: Maxwell Weiss, Noah Panto, Issac Davis, Isiah Edgehill, and Jerica Fitzgerald
