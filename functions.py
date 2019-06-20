


def help_menu():
    help_text = """speedfetch -- a program for fetching internet speeds and other miscellaneous information about your network

Usage:

speedfetch (no args required but are optional)

ARGS:
--hide-country/-hc: Hides the country when passed
--hide-isp/-hisp: Hides the ISP when passed
--version/-v: Shows the current version of the program
--help/-h: Shows this menu (for help)"""

    print(help_text)

def version_menu():
    text = """
[Version of speedfetch: 1.0]

https://github.com/polisflatt/speedfetch
polisflatt@gmail.com"""

    print(text)


# Convert bits per second to mbps thru divison
def bps_to_mbps(bitspersecond):
    return bitspersecond / 1000000

