#!/usr/bin/env python

import sys
import threading

from persistqueue import Queue
from stockfish.models import Stockfish

from stockbird.api import TwitterAPI
from stockbird.cli_access import cli_access
from stockbird.config import logger
from stockbird.get_mentions import get_mentions_factory
from stockbird.handle_tweets import handle_tweets_factory


def __init__(api, tweet_queue, stockfish, args: str = None):
    if args == "cli":
        cli_access(api)

    mention_getter = threading.Thread(
        target=get_mentions_factory(api, tweet_queue)
    )
    tweet_handler = threading.Thread(
        target=handle_tweets_factory(api, tweet_queue, stockfish)
    )
    mention_getter.start()
    tweet_handler.start()


if __name__ == "__main__":
    api = TwitterAPI().api
    tweet_queue = Queue(".queues/queue")
    stockfish = Stockfish()

    try:

        if len(sys.argv) > 1:
            __init__(
                api=api,
                tweet_queue=tweet_queue,
                stockfish=stockfish,
                args=sys.argv[1],
            )

        else:
            __init__(api=api, tweet_queue=tweet_queue, stockfish=stockfish)

    except KeyboardInterrupt:
        logger.warn("\nExiting.")
        sys.exit(0)
