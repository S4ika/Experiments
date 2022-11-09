from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Play'
            on_press: root.manager.current = 'settings'

        Button:
            text: 'Quit'
            on_press : app.stop()

<SettingsScreen>:
    BoxLayout:
        GridLayout:
            rows:3
            Button:
                text: 'TicTacToe 3x3'
                on_press: root.manager.current = 'tictactoe'
            Button:
                text: 'TicTacToe 4x4'
                on_press: root.manager.current = 'tictactoe4'
            Button:
                text: 'TicTacToe 5x5'
                on_press: root.manager.current = 'tictactoe5'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'

<TicTacToe>:
    button_1 : button_1
    button_2 : button_2
    button_3 : button_3
    button_4 : button_4
    button_5 : button_5
    button_6 : button_6
    button_7 : button_7
    button_8 : button_8
    button_9 : button_9

    BoxLayout:
        GridLayout:
            rows: 3
            Button:
                id:button_1
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(1)
            Button:
                id:button_4
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(4)
            Button:
                id:button_7
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(7)
        GridLayout:
            rows: 3
            Button:
                id:button_2
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(2)
            Button:
                id:button_5
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(5)
            Button:
                id:button_8
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(8)
        GridLayout:
            rows: 3
            Button:
                id:button_3
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(3)
            Button:
                id:button_6
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(6)
            Button:
                id:button_9
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(9)

        GridLayout:
            rows: 3
            Button:
                text: "Restart"
                on_press: root.restart()

            Button:
                text: "Start game"
                on_press: root.start_game()


            Button:
                text: 'Change grid'
                on_press: root.manager.current = 'settings'

<TicTacToe4x4>
    button_1 : button_1
    button_2 : button_2
    button_3 : button_3
    button_4 : button_4
    button_5 : button_5
    button_6 : button_6
    button_7 : button_7
    button_8 : button_8
    button_9 : button_9
    button_10 : button_10
    button_11 : button_11
    button_12 : button_12
    button_13 : button_13
    button_14 : button_14
    button_15 : button_15
    button_16 : button_16

    BoxLayout:
        GridLayout:
            rows: 4
            Button:
                id:button_1
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(1)
            Button:
                id:button_5
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(5)
            Button:
                id:button_9
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(9)
            Button:
                id:button_13
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(13)
        GridLayout:
            rows: 4
            Button:
                id:button_2
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(2)
            Button:
                id:button_6
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(6)
            Button:
                id:button_10
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(10)
            Button:
                id:button_14
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(14)
        GridLayout:
            rows: 4
            Button:
                id:button_3
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(3)
            Button:
                id:button_7
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(7)
            Button:
                id:button_11
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(11)
            Button:
                id:button_15
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(15)
        GridLayout:
            rows: 4
            Button:
                id:button_4
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(4)
            Button:
                id:button_8
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(8)
            Button:
                id:button_12
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(12)
            Button:
                id:button_16
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(16)

        GridLayout:
            rows: 3
            Button:
                text: "Restart"
                on_press: root.restart()

            Button:
                text: "Start game"
                on_press: root.start_game()


            Button:
                text: 'Change grid'
                on_press: root.manager.current = 'settings'

<TicTacToe5x5>
    button_1 : button_1
    button_2 : button_2
    button_3 : button_3
    button_4 : button_4
    button_5 : button_5
    button_6 : button_6
    button_7 : button_7
    button_8 : button_8
    button_9 : button_9
    button_10 : button_10
    button_11 : button_11
    button_12 : button_12
    button_13 : button_13
    button_14 : button_14
    button_15 : button_15
    button_16 : button_16
    button_17 : button_17
    button_18 : button_18
    button_19 : button_19
    button_20 : button_20
    button_21 : button_21
    button_22 : button_22
    button_23 : button_23
    button_24 : button_24
    button_25 : button_25

    BoxLayout:
        GridLayout:
            rows: 5
            Button:
                id:button_1
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(1)
            Button:
                id:button_6
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(6)
            Button:
                id:button_11
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(11)
            Button:
                id:button_16
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(16)
            Button:
                id:button_21
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(21)
        GridLayout:
            rows: 5
            Button:
                id:button_2
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(2)
            Button:
                id:button_7
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(7)
            Button:
                id:button_12
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(12)
            Button:
                id:button_17
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(17)
            Button:
                id:button_22
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(22)
        GridLayout:
            rows: 5
            Button:
                id:button_3
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(3)
            Button:
                id:button_8
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(8)
            Button:
                id:button_13
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(13)
            Button:
                id:button_18
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(18)
            Button:
                id:button_23
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(23)
        GridLayout:
            rows: 5
            Button:
                id:button_4
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(4)
            Button:
                id:button_9
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(9)
            Button:
                id:button_14
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(14)
            Button:
                id:button_19
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(19)
            Button:
                id:button_24
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(24)
        GridLayout:
            rows: 5
            Button:
                id:button_5
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(5)
            Button:
                id:button_10
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(10)
            Button:
                id:button_15
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(15)
            Button:
                id:button_20
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(20)
            Button:
                id:button_25
                color :(0, 0, 0, 1)
                font_size:24
                disabled:False
                on_press:root.tic_tac_toe(25)

        GridLayout:
            rows: 3
            Button:
                text: "Restart"
                on_press: root.restart()

            Button:
                text: "Start game"
                on_press: root.start_game()


            Button:
                text: 'Change grid'
                on_press: root.manager.current = 'settings'
