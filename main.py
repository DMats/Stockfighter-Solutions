#! /usr/bin/env python3

import requests

# Only valid for the current session.  Update each time you log in.
temporary_api_key = 'd7e69a55ef9610caa9a94a97af07c514e8ac4020'
account_number = 'SLM53886878'
stock_symbol = ''
venue_symbol = ''

base_url = 'https://api.stockfighter.io/ob/api'