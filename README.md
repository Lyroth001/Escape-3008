Created by Zac.D for AQA A-Level computer science

How to start:

```
Run --------.py
```

## To Build for Distribution:

FIRST TIME ONLY: 
```
pyinstaller --onefile .\mainGame.py --collect-data Assets\\Environments --collect-data Assets\\UI_elements\\RetroWindowsGUI --windowed
```

Then edit `GameCode\mainGame.spec`:  
Change the empty array `datas` to 
`datas = [('Assets/UI_elements/RetroWindowsGUI/*','Assets/UI_elements/RetroWindowsGUI'), ('Assets/Environments/*', 'Assets/Environments')]`

To rebuild call:
```
pyinstaller mainGame.spec
```

Then run from `.\dist\mainGame.exe`

## Licensing
Content relating to the SCP Foundation, including the SCP Foundation logo, is licensed under Creative Commons Sharealike 3.0 and all concepts originate from https://scpwiki.com/ and its authors. Escape 3008, being derived from this content, is hereby also released under Creative Commons Sharealike 3.0."
------------------------------------------------------==CREDITS==------------------------------------------------------------------------
Credits can be seen in game, under the options menu, and are included here. All SCP articles can be found on the [SCP wiki](https://scpwiki.com/):

Assets:
	Modern Fantasy JRPG Character Sprites- Spriter Theo (spriter-theo.itch.io)
	1-bit 8x8 universal roguelike asset pack- Lazy Fox (lazy-fox.itch.io)
	Potions- Onocentaur (onocentaur.itch.io)
	1 million micro sprites- ivan-baranov (ivan-baranov.itch.io)
	Macks WW2 Mega gun pack[FREE]- Mack (bigmack.itch.io)

SCP articles:
	SCP-3008 by Mortos
