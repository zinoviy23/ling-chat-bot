import webbrowser
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json

class Module:
    MODULE_NAME = "qa"
    MENU_TEXT = "Почемучник"



    def Request(self, step, event, module_num):

        def add_url(ans):
            if ans == 'Про Вышку':
                return 'abouthse'
            if ans == 'Про учебу':
                return 'aboutstudy'
            if ans == 'Про науку':
                return 'science'
            if ans == 'Жизнь в Вышке':
                return 'life'
            if ans == 'Мировая Вышка':
                return 'world'
            if ans == 'Взгляд в будущее':
                return 'prospection'
            if ans == 'Волонтерство и благотворительность':
                return 'charity'
            if ans == 'Студенческая жизнь':
                return 'studlife'
            if ans == 'Будь в курсе':
                return 'inet'

        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Про Вышку', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Про учебу', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Про науку', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Жизнь в Вышке', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Мировая Вышка', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Взгляд в будущее', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Волонтерство и благотворительность', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Студенческая жизнь', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Будь в курсе', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 2}))

        if(step):
            url = 'https://www.hse.ru/pochemuchnik2018/'
            url += add_url(event.obj.text)

            return url, keyboard

        else:

            return "Выберите раздел", keyboard

