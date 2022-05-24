# pharm-scraper
Allows for scraping of prices for pharmaceutical sites

# Requirements

Before attempting to run, make sure all of the requirements specified by the requirements.txt file are installed in your environment. 

## Python Reqs

Mac:

```
python3 -m pip install --upgrade pip
# Create Virtual Environment in Root Level Folder of Repo
python3 -m venv env
source env/bin/activate
# Install Requirements
python3 -m pip install -r requirements.txt

```

Windows:
```
py -m pip install --upgrade pip
# Create Virtual Env
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
py -m pip install -r requirements.txt
```



Furthermore, you will need to install [ChromeDriver](https://chromedriver.chromium.org/downloads) for the operating system that will be running this script. The script assumes it is installed to the default PATH or within the root level of the repo. 

# Usage

In order to run script (once all requirements have been installed on machine), execute it by running the python script below:
```
python3 goodrx.py
python3 singlecare.py
```


