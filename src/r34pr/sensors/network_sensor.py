# collect network info and interfaces on machine

import subprocess


def get_interfaces():
    interfaces = subprocess.run(["ip", "-j", "-p", "a"], text=True, capture_output=True)

    with open("interfaces.json", "w") as f:
        f.write(interfaces.stdout)
    # ethernet, wireless, bluetooth
