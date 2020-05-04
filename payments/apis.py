import requests
import base64
import datetime
from requests.auth import HTTPBasicAuth


class MpesaBase:
    def __init__(self, env="sandbox", app_key=None, app_secret=None, sandbox_url="https://sandbox.safaricom.co.ke",
                 live_url="https://safaricom.co.ke"):
        self.env = env
        self.app_key = app_key
        self.app_secret = app_secret
        self.sandbox_url = sandbox_url
        self.live_url = live_url
        self.token = None

    def authenticate(self):
        """
        **Args:**
            - env (str): Current app environment. Options: sandbox, live.
            - app_key (str): The app key obtained from the developer portal.
            - app_secret (str): The app key obtained from the developer portal.
            - sandbox_url (str): Base Safaricom sandbox url.
            - live_url (str): Base Safaricom live url.

        **Returns:**
            - access_token (str): This token is to be used with the Bearer header for further API calls to Mpesa.

        """
        if self.env == "production":
            base_safaricom_url = self.live_url
        else:
            base_safaricom_url = self.sandbox_url
        authenticate_uri = "/oauth/v1/generate?grant_type=client_credentials"
        authenticate_url = f"{base_safaricom_url}{authenticate_uri}"
        r = requests.get(authenticate_url,
                         auth=HTTPBasicAuth(self.app_key, self.app_secret))
        self.token = r.json()['access_token']
        return r.json()['access_token']


class C2B(MpesaBase):
    def __init__(self, env="sandbox", app_key=None, app_secret=None, sandbox_url=None, live_url=None):
        MpesaBase.__init__(self, env, app_key, app_secret,
                           sandbox_url, live_url)
        self.authentication_token = self.authenticate()

    def register(self, shortcode=None, response_type=None, confirmation_url=None, validation_url=None):
        """This method uses Mpesa's C2B API to register validation and confirmation URLs on M-Pesa.

        **Args:**
            - shortcode (int): The short code of the organization.
            - response_type (str): Default response type for timeout. Incase a tranaction times out,
                 Mpesa will by default Complete or Cancel the transaction.
            - confirmation_url (str): Confirmation URL for the client.
            - validation_url (str): Validation URL for the client.


        **Returns:**
            - OriginatorConverstionID (str): The unique request ID for tracking a transaction.
            - ConversationID (str): The unique request ID returned by mpesa for each request made
            - ResponseDescription (str): Response Description message


        """

        payload = {
            "ShortCode": shortcode,
            "ResponseType": response_type,
            "ConfirmationURL": confirmation_url,
            "ValidationURL": validation_url
        }
        headers = {'Authorization': f'Bearer {self.authentication_token}', 'Content-Type': "application/json"}
        if self.env == "production":
            base_safaricom_url = self.live_url
        else:
            base_safaricom_url = self.sandbox_url
        saf_url = f"{base_safaricom_url}/mpesa/c2b/v1/registerurl"
        r = requests.post(saf_url, headers=headers, json=payload)
        return r.json()

    def simulate(self, shortcode=None, command_id=None, amount=None, msisdn=None, bill_ref_number=None):
        """This method uses Mpesa's C2B API to simulate a C2B transaction.
        N/B. This method is only used in testing and development environment.

            **Args:**
                - shortcode (int): The short code of the organization.
                - command_id (str): Unique command for each transaction type.
                          CustomerPayBillOnline,CustomerBuyGoodsOnline.
                - amount (int): The amount being transacted
                - msisdn (int): Phone number (msisdn) initiating the transaction MSISDN(12 digits)
                - bill_ref_number: Optional


            **Returns:**
                - OriginatorConverstionID (str): The unique request ID for tracking a transaction.
                - ConversationID (str): The unique request ID returned by mpesa for each request made
                - ResponseDescription (str): Response Description message


        """

        payload = {
            "ShortCode": shortcode,
            "CommandID": command_id,
            "Amount": amount,
            "Msisdn": msisdn,
            "BillRefNumber": bill_ref_number
        }
        headers = {'Authorization': f'Bearer {self.authentication_token}', 'Content-Type': "application/json"}
        if self.env == "production":
            base_safaricom_url = self.live_url
        else:
            base_safaricom_url = self.sandbox_url
        saf_url = f"{base_safaricom_url}/mpesa/c2b/v1/simulate"
        r = requests.post(saf_url, headers=headers, json=payload)
        return r.json()


