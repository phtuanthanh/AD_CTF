#!/usr/bin/env python3
import os,sys
import logging
import requests
from bs4 import BeautifulSoup

from lib.lib import BaseChecker, CheckResult, get_flag, set_flagid, load_state, run_check, store_state

PORT_SERVICE = 5000
TOKEN = ''
# IP='100.82.191.96'
class ExampleChecker(BaseChecker):
    def check_service(self):
        global TOKEN
        username = 'root'
        password = 'QsrXM&Tz)PxMq5,9C~!"QH8.3FGW8sD6'
        
        session = requests.Session()
        r = session.post(url="http://"+str(self.ip)+":"+str(PORT_SERVICE)+"/login", data={'username': username, 'password': password})

        if(r.status_code != 200):
            logging.warning('Login failed')
            return CheckResult.DOWN
        try:
            data = r.json()

            if data['success'] == False:
                logging.warning('Login failed')
                return CheckResult.FAULTY
            
            TOKEN =  r.headers.get('Set-Cookie', '')
            if TOKEN:
                parts = TOKEN.split(';')
                for part in parts:
                    if part.strip().startswith('jwt='):
                        TOKEN = part.strip()[len('jwt='):]
            else:
                logging.warning('No Set-Cookie header found')
        except ValueError:
            logging.warning('Invalid JSON response')
            return CheckResult.FAULTY
           
        logging.warning('Login successful, token: %s', TOKEN)
        return CheckResult.OK
    
    def place_flag(self, tick):
        global TOKEN
        flag = get_flag(tick)
        logging.warning(f"current of tick --> {flag}")
        r = requests.post(url="http://"+str(self.ip)+":"+str(PORT_SERVICE)+"/update_doc/12", data={'title': flag,'content':flag}, cookies={'jwt':TOKEN})

        if(r.status_code == 500):
            logging.warning('Not valid token')
            return CheckResult.DOWN
        if(r.status_code == 200):
            logging.warning('Flag placed successfully')
        return CheckResult.OK

    def check_flag(self, tick):
        global TOKEN
        flag = get_flag(tick)
        logging.warning(f"current of tick --> {flag}")
        r = requests.get(url="http://"+str(self.ip)+":"+str(PORT_SERVICE)+"/view_docs/12",cookies={'jwt':TOKEN})

        if(r.status_code == 403):
            logging.warning('Error')
            return CheckResult.FAULTY
        if(r.status_code == 500):
            logging.warning('Not valid token')
            return CheckResult.DOWN
        try:
            soup = BeautifulSoup(r.text, "html.parser")
            title = soup.find(class_="doc-title")
            flag_on_target = title.get_text(strip=True)
            logging.warning(f"flag on target --> {flag_on_target}")
            if( flag_on_target != flag):
                logging.warning('Flag not found')
                return CheckResult.FLAG_NOT_FOUND
        except UnicodeDecodeError:
            logging.warning('Error decoding HTML')
            return CheckResult.FAULTY
        return CheckResult.OK

if __name__ == '__main__':
    run_check(ExampleChecker)
