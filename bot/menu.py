from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import os


class Module:
    MODULE_NAME = "menu"
    MENU_TEXT = "Меню на сегодня"


def upl_img(filename):
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
        filename,
        album_id=260945181,
        group_id=181385414)
    vk_photo_url = 'https://vk.com/photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id'])
    return vk_photo_url


def get_menu(dt):
    os.getcwd()
    os.chdir('./menu/' + dt)
    photo_list = []
    for filename in os.listdir():
        photo_list += upl_img(filename)
    return photo_list

def Request(self, step, event, module_num):
    keyboard = VkKeyboard(one_time=True)
    return photo_list, None
