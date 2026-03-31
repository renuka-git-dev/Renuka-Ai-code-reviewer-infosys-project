import reflex as rx
import requests
import random

class mystate(rx.state):
    quote=""
    author=""
    def get_quote(self):
        url="https://type.fit/api/quotes"
        res=requests.get(url)
        data = res.json()
        rand_num=random.randrange(0, len(data))
        self.quote=data[0]['text']
        self.author=data[0]['text']




























        def quote():
            return rx.box(
                rx.text(mystate.quote, font_weight="bold")
                rx.text(mystate.author)
            )