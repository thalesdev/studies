class TuringMachine:
    def __init__(self,final_state):
        self.tape = []
        self.head = 0
        self.final_state = final_state
        self.actual_state = 0
        self.__transactions = []
    @property
    def tape(self):
        return self.__tape
    @tape.setter
    def tape(self, _tape):
        if (isinstance(_tape, list)):
            self.__tape = _tape
        else:
            raise Exception("Tipo de fita invalido")
    def push_transactions(self, transactions = []):
        self.__transactions.extend(transactions)
    def push_transaction(self, transaction):
        self.__transactions.append(transaction)
    def remove_transaction(self, transaction):
        self.__transactions.remove(transaction)
    def remove_transactions(self, transactions = []):
        for transaction in transactions:
            self.remove_transaction(transaction)
    def recoginize(self, word, logging=False):
        self.tape = list(word)
        # Reset values
        self.head = 0
        self.actual_state = 0
        self.epoch = 0
        computing = True
        if logging:
            print("Log de transações:\n")
        while(computing):
            computing = False
            if ( 0 <= self.head <= len(self.tape)-1):
                char_r = self.tape[self.head]
            else:
                char_r = Transaction.LAMBDA
            for transaction in self.__transactions:
                if transaction.match((self.actual_state, char_r)):       
                    if logging:
                        print("({},{})->({},{},{})".format(self.actual_state, char_r,transaction.state_f, transaction.char_write, transaction.direction ))            
                    if  0 <= self.head <= len(self.tape)-1:
                        self.tape[self.head] = transaction.char_write
                    self.head += -1 if transaction.direction == Transaction.LEFT else 1
                    self.actual_state = transaction.state_f
                    computing = True
                    break
            self.epoch += 1
        #print(self.tape)
        if self.actual_state == self.final_state:
            print("A palavra \"{}\" é reconhecida pela linguagem.\nforam feitas {} iteraçõe(s) a palavra contem {} caractere(s).".format(word, self.epoch, len(word)))
        else:
            print("A palavra \"{}\" não é reconhecida pela linguagem.".format(word))

# (state_inital, character_readed) -> (state_final, character_writed, direction)
class Transaction:
    
    LEFT = "E"
    RIGHT = "D"
    LAMBDA = "V"

    def __init__(self, state_i, char_read, state_f, char_write, direction ):
        
        self.state_i = state_i
        self.char_read = char_read
        self.state_f = state_f
        self.char_write = char_write
        self.direction = direction

    def match(self, args):
        """
        Args[0] : state i
        Args[1] : char_read

        """
        return args[0] == self.state_i and args[1] == self.char_read


def e_4a(word):
    """
     L = L(aba*b)
    """
    print("L = L(aba*b)")
    tm = TuringMachine(3)
    trans = [
        Transaction(0,"a",1,"a",Transaction.RIGHT),
        Transaction(1,"b",2,"b",Transaction.RIGHT),
        Transaction(2,"a",2,"a",Transaction.RIGHT),
        Transaction(2,"b",3,"b",Transaction.RIGHT),
    ]
    tm.push_transactions(trans)
    tm.recoginize(word)
def e_4b(word):
    """
     W c {a,b}*
     L = L = { W / |W| é par}
    """
    print("L = L = { W / |W| é par} para todo W c {a,b}*")
    tm = TuringMachine(2)
    trans = [
        Transaction(0,"a",1,"a",Transaction.RIGHT),
        Transaction(0,"b",1,"b",Transaction.RIGHT),
        Transaction(1,"a",0,"a",Transaction.RIGHT),
        Transaction(1,"b",0,"b",Transaction.RIGHT),
        Transaction(0,Transaction.LAMBDA,2,Transaction.LAMBDA,Transaction.RIGHT)
    ]
    tm.push_transactions(trans)
    tm.recoginize(word)

