from otimizacao import Otimizador
otimizar = Otimizador()
otimizar.adicionar_funcao_objetivo('min. + 3000x_1 + 20000x_2 + 30000x_3 + 10000x_4')
otimizar.adicionar_restricao('x_1 + x_2 + x_3 + x_4 == 20')
otimizar.adicionar_restricao('+ 20x_1 + 5x_2 + 10x_3 + 2x_4 <= 200')
otimizar.adicionar_restricao('+ 10x_1 + 20x_2 + 20x_3 + 15x_4 >= 80')
otimizar.simplex(calculo_visivel=True)