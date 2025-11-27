# MaxCatcherV1

> **Note:** I am **not responsible for gallery-dl**. Please **do not
> open issues related to gallery-dl** here.
> MaxCatcher is only a wrapper and automation tool built on top of
> gallery-dl.

------------------------------------------------------------------------

## About

MaxCatcher is a simple **Python-based utility** designed to automate
bulk downloads using **gallery-dl** on Windows.
It allows you to archive multiple artist pages or tag-based galleries in
one run --- clean, fast, and fully automated.

### Features

-   Supports unlimited URLs
-   Automatically sorts and archives all downloaded files
-   12-hour automatic re-check and download cycle
-   Clear progress output directly in the terminal
-   Easy-to-edit Python configuration
-   Simple start/cancel prompt

------------------------------------------------------------------------

## How to Use

1.  **Download** the repository and extract `maxcatcher.py`.
2.  **Place** both `maxcatcher.py` and `gallery-dl.exe` in the same
    folder.
3.  **Edit** the URL section inside `maxcatcher.py` and insert your
    desired gallery or artist links:

``` py
urls = [
    "https://yourlink.here",
    "https://yourlink.here",
    "https://yourlink.here"
]
```

4.  **Open** a command prompt in the same folder.
5.  Start the script by running: `maxcatcher.py`

7.  Choose **1** to start or **2** to cancel.

*Optional tip: You can safely minimize the terminal --- the script will
continue running until the cycle completes.*

------------------------------------------------------------------------

## License

This project is licensed under the **Creative Commons Attribution 4.0
International License (CC BY 4.0)**.\
You may use, share, and adapt this script as long as proper credit is
given.

Full license text:\
https://creativecommons.org/licenses/by/4.0/
