# New Yume  
A psychological visual novel made with Ren’Py


## About  
New Yume is a psychological visual novel about a girl named Yume who wakes up inside a mysterious abandoned church. There, she meets two guiding figures: Yoru, who offers comfort and escape through an idealized dream world, and Satoshi, who represents painful truth and reality.

As Yume explores the church, she is forced to choose between staying in a comforting illusion or facing a harsh awakening. The game explores themes like escapism, trauma, and the difference between fantasy and reality.

The game has multiple choices and two different endings depending on the player’s decisions.


## How to Play  
- Click to progress through dialogue and story  
- Make choices when they appear on screen  
- Your choices affect the ending you get  


## How to Run the Game  
1. Download or clone this repository  
2. Open Ren’Py Launcher  
3. Click on “Add Existing Project”  
4. Select the **New Yume** folder  
5. Click **Launch Project** to play  


## How to Build (Export Game)  
1. Open Ren’Py Launcher  
2. Select the project  
3. Go to **Build Distributions**  
4. Choose the platform (Windows / Mac / Linux)  
5. Click **Build**  


## Features  
- Branching story with choices  
- Two different endings  
- Psychological horror / mystery theme  
- Dialogue-driven gameplay  


## Project Structure  
- `/game` → main game files (scripts, images, audio)  
- `script.rpy` → main story and dialogue  
- `screens.rpy` → UI and menus  


## Development Notes  
This game was made using Ren’Py. I focused on writing the story, creating the branching choices, and scripting the dialogue system. Some parts of the code were copied and adapted, while others I built and adjusted myself to fit the story.


## Code Example  
Example of a choice system used in the game:

```renpy
menu:
    "Door 1 - Satoshi":
        jump satoshi_route

    "Door 2 - Yoru":
        jump yoru_route
```

This code allows the player to choose between two story paths that lead to different endings.


## Credits  
- Images and inspiration: Pinterest  
- Engine: Ren’Py  
- Development: Me  
