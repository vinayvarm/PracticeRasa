# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.save_data import save_data, store_data


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        firstname=tracker.get_slot('firstname')
        # dispatcher.utter_message(text= f"thanks {fullname} for submitting details we asked")

        product = tracker.get_slot('product')
        email= tracker.get_slot('email')
        store_data(firstname,product,email)


        # save_data(firstname,product,email)




        return []
