#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu July 29 2021

@author: imasimali
"""
# required libraries
import requests

data = {"entity_id":"95483450","platform":"web"}
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'origin': 'https://www.fiverr.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1'
}
requests.post('https://www.fiverr.com/transmitter/api/v1/online', json=data, headers=headers)
