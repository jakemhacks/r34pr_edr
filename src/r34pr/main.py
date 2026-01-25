###########################################################
#
# @@@@@@@   @@@@@@        @@@   @@@@@@@   @@@@@@@
# @@@@@@@@  @@@@@@@      @@@@   @@@@@@@@  @@@@@@@@
# @@!  @@@      @@@     @@!@!   @@!  @@@  @@!  @@@
# !@!  @!@      @!@    !@!!@!   !@!  @!@  !@!  @!@
# @!@!!@!   @!@!!@    @!! @!!   @!@@!@!   @!@!!@!
# !!@!@!    !!@!@!   !!!  !@!   !!@!!!    !!@!@!
# !!: :!!       !!:  :!!:!:!!:  !!:       !!: :!!
# :!:  !:!      :!:  !:::!!:::  :!:       :!:  !:!
# ::   :::  :: ::::       :::    ::       ::   :::
#  :   : :   : : :        :::    :         :   : :
#
# Title: R34PR Endpoint Detection and Response
# Author: Jake Murray
# Description: This is a VERY simple EDR learning project
#
#              NOT FOR REAL-WORLD USE!
#
###########################################################
from . import sensor


def welcome() -> None:
    print("Welcome to R34PR EDR")
    print("Written by a guy named Jake")
    print("This is a learning project....it's not intended for real use....yet\n")


def main():
    welcome()
    print("======= Initiating R34PR scan =======")

    cpu_perc: float = sensor.get_cpu_percent()
    print(f"Current CPU usage: {cpu_perc}\n")

    print("======= Current Running Processes")
    sensor.print_procs()


if __name__ == "__main__":
    main()
