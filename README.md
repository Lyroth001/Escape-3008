Created by Zac.D for AQA A-Level computer science

How to start:

```
Run --------.py
```

## To Build for Distribution:

FIRST TIME ONLY: 
```
pyinstaller --onefile .\mainGame.py --add-data '.\Assets\Environments;Assets/Environments' --add-data '.\Assets\UI_elements\RetroWindowsGUI;Assets/UI_elements/RetroWindowsGui' --windowed
```

To rebuild call:
```
pyinstaller mainGame.spec
```

Then run from `.\dist\mainGame.exe`

## Licensing
Content relating to the SCP Foundation, including the SCP Foundation logo, is licensed under Creative Commons Sharealike 3.0 and all concepts originate from https://scpwiki.com/ and its authors. Escape 3008, being derived from this content, is hereby also released under Creative Commons Sharealike 3.0."

------------------------------------------------------==CREDITS==--------------------------------------------------

Credits can be seen in game, under the options menu, and are included here. All SCP articles can be found on the [SCP wiki](https://scpwiki.com/):

Assets:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Topdown interior home tileset (housetile.png) by BTL games  [Link](https://btl-games.itch.io/topdown)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Free space station game asset (SpaceStationTileset.png) by Jonik9i  [Link](https://jonik9i.itch.io/free-space-station-game-asset)
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Retro windows gui by Comp-3 Interactive  [Link](https://comp3interactive.itch.io/retro-windows-gui)



SCP articles:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SCP-3008 by Mortos

Modules and tools that were used in development:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Game written in python

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exe file built using pyinstaller

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Game built using pygame
