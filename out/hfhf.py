# hfhf (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage



stage = Stage()
zombie = stage.add_a_sprite()

def doit(zombie: Sprite):
    for i in range(4):
        zombie.move(10)
        zombie.turn_left(90)
        zombie.wait(1)

zombie.when_program_starts(doit)
stage = Stage()
stage.add_backdrop(r'C:\Users\Admin\Downloads\CSAI\out\images\backdrop1.png')
stage.add_backdrop('/galaxy')
stage.create_variable('my variable')
stage.create_variable('NAME')
stage.show_variable("NAME")
stage.set_monitor_position("NAME", -235, 175)
retro_robot = stage.add_a_sprite(None)
retro_robot.set_name("Retro Robot")
retro_robot.set_x(-9)
retro_robot.set_y(23)
retro_robot.go_to_back_layer()
retro_robot.go_forward(1)
retro_robot.add_costume('/retro_robot_a', center_x=55.04000000000008, center_y=85.55)
retro_robot.add_costume('/retro_robot_b', center_x=50.49583299552708, center_y=87.39)
retro_robot.add_costume('/retro_robot_c', center_x=70.61999999999998, center_y=90.3795)
retro_robot.add_sound('/computer_beeps1')
retro_robot.add_sound('/computer_beeps2')

def when_this_sprite_clicked_1(self):
    "NO TRANSLATION: text2speech_setLanguage"
    "NO TRANSLATION: text2speech_setVoice"
    "NO TRANSLATION: text2speech_speakAndWait"
    self.say_for_seconds("Hello!", 2.0)
    "NO TRANSLATION: text2speech_speakAndWait"
    self.ask_and_wait("What's your name?")
    self.set_variable("NAME", self.answer())
    "NO TRANSLATION: text2speech_speakAndWait"
    self.say_for_seconds("".join(["Hello ", self.get_variable("NAME")]), 3.0)
    "NO TRANSLATION: text2speech_speakAndWait"
    self.ask_and_wait("What's your dream profession?")
    "NO TRANSLATION: text2speech_speakAndWait"
    self.say_for_seconds("Oww Nice to hear!", 2.0)
    "NO TRANSLATION: text2speech_speakAndWait"
    self.ask_and_wait("Have you taken any career assessments or personality tests?")
    if (self.answer() == "yes"):
        self.switch_costume_to("retro_robot_a")
        "NO TRANSLATION: text2speech_speakAndWait"
        self.say_for_seconds("Great! You achieve your first step to your career. ", 2.0)
        "NO TRANSLATION: text2speech_speakAndWait"
        self.ask_and_wait("how many points you gain?")
        "NO TRANSLATION: text2speech_speakAndWait"
        self.say_for_seconds("great!", 2.0)
    else:
        self.switch_costume_to("retro_robot_b")
        "NO TRANSLATION: text2speech_speakAndWait"
        self.say_for_seconds("i recommended you to do your assessment first!", 2.0)

    "NO TRANSLATION: text2speech_speakAndWait"
    self.ask_and_wait("in which standard you are studying?")
    "NO TRANSLATION: text2speech_speakAndWait"
    self.say_for_seconds("Great!", 2.0)
    if ((self.answer() == 8) and (self.answer() == 9)):
        self.switch_costume_to("retro_robot_c")
        "NO TRANSLATION: text2speech_speakAndWait"
        self.say_for_seconds("try trigonometry game! ", 2.0)
    else:
        "NO TRANSLATION: text2speech_speakAndWait"
        self.ask_and_wait("in which field you want to go?")
        if (self.answer() == "Science "):
            "NO TRANSLATION: text2speech_speakAndWait"
            self.ask_and_wait("In which group you want to go?  Group A or B")
            "NO TRANSLATION: text2speech_speakAndWait"
            self.say_for_seconds("Nice!", 2.0)
        else:
            "NO TRANSLATION: text2speech_speakAndWait"
            self.say_for_seconds("Nice!", 2.0)

retro_robot.when_this_sprite_clicked(when_this_sprite_clicked_1)

stage.play()

