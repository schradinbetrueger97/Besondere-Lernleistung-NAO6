# OPTION 1
import rclpy

from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Int8

class CompleteConversation(Node):
    def __init__(self):
        super().__init__('complete_conversation')   # initiate object
        
        # initiate variable 'name'
        self.interaction_name = ""
        # initiate varaiable 'number_of_feeling'
        self.number_of_feeling = ""
        # initiate variable 'current_input_string'
        self.current_input_string = ""
        
        # spin head_touch_callback
        
        # spin greeting
        
        # spin greeting_answer
        # Heard into Variable 'name' | TYPKONVERTIERUNG
        # name = str()
        
        # spin thanks_giving
        
        # spin question
        
        # spin question_answer
        # Heard into variable 'number_of_feeling' | TYPKONVERTIERUNG
        
        # spin say_opinion
        
        # spin good_bye

    def head_touch_cb(self):
        # head_touch_sub = Subscriber()
        if
            # finish
        else
            # repeat
            
    def greeting(self):
        dialog_talker = rclpy.Publisher()
        # say 'Hallo ich bin der kleine humanoide Roboter NAO und ich würde gerne mit Ihnen eine kleine Konversation führen. Wie heißen Sie denn?'

    def greeting_answer(self):
       dialog_listener = ActionClient(self.current_input_string) # or dialog_listener = ActionClient()
       # needed:    listener_response_cb and listener_result_cb

    def thanks_giving(self):
        dialog_talker = rclpy.Publisher()
        # say 'Danke für die Antwort, <name>'
    
    def question(self):
        dialog_talker = rclpy.Publisher()
        # say 'Wie geht es Ihnen auf einer Skala von 1 bis 10? 1 wenn es ihnen schlecht geht und 10 wenn es Ihnen blendend geht.'

    def question_answer(self):
        dialog_listener = ActionClient(self.current_input_string)
        # needed:   listener_result_cb
        
        

    def say_opinion(self):
        if # number from 1 to 3
            dialog_talker = rclpy.Publisher() 
            # say 'Das ist aber schlecht. Die nächste Zeit wir bestimmt schöner für dich.'
        if # number from 4 to 6
            dialog_talker = rclpy.Publisher()  
            # say 'Das hört sich okay an. Das wird in nächster Zeit bestimmt besser.'  
        if # number from 7 to 10
            dialog_talker = rclpy.Publisher()
            # say 'Das freut mich zu hören. Hoffentlich bleibt das so.'
        else # repeat if anything else was spoken
            dialog_talker = rclpy.Publisher()
            # say 'Kannst du das bitte wiederholen, damit kann ich leider nicht arbeiten.'
            # go back to def question_answer

    def good_bye(self):
        dialog_talker = rclpy.Publisher()
        # say 'Danke für die nette Unterhaltung und bis bald <name>'
            

            
def main(args=None):
    rclpy.init(args=args)

    complete_conversation = CompleteConversation()

    rclpy.spin(complete_conversation)
    
    complete_conversation.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()