class Banco(object):
    __total=10000
    taxaReserva=0.1
    __reservaExigida=__total*taxaReserva

    def podeFazerEmprestimo(valor):
        if Banco.reservaExigida>=valor:
            return True
        else:
            return False

    def MudaTotal(valor):
        Banco.__total=valor


class Conta(object):

    """
    Objeto do tipo conta, representa uma conta qualque.
    """

    def __init__(self,saldo,ID,senha):
        self.__saldo=saldo
        self.__ID=ID
        self.__senha=senha

    def deposito(self,senha, valor):
        if self.__senha==senha:
            self.__saldo+=valor
            Banco.MudaTotal(valor)

    def saque(self,senha, valor):
        if self.__senha==senha:
            self.__saldo-=valor
            Banco.MudaTotal(-valor)

    def podeReceberEmprestimo(self,valor):
        return Banco.podeFazerEmprestimo(valor)

    def saldo(self):
        print(self.__saldo)




BB=Conta(428,1321,"hjp")
BB.saldo()
BB.saque("hjp",120.00)
BB.saldo()
BB.deposito("hjp",50)
BB.saldo()
print(BB.__doc__)
print(BB.__dict__)