from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json

TAGS = ["Бытовые", "Расписание", "Пересечение аудиторий", "Всякое"]
RANGS = ["Очень важно", "Важно", "Не важно"]


class Module:
    MODULE_NAME = "Issue"
    MENU_TEXT = "Пожаловаться"

    def Request(self, step, event, module_num):
        if step == 0:
            return "Выберете тип проблемы", self.keyboard_of_tags(module_num)
        if step == 1:
            return "Выберете важность проблемы"

    @staticmethod
    def keyboard_of_tags(module_num):
        keyboard = VkKeyboard(one_time=True)

        for tag in TAGS:
            keyboard.add_button(tag, color=VkKeyboardColor.DEFAULT,
                                payload=json.dumps({"module": module_num,
                                                    "step": 1,
                                                    "active": 1,
                                                    "tag": tag}))
            keyboard.add_line()

        return keyboard

    @staticmethod
    def keyboard_of_rangs(event):
        keyboard = VkKeyboard(one_time=True)

        for rang in RANGS:
            keyboard.add_button(rang, color=VkKeyboardColor.DEFAULT,
                                payload=json.dumps({
                                    "module": event.obj.payload.module,
                                    "step": 2,
                                    "active": 1,
                                    "tag": event.obj.payload.tag,
                                    "rang": rang
                                }))
            keyboard.add_line()

        return keyboard

