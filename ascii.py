from blessed import Terminal

t = Terminal()

# Dictionary containing ASCII art of the various ISPs, they are also coloured according to blessed's functions on them

ascii = {
    "Spectrum": t.bold_green(r"""
________                  _____                          
__  ___/____________________  /___________  ________ ___ 
_____ \___  __ \  _ \  ___/  __/_  ___/  / / /_  __ `__ \
____/ /__  /_/ /  __/ /__ / /_ _  /   / /_/ /_  / / / / /
/____/ _  .___/\___/\___/ \__/ /_/    \__,_/ /_/ /_/ /_/ 
       /_/                                                                                                                                                                                                                  
    """),
    "AT&T": t.bold_blue(r"""
    ____________________  ________
___    |__  __/_( _ ) ___  __/
__  /| |_  /  _  __ \/|_  /   
_  ___ |  /   / /_/  <_  /    
/_/  |_/_/    \____/\//_/     
    """),
    "Comcast": t.bold_red(r"""
     ____                                                 __      
/\  _`\                                              /\ \__   
\ \ \/\_\    ___     ___ ___     ___     __      ____\ \ ,_\  
 \ \ \/_/_  / __`\ /' __` __`\  /'___\ /'__`\   /',__\\ \ \/  
  \ \ \L\ \/\ \L\ \/\ \/\ \/\ \/\ \__//\ \L\.\_/\__, `\\ \ \_ 
   \ \____/\ \____/\ \_\ \_\ \_\ \____\ \__/.\_\/\____/ \ \__\
    \/___/  \/___/  \/_/\/_/\/_/\/____/\/__/\/_/\/___/   \/__/
                                                              
                                                              
    """),
    "Verizon": t.bold_red(r"""
    ___    __           _____                    
__ |  / /______________(_)__________________ 
__ | / /_  _ \_  ___/_  /___  /_  __ \_  __ \
__ |/ / /  __/  /   _  / __  /_/ /_/ /  / / /
_____/  \___//_/    /_/  _____/\____//_/ /_/ 
                                             
    """),
    "Cox": t.bold_blue(r"""

    .oooooo.                         
 d8P'  `Y8b                        
888           .ooooo.  oooo    ooo 
888          d88' `88b  `88b..8P'  
888          888   888    Y888'    
`88b    ooo  888   888  .o8"'88b   
 `Y8bood8P'  `Y8bod8P' o88'   888o 
                                                    
    """),

    "Frontier": t.bold_yellow(r"""
    __________                   __________             
___  ____/_____________________  /___(_)____________
__  /_   __  ___/  __ \_  __ \  __/_  /_  _ \_  ___/
_  __/   _  /   / /_/ /  / / / /_ _  / /  __/  /    
/_/      /_/    \____//_/ /_/\__/ /_/  \___//_/     
                                                    
    """),
    "UNKNOWN ISP": t.bold_red(r"""                                           
#     # #    # #    # #    #  ####  #    # #    # 
#     # ##   # #   #  ##   # #    # #    # ##   # 
#     # # #  # ####   # #  # #    # #    # # #  # 
#     # #  # # #  #   #  # # #    # # ## # #  # # 
#     # #   ## #   #  #   ## #    # ##  ## #   ## 
 #####  #    # #    # #    #  ####  #    # #    #
    """)
}