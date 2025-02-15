# Poses Random Execution
I am currently preparing myself for my very first bodybuilding competition. It has been a real big challenge, but I'm really looking forward to it :) Naturally, I need to create a posing routine, beying 30min-1hour daily basis.

For that, I've created a spreadsheet with details about each pose and what to pay attention to when posing. This works but it makes the posing routine a bit inefficient, because I have to:
- make the pose
- read the 'observations' column in the spreadsheets
- remember what I've done when posing
- trying to pose again remebering everything I've just read...
- Repeat the process

I mean, this is a bit costing, isn't it?

Another 'problem' is about the poses order. When the competition arrives, the poses will be set in a completely random order (besides some specific cases), and I must be prepared for that with confidence!!

This is why I have created this repository: I created `mp3` audios that calls poses and read the spreadsheet observations in a 20-25 seconds long file and stored them in the `media` folder. After that, the single and simple `main.py` calls each pose to be executed, so I just need to listen to the script calling while posing and not reading spreadsheets anymore!

First, the `iniciando.mp3` starts, indicating that the posing routine will start. Then the `sequential` folder is executed sequentially. After that, the `random` folder is executed in a random order, and the `finalizando.mp3` plays, indicating that the round is over. Another round starts again after some rest. The rounds are repeated some times, so that I don't need to play it all the time I want a round to start :)
