#!/usr/bin/python3

class Say:
    def coucou(self):
        self._say("coucou")

    def helloWorld(self):
        self._say("Hello world!")

    def _say(self, text: str):
        print(f"I say {text}")