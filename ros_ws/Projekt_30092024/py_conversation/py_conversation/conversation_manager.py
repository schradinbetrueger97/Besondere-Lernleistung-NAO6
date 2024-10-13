import rclpy
import time

from rclpy.node import Node
from rclpy.action import ActionClient

from std_msgs.msg import String
from naoqi_bridge_msgs.action import Listen
from naoqi_bridge_msgs.msg import HeadTouch


class DialogManagerNode(Node):
    def __init__(self):
        super().__init__("dialog_manager_node")
       
        # initiate variable 'name'
        self.interaction_name = ""
        # initiate varaiable 'number_of_feeling'
        self.number_of_feeling = ""
        # initiate variable 'current_input_string'
        self.current_input_string = ""
        
        self.dialog_talker = rclpy.Publisher(String, "speech", 10) # published zu sprechenden Text        
        self.dialog_listener = ActionClient(self, Listen) # liefert gehörten Text
        
        self.head_touch_sub = rclpy.Subscriber(HeadTouch, "", self.head_touch_cb, 10) # schaut, ob knopf am kopf gedrückt wurde
        
    def head_touch_cb(self, msg: HeadTouch):
        # HIER IST DEIN EINSTIEGSPUNKT!
        # NAOs KOPF WURDE BERÜHRT!
        if msg.state == HeadTouch.STATE_RELEASED:
            self.fuehre_unterhaltung()
        
    def listener_response_cb(self, future):
        # HIER BEKOMMST DU INFORMATION DARÜBER OB 
        # ACTION ANGELAUFEN IST
        # ALSO OB NAO ZUHÖRT
        # hinzufügen von result_cb

        goal_handle = future.result()
        if not goal_handle.accepted:
            nao_excuse_text = "Es tut mir leid, aber ich kann derzeitig nicht zuhören."
            nao_excuse_msg = String()
            nao_excuse_msg.data = nao_excuse_text
            self.dialog_talker.publish(nao_excuse_msg)
            return
        
        self.answer_goal_future = goal_handle.get_result_async()
        self.answer_goal_future.add_done_callback(self.listener_result_cb) 


        
    def listener_result_cb(self, future):
        # HIER KOMMT DAS EIGENTLICHE ERGEBNIS AN
        
        # prüfe ob das ergebnis valide ist
        # speichere den text aus dem Ergebnis ab
        # ---> in self.current_input_string
        # meine_variable = (parameter.funktion).Attribut    |   (parameter.funktion)   = Objekt
        result_obj = future.result()     
        result = result_obj.result
        verstandener_text = result[0]
        # check substring for "ich heiße"
        if "ich heiße" in str.lower(verstandener_text):          # str.lower --> alle Buchstaben klein
            self.interaction_name = self.filter_name(str.lower(verstandener_text))
            # weiterleiten zu: self.fuehre_unterhaltung_weiter
            self.fuehre_unterhaltung_weiter()

        if "mir geht es" in str.lower(verstandener_text):
            self.number_of_feeling = self.filter_number(str.lower(verstandener_text))
            self.fuehre_unterhaltung_weiter2()

            
    def filter_name(self, text):
       # filtere den namen aus self.current_input_string und speichere in self.interaction_name
       return text.replace("ich heiße ", "")
       
    def filter_number(self, text):
        # filter den namen aus self.current_input_string und speicher in self.number_of_feeling
        self.get_logger().info(f"Filter Nummer aus Text: {text}")
        return text.replace("mir geht es ", "")
        
    
    def fuehre_unterhaltung(self):
        # greeting()
        greeting_text = "Hallo ich bin NAO. Wie heißt du denn?"
        greeting_msg = String()
        greeting_msg.data = greeting_text
        self.dialog_talker.publish(greeting_msg)
        # warte bis NAO den Text gesagt hat
        time.sleep(5)

        # greeting_answer() # hier ist interaktion mit dem action client dialog_listener
        # hier steht dann irgendwas in self.current_input_string
        # -> bearbeite self.current_input_string

        answer_goal = Listen.Goal()
        answer_goal.expected = []
        answer_goal.language = "de" 

        self.dialog_listener.wait_for_server()
        self.answer_future = self.dialog_listener.send_goal_async(answer_goal)

        self.answer_future.add_done_callback(self.listener_response_cb)

    def fuehre_unterhaltung_weiter(self):
        
        thanks_giving_text = f"Danke für die Antwort {self.interaction_name}"               # f vor String ruft .format auf
        thanks_giving_msg = String()
        thanks_giving_msg.data = thanks_giving_text
        self.dialog_talker.publish(thanks_giving_msg)

        time.sleep(2)

        self.question_feeling()

    def question_feeling(self):
        question_text = "Wie geht es dir auf einer Skala von 1 bis 10? 1 steht dabei für sehr schlecht und 10 für sehr gut."
        question_msg = String()
        question_msg.data = question_text
        self.dialog_talker.publish(question_msg)

        time.sleep(6)

        answer_goal = Listen.Goal
        answer_goal.expected = []
        answer_goal.language = "de"

        self.dialog_listener.wait_for_server()
        self.answer_future = self.dialog_listener.send_goal_async(answer_goal)

        self.answer_future.add_done_callback(self.listener_response_cb)

    def fuehre_unterhaltung_weiter2(self):
        opinion_number = int(self.number_of_feeling)
        opinion_msg = String()

        if opinion_number > 0 and opinion_number <= 3:
            opinion_text = "Das ist aber schlecht. Die nächste Zeit wir bestimmt schöner für dich."
        if opinion_number > 3 and opinion_number <= 6:
            opinion_text = "Das hört sich okay an. Das wird in nächster Zeit bestimmt besser."
        if opinion_number > 6 and opinion_number <= 10:
            opinion_text = "Das freut mich zu hören. Hoffentlich bleibt das so."
        if opinion_number <= 0 or opinion_number > 10:
            opinion_text = "Es tut mir leid, die gesagte Zahl ist nicht verständliche. Vielleicht mal deutlicher Reden."
            opinion_msg.data = opinion_text
            self.dialog_talker.publish(opinion_msg)
            time.sleep(5)
            self.question_feeling()
        
        opinion_msg.data = opinion_text
        self.dialog_talker.publish(opinion_msg)

        time.sleep(5)

        good_bye_text = "Danke für die nette Unterhaltung und bis bald!"
        good_bye_msg = String()
        good_bye_msg.data = good_bye_text
        self.dialog_talker.publish(good_bye_msg)

        


def main(args=None):
    rclpy.init(args=args)

    dialog_manager_node = DialogManagerNode()

    rclpy.spin(dialog_manager_node)
    
    dialog_manager_node.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()