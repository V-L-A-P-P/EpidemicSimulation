import json


class StylesGetter:
    @staticmethod
    def get_error_coef_input_style():
        with open('Styles/error_coef_input_style.txt', 'r') as read_file:
            style_text = read_file.read()
        return style_text

    @staticmethod
    def get_init_coef_input_style():
        with open('Styles/init_coef_input_style.txt', 'r') as read_file:
            style_text = read_file.read()
        return style_text

    @staticmethod
    def get_error_people_input_style():
        with open('Styles/error_people_input_style.txt', 'r') as read_file:
            style_text = read_file.read()
        return style_text

    @staticmethod
    def get_init_people_input_style():
        with open('Styles/init_people_input_style.txt', 'r') as read_file:
            style_text = read_file.read()
        return style_text
