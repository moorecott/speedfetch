# speedfetch
-- A (GNU/Linux based/oriented) program for fetching speed test results on the command line.
Version 1.1

## Screenshots
![enter image description here](https://i.ibb.co/86RgHVY/2019-06-20-103106-476x314-scrot.png)

## Installation

Installation (or just simple testing) can be done by either manually running the Python scripts or by installing through pip (recommended). In order to install through pip (a Python package manager) do `$ pip install speedfetch .`Then, run speedfetch.

However, some dependencies are:

- blessed (`pip install blessed`)
- speedtest-cli (`pip install speedtest-cli`)


## Misc

Usage can be found by supplying the argument *--help/h* to the program whenever you execute it. However, no arguments are required -- speedfetch essentially just does its thing when you execute it (although some arguments are there).

    
    Usage:
    
    speedfetch (no args required but are optional)
    
    ARGS:
    --hide-country/-hc: Hides the country when passed
    --hide-isp/-hisp: Hides the ISP when passed
    --version/-v: Shows the current version of the program
    --help/-h: Shows this menu (for help)

 
The program uses the speedtest-cli library and is highly dependent on it. Without it, this library would have taken much longer, so thank you to those who made that library. The speedtest library also is based off of speedtest.net.

However, this program is NOT entirely accurate as you can see, but it does give a very good idea of what your internet speed is and thus has some usage. This program is not to be exactly preferred over speedtest.net or any other (better) speed test utility, but this program's purpose is merely for show or to look good on your terminal.
 
