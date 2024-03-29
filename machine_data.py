logo = """
 a88888b.          .8888b .8888b                                                   dP       oo                   
d8'   `88          88   " 88   "                                                   88                            
88        .d8888b. 88aaa  88aaa  .d8888b. .d8888b.    88d8b.d8b. .d8888b. .d8888b. 88d888b. dP 88d888b. .d8888b. 
88        88'  `88 88     88     88ooood8 88ooood8    88'`88'`88 88'  `88 88'  `"" 88'  `88 88 88'  `88 88ooood8 
Y8.   .88 88.  .88 88     88     88.  ... 88.  ...    88  88  88 88.  .88 88.  ... 88    88 88 88    88 88.  ... 
 Y88888P' `88888P' dP     dP     `88888P' `88888P'    dP  dP  dP `88888P8 `88888P' dP    dP dP dP    dP `88888P' 
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo                                                                                                            
"""

wrong_input = """
  ___              _ _    _   ___                _   _ 
 |_ _|_ ___ ____ _| (_)__| | |_ _|_ _  _ __ _  _| |_| |
  | || ' \ V / _` | | / _` |  | || ' \| '_ \ || |  _|_|
 |___|_||_\_/\__,_|_|_\__,_| |___|_||_| .__/\_,_|\__(_)
                                      |_|              
"""

prompt = """
What would you like? (espresso/latte/cappuccino): """

out_resource = """
   ___       _          __                                      
  / _ \ _  _| |_   ___ / _|  _ _ ___ ___ ___ _  _ _ _ __ ___ ___
 | (_) | || |  _| / _ \  _| | '_/ -_|_-</ _ \ || | '_/ _/ -_|_-<
  \___/ \_,_|\__| \___/_|   |_| \___/__/\___/\_,_|_| \__\___/__/
                                                                
"""

not_enough_resources_logo = """
  _  _     _                            _                                         
 | \| |___| |_   ___ _ _  ___ _  _ __ _| |_    _ _ ___ ___ ___ _  _ _ _ __ ___ ___
 | .` / _ \  _| / -_) ' \/ _ \ || / _` | ' \  | '_/ -_|_-</ _ \ || | '_/ _/ -_|_-<
 |_|\_\___/\__| \___|_||_\___/\_,_\__, |_||_| |_| \___/__/\___/\_,_|_| \__\___/__/
                                  |___/                                           
"""

payment_logo = """
  ___                         _   
 | _ \__ _ _  _ _ __  ___ _ _| |_ 
 |  _/ _` | || | '  \/ -_) ' \  _|
 |_| \__,_|\_, |_|_|_\___|_||_\__|
           |__/                   
"""

final_coffee = """
        ..
      ..  ..
            ..
             ..
            ..
           ..
         ..
##       ..    ####
##.............##  ##
##.............##   ##
##.............## ##
##.............###
 ##...........##
  #############
  #############
#################"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
