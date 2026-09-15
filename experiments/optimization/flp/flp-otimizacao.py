from otimizacao import Otimizador
otimizar = Otimizador()
otimizar.adicionar_funcao_objetivo('max. + 0x_1 + 0x_3 + 0x_2 + 0x_4 + x_5')
otimizar.adicionar_restricao('3000x_1+30000x_3+20000x_2 +10000x_4+37777x_5<=137777')
otimizar.adicionar_restricao('+ x_1 + x_3 + x_2 + 1x_4 + 5x_5 == 25')
otimizar.adicionar_restricao('+ 20x_1 + 10x_3 + 5x_2 + 2x_4 + 250x_5 <= 500')
otimizar.adicionar_restricao('10x_1 + 20x_3 + 20x_2 + 15x_4 - 50x_5 >= 50')
otimizar.adicionar_restricao('+ 0x_1 + 0x_3 + 0x_2 + 0x_4 + 1x_5 <= 1')
otimizar.simplex(calculo_visivel=False)