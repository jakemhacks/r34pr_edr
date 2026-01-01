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

"""
Build Phase 1 - Process Monitoring

----------------------------           ----------------------------
| Monitor process creation |     ->    | Alert user on detection  |
| and termination          |     |     |                          |
----------------------------     |     ----------------------------
             |                   |                  |
             |                   |                  |
----------------------------     |     ----------------------------
| Event Listeners          |     |     | Kill malicious processes |
----------------------------     |     ----------------------------
             |                   |
             |                   |
----------------------------     |
| Store events in          |     |
| SQLite Database          |     |
----------------------------     |
             |                   |
             |                   |
----------------------------     |
| Check events against     |     |
| detection rules          |     |
----------------------------     |
             |                   ^
             |___________________|

"""

import psutil


def process_monitor():
    # This is the main process monitor
    # it will take the name, pid and username of each process
    for proc in psutil.process_iter(['pid','name', 'username']):
        print(f"{proc.ppid()} : {proc.name()} : {proc.is_running()}")

    # Make a database of running processes w/ info


def main():
    process_monitor()


if __name__ == "__main__":
    main()
