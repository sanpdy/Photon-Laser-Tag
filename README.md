# Team 16 Photon README

## About

This project is a modern replica of the software for Photon, a laser tag game created in March 1984, made in Python.
This is being developed for Ubuntu 22.04 systems, though will work on any system with a Python interpreter.

## Team 16 Members

| GitHub        | Real Name       |
| ------------- | --------------- |
| @sanpdy       | Sankalp Pandey  |
| @jjmen98      | Jonathan Mendez |
| @amwells-git  | Alexander Wells |
| @bmwodka      | Benjamin Wodka  |
| @recolaa      | Haden Fowler    |
| @GabeKincade  | Gabriel Kincade |
| @TheGreatestt | Brad Daugherty  |


## Required Python Packages

This Python project uses Supabase open-source python integration, PyQt6, Pygame, and the python-dotenv packages.
All of these packages can be found & installed by pip

*Supabase*

>pip install supabase

*PyQt6*

>pip install PyQt6

*Pygame*

>pip install pygame

*python-dotenv*

>pip install python-dotenv

## Required Ubuntu Packages

This project uses the PyQt6 QMutimedia module, which requires an Ubuntu package to run without error.
This package is the libva-dev package, a Video Acceleration API for Linux. You can install the required package with 
the following command

>sudo apt-get install -y libva-dev

## Running the Program

To run this project, download & extract the main branch to a directory on your system

Then, run your Python3 compiler from the extracted folder containing main.py using

>python3 main.py

### Player Entry:
- To add a player, input their unique player ID and hit Enter or click the add player button
- If the player ID is recognized, their codename will be updated from the database; otherwise, you will be asked to input a codename and hit Enter or click the add player button.
- Then enter the equipment ID and hit enter or click the add player button
- To clear player entries, either click "Delete Game"

### Starting the Game:
- Once all players and their details are entered, click "Start Game"
- This will initiate a 30-second countdown before transitioning to the Game Action screen.

### Game Action:
- This screen displays player codenames and their scores for the ongoing game, as well as Play-by-Play event list.
- The game will play out for 6 minutes, after which a button at the bottom of the screen will appear to return to player entry.