""")



# Declare both screens
class TicTacToe(Screen):
    def restart(self):
        self.switch = True

        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""
            button.disabled = False




    def tic_tac_toe(self, arg):
        self.buttons[arg - 1].disabled = True
        self.buttons[arg - 1].text = 'X' if self.switch else 'O'
        self.switch = not self.switch

        coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
            (0, 4, 8), (2, 4, 6),  # D
        )

        vector = lambda item: [self.buttons[x].text for x in item]

        color = [0, 1, 0, 1]

        for item in coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break

    def start_game(self):
        self.switch = True
        self.buttons = []
        self.buttons.append(self.button_1)
        self.buttons.append(self.button_2)
        self.buttons.append(self.button_3)
        self.buttons.append(self.button_4)
        self.buttons.append(self.button_5)
        self.buttons.append(self.button_6)
        self.buttons.append(self.button_7)
        self.buttons.append(self.button_8)
        self.buttons.append(self.button_9)



class TicTacToe4x4(Screen):
    def restart(self):
        self.switch = True

        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""
            button.disabled = False

    def tic_tac_toe(self, arg):
        self.buttons[arg - 1].disabled = True
        self.buttons[arg - 1].text = 'X' if self.switch else 'O'
        self.switch = not self.switch

        coordinate = (
            (0, 1, 2), (1, 2, 3), (4, 5, 6), (5, 6, 7), (8, 9, 10), (9, 10, 11), (12, 13, 14), (13, 14, 15),  # X
            (0, 4, 8), (4, 8, 12), (1, 5, 9), (5, 9, 13), (2, 6, 10), (6, 10, 14), (3, 7, 11), (7, 11, 15),  # Y
            (0, 5, 10), (5, 10, 15), (1, 6, 11), (4, 9, 14), (2, 5, 8), (3, 6, 9), (6, 9, 12), (7, 10, 13),  # D
        )

        vector = lambda item: [self.buttons[x].text for x in item]

        color = [0, 1, 0, 1]

        for item in coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break

    def start_game(self):
        self.switch = True
        self.buttons = []
        self.buttons.append(self.button_1)
        self.buttons.append(self.button_2)
        self.buttons.append(self.button_3)
        self.buttons.append(self.button_4)
        self.buttons.append(self.button_5)
        self.buttons.append(self.button_6)
        self.buttons.append(self.button_7)
        self.buttons.append(self.button_8)
        self.buttons.append(self.button_9)
        self.buttons.append(self.button_10)
        self.buttons.append(self.button_11)
        self.buttons.append(self.button_12)
        self.buttons.append(self.button_13)
        self.buttons.append(self.button_14)
        self.buttons.append(self.button_15)
        self.buttons.append(self.button_16)


class TicTacToe5x5(Screen):
    def restart(self):
        self.switch = True

        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""
            button.disabled = False

    def tic_tac_toe(self, arg):
        self.buttons[arg - 1].disabled = True
        self.buttons[arg - 1].text = 'X' if self.switch else 'O'
        self.switch = not self.switch

        coordinate = (
            (0, 1, 2, 3), (1, 2, 3, 4), (5, 6, 7, 8), (6, 7, 8, 9), (10, 11, 12, 13), (11, 12, 13, 14),
            (15, 16, 17, 18), (16, 17, 18, 19), (20, 21, 22, 23), (21, 22, 23, 24),  # X
            (0, 5, 10, 15), (5, 10, 15, 20), (1, 6, 11, 16), (6, 11, 16, 21), (2, 7, 12, 17), (7, 12, 17, 22),
            (3, 8, 13, 18), (8, 13, 18, 23), (4, 9, 14, 19), (9, 14, 19, 24),  # Y
            (1, 7, 13, 19), (0, 6, 12, 18), (6, 12, 18, 24), (5, 11, 17, 23), (3, 7, 11, 15), (4, 8, 12, 16),
            (8, 12, 16, 20), (9, 13, 17, 21),  # D
        )

        vector = lambda item: [self.buttons[x].text for x in item]

        color = [0, 1, 0, 1]

        for item in coordinate:
            if vector(item).count('X') == 4 or vector(item).count('O') == 4:
                win = True
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break

    def start_game(self):
        self.switch = True
        self.buttons = []
        self.buttons.append(self.button_1)
        self.buttons.append(self.button_2)
        self.buttons.append(self.button_3)
        self.buttons.append(self.button_4)
        self.buttons.append(self.button_5)
        self.buttons.append(self.button_6)
        self.buttons.append(self.button_7)
        self.buttons.append(self.button_8)
        self.buttons.append(self.button_9)
        self.buttons.append(self.button_10)
        self.buttons.append(self.button_11)
        self.buttons.append(self.button_12)
        self.buttons.append(self.button_13)
        self.buttons.append(self.button_14)
        self.buttons.append(self.button_15)
        self.buttons.append(self.button_16)
        self.buttons.append(self.button_17)
        self.buttons.append(self.button_18)
        self.buttons.append(self.button_19)
        self.buttons.append(self.button_20)
        self.buttons.append(self.button_21)
        self.buttons.append(self.button_22)
        self.buttons.append(self.button_23)
        self.buttons.append(self.button_24)
        self.buttons.append(self.button_25)


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    def change_text(self):
        self.label_id = self.text_input.text


class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(TicTacToe(name='tictactoe'))
        sm.add_widget(TicTacToe4x4(name='tictactoe4'))
        sm.add_widget(TicTacToe5x5(name='tictactoe5'))
        return sm


if __name__ == '__main__':
    TestApp().run()