def e_4g(word):
    """
         L = { W / Na(W)=N(b)}  
    """
    print("L = { W / Na(W) = Nb(W)}")
    tm = TuringMachine(7)
    trans = [
        Transaction(0,"a",1, "x", Transaction.RIGHT),
        Transaction(1,"a",1,"a",Transaction.RIGHT),
        Transaction(1,Transaction.LAMBDA,7,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(1,"x",1,"x",Transaction.RIGHT),
        Transaction(1,"b", 4, "x",Transaction.LEFT),
        Transaction(4,"x", 4, "x",Transaction.LEFT),
        Transaction(4,"a", 1, "x",Transaction.RIGHT),
        Transaction(4,"b", 2, "x",Transaction.RIGHT),
        Transaction(4, Transaction.LAMBDA, 5,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(5,"x", 5, "x",Transaction.RIGHT),
        Transaction(5,"a", 1, "x",Transaction.RIGHT),
        Transaction(5,"b", 2, "x",Transaction.RIGHT),
        Transaction(5, Transaction.LAMBDA, 6,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(0,"b",2, "x", Transaction.RIGHT),
        Transaction(2,"b",2, "b", Transaction.RIGHT),
        Transaction(2,Transaction.LAMBDA,7,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(2,"x",2,"x",Transaction.RIGHT),
        Transaction(1,"a", 8, "x",Transaction.LEFT),
        Transaction(8,"x", 8, "x",Transaction.LEFT),
        Transaction(8,"b", 2, "x",Transaction.RIGHT),
        Transaction(8,"a", 1, "x",Transaction.RIGHT),    
        Transaction(8, Transaction.LAMBDA, 8,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(9,"x", 9, "x",Transaction.RIGHT),
        Transaction(9,"b", 2, "x",Transaction.RIGHT),
        Transaction(9,"a", 1, "x",Transaction.RIGHT),
        Transaction(9, Transaction.LAMBDA, 6,Transaction.LAMBDA,Transaction.RIGHT)
    ]
    tm.push_transactions(trans)
    tm.recoginize(word, True)
def e_4d(word):
    """
         L = {{a^n}{b^m} / n>= 1 and n!=m}  
    """
    print("L = {{a^n}{b^m} / n>= 1 and n!=m}")
    tm = TuringMachine(2)
    trans = [
                 #estado_i,letra_l,estado_f,letra_e,sentido
        Transaction(0,"a",1,"A",Transaction.RIGHT),
        Transaction(0,"b",2,"B",Transaction.RIGHT),
        Transaction(1,"a",1,"a",Transaction.RIGHT),
        Transaction(1,"b",1,"b",Transaction.RIGHT),
        Transaction(1,Transaction.LAMBDA,2,Transaction.LAMBDA,Transaction.LEFT),
        Transaction(2,Transaction.LAMBDA,4,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(1,"B",2,"B",Transaction.LEFT),
        Transaction(2,"b",3,"B",Transaction.LEFT),
        Transaction(2,"B",2,"B",Transaction.LEFT),
        Transaction(3,"b",3,"b",Transaction.LEFT),
        Transaction(3,"a",3,"a",Transaction.LEFT),
        Transaction(3,"A",0,"A",Transaction.RIGHT),
        Transaction(0,"B",4,"B",Transaction.RIGHT),
        Transaction(3,"B",2,"B",Transaction.RIGHT)
    ]
    tm.push_transactions(trans)
    tm.recoginize(word, True)
def e_4h(word):
    """
         L = { W / Na(W)<N(b)}  
    """
    print("L = { W / Na(W) < Nb(W)}")
    tm = TuringMachine(6)
    trans = [
        Transaction(0,"a",1, "x", Transaction.RIGHT),
        Transaction(1,"a",1,"a",Transaction.RIGHT),
        Transaction(1,Transaction.LAMBDA,6,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(1,"x",1,"x",Transaction.RIGHT),
        Transaction(1,"b", 4, "x",Transaction.LEFT),
        Transaction(4,"x", 4, "x",Transaction.LEFT),
        Transaction(4,"a", 1, "x",Transaction.RIGHT),
        Transaction(4,"b", 2, "x",Transaction.RIGHT),
        Transaction(4, Transaction.LAMBDA, 5,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(5,"x", 5, "x",Transaction.RIGHT),
        Transaction(5,"a", 1, "x",Transaction.RIGHT),
        Transaction(5,"b", 2, "x",Transaction.RIGHT),
        Transaction(5, Transaction.LAMBDA, 7,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(0,"b",2, "x", Transaction.RIGHT),
        Transaction(2,"b",2, "b", Transaction.RIGHT),
        Transaction(2,Transaction.LAMBDA,7,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(2,"x",2,"x",Transaction.RIGHT),
        Transaction(1,"a", 8, "x",Transaction.LEFT),
        Transaction(8,"x", 8, "x",Transaction.LEFT),
        Transaction(8,"b", 2, "x",Transaction.RIGHT),
        Transaction(8,"a", 1, "x",Transaction.RIGHT),    
        Transaction(8, Transaction.LAMBDA, 8,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(9,"x", 9, "x",Transaction.RIGHT),
        Transaction(9,"b", 2, "x",Transaction.RIGHT),
        Transaction(9,"a", 1, "x",Transaction.RIGHT),
        Transaction(9, Transaction.LAMBDA, 7,Transaction.LAMBDA,Transaction.RIGHT)
    ]
    tm.push_transactions(trans)
    tm.recoginize(word, True)
def e_4o(word):
    """
            L = { a^{n}b^{2n}a^{n} / n = 2k+1 (impar)}  
    """
    print("L = { a^{n}b^{2n}a^{n} / n = 2k+1 (impar)}")
    tm = TuringMachine(6)
    trans = [
        # die state : 99
        Transaction(0,"b",5, "b", Transaction.RIGHT),
        Transaction(0,"a",1,"x",Transaction.RIGHT),
        Transaction(0,"x",0,"x",Transaction.RIGHT),
        Transaction(1,"a",1,"a",Transaction.RIGHT),
        Transaction(1,"x",1,"x",Transaction.RIGHT),
        Transaction(1,"b",2,"x",Transaction.RIGHT),
        Transaction(2,"b",3,"x",Transaction.RIGHT),
        Transaction(3,"b",3,"b",Transaction.RIGHT),
        Transaction(3,"x",3,"x",Transaction.RIGHT),
        Transaction(3,"a",4,"x",Transaction.LEFT),
        Transaction(3, Transaction.LAMBDA, 5, Transaction.LAMBDA, Transaction.RIGHT),
        Transaction(4,"x",4,"x",Transaction.LEFT),
        Transaction(4,"a",4,"a",Transaction.LEFT),
        Transaction(4,"b",4,"b",Transaction.LEFT),
        Transaction(4,Transaction.LAMBDA,0,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(0,Transaction.LAMBDA,6,Transaction.LAMBDA,Transaction.RIGHT)
    ]
    tm.push_transactions(trans)
    tm.recoginize(word, True)

def e_4p(word):
    """
            L = {a^{n}b^{2n}}  
    """
    print("L = {a^{n}b^{2n}}")
    tm = TuringMachine(6)
    trans = [
        Transaction(0,"b",5, "b", Transaction.RIGHT),
        Transaction(0,"a",1,"x",Transaction.RIGHT),
        Transaction(0,"x",0,"x",Transaction.RIGHT),
        Transaction(1,"a",1,"a",Transaction.RIGHT),
        Transaction(1,"x",1,"x",Transaction.RIGHT),
        Transaction(1,"b",2,"x",Transaction.RIGHT),
        Transaction(2,"b",3,"x",Transaction.LEFT),
        Transaction(3,"x",3,"x",Transaction.LEFT),
        Transaction(3,"a",3,"a",Transaction.LEFT),
        Transaction(3,Transaction.LAMBDA,0,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(0,Transaction.LAMBDA,6,Transaction.LAMBDA,Transaction.RIGHT)
    ]


    tm.push_transactions(trans)
    tm.recoginize(word, True)









def e_4r(word):
    """
            L = {WW / W e {a,b}*}  
    """
    print("L = {WW / W e {a,b}*}")
    tm = TuringMachine(11)
    trans = [
        # Rotinas Iniciais
        # Separar a Palavra em We e Wd
        Transaction(0,"Ae",0,"Ae",Transaction.RIGHT),
        Transaction(0,"Be",0,"Be",Transaction.RIGHT),
        Transaction(0,"b",2, "Be", Transaction.RIGHT),
        Transaction(0,"a",2,"Ae",Transaction.RIGHT),
        Transaction(2,"Ae",2,"Ae",Transaction.RIGHT),
        Transaction(2,"Be",2,"Be",Transaction.RIGHT),
        Transaction(2,"Bd",2,"Bd",Transaction.RIGHT),
        Transaction(2,"Ad",2,"Ad",Transaction.RIGHT),
        Transaction(2,"a",2,"a",Transaction.RIGHT),
        Transaction(2,"b",2,"b",Transaction.RIGHT),
        Transaction(2, Transaction.LAMBDA, 3, Transaction.LAMBDA,Transaction.LEFT),
        Transaction(3, "Ad", 3, "Ad",Transaction.LEFT),
        Transaction(3, "Bd", 3, "Bd",Transaction.LEFT),
        Transaction(3, "a", 4, "Ad",Transaction.LEFT),
        Transaction(3, "b", 4, "Bd",Transaction.LEFT),
        Transaction(4,"Ae",4,"Ae",Transaction.LEFT),
        Transaction(4,"Be",4,"Be",Transaction.LEFT),
        Transaction(4,"Bd",4,"Bd",Transaction.LEFT),
        Transaction(4,"Ad",4,"Ad",Transaction.LEFT),
        Transaction(4,"a",4,"a",Transaction.LEFT),
        Transaction(4,"b",4,"b",Transaction.LEFT),
        Transaction(4, Transaction.LAMBDA, 0, Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(0,"Ad",5,"Ad",Transaction.LEFT),
        Transaction(0,"Bd",5,"Bd",Transaction.LEFT),

        # Segunda rotina resetar e depois partir pra verificar se as cadeias sao iguais

        Transaction(5,"Ae",5,"Ae",Transaction.LEFT),
        Transaction(5,"Be",5,"Be",Transaction.LEFT),
        Transaction(5,"Bd",5,"Bd",Transaction.LEFT),
        Transaction(5,"Ad",5,"Ad",Transaction.LEFT),
        Transaction(5, Transaction.LAMBDA,6, Transaction.LAMBDA, Transaction.RIGHT),

        # Rotina de verificar se achar um Ae tem que procurar um Ae
        Transaction(6,"Ae",7,"x",Transaction.RIGHT),
        # Skips
        Transaction(6,"x",6,"x",Transaction.RIGHT),
        Transaction(7,"Ae",7,"Ae",Transaction.RIGHT),
        Transaction(7,"Be",7,"Be",Transaction.RIGHT),
        Transaction(7,"x",7,"x",Transaction.RIGHT),
        # Achou Reseta
        Transaction(7,"Ad",8,"x",Transaction.LEFT),
        # Skip all ate resetar
        Transaction(8,"Ae",8,"Ae",Transaction.LEFT),
        Transaction(8,"Ad",8,"Ad",Transaction.LEFT),
        Transaction(8,"Be",8,"Be",Transaction.LEFT),
        Transaction(8,"Bd",8,"Bd",Transaction.LEFT),
        Transaction(8,"x",8,"x",Transaction.LEFT),
        Transaction(8,Transaction.LAMBDA,6,Transaction.LAMBDA,Transaction.RIGHT),
        # Rotina de verificar se achar um Be tem que procurar um Bd
        Transaction(6,"Be",9,"x",Transaction.RIGHT),
        #SKips
        Transaction(9,"Ae",9,"Ae",Transaction.RIGHT),
        Transaction(9,"Be",9,"Be",Transaction.RIGHT),
        Transaction(9,"x",9,"x",Transaction.RIGHT),
        # Achou Reseta
        Transaction(9,"Bd",8,"x",Transaction.LEFT),

        #  INICIA A ROTINA DE FIM
        Transaction(6, Transaction.LAMBDA,10, Transaction.LAMBDA,Transaction.LEFT),
        Transaction(10, "x",10, "x",Transaction.LEFT),
        Transaction(10,  Transaction.LAMBDA,11,Transaction.LAMBDA,Transaction.LEFT),
    ]
    tm.push_transactions(trans)
    tm.recoginize(word, True)

    #print(len(trans))
    def e_4j(word):
        
    """
         L = { W / Na(W) < 2*N(b)}  
    """
    print("L = { W / Na(W) < 2*Nb(W)}")
    tm = TuringMachine(6)
    trans = [
        Transaction(0,"a",1, "x", Transaction.RIGHT),
        Transaction(1,"a",1,"a",Transaction.RIGHT),
        Transaction(1,Transaction.LAMBDA,6,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(1,"x",1,"x",Transaction.RIGHT),
        Transaction(1,"b", "?", "x",Transaction.LEFT),
        Transaction(4,"x", 4, "x",Transaction.LEFT),
        Transaction(4,"a", 1, "x",Transaction.RIGHT),
        Transaction(4,"b", 2, "x",Transaction.RIGHT),
        Transaction(4, Transaction.LAMBDA, 5,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(5,"x", 5, "x",Transaction.RIGHT),
        Transaction(5,"a", 1, "x",Transaction.RIGHT),
        Transaction(5,"b", 2, "x",Transaction.RIGHT),
        Transaction(5, Transaction.LAMBDA, 7,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(0,"b",2, "x", Transaction.RIGHT),
        Transaction(2,"b",2, "b", Transaction.RIGHT),
        Transaction(2,Transaction.LAMBDA,7,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(2,"x",2,"x",Transaction.RIGHT),
        Transaction(1,"a", 8, "x",Transaction.LEFT),
        Transaction(8,"x", 8, "x",Transaction.LEFT),
        Transaction(8,"b", 2, "x",Transaction.RIGHT),
        Transaction(8,"a", 1, "x",Transaction.RIGHT),    
        Transaction(8, Transaction.LAMBDA, 8,Transaction.LAMBDA,Transaction.RIGHT),
        Transaction(9,"x", 9, "x",Transaction.RIGHT),
        Transaction(9,"b", 2, "x",Transaction.RIGHT),
        Transaction(9,"a", 1, "x",Transaction.RIGHT),
        Transaction(9, Transaction.LAMBDA, 7,Transaction.LAMBDA,Transaction.RIGHT)
    ]
    tm.push_transactions(trans)
    tm.recoginize(word, True)

def e_extra(word):
    """
         L = {{a^n}{b^n} / n>= 1}  
    """
    
    tm = TuringMachine(4)
    trans = [
        Transaction(0,"a",1,"A",Transaction.RIGHT),
        Transaction(1,"a",1,"a",Transaction.RIGHT),
        Transaction(1,"b",1,"b",Transaction.RIGHT),
        Transaction(1,Transaction.LAMBDA,2,Transaction.LAMBDA,Transaction.LEFT),
        Transaction(1,"B",2,"B",Transaction.LEFT),
        Transaction(2,"b",3,"B",Transaction.LEFT),
        Transaction(2,"B",2,"B",Transaction.LEFT),
        Transaction(3,"b",3,"b",Transaction.LEFT),
        Transaction(3,"a",3,"a",Transaction.LEFT),
        Transaction(3,"A",0,"A",Transaction.RIGHT),
        Transaction(0,"B",4,"B",Transaction.RIGHT)
    ]
    tm.push_transactions(trans)
    tm.recoginize(word)


if __name__ == "__main__":
    e_4r("aaaaaaaaaabbabbabababbabaaaaaaaaaaabbabbabababbaba")



