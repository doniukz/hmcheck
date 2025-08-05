Toolname: hmcheck.py
===============================

Description:
---------
This tool checks which HTTP methods (GET, POST, PUT, DELETE, etc.) are supported by a given URL.  
It sends requests using different HTTP methods and shows which methods are allowed.

Requirements:
---------
- Python 3.x required
- Required libraries: urllib3, colorama

Install dependencies:
---------
pip install urllib3 colorama

Usage:
---------
python hmcheck.py -u <URL>

Arguments:
---------
-u, --url   The target URL to be tested.

Example:
---------
python hmcheck.py -u https://example.com

When pressing Ctrl+C (KeyboardInterrupt), the program exits gracefully with the message "User stopped".

License:
--------
Open source, free to use.

Author: doni

Images:
--------
<img width="689" height="292" alt="image" src="https://github.com/user-attachments/assets/58480f7f-6629-4375-a0d6-c1912becbdaa" />

