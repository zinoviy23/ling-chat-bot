from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import os
import vk_api
import datetime

class Module:
    MODULE_NAME = "menu"
    MENU_TEXT = "Меню на сегодня"

     #photo181385414_456239024
    def Request(self, step, event, module_num, vk_session):

        return "Меню на сегодня:", None, "https//www.yandex.ru"
