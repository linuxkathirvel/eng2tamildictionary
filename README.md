# eng2tamildictionary
English - Tamil Dictionary - Offline

# Steps to run
* ![Download](https://github.com/linuxkathirvel/eng2tamildictionary/archive/master.zip) or ![clone](https://github.com/linuxkathirvel/eng2tamildictionary.git)
* Open the ![english_to_tamil.html](english_to_tamil.html) file in Firefox browser
* Type english words
* Click the autocomplete word or press search button.
* Get tamil meaning.

# Source of dictionary
* English-Tamil-Dictionary.xls file from Tamil Nadu Free Laptop Scheme
* [University of Madras Dictionary](http://www.tamilvu.org/library/pmdictionary/html/madsind.htm)

# How it works
* xls file contents converted as [JSON file](dictionary.json) using [excel_to_html.py](excel_to_html.py) python script
* [english_to_tamil.html](english_to_tamil.html) is front page of Dictionary
* jQuery AJAX calling find the search words from [JSON file](dictionary.json) and finally Tamil meaning of english word displayed.

# Features
* Offline
* No Ads.
* [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) browser only enough

# Requirements
* [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)

# FAQ
* Can I use Google Chrome browser?
No. Google Chrome browser not support [JSON file](dictionary.json) reading using jQuery. JSON file is source of our Dictionary
* Internet connection needed?
No. It is an offlince Dictionary. [JSON file](dictionary.json) is a source of Dictionary
* How many words are available?
56855 words are available now. Number of words increase in future.

