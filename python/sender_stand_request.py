import configuration
import requests
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)


def get_order_by_track(track):
    params = {
        "t": track
    }

    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=params,
                        headers=data.headers)
