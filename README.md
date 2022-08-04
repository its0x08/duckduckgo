# DuckDuckGo URL scraper v0.0.1-beta
duckduckgo.py is a simple python module to scrape the duckduckgo search results. The ddg script can be used as a command line utility in a shell pipeline.

---
## Warning!
This code is intended as a demonstration and, as all scraping utilities, should be used with great caution. By default the code will pause a few milliseconds each time it yields a result to avoid overloading the DDG servers.

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fits0x08%2Fduckduckgo&countColor=%232ccce4&style=flat-square)
[![CodeQL](https://github.com/its0x08/duckduckgo/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/its0x08/duckduckgo/actions/workflows/codeql-analysis.yml)
[![Semgrep](https://github.com/its0x08/duckduckgo/actions/workflows/semgrep.yml/badge.svg?branch=main)](https://github.com/its0x08/duckduckgo/actions/workflows/semgrep.yml)
[![Pylint](https://github.com/its0x08/duckduckgo/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/its0x08/duckduckgo/actions/workflows/pylint.yml)
[![Codacy Security Scan](https://github.com/its0x08/duckduckgo/actions/workflows/codacy.yml/badge.svg?branch=main)](https://github.com/its0x08/duckduckgo/actions/workflows/codacy.yml)

---
## Usage
```bash
git clone https://github.com/its0x08/duckduckgo
cd duckduckgo
python ddg.py -h
usage: ddg.py [-h] [-n MAX_RESULTS] [-t] [-o FILE_OUTPUT] keyword

DuckDuckGo URL scraper by 0x08

positional arguments:
  keyword         search string

options:
  -h, --help      show this help message and exit
  -n MAX_RESULTS  number of results (default: all)
  -t              execution time (default: False)
  -o FILE_OUTPUT  save output to file
```

Simple search
```bash
python ddg.py search something
```

Showing execution time by using `-t` flag and result number by using `-n [Num]`.
```bash
python ddg.py -n 10 -t search something
```

Save output to file by using `-o` flag.
```bash
python ddg.py -n 10 -o output_file.log search something
```

## TODO
- [ ] Add installer script
- [x] ~~Add `-o` to save output to file~~

## Contributors

If you decide to make a pull request to suggest your changes to the project, please don't forget to add your name to the CONTRIBUTING.md file.

## Pull Requests & Issues
You have a new feature in mind?

The code is buggy, wont run as expected and you happen to know __python__?

Please make a __Pull Request (_PR_)__ suggesting you changes.

Otherwise you can always open an __Issue__ to help improve this project.
