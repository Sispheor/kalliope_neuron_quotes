import json
import logging

import requests

from kalliope.core import NeuronModule

logging.basicConfig()
logger = logging.getLogger("kalliope")

QUOTE_API_URL = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"


class Quotes(NeuronModule):

    def __init__(self, **kwargs):
        super(Quotes, self).__init__(**kwargs)

        r = requests.get(url=QUOTE_API_URL)

        self.content = r.content
        # we try to load into a json object the content. So Kalliope can use it to talk
        try:
            self.content = json.loads(self.content.decode())

            message = {
                "quote_text": str(self.content["quoteText"]),
                "quote_author": str(self.content["quoteAuthor"])
            }

            logger.debug("[quotes] %s" % message)

            self.say(message)

        except ValueError:
            logger.debug(self.neuron_name + "cannot get a valid json from returned content")
            pass
