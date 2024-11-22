Description This script is written in Python and aims to extract links (URLs) from a text file containing mixed data, such as texts and links, while removing any unwanted symbols that may be attached to the links (such as ], [, !, etc.). Clean links are saved in a new file.

#How the script works Read data: The script reads the contents of an input file (domins.txt) that contains mixed texts and links. Extracting links: Using regular expressions, the script identifies links. Link Cleanup: Removes any unwanted codes associated with links. Save results: Clean links are saved in a new file (all.txt).

#Requires Python 3.6 or later. An input file containing text and links (domins.txt).

#How to use

Preparing the script: Download the script and save it in a file named clean_links.py.
Create the input file: Create a file named domins.txt and put the text and links in it.
Run the script: Open a command line or terminal and navigate to the folder containing the script. Execute the following command to run the script:
python clean_links.py

#Conclusion: Before running the script, you need to create a file called domins.txt that will contain the links. After that, run the script with the python command clean_links.py. You will find a file named all.txt that contains the cleaned links.



   ## Usage:
    ```bash
    git clone https://github.com/zooka777/urlclen
    cd urlclen
    python --version
    pip install -r requirements.txt
    python clean_links.py

## Examples
![Nature View](https://i.imgur.com/YiuHq2i.png)
