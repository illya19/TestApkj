from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from random import randint

class WalletGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super(WalletGenerator, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        self.generate_button = Button(text='Сгенерировать кошелек', on_press=self.generate_wallet)
        self.add_widget(self.generate_button)

    def generate_wallet(self, instance):
        address = ''.join([chr(randint(65, 90)) for _ in range(4)])
        popup = Popup(title='Адрес кошелька', content=Label(text=f'Ваш адрес кошелька: {address}'), size_hint=(None, None), size=(400, 200))
        popup.open()

class WalletLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(WalletLogin, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        self.wallet_address_input = TextInput(hint_text='Введите адрес кошелька')
        self.pin_code_input = TextInput(hint_text='Введите пин-код', password=True)
        self.login_button = Button(text='Войти', on_press=self.login)

        self.add_widget(Label(text='Меню входа'))
        self.add_widget(self.wallet_address_input)
        self.add_widget(self.pin_code_input)
        self.add_widget(self.login_button)

    def login(self, instance):
        wallet_address = self.wallet_address_input.text
        pin_code = self.pin_code_input.text

        # Проверка адреса кошелька и пин-кода
        if wallet_address == 'сгенерированный_адрес' and pin_code == 'установленный_пин_код':
            self.parent.current = 'earning_menu'
        else:
            popup = Popup(title='Ошибка', content=Label(text='Неверный адрес кошелька или пин-код'), size_hint=(None, None), size=(400, 200))
            popup.open()

class EarningMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(EarningMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        self.earn_button = Button(text='Получить 1 TON', on_press=self.earn)
        self.invest_button = Button(text='Инвестировать в TON', on_press=self.invest)
        self.invest_amount_input = TextInput(hint_text='Введите сумму для инвестирования')

        self.add_widget(Label(text='Меню заработка'))
        self.add_widget(self.earn_button)
        self.add_widget(self.invest_button)
        self.add_widget(self.invest_amount_input)

    def earn(self, instance):
        # Логика для получения 1 TON
        pass

    def invest(self, instance):
        invest_amount = float(self.invest_amount_input.text)
        return_amount = invest_amount * 1.12  # Возврат с 12% прибылью

        popup = Popup(title='Инвестиция', content=Label(text=f'Ваша прибыль: {return_amount} TON'), size_hint=(None, None), size=(400, 200))
        popup.open()

class WalletApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        wallet_generator = WalletGenerator()
        wallet_login = WalletLogin()
        earning_menu = EarningMenu()

        root.add_widget(wallet_generator)
        root.add_widget(wallet_login)
        root.add_widget(earning_menu)

        return root

if __name__ == '__main__':
    WalletApp().run()