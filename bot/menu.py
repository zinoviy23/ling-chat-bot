import webbrowser
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json

class Module:
    MODULE_NAME = "menu"
    MENU_TEXT = "Меню на сегодня"



    def Request(self, step, event, module_num, vk_session):

        def get_menu(ans):
            if ans == 'Холодные закуски':
                return '''Салат из моркови с сыром, Винегрет овощной, 
Салат из огурцов с томатами, салатом Айсберг и домашней заправкой,
Редька по-корейски, Салат из крабовых палочек с огурцом, кукурузой и майонезом,
Салат "Оливье" с колбасой '''
            if ans == 'Первые блюда':
                return '''Суп-пюре из курицы, Бульон куриный натуральный с 
яйцом'''
            if ans == 'Вторые блюда':
                return '''Цыпленок с овощами и соусом Терияки, Рыба жареная,
Тефтели "Ежики"/Hedgehog Meatballs, Котлета "Пожарская"'''
            if ans == 'Гарниры':
                return '''Гречка отварная, Картофель жареный, Овощи отварные'''
            if ans == 'Диетические блюда':
                return '''Куриные окорочка отварные, Щи зеленые постные'''
            if ans == 'Овощное (вегетарианское блюдо)':
                return '''Рис с овощами'''
            if ans == 'Напитки':
                return '''Напиток из ананасов с ягодами'''

        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Холодные закуски', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Первые блюда', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Вторые блюда', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Гарниры', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Диетические блюда', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Овощное (вегетарианское блюдо)', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))

        keyboard.add_line()
        keyboard.add_button('Напитки', color=VkKeyboardColor.DEFAULT,
                            payload=json.dumps({"module": module_num, "step": 1, "active": 1}))


        if(step):
            text = get_menu(event.obj.text)
            return text, keyboard, None

        else:

            return "Меню на сегодня", keyboard, None


