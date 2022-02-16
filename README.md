# duckduckgo.py
duckduckgo.py is a simple python module to scrape the duckduckgo search results. The ddg script can be used as a command line utility in a shell pipeline.

---
## Warning!
This code is intended as a demonstration and, as all scraping utilities, should be used with great caution. By default the code will pause a few milliseconds each time it yields a result to avoid overloading the DDG servers.

---
## Usage
```bash
git clone https://github.com/its0x08/duckduckgo
duckduckgo
chmod +x ddg
./ddg -h
usage: ddg [-h] [-n MAX_RESULTS] [-t [TIME]] keyword [keyword ...]

DuckDuckGo URL scraper by 0x08

positional arguments:
  keyword         search string

options:
  -h, --help      show this help message and exit
  -n MAX_RESULTS  number of results (default: all)
  -t [TIME]       execution time
```

Simple search
```bash
./ddg search something
```

Showing execution time by using `-t` flag and result number by using `-n [Num]`.
```bash
./ddg -n 10 -t search something
```
## TODO
* Add installer script
* 1) Install the project as cli tool
* 2) Install the project as python module
* Add -o to save output to file

## Contributors

If you decide to make a pull request to suggest your changes to the project, please dont forget to add your name to the CONTRIBUTING.md file.

## Pull Requests & Issues
You have a new feature in mind?
The code is buggy, wont run as expected and you happen to know __python__?
Please make a __Pull Request (_PR_)__ suggesting you changes.
Otherwise you can always open an __Issue__ to help imporve this project.