#!/usr/bin/python3

import speedtest

import os
import sys

import blessed
from blessed import Terminal


from functions import *
import ascii

t = Terminal()
globals()["hide_country"] = False
globals()["hide_isp"] = False

def parse_args():
    args = sys.argv[1:]
    argc = len(args)

    if (argc > 0):
        for arg in args:
            if (arg == "--hide-isp" or arg == "-hisp"):
                globals()["hide_isp"] = True
            
            elif (arg == "--hide-country" or arg == "-hc"):
                globals()["hide_country"] = True
            
            elif (arg == "--version" or arg == "-v"):
                version_menu()
                exit()

            elif (arg == "--help" or arg == "-h"):
                help_menu()
                exit()
            
            else:
                print("Invalid argument\n")
                
                help_menu()
                exit()
            


def main():
    parse_args()

    # https://github.com/sivel/speedtest-cli/wiki
    # https://github.com/sivel/speedtest-cli
    # Credit goes to above for their amazing library!


    # Initalize Speedtest class
    test = speedtest.Speedtest()

    # Obtain servers
    test.get_servers([])
    test.get_best_server()

    # Preform download test
    test.download()

    # Preform upload test
    test.upload()

    # Finalize
    test.results.share()
    results = test.results.dict()

    # Declare variables for printing

    download_speed = round(bps_to_mbps(results["download"]), 2)
    upload_speed = round(bps_to_mbps(results["upload"]), 2)
    ping = results["ping"]

    client_class = results["client"]



    country = client_class["country"]
    isp = client_class["isp"]
    isp_rating = client_class["isprating"]

    if (globals()["hide_country"] == True):
        country = "HIDDEN"
    
    if (globals()["hide_isp"] == True):
        isp = "HIDDEN"
        isp_rating = "HIDDEN"

    # Print the ASCII art associated with the ISP
    try:
        print(ascii.ascii[isp])
    except KeyError:
        print(ascii.ascii["UNKNOWN ISP"])


    # Format for how the fetch will be displayed
    # Very ugly, because I had to manually enter the terminal codes for bold text on certain items, due to the way I had implemented this. Bad idea, but may change in the future.
    fetch = """
\033[1mCountry:\033[0m {country}

\033[1mISP:\033[0m {isp}
\033[1mISP Rating:\033[0m {isp_rating} 

\033[1mDownload Speed (Mbps):\033[0m {download_speed}Mbps
\033[1mUpload Speed (Mbps):\033[0m {upload_speed}Mbps
\033[1mPing (ms):\033[0m {ping}ms
    """.format ( # Format and put variables in.
        country = country,
        isp = isp,
        isp_rating = isp_rating,
        download_speed = download_speed,
        upload_speed = upload_speed,
        ping = ping
    )

    # Finally print the fetch

    print(fetch)


if __name__ == "__main__":
    main()