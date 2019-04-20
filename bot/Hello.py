from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class Module:
    MODULE_NAME = "Hello"
    MENU_TEXT = "Приветствие"

    def Request(self, step, event, module_num):
        if(step == 0):
            print("Работа в модуле привет")
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("Ура!!!!!!!!", color=VkKeyboardColor.DEFAULT)
            return 'Привет, я твой лучший друг', keyboard