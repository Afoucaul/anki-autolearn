# Autolearn for Anki

You wish you could keep on studying while working all day long on your PC?
Autolearn is here for you!

This simple plugin will make Anki appear in foreground at a customizable time interval, to have you study every now and then.
As soon as you answered a card, Anki will vanish and let you work, only to appear some minutes later with a fresh new one.


## Installation

As for now, this add-on relies on a non-standard hook, `'cardAnswered'`, fired whenever you answer a card.
This is the only difference with the official Anki branch, so I hope I can have it merged soon.
For the time being, you will have to install Anki from my fork, at https://github.com/Afoucaul/anki.git.

To do this, you just have to clone the said repo, and run `sudo make install` in it.
If you have any trouble with this step, please open an issue at the official Anki repo; I'll be glad to help there.

Once this is done, you can install this add-on just like any other regular add-on.
First, clone this repo, then open Anki, go to `Tools > Add-ons > View files` to check the directory where add-ons are installed, and finally copy (or better, make a symlink) the `src` directory into the add-ons directory.


## How to

The configuration of this add-on is plain simple and straightforward.
You'll find in the `Tools` menu a `Autolearn` line, that will open a simple dialog.
There, you can set up the delay between two appearances from Anki.
That's it!