class MpesaExpress(MpesaBase):
    def __init__(self, env="sandbox", app_key=None, app_secret=None, sandbox_url=None, live_url=None):
        MpesaBase.__init__(self, env, app_key, app_secret,
                           sandbox_url, live_url)
        self.authentication_token = self.authenticate()

    def stk_push(self, business_shortcode=None, passcode=None, amount=None, callback_url=None,
        reference_code=None, phone_number=None, description=None):
        """This method uses Mpesa's Express API to initiate online payment on behalf of a customer..

        **Args:**
            - business_shortcode (int): The short code of the organization.
            - passcode (str): Get from developer portal
            - amount (int): The amount being transacted
            - callback_url (str): A CallBack URL is a valid secure URL that is used to
                receive notifications from M-Pesa API.
            - reference_code: Account Reference: This is an Alpha-Numeric parameter that is defined
                by your system as an Identifier of the transaction for CustomerPayBillOnline transaction type.
            - phone_number: The Mobile Number to receive the STK Pin Prompt.
            - description: This is any additional information/comment that can be sent along
                with the request from your system. MAX 13 characters


        **Returns:**
            - CustomerMessage (str):
            - CheckoutRequestID (str):
            - ResponseDescription (str):
            - MerchantRequestID (str):
            - ResponseCode (str):

        """

        time = str(datetime.datetime.now()).split(".")[0].replace(
            "-", "").replace(" ", "").replace(":", "")
        password = f"{str(business_shortcode)}{str(passcode)}{time}"
        encoded = base64.b64encode(password.encode())
        payload = {
            "BusinessShortCode": business_shortcode,
            "Password": encoded,
            "Timestamp": time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": int(phone_number),
            "PartyB": business_shortcode,
            "PhoneNumber": int(phone_number),
            "CallBackURL": callback_url,
            "AccountReference": reference_code,
            "TransactionDesc": description
        }
        headers = {'Authorization': f'Bearer {self.authentication_token}', 'Content-Type': "application/json"}
        if self.env == "production":
            base_safaricom_url = self.live_url
        else:
            base_safaricom_url = self.sandbox_url
        saf_url = f"{base_safaricom_url}/mpesa/stkpush/v1/processrequest")
        r=requests.post(saf_url, headers = headers, json = payload)
        return r.json()

    def query(self, business_shortcode = None, checkout_request_id = None, passcode = None):
        """This method uses Mpesa's Express API to check the status of a Lipa Na M-Pesa Online Payment..

        **Args:**
            - business_shortcode (int): This is organizations shortcode (Paybill or Buygoods - A 5 to 6
                 digit account number) used to identify an organization and receive the transaction.
            - checkout_request_id (str): This is a global unique identifier of the processed checkout
                transaction request.
            - passcode (str): Get from developer portal


        **Returns:**
            - CustomerMessage (str):
            - CheckoutRequestID (str):
            - ResponseDescription (str):
            - MerchantRequestID (str):
            - ResponseCode (str):


        """

        time=str(datetime.datetime.now()).split(".")[0].replace(
            "-", "").replace(" ", "").replace(":", "")
        password=f"{str(business_shortcode)}{str(passcode)}{time}"
        encoded=base64.b64encode(password.encode())
        payload={
            "BusinessShortCode": business_shortcode,
            "Password": encoded,
            "Timestamp": time,
            "CheckoutRequestID": checkout_request_id
        }
        headers = {'Authorization': f'Bearer {self.authentication_token}', 'Content-Type': "application/json"}
        if self.env == "production":
            base_safaricom_url = self.live_url
        else:
            base_safaricom_url = self.sandbox_url
        saf_url = f"{base_safaricom_url}/mpesa/stkpushquery/v1/query")
        r=requests.post(saf_url, headers = headers, json = payload)
        return r.json()
