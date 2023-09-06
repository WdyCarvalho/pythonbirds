class Pessoa:
    def cumprimentar(self):# o primeiro parâmetro do método, por convenção é chamado 'self'
        return 'olá!'

if __name__ == '__main__':
    p = Pessoa() #Variável P recebe a classe Pessoa()
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar( ))