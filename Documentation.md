# Welcome to **MaxcatcherDL** -- The Windows Port of *MarecatcherDL*

This documentation aims to give you a clear, personal, yet professional
overview of what **maxcatcherdl.py** does and how to use it effectively.

------------------------------------------------------------------------

## Requirements

-   **Python 3** (easily installable via [Ninite](https://ninite.com/python-python3-pythonx3/))
-   **maxcatcherdl.py**
-   **gallery-dl.exe** (can be downloaded at [Github](https://github.com/mikf/gallery-dl?tab=readme-ov-file#standalone-executable))

------------------------------------------------------------------------

## Purpose of This Software

Maxcatcher is a Python script that allows you to download and archive
files from websites like *e621* in full resolution and in clean,
organized folders.\
The script relies on Gallery-DL as its download engine.\
With a proper Maxcatcher setup, you can archive as many artists as you
want simultaneously.

------------------------------------------------------------------------

## How to Run the Software

After installing Python, place both `gallery-dl.exe` and `maxcatcher.py`
in the same folder. This folder will also be the destination where all
downloaded files will be stored.

Next, decide which artists you want to archive.\
For this example, we'll use three e621 artists: **BnBigus, Whygena, and
Haltie**.\
Search for their artist tags on e621 and copy the URLs:

-   https://e621.net/posts?tags=bnbigus
-   https://e621.net/posts?tags=whygena
-   https://e621.net/posts?tags=haltie

Open `maxcatcher.py` with a text editor and insert them into the URL
section:

``` py
# Define the URLs you wanna download here!
urls = [
    "https://e621.net/posts?tags=bnbigus",
    "https://e621.net/posts?tags=whygena",
    "https://e621.net/posts?tags=haltie"
]
```

Example of correct multi-line usage:

``` py
urls = [
    "https://e621.net/posts?tags=bnbigus",
    "https://e621.net/posts?tags=whygena",
    "https://e621.net/posts?tags=haltie",
    "https://e621.net/posts?tags=punkinbuu",
    "https://e621.net/posts?tags=dripponi"
]
```

Save the file --- you're ready to begin catching Max.

------------------------------------------------------------------------

## Starting Maxcatcher via Command Line

Open the folder where Maxcatcher and Gallery-DL are located.\
Open a command prompt in that directory (by typing `cmd` into the path
bar) or navigate manually via `cd`.

Start the script:

    maxcatcherdl.py

Choose **1** to start scraping.\
Press `CTRL + C` to stop at any time.

Once finished, the script sleeps for 12 hours.\
Exit the loop with `CTRL + C`.

------------------------------------------------------------------------

I hope this script brings you some joy. Archive the content you care
about --- artists can delete their work at any time.

**(C) All rights reserved. Maxcatcher --- a Windows port of Marecatcher
by fuchs.gay**
