"""stores the yelp api client id and api key in a separate file for security and best practice"""

def return_api_key():
    """returns api key for yelp api"""
    api_key = 'uNl2P8lCIz4hbsCFkMQLXIFl0I1Uik1jhztfQm93ptZ6n7ZeMMW0HryRudDxRetw5Az9L-7ckY-DNmcDi0WQz_CYTHi7Jd13Zn4lHzl2hpQyZAS-MaVPcsl6AmlIXXYx'
    return api_key

def return_client_id():
    """returns client id for yelp api"""
    client_id = 'N00975Ig6_mX73MHGdtVUA'
    return client_id
print(__name__)
if __name__ == '__main__':
    print('in main')
    print(return_api_key())
