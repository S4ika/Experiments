from pyswip import Prolog,Functor, Variable, Query, call


class Work_with_Prolog:
    flag = False
    moves = {'X' : False,'O' : True}

    def valid_moves(self):

        prolog = Prolog()

        # Файл с игрой
        prolog.consult("tic tac toe gameees.pl")

        # Подключаем кодировку
        prolog.query("set_prolog_flag(encoding, utf8)")
        # start = list(prolog.query("play"))
        # move = list(prolog.query("move(o,0,1)"))
        #Work
        valid_moves = list(prolog.query("valid_moves(ValidMoves, Game, x)"))
        self.list_valid_moves = [] # список доступных ходов, номера от 0 до 8
        for i in valid_moves[0]['Game']:
            st = str(i)
            st = st.split(', ')
            # print(st)
            self.list_valid_moves.append(int(st[1])*3 + int(st[2][0]))

    def new_move(self, move):
        prolog = Prolog()
        if move in self.list_valid_moves:
            self.list_valid_moves.remove(move)
            self.flag = not self.flag
            new_move = prolog.query("ask_move(Move, ValidMoves)")
            self.new_move(new_move)
        elif len(self.list_valid_moves) == 0:
            prolog.query("any_valid_moves([], _)")
        else:
            prolog.query("ask_move(Move, ValidMoves)")
