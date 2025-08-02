# verify_shell_location.py
# Prof Lillian Lee (LJL2), Molly Feldman (MQF3), and Amol Tandel (AT766)
# Jan 2025

"""Check if the user has placed this and all the first-module-lab files in 
a folder with name specified in global variable LDIRNAME below."""

import os
import sys
LDIRNAME = "lab03"


#if not (sys.version_info[0] == 3 and sys.version_info[1] >= 6):
if sys.version_info[0] <= 2:
    print("\n.... CS1110 problem: unexpected Python version " +
          str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "....\n")
    print("Please ask your lab staff for help with your Python installation.")
    sys.exit(1)


right_dir=False

desired_dir_substring = "lab03"

print()
if os.path.basename(os.getcwd()) !=  desired_dir_substring:
        print("CS1110 WARNING: the working directory (folder) seems incorrect.")
        print("  We were expecting to be in a directory named " + desired_dir_substring + ",")
        print("  but your working dir is " + os.getcwd())
        print()
        print("*** Ask a staff member to check your directory setup. ***")
        print()
else:
    right_dir=True
    print("The name of the working directory looks correct.\n")

filenames = ["verify_shell_location.py", "greetings.py",
              "last_task.py"]
test_results = []

for f in filenames:
    test_results.append(os.path.isfile(f))

if all(test_results):
    msg= "he working directory contains the necessary files."
    if right_dir:
        msg= "T"+msg+"\nHurrah!"
    else:
        msg= "Although its name is unexpected, t"+msg
    print(msg)
else:
    print("CS1110 problem: The directory seems to be missing at least one file.")
    print("Diagnostic info: ")
    for i in range(len(filenames)):
        print (filenames[i] + ": " + ("found" if test_results[i] else "not found"))
    print("\n*** Ask a staff member for help. ***")
