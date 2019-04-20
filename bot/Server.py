import vk_api
import sys
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json

# Указываем ключи доступа, id группы и версию API
VK_API_ACCESS_TOKEN = 'a37fb7dc758520b0f40d3257f62a88bab60ac8ac7c3ea1a54095e35024c07b25b967795d096e78373d63b'
VK_API_GROUP_ID = 181385414



def main():
    """ Пример использования bots longpoll
        https://vk.com/dev/bots_longpoll
    """
    module_mas = []
    module_mas.append(addFile("Hello"))
    module_mas.append(addFile("qa"))
    module_mas.append(addFile("menu"))

    vk_session = vk_api.VkApi(token=VK_API_ACCESS_TOKEN)
    vk = vk_session.get_api()

    longpoll = VkBotLongPoll(vk_session, VK_API_GROUP_ID)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')

            print(event.obj.from_id)

            print('Текст:', event.obj.text)
            print('Кнопка:', event.obj.payload)
            print()

            mes, key, attachment = status(event, module_mas, vk_session)
            print(attachment)
            if(key == None and attachment == None):
                vk.messages.send(
                    peer_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=mes
                )

            if(key != None and attachment == None):
                vk.messages.send(
                    peer_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=mes,
                    keyboard = key.get_keyboard()
                )

            if(key == None and attachment != None):
                vk.messages.send(
                    peer_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=mes,
                    attachment=attachment
                )

            if (key != None and attachment != None):
                vk.messages.send(
                    peer_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=mes,
                    attachment=attachment,
                keyboard = key.get_keyboard()
                )

        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print('Новое сообщение:')

            print('От меня для: ', end='')

            print(event.obj.peer_id)

            print('Текст:', event.obj.text)
            print('Прикреплено', event.obj.attachment)
            print()

        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print('Печатает ', end='')

            print(event.obj.from_id, end=' ')

            print('для ', end='')

            print(event.obj.to_id)
            print()

        elif event.type == VkBotEventType.GROUP_JOIN:
            print(event.obj.user_id, end=' ')

            print('Вступил в группу!')
            print()

        elif event.type == VkBotEventType.GROUP_LEAVE:
            print(event.obj.user_id, end=' ')

            print('Покинул группу!')
            print()

        else:
            print(event.type)
            print()

def status(event, module_mas, vk_session):
    if(event.obj.payload != None):
        print("Есть ответ от кнопки")
        js = json.loads(event.obj.payload)
        print(js)
        #Исполняемая кнопка
        if(js["active"] == 1):
            print(js["module"]) #Debug
            return module_mas[js["module"]].Request(js['step'], event, js["module"], vk_session)
        if(js["active"] == 2):
            return menu(module_mas)
    else:
        print("Кнопка не нажата")
        return menu(module_mas)

def menu(module_mas):
    keyboard = VkKeyboard(one_time=True)
    print(module_mas)
    i = 0
    for module in module_mas:
        keyboard.add_button(module.MENU_TEXT, color=VkKeyboardColor.DEFAULT, payload=json.dumps({"module":i, "step":0, "active":1}))
        if(i < len(module_mas) - 1):
            keyboard.add_line()
        i+=1
    print("Клавиатура создана")
    return "Привет, выбери вариант", keyboard, None

def addFile(name):
    print(sys.path)
    sys.path.append(sys.path[0] + "/" + name + ".py")
    moduleImport = __import__(name)
    sys.path.remove(sys.path[0] + "/" + name + ".py")

    module = moduleImport.Module()
    return module


if __name__ == '__main__':
    main()

