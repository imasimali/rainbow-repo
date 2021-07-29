[![fiverr-pinger](https://github.com/imasimali/rainbow-fiverr-ping/actions/workflows/fiverr-pinger.yml/badge.svg?branch=main)](https://github.com/imasimali/rainbow-fiverr-ping/actions/workflows/fiverr-pinger.yml)

# covid-19-san-juan  

This repository contains a python script to scrape the "Coronavirus Module" maintained by the Government of San Juan Province, in Argentina. Link: https://sisanjuan.gob.ar/modulo-coronavirus  

This module shows information about coronavirus cases in San Juan Province, Argentina. The scraper runs dialy at 09:00 UTC-3 using GitHub Actions, retrieves the information, and saves it to a csv file.

Content:  

* `sj-gobierno.py`: python script that performs the scraping and saves the data to a csv file.  

* `requirements.txt`: holds a list with the requiered libraries to run the python script. It is used to install these libraries in the GitHub runner.

* `data/covid-san-juan.csv`: new data is saved here after each daily run.

Full details in blogpost: https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/
