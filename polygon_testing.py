import time
from polygon import WebSocketClient, STOCKS_CLUSTER, RESTClient
from keys import polygon_key


def my_custom_process_message(message):
    print("this is my custom message processing", message)


def my_custom_error_handler(ws, error):
    print("this is my custom error handler", error)


def my_custom_close_handler(ws):
    print("this is my custom close handler")


def main():
    key = polygon_key

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.stocks_equities_grouped_daily(locale = "us", market = "stocks", date = "2021-06-11")
        for i in range(resp.queryCount):
            print(f"On: {resp.results[i]['t']} {resp.results[i]['T']} opened at {resp.results[i]['o']} and closed at {resp.results[i]['c']}")


if __name__ == "__main__":
    main()