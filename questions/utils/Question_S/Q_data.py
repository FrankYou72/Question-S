import random
from sympy import symbols, Eq, solve, sin, cos, sqrt, pi, tan, init_printing, acos, asin, atan, log, exp, rad, Abs

opes = ['+', '-', '*', '/', '**', 'log', 'ln', 'exp', '(', ')', 'sqrt', '[', ']']

class Pack():
    def __init__(self, name, vrs, eqts, qnts, unts, prompt):
        self.name = name
        self.vrs = vrs
        self.eqts = eqts
        self.qnts = qnts
        self.unts = unts
        self.prompt = prompt

S, S0, deltaS, vm, v, v0, vf, deltav, a, am, D, h, t, deltat, S01, S02, v1, v2, a1, a2, tult = symbols('S S0 deltaS vm v v0 vf deltav a am D h t deltat S01 S02 v1 v2 a1 a2 tult')
theta, theta0, deltatheta, wm, w, w0, deltaw, alpha, alpham, vlin, T, f, R, n, acp = symbols('theta theta0 deltatheta wm w w0 deltaw alpha alpham vlin T f R n acp')

### Pack Cinemática ###

Kin_Vars = {S : symbols('S'), S0: symbols('S0'), deltaS : symbols('deltaS'), vm : symbols('vm'),
                   v : symbols('v'), v0 : symbols('v0'), deltav : symbols('deltav'), a : symbols('a'),
                   am : symbols('am'), D : symbols('D'), h : symbols('h'), deltat : symbols('deltat'),
                   t: symbols('t'), S01 : symbols('S01'), S02 : symbols('S02'), v1 : symbols('v1'),
                   v2 : symbols('v2'), tult : symbols('tult'), vf : symbols('vf')}
Kin_Eq = {'Deslocamento': [Eq(deltaS - S + S0, 0), 'Em um movimento de um corpo, sabe-se que:'],
          'Velocidade média':[Eq(vm - deltaS / deltat, 0), 'Em um movimento de um corpo, sabe-se que:'],
          'Posição MRU': [Eq(S - S0 - v * t, 0), 'Um corpo está em MRU. Sabe-se que:'],
          'Velocidade': [Eq(v - v0 - a * t, 0), 'Um corpo está em MRUV. Sabe-se que:'],
          'Variação de velocidade': [Eq(deltav - v + v0, 0), 'Um corpo se move em linha reta. Sabe-se que:'],
          'Aceleração média': [Eq(am - deltav / deltat, 0), 'Um corpo se move com as seguintes propriedades:'],
          'Posição MRUV': [Eq(S - S0 - v0 * t - 0.5 * a * t ** 2, 0), 'Um corpo se move com aceleração constante. Sabe-se que:'],
          'Torricelli': [Eq(vf ** 2 - v0 ** 2 - 2 * a * deltaS, 0), 'Um corpo se desloca com aceleração constante. Sabe-se que:'],
          'Momento de ultrapassagem MRU' : [Eq(tult - (S01 - S02)/(v2 - v1),0), 'Dois corpos se movem com velocidade constante sobre um eixo. Sabe-se que:']}
Kin_Quant = {S : 'Posição final', S0: 'Posição inicial', deltaS : 'Deslocamento', vm : 'Velocidade média',
                   v : 'velocidade instantânea', v0 : 'Velocidade inicial', deltav : 'Variação de velocidade',
                   a : 'aceleração', am : 'aceleração média', D : 'Distância', h : 'altura', t : 'instante',
                   deltat : 'intervalo de tempo', S01 : 'Posição inicial do corpo 1',
                   S02 : 'Posição inicial do corpo 2', v1 : 'Velocidade do corpo 1', v2 : 'Velocidade do corpo 2',
                   tult : 'instante de ultrapassagem/cruzamento', vf : 'Velocidade final'}
Kin_Units = {S : ['m', (0, 30, 1)], S0: ['m', (-30, 30, 1)] , deltaS : ['m',(-50, 50, 1)], vm : ['m/s', (-30, 30, 1)],
            v : ['m/s', (-50, 50, 1)], v0 : ['m/s',(-15, 15, 1)], deltav : ['m/s', (-30, 30, 1)], a : ['m/s^2', (-15,15,1)],
            am : ['m/s^2', (-15, 15, 1)], D : ['m', (0, 100, 1)], h : ['m', (0, 80, 1)], t : ['s', (0, 30, 1)], deltat : ['s', (0, 30, 1)],
            S01 : ['m', (0, 50, 1)], S02 : ['m', (50, 100, 1)], v1 : ['m/s', (0, 20, 1)], v2 : ['m/s', (-20, 0, 1)], tult : ['s', (0, 15, 1)],
            vf : ['m/s', (-50, 50, 1)]}
Kin_Pack = (Kin_Vars, Kin_Eq, Kin_Quant, Kin_Units)
Kin = Pack('Cinemática', Kin_Vars, Kin_Eq, Kin_Quant, Kin_Units,
           'Em um movimento de um corpo sabe-se que')

### Pack Cinemática Rotacional ###

Rot_Kin_Vars = {theta: symbols('theta'), theta0 : symbols('theta0'), deltatheta : symbols('deltatheta'),
                wm : symbols('wm'), w : symbols('w'), w0 : symbols('w0'), deltaw : symbols('deltaw'),
                alpha : symbols('alpha'), alpham : symbols('alpham'), t : symbols('t'), deltat : symbols('deltat'),
                vlin: symbols('vlin'), T : symbols('T'), f : symbols('f'), R : symbols('R'), n : symbols('n'),
                acp : symbols('acp')}
Rot_Kin_Eq = {'Deslocamento angular': [Eq(deltatheta - theta + theta0, 0),'Um corpo está girando sobre um disco. Sabe-se que:'],
              'Velocidade angular média':[Eq(wm - deltatheta / deltat, 0),'Um corpo está girando sobre um disco. Sabe-se que:'],
              'Posição angular MCU': [Eq(theta - theta0 - w * t, 0),'Um corpo descreve uma circunferência em MCU. Sabe-se que:'],
              'Velocidade angular': [Eq(w - w0 - alpha * t, 0),'Um corpo está girando sobre um disco com aceleração angular constante. Sabe-se que:'],
              'Variação de velocidade angular': [Eq(deltaw - w + w0, 0),'Um corpo está girando sobre um disco com velocidade angular variável. Sabe-se que:'],
              'Aceleração angular média': [Eq(alpham - deltaw / deltat, 0),'Um corpo está girando sobre um disco com velocidade angular variável. Sabe-se que:'],
              'Posição MCUV': [Eq(theta - theta0 - w0 * t - 0.5 * alpha * t ** 2, 0),'Um corpo está girando sobre um disco com aceleração angular constante. Sabe-se que:'],
              'Velocidade linear' : [Eq(vlin - n*2*pi*R/deltat, 0),'Um corpo descreve uma circunferência em MCU. Sabe-se que:'],
              'Período v' : [Eq(T - 2*pi*R/(vlin), 0),'Um corpo descreve uma circunferência em MCU. Sabe-se que:'],
              'frequência v' : [Eq(f - vlin/(2*pi*R), 0),'Um corpo descreve uma circunferência em MCU. Sabe-se que:'],
              'Velocidade angular/ linear' :  [Eq(w - vlin/R, 0),'Um corpo descreve uma circunferência em MCU. Sabe-se que:'],
              'Período w': [Eq(T - 2*pi/w, 0),'Um corpo descreve uma circunferência em MCU. Sabe-se que:'],
              'frequência w' : [Eq(f - w/(2*pi), 0),'Um corpo descreve uma circunferência em MCU. Sabe-se que:'],
              'Aceleração centrípeta' : [Eq(acp - (vlin**2)/R, 0), 'Um corpo descreve uma circunferência em MCU. Sabe-se que:']}
Rot_Kin_Quant = {theta : 'Posição angular final', theta0: 'Posição angular inicial',
                 deltatheta : 'Deslocamento angular', wm : 'Velocidade angular média',
                 w : 'velocidade angular instantânea', w0 : 'Velocidade angular inicial',
                 deltaw : 'Variação de velocidade angular',
                 alpha : 'aceleração angular', alpham : 'aceleração angular média', t : 'instante',
                 deltat : 'intervalo de tempo', vlin : 'Velocidade linear/ tangencial', T : 'Período de rotação',
                 f : 'frequência de giro', R: 'Raio', n : 'número de voltas', acp : 'aceleração centrípeta'}
Rot_Kin_Units = {theta : ['rad', (0, 630, 100)], theta0 : ['rad', (0, 630, 100)],
                deltatheta : ['rad', (-630, 630, 100)], wm : ['rad/s', (1, 315, 100)], w : ['rad/s', (0, 630, 100)],
                w0 : ['rad/s', (-315, 315, 100)], deltaw : ['rad/s', (-160, 160, 100)], alpha : ['rad/s^2', (-160, 160, 100)],
                alpham : ['rad/s^2', (-160, 160, 100)], t : ['s', (1, 20, 1)], deltat : ['s', (1, 20, 1)],
                vlin : ['m/s', (-40, 40, 1)], T : ['s', (0, 100, 10)], f : ['Hz', (0, 100, 1)],
                R : ['m', (0, 10, 1)], n : ['voltas', (0, 10, 1)], acp : ['m/s^2', (0, 300, 1)]}
Rot_Kin_Pack = (Rot_Kin_Vars, Rot_Kin_Eq, Rot_Kin_Quant, Rot_Kin_Units)
Rot_Kin = Pack('Cinemática Rotacional', Rot_Kin_Vars, Rot_Kin_Eq, Rot_Kin_Quant, Rot_Kin_Units,
               'Em um movimento de um corpo sabe-se que ')

### Pack Lançamento de projétil ###
x, vx, deltax, y0, y, vy0, vy, g, deltay, Dmax, hmax, hlv, hlh, v0, hql = symbols('x vx deltax y0 y vy0 vy g deltay Dmax hmax hlv hlh v0 hql')

Projectiles_Vars = {x : symbols('x'), vx : symbols('vx'), deltax : symbols('deltax'),
                    y0 : symbols('y0'), y : symbols('y'), vy0 : symbols('vy0'), vy: symbols('vy'),
                    deltay : symbols('deltay'), deltat : symbols('deltat'), t : symbols('t'), Dmax : symbols('Dmax'),
                    hmax: symbols('hmax'), hlh : symbols('hlh'), hlv : symbols('hlv'), theta : symbols('theta'),
                    v0 : symbols('v0'), hql : symbols('hql')}
Projectiles_Eq = {'Posição LV' : [Eq(hlv -vy0*deltat +5*(deltat**2), 0),'Um corpo é lançado verticalmente para cima. Sabe-se que:\ng = 10 m/s^2'],
                  'Altura máxima' : [Eq(hmax - (vy0**2)/(20), 0),'Um corpo é lançado verticamente para cima. Sabe-se que:\ng = 10 m/s^2'],
                  'Altura QL' : [Eq(hql - 5*deltat**2, 0),'Um corpo é abandonado em queda livre. Sabe-se que:\ng = 10 m/s^2'],
                  'Alcance máximo LH' : [Eq(Dmax - vx*sqrt((2*hlh)/10), 0),'Um corpo é lançado horizontalmente. Sabe-se que:\ng = 10 m/s^2'],
                  'Alcance Máximo LO' : [Eq(Dmax - ((v0**2)*sin(2*rad(theta)))/10, 0),'Um corpo é lançado obliquamente em relação ao solo. Sabe-se que:\ng = 10 m/s^2']}
Projectiles_Quant = {x : 'Posição horizontal', vx : 'velocidade horizontal', deltax : 'deslocamento',
                     y0 : 'altura inicial', y : 'posição vertical', vy0 : 'velocidade vertical inicial',
                     vy : 'velocidade vertical instantânea',
                     deltay : 'deslocamento vertical', Dmax : 'alcance máximo', hmax : 'altura máxima',
                     theta : 'ângulo de lançamento', hlv : 'Posição vertical do corpo', t : 'instante',
                     deltat: 'tempo de viagem do projétil', hlh : 'altura de lançamento',
                     v0 : 'velocidade inicial de disparo', hql: 'altura de queda'}
Projectiles_Units = {x : ['m', (0, 100, 1)], vx : ['m/s', (0, 100, 10)], deltax : ['m', (0, 100, 1)],
                    y0 : ['m', (0, 40, 1)], y : ['m', (0, 100, 1)], vy0 : ['m/s', (0, 100, 10)],
                    vy : ['m/s', (0, 100, 10)], deltay : ['m', (0, 60, 1)],
                    Dmax : ['m', (0, 100, 1)], hmax : ['m', (0, 100, 1)], theta : ['°', (0, 90, 1)],
                    h : ['m', (0, 40, 1)], t : ['s', (0, 20, 1)], deltat : ['s', (1, 20, 1)],
                    hlv : ['m', (10, 100, 1)], hlh : ['m', (0, 40, 1)], hql: ['m', (0, 30, 1)], 
                    v0 : ['m/s', (30, 150, 1)]}
Projectiles_Pack = (Projectiles_Vars, Projectiles_Eq, Projectiles_Quant, Projectiles_Units,
                'Um projétil é lançado com as seguintes configurações: ')
Projectiles = Pack('Lançamento de projétil', Projectiles_Vars, Projectiles_Eq, Projectiles_Quant,
                   Projectiles_Units, 'Um projétil é lançado com as seguintes configurações: ')

### Pack Mecânica Newtoniana ###

F1, F2, F3, m, m1, m2, a1, a2, P, Normal, mu, T1, T2, Fel, k, Fatc, Fate, Fres, F, ma, mb, mc, Fa, Fb, Fc, Fab, Fbc, Fat, asis, Fata, Fressis = symbols('F1 F2 F3 m m1 m2 a1 a2 P Normal mu T1 T2 Fel k Fatc Fate Fres F ma mb mc Fa Fb Fc Fab Fbc Fat asis Fata Fressis')
Newton_Vars = {F1 : symbols('F1'), F2 : symbols('F2'), F3 : symbols('F3'), m : symbols('m'), m1 : symbols('m1'),
               m2 : symbols('m2'), a1 : symbols('a1'), a2 : symbols('a2'), P : symbols('P'),
               Normal : symbols('Normal'), mu: symbols('mu'), T1 : symbols('T1'), T2 : symbols('T2'),
               Fel : symbols('Fel'), k : symbols('k'), Fatc : symbols('Fatc'), Fate : symbols('Fate'),
               Fres : symbols('Fres'), F : symbols('F'), ma : symbols('ma'), mb : symbols('mb'), mc : symbols('mc'),
               Fa : symbols('Fa'), Fb : symbols('Fb'), Fc : symbols('Fc'), Fab : symbols('Fab'), Fbc : symbols('Fbc'),
               deltat : symbols('deltat'), deltaS : symbols('deltaS'), v0 : symbols('v0'), alpha : symbols('alpha'),
               asis : symbols('asis'), Fata : symbols('Fata'), Fressis : symbols('Fressis'), x : symbols('x'),
               g : symbols('g'), a : symbols('a'), T : symbols('T')}
Newton_Eq = {'Inércia' : [Eq(F1 + F2 + F3, 0),'Três forças de mesma direção agem sobre um corpo em inércia. Sabe-se que:'],
             'PFD 2 forças' : [Eq(F1 + F2 - m*a, 0),'Sobre um corpo, agem duas forças de mesma direção. Sabe-se que:'],
             'PFD 3 forças' : [Eq(F1 + F2 + F3 - m*a, 0),'Sobre um corpo, agem três forças de mesma direção. Sabe-se que:'],
             'PFD resultante fácil' : [Eq(Fres - m*a, 0),'Sobre um corpo atua uma força resultante. Sabe-se que:'],
             'PFD resultante difícil' : [Eq(Fres - m*((2*(deltaS - v0*deltat))/deltat**2), 0),'Sobre um corpo atua uma força resultante. Sabe-se que:'],
             'Ação e reação sem força' : [Eq(m1*a1 + m2*a2, 0),'Dois corpos interagem por meio de um par de forças. Sabe-se que:'],
             'Ação e reação com força' : [Eq(F1 + m2*a2, 0),'Dois corpos interagem por meio de um par de forças. Sabe-se que:'],
             'Força peso' : [Eq(P -m*10, 0),'Dado um corpo qualquer, sabe-se que:\ng = 10 m/s^2'],
             'Força normal' : [Eq(Normal - m*-10*cos(rad(alpha)), 0),'Um corpo está em um plano com inclinação alpha. Sabe-se que:\ng = 10 m/s^2'],
             'Tensão' : [Eq(T1 + T2, 0),'Um corpo mantém uma corda tensionada. Sabe-se que:'],
             'Força elástica' : [Eq(Fel + k*x, 0),'Uma força é aplicada sobre uma mola. Sabe-se que:'],
             'Força elástica aceleração' : [Eq(m*a + k*x, 0),'Um corpo é associado a uma mola que sofre uma distenção. Sabe-se que:'],
             'Força elástica peso' : [Eq(m*-10 + k*x, 0),'Um corpo está pendurado por uma mola. Sabe-se que:\ng = 10 m/s^2'],
             'Força de atrito estático' : [Eq(F + mu*m*-10, 0),'Um corpo está sobre uma superfíce com atrito e na iminência de movimento. Sabe-se que:\ng = 10 m/s^2'],
             'Força de atrito cinético resultante' : [Eq(Fres - F + Fatc, 0),'Um corpo é impulsionado por uma força sobre uma superfíce com atrito. Sabe-se que:'],
             'Força de atrito cinético massa' : [Eq(m*(mu*-10 +a) - F, 0),'Um corpo é impulsionado por uma força sobre uma superfíce com atrito. Sabe-se que:\ng = 10 m/s^2'],
             'Coeficiente de atrito' : [Eq(a - mu*10, 0),'Um corpo é empurrado sobre uma superfície com atrito. Sabe-se que:\ng = 10 m/s^2'],
             'Plano inclinado sem atrito resultante' : [Eq(Fres - m*-10*sin(rad(alpha)), 0),'Um corpo desliza sobre um plano inclinado sem atrito. Sabe-se que:\ng = 10 m/s^2'],
             'Plano inclinado sem atrito aceleração' : [Eq(a - -10*sin(rad(alpha)), 0),'Um corpo desliza sobre um plano inclinado sem atrito. Sabe-se que:\ng = 10 m/s^2'],
             'Plano inclinado atrito estático' : [Eq(Fate - m*-10*sin(rad(alpha)),0),'Um corpo repousa sobre um plano inclinado. Sabe-se que:\ng = 10 m/s^2'],
             'Plano inclinado atrito estático coeficiente' : [Eq(mu - tan(rad(alpha)),0),'Um corpo repousa sobre um plano inclinado. Sabe-se que:'],
             'Plano inclinado atrito cinético resultante' : [Eq(Fres - m*-10*sin(rad(alpha)) + Fatc,0),'Um corpo desliza sobre um plano inclinado com atrito. Sabe-se que:\ng = 10 m/s^2'],
             'Plano inclinado atrito cinético' : [Eq(Fatc - m*(-10*sin(rad(alpha)) - a),0),'Um corpo desliza sonbre um plano inclinado. Sabe-se que:\ng = 10 m/s^2'],
             'Plano inclinado atrito cinético coeficiente' : [Eq(a + 10*(sin(rad(alpha)) - mu*cos(rad(alpha))),0),'Um corpo desliza sobre um plano inclinado. Sabe-se que:\ng = 10 m/s^2'],
             'Plano inclinado atrito cinético resultante difícil' : [Eq(Fres - m*-10*(sin(rad(alpha)) - mu*cos(rad(alpha))),0),'Um corpo desliza sobre um plano inclinado. Sabe-se que:\ng = 10 m/s^2'],
             'Sistema 2 resultante' : [Eq(Fressis - (ma + mb)*asis,0),'Um força horizontal é aplicada sobre um sistema de dois corpos. Sabe-se que:'],
             'Sistema 2 interação' : [Eq(Fab - (mb*F)/(ma + mb) ,0),'Uma força horizontal é aplicada sobre um sistema de dois corpos. Sabe-se que:'],
             'Sistema 2 força a' : [Eq(Fa - (ma*F)/(ma + mb),0),'Uma força horizontal é aplicada sobre um sistema de dois corpos. Sabe-se que:'],
             'Sistema 3 resultante' : [Eq(Fressis - (ma + mb + mc)*asis,0),'Uma força horizontal é aplicada sobre um sistema de três corpos. Sabe-se que:'],
             'Sistema 3 força a' : [Eq(Fa - (ma*F)/(ma + mb + mc),0),'Uma força horizontal é aplicada sobre um sistema de três corpos. Sabe-se que:'],
             'Sistema 3 força b' : [Eq(Fb - (mb*F)/(ma + mb + mc),0),'Uma força horziontal é aplicada sobre um sistema de três corpos. Sabe-se que:'],
             'Sistema 3 força c' : [Eq(Fc - (mc*F)/(ma + mb + mc),0),'Uma força horizontal é aplicada sobre um sistema de três corpos. Sabe-se que:'],
             'Sistema 3 força ab' : [Eq(Fab - F + (ma*F)/(ma + mb + mc),0),'Uma força horizontal é aplicada sobre um sistema de três corpos. Sabe-se que:'],
             'Atwood sem atrito sistema' : [Eq(mb*10 - (ma + mb)*asis,0), 'Em uma máquina de Atwood (corpo A sobre a superfície e corpo B pendente) sobre uma superfície sem atrito sabe-se que:\ng = 10 m/s^2'],
             'Atwood sem atrito tração' : [Eq(T - mb*(10-asis),0), 'Em uma máquina de Atwood (corpo A sobre a superfície e corpo B pendente) sobre uma superfície sem atrito sabe-se que:\ng = 10 m/s^2'],
             'Atwood atrito estático' : [Eq(Fate - mb*10, 0), 'Em uma máquina de Atwood estática (corpo A sobre a superfície e corpo B pendente) sabe-se que:\ng = 10 m/s^2'],
             'Atwood atrito estático tração' : [Eq(T - mb*10, 0), 'Em uma máquina de Atwood estática (corpo A sobre a superfície e corpo B pendente) sabe-se que:\ng = 10 m/s^2'],
             'Atwood atrito estático coeficiente' : [Eq(mu*ma*10 - mb*10, 0), 'Em uma máquina de Atwood estática (corpo A sobre a superfície e corpo B pendente) sabe-se que:\ng = 10 m/s^2'],
             'Atwood atrito' : [Eq(Fressis - mb*10 + Fata,0), 'Em uma máquina de Atwood (corpo A sobre a superfície e corpo B pendente) sabe-se que:\ng = 10 m/s^2'],
             'Atwood atrito difícil' : [Eq(Fressis - 10*(mb + mu*ma), 0), 'Em uma máquina de Atwood (corpo A sobre a superfície e corpo B pendente) sabe-se que:\ng = 10 m/s^2'],
             'Atwood atrito aceleração' : [Eq(a*(mb + ma) - mu*10*(mb - ma),0), 'Em uma máquina de Atwood (corpo A sobre a superfície e corpo B pendente) sabe-se que:\ng = 10 m/s^2'],
             'Atwood tração' : [Eq((mb + ma)*(mb*10 - T) - mb*mu*10*(mb - ma),0), 'Em uma máquina de Atwood (corpo A sobre a superfície e corpo B pendente) sabe-se que:\ng = 10 m/s^2']}
Newton_Quant = {F1 : 'Força 1', F2 : 'Força 2', F3 : 'Força 3', m : 'massa do corpo', m1 : 'massa do corpo 1',
                m2 : 'massa do corpo 2', a1 : 'aceleração do corpo 1', a2 : 'aceleração do corpo 2',
                P : 'Peso do corpo', Normal : 'Força Normal', mu: 'coeficiente de atrito',
                T1 : 'Tensão no lado direito do cabo', T2 : 'Tensão no lado direito do cabo', Fel : 'Força elástica',
                k : 'constante elástica', Fatc : 'Força de atrito cinético', Fate : 'Força de atrito estático',
                Fres : 'Força resultante', F : 'Força aplicada', ma : 'massa do corpo a', mb : 'massa do corpo b',
                mc : 'massa do corpo c', Fa : 'Força resultante no corpo a', Fb : 'Força resultante no corpo b',
                Fc : 'Força resultante no corpo c', Fab : 'Força que o corpo a aplica no corpo b',
                Fbc : 'Força que o corpo b aplica no corpo c', deltat : 'intervalo de tempo', deltaS : 'deslocamento',
                v0 : 'velocidade inicial do corpo', alpha : 'ângulo de inclinação do plano',
                asis : 'aceleração resultante do sistema', Fata : 'Força de atrito no corpo a',
                Fressis : 'Força resultante no sistema', x : 'distensão da mola',
                a: 'aceleração do corpo', T : 'tração no fio' }
Newton_Units = {F1 : ['N', (-1000, 1000, 1)], F2 : ['N', (-1000, 1000, 1)], F3 : ['N', (-1000, 1000, 1)],
                m : ['kg', (0, 100, 1)], m1 : ['kg', (0, 100, 1)], m2 : ['kg', (0, 100, 1)], a1 : ['m/s^2', (-20, 20, 1)],
                a2 : ['m/s^2', (-20, 20, 1)], P : ['N', (-1000, 1000, 1)], Normal : ['N', (-1000, 1000, 1)],
                mu: ['', (0, 30, 10)], T1 : ['N', (-100, 100, 1)], T2 : ['N', (-100, 100, 1)], Fel : ['N', (-1000, 0, 1)],
                k : ['N/m', (0, 300, 1)], Fatc : ['N', (0, 1000, 1)], Fate : ['N', (0, 1000, 1)], Fres : ['N', (0, 1000, 1)],
                F : ['N', (100, 1000, 1)], ma : ['kg', (0, 100, 1)], mb : ['kg', (0, 100, 1)], mc : ['kg', (0, 100, 1)],
                Fa : ['N', (0, 400, 1)], Fb : ['N', (0, 400, 1)], Fc : ['N', (0, 400, 1)], Fab : ['N', (0, 400, 1)],
                Fbc : ['N', (0, 400, 1)], deltat : ['s', (0, 20, 1)], deltaS : ['m', (0, 100, 1)], v0 : ['N', (0, 100, 10)],
                alpha : ['°', (0, 90, 1)], asis : ['m/s^2', (0, 20, 1)], Fata : ['N', (0, 30, 1)], Fressis : ['N', (0, 1000, 1)],
                x : ['m', (0, 100, 10)], a: ['m/s^2', (0, 20, 1)], T : ['N', (0, 1000, 1)]}
Newton_Pack = (Newton_Vars, Newton_Eq, Newton_Quant, Newton_Units)

### Pack Gravitação Universal ###

deltaA1, deltaA2, deltat1, deltat2, Tk, Torb, Rm, K, Fg, d, mc, M, vorb, vorbk, gt, horb, Rorb = symbols('deltaA1 deltaA2 deltat1 deltat2 Tk Torb Rm K Fg d mc M vorb vorbk gt horb Rorb')
Gravitation_Vars = {deltaA1 : symbols('deltaA1'), deltaA2 : symbols('deltaA2'), deltat1 : symbols('deltat1'),
                    deltat2 : symbols('deltat2'), Torb : symbols('Torb'), Rm : symbols('Rm'), K : symbols('K'),
                    Fg : symbols('Fg'), m1 : symbols('m1'), m2 : symbols('m2'), d : symbols('d'),
                    mc : symbols('mc'), gt : symbols('gt'), Tk : symbols('Tk'), M : symbols('M'),
                    vorb : symbols('vorb'), g : symbols('g'), h : symbols('h'), R : symbols('R'),
                    vorbk : symbols('vorbk'), horb : symbols('horb'), Rorb : symbols('Rorb')}
Gravitation_Eq = {'Segunda Lei de Kepler':[Eq(deltaA1/deltat1 - deltaA2/deltat2,0),'Um corpo celeste orbita um outro corpo central. Observa-se que:'],
                  'Terceira Lei de Kepler Sistema Solar':[Eq((Tk**2)/(Rm**3) - 1,0),'Um corpo celeste orbita nosso Sol com as seguntes características:\nConstante Kepleriana = 1 ano^2/UA^3'],
                  'Terceira Lei de Kepler geral':[Eq((Tk**2)/(Rm**3) - K,0),'Um corpo celeste orbita um corpo maior com as seguntes características:'],
                  'Lei da Gravitação Universal' : [Eq(Fg - (6.67E-11*m1*m2)/(d**2),0), 'Dois corpos no espaço sofrem atração gravitacional. Sabe-se que:\n Constante universal de gravitação: 6.67x10^-11 Nm^2/kg^2'],
                  'Lei da Gravitação Universal Terra' : [Eq(Fg - (6.67E-11*6E24*mc)/(6.4E6 + h)**2,0), 'Um corpo na vizinhança da Terra sofre atração gravitacional. Sabe-se que:\n Massa da Terra = 6x10^24 kg\n Raio da Terra = 6400 km\n Constante universal de gravitação: 6.67x10^-11 Nm^2/kg^2'],
                  'Campo gravitacional na superfície' : [Eq(g - (6.67E-11*M)/(R**2),0), 'Um corpo gera um campo gravitacional ao seu redor. Sabe-se que:'],
                  'Campo gravitacional da Terra' : [Eq(gt - (6.67E-11*6E24)/(6.4E6 + h)**2, 0), 'A Terra gera um campo gravitacional em determinada altura h. Sabe-se que:\n Massa da Terra = 6x10^24 kg\n Raio da Terra = 6400 km\n Constante universal de gravitação: 6.67x10^-11 Nm^2/kg^2'],
                  'Velocidade Orbital' : [Eq(vorb - sqrt((6.67E-20*M)/(0.001*Rorb)), 0), 'Um corpo orbita um corpo maior a uma distância da superfície muito menor que o raio do planeta. Sabe-se que:\nConstante universal de gravitação: 6.67x10^-20 km^3/skg'],
                  'Velocidade Orbital Terra': [Eq(vorb - sqrt((6.67E-20*6E24)/(6.4E3 + horb)) ,0), 'Um corpo descreve uma órbita a uma altura h da superfície da Terra. Sabe-se que:\n Massa da Terra = 6x10^24 kg\n Raio da Terra = 6400 km\n Constante universal de gravitação: 6.67x10^-20 km^3/skg'],
                  'Período Orbital' : [Eq(Torb - 2*pi*Rorb*(sqrt((0.001*Rorb)/(2.4E-16*M))) ,0), 'Um corpo orbita um corpo maior a uma distância da superfície muito menor que o raio do planeta. Sabe-se que:\n Constante universal de gravitação: 2.4x10^-16 km^3/hkg'],
                  'Período Orbital Terra': [Eq(Torb - (2*pi*(6.4E3 + horb))*sqrt((6.4E3 + horb)/(2.4E-16*6E24)), 0), 'Um corpo descreve uma órbita a uma altura h da superfície da Terra. Sabe-se que:\n Massa da Terra = 6x10^24 kg\n Raio da Terra = 6400 km\n Constante universal de gravitação: 2.4x10^-16 km^3/hkg']}
Gravitation_Quant = {deltaA1 : 'Área varrida no intervalo de tempo 1',
                     deltaA2 : 'Área varrida no intervalo de tempo 2', deltat1 : 'Intervalo de tempo 1',
                     deltat2 : 'Intervalo de tempo 2', Torb : 'Período orbital', Rm : 'Raio médio da órbita',
                     K : 'Constante Kepleriana', Fg : 'Força gravitacional',
                     m1 : 'Massa do corpo 1', m2 : 'Massa do corpo 2', d : 'Distância entre os corpos',
                     mc : 'Massa do corpo', gt : 'Campo gravitacional da Terra à altura h', g: 'Campo gravitacional na superfície do planeta',
                     Tk : 'Período Orbital', M : 'Massa do planeta', vorb : 'Velocidade orbital do planeta',
                     h: 'Altura do corpo em relação à superfície da Terra', R : 'Raio do planeta',
                     horb : 'Altura do corpo em relação à superfície', Rorb: 'Raio do planeta'}
Gravitation_Units = {deltaA1 : ['UA^2', (0, 300, 10)], deltaA2 : ['UA^2', (0, 300, 10)], deltat1 : ['meses', (0, 12, 1)],
                    deltat2 : ['meses', (0, 12, 1)], Torb : ['h', (0, 50, 1)], Rm : ['UA', (0, 300, 10)],
                    K : ['ano^2/UA^3', (0, 100, 10)], Fg : ['N', (0, 100, 10, 0, 2)], m1 : ['kg', (0, 100, 10, 5, 15)],
                    m2 : ['kg', (0, 100, 10, 5, 15)], d : ['m', (0, 100, 10, 0, 9)], mc : ['kg', (0, 100, 10, 10, 24)],
                    g : ['N/kg', (0, 200, 10)], gt : ['N/kg', (0, 100, 10)], Tk : ['anos', (0, 100, 1)],
                    M : ['kg', (0, 100, 10, 18, 30)], vorb : ['km/s', (1, 100, 10)], h : [ 'm', (1, 100, 10, 2, 6)],
                    R : [ 'm', (1, 100, 10, 5, 7)], horb : ['km', (1, 2000, 1)], Rorb : ['km', (1, 100, 10, 2, 5)]}
Gravitation_Pack = (Gravitation_Vars, Gravitation_Eq, Gravitation_Quant, Gravitation_Units)

### Equilibrium Pack 

T3, tau, tau1, tau2, tau3, d1, d2, d3, mb, lb, axis, theta1, theta2, taures = symbols('T3 tau tau1 tau2 tau3 d1 d2 d3 mb lb axis theta1 theta2 taures')
Equilibrium_Vars = {T1 : symbols('T1'), T2 : symbols('T2'), T3 : symbols('T3'), m : symbols('m'),
                    tau : symbols('tau'), F : symbols('F'), d : symbols('d'), tau1 : symbols('tau1'),
                    tau2 : symbols('tau2'), tau3 : symbols('tau3'), F1: symbols('F1'), F2 : symbols('F2'),
                    F3 : symbols('F3'), d1 : symbols('d1'), d2 : symbols('d2'), d3 : symbols('d3'), m1: symbols('m1'),
                    m2: symbols('m2'), mb : symbols('mb'), lb : symbols('lb'), axis : symbols('axis'),
                    theta1 : symbols('theta1'), theta2 : symbols('theta2'), theta : symbols('theta'), taures : symbols('taures')}
Equilibrium_Eq = {'Equilíbrio de ponto material Tensão':[Eq(T1*cos(rad(180-theta1)) + T2*cos(rad(theta2)),0),
                                                         'Um corpo está sendo mantido em equilíbrio por meio de dois cabos que formam ângulos theta com a horizontal. Sabe-se que:\ng = 10 m/s^2'],
                  'Equilíbrio de ponto material massa':[Eq(T1*sin(rad(theta1)) + T2*sin(rad(theta2)) - m*10,0),
                                                         'Um corpo está sendo mantido em equilíbrio por meio de dois cabos que formam ângulos theta com a horizontal. Sabe-se que:\ng = 10 m/s^2'],
                  'Torque':[Eq(tau - F*d*sin(rad(theta)),0), 'Uma força é aplicada em uma barra que é fixa em um eixo formando um ângulo theta com a linha que liga o ponto de aplicação e o eixo. Sabe-se que:'],
                  'Sistema Torque':[Eq(taures - tau1 - tau2 - tau3,0), 'Três forças causam três torques em uma barra. Sabe-se que:'],
                  'Sistema Torque equilíbrio':[Eq(tau1 + tau2 + tau3,0), 'Três forças causam três torques em uma barra mas ela não gira. Sabe-se que:'],
                  'Sistema Torque forças':[Eq(F1*d1 + F2*d2 + F3*d3,0), 'Três forças perpendiculares aos seus respectivos braços causam três torques em uma barra que não gira. Sabe-se que:'],
                  'Sistema Torque forças ângulo':[Eq(taures - F1*d1*sin(rad(theta1)) - F2*d2*sin(rad(theta2)),0), 'Duas forças causam dois torques em uma barra. Sabe-se que:'],
                  'Equilíbrio barra eixo':[Eq(m*10*axis + mb*10*(axis/lb)*(axis/2) - 10*(mb*(lb-axis)/(2*lb)),0), 'Uma barra se se equilibra sobre um eixo com uma massa adcional em sua extremidade esquerda. Sabe-se que:\ng = 10 m/s^2'],
                  'Gangorra':[Eq(10*m1*d1 - 10*m2*d2,0), 'Dois corpos estão em equilíbrio em uma gangorra. Sabe-se que:\ng = 10 m/s^2']}
Equilibrium_Quant = {T1 : 'Tração no cabo 1', T2 : 'Tração no cabo 2', T3 : 'Tração no cabo 3', m : 'Massa do corpo',
                     tau : 'Torque', F : 'Força aplicada', d : 'Braço da força', tau1 : 'Torque 1', tau2 : 'Torque 2',
                     tau3 : 'Torque 3', F1 : 'Força 1', F2 : 'Força 2', F3 : 'Força 3', d1 : 'Braço da força 1',
                     d2 : 'Braço da força 2', d3 : 'Braço da força 3', m1 : 'Massa do corpo 1', m2 : 'Massa do corpo 2',
                     mb : 'Massa da barra', lb : 'Comprimento da Barra',
                     axis : 'Distância da extremidade esquerda da barra ao eixo', theta1 : 'Ângulo de aplicação da força/tração 1',
                     theta2 : 'Ângulo de aplicação da força/tração 2',
                     theta : 'Ângulo entre a linha de ação da força e o a linha do ponto de aplicação ao eixo',
                     taures : 'Torque resultante'}
Equilibrium_Units = {T1 : ['N', (0, 300, 1)], T2 : ['N', (0, 300, 1)], T3 : ['N', (0, 400, 1)], m : ['kg', (0, 300, 10)],
                    tau : ['Nm', (0, 1000, 1)], F : ['N', (0, 400, 1)], d : ['m', (0, 40, 10)],
                    tau1 : ['Nm', (-100, 100, 1)], tau2 : ['Nm', (-100, 100, 1)], tau3 : ['Nm', (-100, 100, 1)],
                    F1 : ['N', (-40, 40, 1)], F2 : ['N', (-40, 40, 1)], F3 : ['N', (-40,40, 1)],
                    d1 : ['m', (0, 40, 10)], d2 : ['m', (0, 40, 10)], d3 : ['m', (0, 40, 10)],
                    m1 : ['kg', (0, 40, 1)], m2 : ['kg', (0, 40, 1)], mb : ['kg', (0, 40, 10)],
                    lb : ['m', (20, 40, 20)], axis : ['m', (0, 20, 40)], theta1 : ['°', (0, 60, 1)],
                    theta2 : ['°', (0,70, 1)], theta : ['°', (0, 180, 1)], taures : ['Nm', (-500, 500, 1)]}
Equilibrium_Pack = (Equilibrium_Vars, Equilibrium_Eq, Equilibrium_Quant, Equilibrium_Units)

### Hydrostatics Pack

p, A, pPa, patm, pcmHg, ppsi, rho, V, ph, phatm, pt, p1, p2, A1, A2, da, ha, db, hb, E, Vd, pct = symbols('p A pPa patm pcmHg ppsi rho V ph phatm pt p1 p2 A1 A2 da ha db hb E Vd pct')
Hydrostatics_Vars = {p: symbols('p'), A : symbols('A'), pPa : symbols('pPa'), patm : symbols('patm'), pcmHg : symbols('pcmHg'),
                        ppsi: symbols('ppsi') , rho : symbols('rho'), V : symbols('V'), ph : symbols('ph'), phatm : symbols('phatm'),
                        pt : symbols('pt'), p1 : symbols('p1'), Normal : symbols('Normal'), A1 : symbols('A1'), A2 : symbols('A2'), da : symbols('da'),
                        ha : symbols('ha'), db : symbols('db'), hb : symbols('hb'), E : symbols('E'), Vd : symbols('Vd'), F : symbols('F'),
                        m : symbols('m'), h : symbols('m'), d : symbols('d'), F1 : symbols('F1'), F2 : symbols('F2'), pct : symbols('pct') }
Hydrostatics_Eq = {'Pressão':[Eq(p - F/A,0),'Uma força é aplicada sobre determinada área, gerando pressão. Sabe-se que:\n'],
                    'Pascal - atm':[Eq(pPa/1E5 - patm,0),'Realize a conversão entre Pascal e atm. Sabe-se que:\n'],
                    'Pascal - cmHg':[Eq(pPa/1E5 - pcmHg/76,0),'Realize a conversão entre Pascal e cmHg. Sabe-se que:\n'],
                    'Pascal - psi':[Eq(pPa/1E5 - ppsi/14,0),'Realize a conversão entre Pascal e psi. Sabe-se que:\n'],
                    'atm - cmHg':[Eq(patm - pcmHg/76,0),'Realize a conversão entre atm e cmHg. Sabe-se que:\n'],
                    'atm - psi':[Eq(patm - ppsi/14,0),'Realize a conversão entre atm e psi. Sabe-se que:\n'],
                    'cmHg - psi':[Eq(pcmHg/76 - ppsi/14,0),'Realize a conversão entre cmHg e psi. Sabe-se que:\n'],
                    'Densidade':[Eq(rho - m/V,0),'Um corpo com determinada massa e volume possui densidade rho. Sabe-se que:\n'],
                    'Pressão mergulho':[Eq(phatm - (1 + h/10),0),'Um mergulhador está a uma profundidade h, sentindo uma pressão resultante. Sabe-se que:\npatm = 1 atm'],
                    'Pressão hidrostática':[Eq(ph - d*10*h,0),'Um liquido de densidade d está em repouso. Sabe-se que:\ng = 10 m/s^2'],
                    'Pressão total':[Eq(pt - (1E5 + d*10*h),0),'Um mergulhador está a uma profundidade h, sentindo uma pressão resultante. Sabe-se que:\ng = 10 m/s^\npatm = 10^5 Pa'],
                    'Princípio de Pascal':[Eq(F1/A1 - F2/A2,0),'Um tubo comunicante possui dois êmbolos de áreas diferentes. Sabe-se que:\n'],
                    'Princípio de Pascal pressão':[Eq(p1 - F2/A2,0),'Um tubo comunicante possui dois êmbolos de áreas diferentes. Sabe-se que:\n'],
                    'Líquidos imiscíveis':[Eq(da*ha - db*hb,0), 'Em um vaso comunicante, dois líquidos estão em repouso sem se misturar. Sabe-se que:\n'],
                    'Empuxo':[Eq(E - d*10*Vd,0), 'Um corpo repousa parcialmente submerso em um líquido. Sabe-se que:\ng = 10 m/s^2'],
                    'Empuxo no fundo':[Eq(d*10*V + Normal - m*10,0), 'Um corpo repousa no fundo de um recipiente com um líquido.Sabe-se que:\ng = 10 m/s^2'],
                    'Empuxo equilíbrio':[Eq(d*V - m,0), 'Um corpo repousa em equilíbrio no meio de um recipiente líquido. Sabe-se que:\n'],
                    'Empuxo boiando':[Eq(rho/d - pct/100,0), 'Um corpo boia parcialmente submerso em um líquido . Sabe-se que:\n'],
                    'Empuxo boiando massa':[Eq(m - d*V*pct/100,0), 'Um corpo boia parcialmente submerso em um líquido. Sabe-se que:\n']}
Hydrostatics_Quant = {p: 'Pressão', A : 'Área', pPa : 'Pressão em Pa', patm : 'Pressão em atm', pcmHg : 'Pressão em cmHg',
                        ppsi: 'Pressão em psi' , rho : 'Densidade do corpo', V : 'Volume do corpo', ph : 'Pressão hidrostática', phatm : 'Pressão à profundidade h',
                        pt : 'Pressão total', p1 : 'Pressão no êmbolo 1', Normal : 'Força Normal de apoio', A1 : 'Área do êmbolo 1', A2 : 'Área do êmbolo 2',
                        da : 'Densidade do líquido A', ha : 'Altura da coluna do líquido A em relação a linha de separação dos líquidos', db : 'Densidade do líquido B',
                        hb : 'Alturea da coluna do líquido B em relação à linha de separação dos líquidos', E : 'Empuxo', Vd : 'Volume submerso do corpo',
                        F : 'Força aplicada', m : 'Massa do corpo', h : 'Profundidade', d : 'Densidade do líquido', F1 : 'Força aplicada no êmbolo 1',
                        F2 : 'Força aplicada no êmbolo 2' , pct : 'Porcentagem do volume do corpo que está submerso' }
Hydrostatics_Units = {p : ['Pa', (0, 50, 1)], A : ['m^2', (0, 100, 100)], pPa : ['Pa', (0, 1000000, 1)],
                    patm : ['atm', (0, 100, 10)], pcmHg : ['cmHg', (0, 1000, 1)], ppsi : ['psi', (0, 200, 1)],
                    rho : ['kg/m^3', (0, 5000, 1)], V : ['m^3', (0, 100, 100)], ph : ['Pa', (1000, 100000, 1)],
                    phatm : ['atm', (10, 100, 10)], pt : ['Pa', (100000, 1000000, 1)], p1 : ['Pa', (0, 50, 1)],
                    Normal : ['N', (0, 50, 1)], A1 : ['m^2', (0, 50, 100)], A2 : ['m^2', (50, 200, 100)],
                    da : ['g/cm^3', (0, 250, 100)], ha : ['cm', (100, 200, 1)], db : ['g/cm^3', (250, 500, 100)],
                    hb : ['cm', (0, 100, 1)], E : ['N', (0, 100, 1)], Vd : ['m^3', (0, 100, 100)], F : ['N', (0, 100, 10)],
                    m : ['kg', (0, 100, 10)], h : ['m', (0, 100, 10)], d : ['kg/m^3', (0, 5000, 1)], F1 : ['N', (0, 50, 10)],
                    F2 : ['N', (0, 50, 10)], pct : ['%', (0, 100, 1)]}
Hydrostatics_Pack = (Hydrostatics_Vars, Hydrostatics_Eq, Hydrostatics_Quant, Hydrostatics_Units)

tau, tau1, tau2, tau3, deltaS1, deltaS2, deltaS3, theta3, eta, taud, taut, Pd, Pt, Ec, Epg, Epe, Eci, Epi, Ecf, Epf, vi, hi, hf= symbols('tau, tau1, tau2, tau3, deltaS1, deltaS2, deltaS3, theta3, eta, taud, taut, Pd, Pt, Ec, Epg, Epe, Eci, Epi, Ecf, Epf, vi, hi, hf', real=True)
Energy_Vars = {tau: symbols('tau'), F: symbols('F'), deltaS: symbols('deltaS'), theta: symbols('theta'), tau1: symbols('tau1'), tau2: symbols('tau2'),
                 tau3: symbols('tau3'), F1: symbols('F1'), F2: symbols('F2'), F3: symbols('F3'), deltaS1: symbols('deltaS1'), deltaS2: symbols('deltaS2'),
                 deltaS3 : symbols('deltaS3'), theta1 : symbols('theta1'), theta2 : symbols('theta2'), theta3 : symbols('theta3'), P : symbols('P'),
                 deltat : symbols('deltat'), v : symbols('v'), eta : symbols('eta'), taud : symbols('taud'), taut : symbols('taut'), Pd : symbols('Pd'),
                 Pt : symbols('Pt'), Ec : symbols('Ec'), v0 : symbols('v0'), m : symbols('m'), Epg : symbols('Epg'), h : symbols('h'), Epe : symbols('Epe'),
                 k : symbols('k'), x : symbols('x'), Eci : symbols('Eci'), Epi : symbols('Epi'), Ecf : symbols('Ecf'), Epf : symbols('Epf'), vi : symbols('vi'), 
                 hi : symbols('hi'), vf : symbols('vf'), hf : symbols('hf')}
Energy_Eq = {'Trabalho':[Eq(tau - F*deltaS*cos(rad(theta)),0),'Uma força é aplicada sobre que se desloca. Sabe-se que:\n'],
                'Trabalho total':[Eq(taut - tau1 - tau2 - tau3,0),'Um corpo sofre trabalhos de várias forças. Sabe-se que:\n'],
                'Trabalho da força resultante':[Eq(tau - ((F1*cos(rad(theta1)) + F2*cos(rad(theta2)) + F3*cos(rad(theta3)))*deltaS),0),'Um corpo sofre trabalho de várias forças enquanto se desloca. Sabe-se que:\n'],
                'Trabalho trajetória':[Eq(tau - (F*deltaS1*cos(rad(theta1)) + F*deltaS2*cos(rad(theta2)) + F*deltaS3*cos(rad(theta3))),0),'Um corpo sofre a ação de uma força enquanto descreve uma trajetória não regular. Sabe-se que:\n'],
                'Potência trabalho':[Eq(P - taut/deltat,0),'Um trabalho é realizado sobre um corpo em um determinado tempo. Sabe-se que:\n'],
                'Potência Força':[Eq( P - F*v,0),'Uma força realiza trabalho em um corpo com velocidade constante. Sabe-se que:\n'],
                'Rendimento trabalho':[Eq(eta - (100 - 100*taud/taut),0),'Parte de um trabalho realizado é dissipado. Sabe-se que:\n'],
                'Rendimento Potência':[Eq(eta - (100 - 100*Pd/Pt),0),'Parte da potência desenvolvida por um trabalho é dissipada. Sabe-se que:\n'],
                'Energia Cinética':[Eq(Ec - (0.5*m*v**2),0),'Um corpo se desloca com velocidade v. Sabe-se que:\n'],
                'Trabalho e Energia':[Eq(tau - (0.5*m*(vf**2 - vi**2)),0),'Um corpo tem sua velocidade alterada ao sofrer trabalho. Sabe-se que:\n'],
                'Trabalho e Energia 2':[Eq(F*deltaS - (0.5*m*(v**2 - v0**2)),0),'Ao aplicar uma força sobre um corpo, sua velocidade se altera enquanto se desloca. Sabe-se que:\n'],
                'Energia Potencial Gravitacional':[Eq(Epg - 10*m*h,0),'Um corpo se encontra à uma altura h da superfície do solo. Sabe-se que:\ng = 10 m/s^2\n'],
                'Energia Potencial Elástica':[Eq(Epe - (0.5*k*x**2),0),'Um corpo se encontra preso a uma mola enquanto ela é esticada/comprimida. Sabe-se que:\n'],
                'Conservação de Energia':[Eq(10*h - 0.5*v**2,0),'Um corpo parte de uma altura h até o chão, chegando com velocidade v. Sabe-se que:\ng = 10 m/s^2\n'],
                'Conservação de Energia 2':[Eq(k*x**2 - m*v**2,0),'Um corpo preso a uma mola comprimida/esticada é solto e adquire velocidade máxima v. Sabe-se que:\n'],
                'Conservação de Energia 3':[Eq(10*m*h - 0.5*k*x**2,0),'Um corpo cai de uma altura h e é amortecido por uma mola que se comprime. Sabe-se que:\ng = 10 m/s^2\n'],
                'Conservação de Energia 4':[Eq(Eci + Epi - Ecf - Epf,0),'Um corpo sofre mudanças em suas energias potencial e cinética em um campo conservativo. Sabe-se que:\n'],
                'Conservação de energia 5':[Eq(0.5*vi**2 + 10*hi - 0.5*vf**2 - 10*hf,0),'Um corpo muda sua posição vertical e sua altura enquanto se desloca em um campo conservativo. Sabe-se que:\ng = 10 m/s^2']}
Energy_Quant = {tau : 'Trabalho', F : 'Força', deltaS: 'Deslocamento', theta: 'Ângulo entre Força e Deslocamento', tau1: 'Trabalho 1',
                tau2 : 'Trabalho 2', tau3 : 'Trabalho 3', F1 : 'Força 1', F2 : 'Força 2', F3 : 'Força 3', deltaS1 : 'Deslocamento 1',
                deltaS2 : 'Deslocamento 2', deltaS3 : 'Deslocamento 3', theta1 : 'Ângulo 1', theta2 : 'Ângulo 2', theta3 : 'Ângulo 3',
                P : 'Potência', deltat : 'Tempo', v : 'Velocidade', eta : 'Rendimento', taud : 'Trabalho dissipado', taut : 'Trabalho total',
                Pd : 'Potência dissipada', Pt : 'Potência total', Ec : 'Energia Cinética', v0 : 'Velocidade inicial',m : 'Massa', Epg : 'Energia Potencial Gravitacional',
                h : 'Altura', Epe : 'Energia Potencial Elástica', k : 'Constante elástica', x : 'Distensão da mola', Eci : 'Energia Cinética inicial',
                Epi : 'Energia Potencial inicial', Ecf : 'Energia cinética final', Epf : 'Energia potencial final', vi : 'Velocidade inicial',
                hi: 'Altura inicial', vf : 'Velocidade final', hf : 'Altura final' }
Energy_Units = {tau : ['J', (-300, 300, 1)], F : ['N', (1, 100, 1)], deltaS : ['m', (1, 100, 10)], theta : ['°', (0, 180, 1)],
                tau1 : ['J', (-100, 100, 1)], tau2 : ['J', (-100, 100, 1)], tau3 : ['J', (-100, 100, 1)], F1 : ['N', (0, 40, 1)],
                F2 : ['N', (0, 40, 1)], F3 : ['N', (0, 40, 1)], deltaS1 : ['m', (1, 50, 10)] , deltaS2 : ['m', (1, 50, 10)],
                deltaS3 : ['m', (1, 50, 10)], theta1 : ['°', (0, 180, 1)], theta2 : ['°', (0, 180, 1)], theta3 : ['°', (0, 180, 1)],
                P : ['W', (0, 500, 1)], deltat : ['s', (1, 50, 10)], v : ['m/s', (1, 100, 10)], eta : ['%', (1, 100, 1)],
                taud : ['J', (1, 250, 1)], taut : ['J', (250, 300, 1)], Pd : ['W', (1, 400, 1)], Pt : ['W', (400, 500, 1)],
                Ec : ['J', (1, 300, 1)], v0 : ['m/s', (1, 30, 10)], m : ['kg', (1, 100, 10)], Epg : ['J', (1, 300, 1)],
                h : ['m', (1, 100, 10)], Epe : ['J', (1, 300, 1)], k : ['N/m', (1, 1000, 10)], x : ['m', (1, 100, 100)],
                Eci : ['J', (1, 300, 1)], Epi : ['J', (1, 300, 1)], Ecf : ['J', (1, 300, 1)], Epf : ['m', (1, 300, 1)],
                vi : ['m/s', (1, 200, 10)], hi : ['m', (1, 100, 10)], vf : ['m/s', (1, 200, 1)], hf : ['m', (1, 100, 10)]}
Energy_Pack = (Energy_Vars, Energy_Eq, Energy_Quant, Energy_Units)

### Pack momentum ###

Q, Qi, Qf, deltaQ, Q1, Q2, v1i, v1f, v2i, v2f, vrel, I = symbols('Q Qi Qf deltaQ Q1 Q2 v1i v1f v2i v2f vrel I')
Momentum_Vars = {Q : symbols('Q'), Q1 : symbols('Q1'), Q2 : symbols('Q2'), Qi : symbols('Qi'), Qf : symbols('Qf'), deltaQ : symbols('deltaQ'),
                m : symbols('m'), m1 : symbols('m1'), m2 : symbols('m2'), v : symbols('v'), v1 : symbols('v1'), v2 : symbols('v2'),
                v1i : symbols('v1i'), v2i : symbols('v2i'), v1f : symbols('v1f'), v2f : symbols('v2f'), vrel : symbols('vrel'),
                I : symbols('I'), F : symbols('F'), deltat : symbols('deltat'), vf : symbols('vf'), theta : symbols('theta')}
Momentum_Eq = {'Momento':[Eq(Q - m*v,0),'Um corpo com massa m se move com velocidade v. Sabe-se que:\n'],
                'Colisão inelástica':[Eq(m1*v1 - (m1 + m2)*vf,0),'Dois corpos se chocam e se mantem unidos após a colisão. Sabe-se que:\n'],
                'Conservação do momento':[Eq(m1*v1i + m2*v2i - (m1*v1f + m2*v2f),0),'Dois corpos se chocam e se separam em uma colisão parcialmente elástica. Sabe-se que:\n'],
                'Colisão elástica 1':[Eq((m1 - m2)*v1i - ((m1 + m2)*v1f),0),'Um corpo se choca com outro corpo em repouso em uma colisão perfeitamente elástica. Sabe-se que:\n'],
                'Colisão elástica 2':[Eq(2*m1*v1i - ((m1 + m2)*v2f),0),'Um corpo se choca com outro corpo em repouso em uma colisão perfeitamente elástica. Sabe-se que:\n'],
                'Colisão elástica 3':[Eq((m1 - m2)*(v1i - v2i) - ((m1 + m2)*(v1i + v1f - v2f)),0),'Dois corpos se chocam em uma colisão elástica direta. Sabe-se que:\n'],
                'Colisão elástica 4':[Eq(2*m1*(v1i - v2i) - ((m1 + m2)*(v2f - v2i)),0),'Dois corpos se chocam em uma colisão elástica direta. Sabe-se que:\n'],
                'Momento 2D 1':[Eq((m1*v1) - ((m1 +m2)*vf*cos(rad(theta))),0),'Um corpo se move sobre o eixo horizontal e se choca com outro corpo que se move sobre o eixo vertical numa colisão perfeitamente inelástica. Sabe-se que:\n'],
                'Momento 2D 2':[Eq(rad(theta) - (atan((m2*v2)/(m1/v1))),0),'Dois corpos se movem em sentido perdendicular um com o outro, após se chocarem, permanecem unidos. Sabe-se que:\n'],
                'Impulso 1':[Eq(I - F*deltat,0),'Um força age sobre um corpo por um determinado tempo. Sabe-se que:\n'],
                'Impulso 2':[Eq(I - (Qf - Qi),0),'Uma força faz com que o momento de um corpo varie. Sabe-se que:\n'],
                'Impulso 3':[Eq((Qf - Qi) - F*deltat,0),'Uma força faz com que o mometo de um corpo varie. Sabe-se que:\n']}
Momentum_Quant = {Q : 'Momento', Q1 : 'Momento do corpo 1', Q2 : 'Momento do corpo 2', Qi : 'Momento inicial', Qf : 'Momento final',
                    deltaQ : 'Variação do momento', m : 'Massa', m1 : 'Massa do corpo 1', m2 : 'Massa do corpo 2', v : 'Velocidade',
                    v1 : 'Velocidade do corpo 1', v2 : 'Velocidade do corpo 2', v1i : 'Velocidade inicial do corpo 1',
                    v2i : 'Velocidade inicial do corpo 2', v1f : 'Velocidade final do corpo 1', v2f : 'Velocidade final do corpo 2',
                    vrel : 'Velocidade relativa entre os corpos', I : 'Impulso', F : 'Força', deltat : 'Intervalo de tempo',
                    vf : 'Velocidade final do conjunto', theta : 'Ângulo do momento com a horizontal'}
Momentum_Units = {Q : ['kgm/s', (1, 100, 1) ], Q1 : ['kgm/s', (25, 100, 1) ], Q2 : ['kgm/s', (1, 75, 1) ], Qi : ['kgm/s', (1, 100, 1) ],
                    Qf : ['kgm/s', (-100, 100, 1) ], deltaQ: ['kgm/s', (-200, 200, 1) ], m : ['kg', (1, 100, 10) ],
                    m1 : ['kg', (1, 100, 10) ], m2 : ['kg', (1, 100, 10) ], v : ['m/s', (-100, 100, 10) ],
                    v1 : ['m/s', (1, 100, 10) ], v2 : ['m/s', (1,100, 10) ], v1i : ['m/s', (1, 100, 10) ],
                    v2i : ['m/s', (-100, -1, 10) ], v1f : ['m/s', (-100, -1, 10) ], v2f : ['m/s', (1, 100, 10) ],
                    vrel : ['m/s',(1, 200, 10) ], I : ['Ns', (1, 200, 1) ], F : ['N', (1, 200, 10) ], deltat : ['s', (1, 100, 10) ],
                    vf : ['m/s', (50, 200, 10) ], theta : ['°', (0, 90, 1)]}
Momentum_Pack = (Momentum_Vars, Momentum_Eq, Momentum_Quant, Momentum_Units)

### Pack thermology and heat ###

Tx, Fx, Ex, deltaVliq, mg = symbols('Tx Fx Ex deltaVliq mg')
TC, TF, TK, deltaL, L, L0, deltaT, deltaA, A0, beta, deltaV, V0, gamma, Vliq, Vap, Vrec, gammaliq, gammaap= symbols('TC TF TK deltaL L L0 deltaT deltaA A0 beta deltaV V0 gamma Vliq Vap Vrec gammaliq gammaap')
gammarec, C, c, La, ca, cb, Tf, T0a, T0b, cc, mag, T0c, T0ag, Lac, Tf, mcq, ccq, T0cq, T0g = symbols('gammarec C c La ca cb Tf T0a T0b cc mag T0c T0ag Lac Tf mcq ccq T0cq T0g')
Heat_Vars = {TC : symbols('TC'), Tx : symbols('Tx'), Fx : symbols('Fx'), Ex: symbols('Ex'), alpha : symbols('alpha'),
            TF : symbols('TF'), TK : symbols('TK'), deltaL : symbols('deltaL'), L : symbols('L'), deltaVliq : symbols('deltaVliq'),
            L0 : symbols('L0'), deltaT : symbols('deltaT'), deltaA : symbols('deltaA'), A0 : symbols('A0'),
            beta : symbols('beta'), deltaV : symbols('deltaV'), V0 : symbols('V0'), gamma : symbols('gamma'),
            Vliq : symbols('Vliq'), Vap : symbols('Vap'), Vrec : symbols('Vrec'), gammaliq : symbols('gammaliq'),
            gammaap : symbols('gammaap'), gammarec : symbols('gammarec'), C : symbols('C'), c : symbols('c'),
            La : symbols('La'), ca : symbols('ca'), cb : symbols('cb'), Tf : symbols('Tf'), T0a : symbols('T0a'),
            T0b : symbols('T0b'), cc : symbols('cc'), mag : symbols('mag'), T0c : symbols('T0c'), m: symbols('m'),
            T0ag : symbols('T0ag'), Lac : symbols('Lac'), Tf : symbols('Tf'), mcq : symbols('mcq'), mg : symbols('mg'),
            ccq : symbols('ccq'), T0cq : symbols('T0cq'), T0g : symbols('T0g'), Q : symbols('Q'), A : symbols('A')}
Heat_Eq = {'Celsius/Farenheit':[Eq((TC/5) - ((TF-32)/9),0),'Converta a temperatura entre graus Celsius e Farenheit. Sabe-se que:\n'],
            'Celsius/Kelvin':[Eq(TC - TK + 273,0),'Converta a temperatura entre graus Celsius e Kelvin. Sabe-se que:\n'],
            'Farenheit/Kelvin':[Eq((TF-32)/9 - (TK-273)/5,0),'Converta a temperatura entre graus Farenheit e Kelvin. Sabe-se que:\n'],
            'Conversão genérica Celsius':[Eq((Tx - Fx)/Ex-Fx - TC/100,0),'Uma temperatura é medida em determinada gradação °X. Sabe-se que:\n'],
            'Conversão genérica Farenheit':[Eq((Tx-Fx)/(Ex-Fx) - (TF-32)/180 ,0),'Uma temperatura é medida em determinada gradação °X. Sabe-se que:\n'],
            'Conversão genérica Celsius':[Eq((Tx-Fx)/(Ex-Fx) - (TK-273)/100,0),'Uma temperatura é medida em determinada gradação °X. Sabe-se que:\n'],
            'Dilatação linear 1':[Eq(deltaL - L0*alpha*deltaT,0),'Um corpo sofre dilatação térmica ao ser aquecido. Sabe-se que:\n'],
            'Dilatação linear 2':[Eq(L - L0*(1 + alpha*deltaT),0),'Um corpo sofre dilatação térmica ao ser aquecido. Sabe-se que:\n'],
            'Dilatação superficial 1':[Eq(deltaA - A0*beta*deltaT,0),'Uma superfície sofre dilatação térmica ao ser aquecida. Sabe-se que:\n'],
            'Dilatação superficial 2':[Eq(A - A0*(1 + beta*deltaT),0),'Uma superfíce sofre dilatação térmica ao ser aquecida. Sabe-se que:\n'],
            'Dilatação superficial 3':[Eq(deltaA - A0*2*alpha*deltaT,0),'Uma superfíce sofre dilatação térmica ao ser aquecida. Sabe-se que:\n'],
            'Dilatação volumétrica 1':[Eq(deltaV - V0*gamma*deltaT,0),'Um corpo sofre dilatação térmica ao ser aquecido. Sabe-se que:\n'],
            'Dilatação volumétrica 2':[Eq(V - V0*(1+gamma*deltaT),0),'Um corpo sofre dilatação térmica ao ser aquecido. Sabe-se que:\n'],
            'Dilatação volumétrica 3':[Eq(deltaV - V0*3*alpha*deltaT,0),'Um corpo sofre dilatação térmica ao ser aquecido. Sabe-se que:\n'],
            'Dilatação líquidos 1':[Eq(deltaVliq - Vliq*gammaliq*deltaT,0),'Um líquido sofre dilatação ao ser aquecido. Sabe-se que:\n'],
            'Dilatação líquidos 2':[Eq(deltaVliq - Vap - Vrec,0),'Um líquido é aquecido enquanto está em um recipiente completamente cheio. Sabe-se que:\n'],
            'Dilatação líquidos 3':[Eq(deltaVliq - Vliq*((Vap)/(Vliq*deltaT) + gammarec)*deltaT,0),'Um líquido é aquecido enquanto está em um recipiente completamente cheio. Sabe-se que:\n'],
            'Capacidade térmica':[Eq(C - Q/deltaT,0),'Um corpo muda sua temperatura ao trocar calor. Sabe-se que:\n'],
            'Calor específico':[Eq(Q - m*c*deltaT,0),'Um corpo muuda sua temperatura ao trocar calor. Sabe-se que:\n'],
            'Calor latente':[Eq(Q - m*La,0),'Um corpo troca calor até completar a mudança de fase. Sabe-se que:\n'],
            'Trocas de calor 1':[Eq(ma*ca*(Tf - T0a) - mb*cb*(Tf - T0b),0),'Dois corpos a e b inicialmente a temperaturas diferentes trocam calor em um sistema isolado. Sabe-se que:\n'],
            'Trocas de calor 2':[Eq(m*cc*(Tf - T0c) - ma*(Tf - T0ag),0),'Um corpo é submerso à uma temperatura diferente da água. Sabe-se que:\nCalor específico da água = 1 cal/g°C'],
            'Trocas de calor 3':[Eq(Q - m*La - m*cc*(deltaT),0),'Um corpo muda de fase e procede trocando calor. Sabe-se que:\n'],
            'Trocas de calor 4':[Eq(Q - mg*(80 + Tf),0),'Um bloco de gelo a 0°C começa a receber calor. Sabe-se que:\nCalor latente do gelo = 80 cal/g\ncalor específico da água = 1 cal/g°C'],
            'Trocas de calor 5':[Eq(mcq*ccq*(Tf - T0cq) - mg*(0.5*T0g + 80 + Tf),0),'Um corpo aquecido é posto em contato com um bloco de gelo. Sabe-se que:\ncalor específico do gelo = 0.5 cal/g°C\nCalor latente do gelo = 80 cal/g\nCalor específico da água = 1 cal/g°C']
            }
Heat_Quant = {TC : 'Temperatura em graus Celsius', TF : 'Temperatura em graus Farenheit', TK : 'Temperatura em Kelvin',
            deltaL : 'Variação de comprimento', L : 'Comprimento final', L0 : 'Comprimento inicial', deltaT : 'Variação de temperatura',
            deltaA : 'Variação de área', A0 : 'Área inicial', Tx: 'Temperatura em graus X', Fx :'Ponto de fusão da água em graus X',
            Ex: 'Ponto de ebulição da água em graus X', alpha : 'Coeficiente de dilatação linear', deltaVliq : 'Variação de volume do líquido',
            beta : 'Coeficiente de dilatação superficial', deltaV : 'Variação de volume', V0 : 'Volume inicial', gamma : 'Coeficiente de dilatação volumétrica',
            Vliq : 'Volume do líquido', Vap : 'Volume dilatado aparente', Vrec : 'Volume dilatado do recipiente',
            gammaliq : 'Coeficiente de dilatação volumétrica do líquido', gammaap : 'Coeficiente de dilatação volumétrica aparente do líquido',
            gammarec : 'Coeficiente de dilatação volumétrica do recipiente', C : 'Capacidade térmica', c : 'Calor específico',
            La : 'Calor latente', ca : 'Calor específico do corpo A', cb : 'Calor específico do corpo B', Tf : 'Temperatura final',
            T0a : 'Temperatura inicial do corpo A', T0b : 'Temperatura inicial do corpo B', cc : 'Calor específico do corpo',
            mag : 'Massa de água', T0c : 'Temperatura inicial do corpo', T0ag : 'Temperatura inicial da água',
            Lac : 'Calor latente do corpo', mcq : 'Massa do corpo aquecido', ccq : 'Calor específico do corpo aquecido',
            T0cq : 'Temperatura inicial do corpo aquecido', T0g : 'Temperatura inicial do gelo', m : 'Massa',
            mg: 'Massa de gelo', Q : 'Calor trocado' }
Heat_Units = {TC : ['°C', (-100, 200,1)], Tx : ['°X', (-200, 400,1)], Fx : ['°X', (-200, 100, 1)], Ex : ['°X', (100, 400, 1)],
            alpha : ['/°C', (1, 50, 1, -6, -5)], TF : ['°F', (-200, 300, 1)], TK : ['K', (0, 600, 1)],
            deltaL : ['m', (1, 100, 10, -4, -1)], L : ['m', (1, 10, 1, -3,  0)], deltaVliq : ['l', (1, 100, 10, -2, 1)],
            L0 : ['m', (1, 10, 1, -2, -1)], deltaT : ['°C', (-100, 100, 1)], deltaA : ['m^2', (1, 100, 10, -3, 0)],
            A0 : ['m^2', (1, 10, 1, -4, -2)], A: ['m^2', (1, 10, 1, -3, 1)],  beta : ['/°C', (1, 100, 1, -6, -5)],
            deltaV : ['m^3', (1, 10, -2, 1)], V0 : ['m^3', (1, 10, 1, -6, -1 )], gamma : ['/°C', (1, 150, 1, -6, -5)],
            Vliq : ['m^3', (1, 10, 1, -5, 0)], Vap : ['m^3', (1, 10, 1, -6, -3)], Vrec : ['m^3', (1, 10, 1, -5, 0)],
            gammaliq : ['/°C', (1, 150, 1, -4, -3)], gammaap : ['/°C', (1, 100, 1, -4, -3)],
            gammarec : ['/°C', (1, 150, 1, -6, -5)], C : ['cal/°C', (1, 500, 1)], c : ['cal/g°C', (1, 200, 100)],
            La : ['cal/g', (1, 300, 10)], ca : ['g', (100, 10000, 1)], cb : ['cal/g°C', (100, 200, 100)],
            Tf : ['°C', (-100, 200, 1)], T0a : ['°C', (50, 200, 1)], T0b : ['°C', (-100, 50, 1)],
            cc : ['cal/g°C', (1, 200, 100)], mag : ['g', (100, 10000, 1)], T0c : ['°C', (-100, 200, 1)], 
            m : ['g', (100, 10000, 1)], T0ag : ['°C', (1, 99, 1)], Lac : ['cal/g', (1, 300, 10)],
            mcq : ['g', (100, 10000, 1)], mg : ['g', (100, 10000, 1)], ccq : ['cal/g°C', (1, 200, 100)],
            T0cq : ['°C', (50, 200, 1)], T0g : ['°C', (-150, 1, 1)], Q : ['cal', (-10000, 10000, 1)]}
Heat_Pack = (Heat_Vars, Heat_Eq, Heat_Quant, Heat_Units)


### Thermodynamics pack

P0, Vi, Ti, Pf, Vf, Ecm, deltaU, Qq, Tq, Tfr, e, etac, emax = symbols('P0 Vi Ti Pf Vf Ecm deltaU Qq Tq Tfr e etac emax')
Thermo_Vars = {
    P0 : symbols('P0'), Vi : symbols('Vi'), Ti : symbols('Ti'), Pf : symbols('Pf'),
    Vf : symbols('Vf'), Ecm : symbols('Ecm'), deltaU : symbols('deltaU'), Qq : symbols('Qq'), Tq : symbols('Tq'),
    P : symbols('P'), V : symbols('V'), n : symbols('n'), T : symbols('T'), Tf : symbols('Tf'), tau : symbols('tau'),
    deltaV : symbols('deltaV'), deltaT : symbols('deltaT'), Q : symbols('Q'), Qf : symbols('Qf'),
    deltaQ : symbols('deltaQ'), S : symbols('S'), eta : symbols('eta'), Tfr : symbols('Tfr'), e: symbols('e'),
    etac : symbols('etac'), emax : symbols('emax')
    }
Thermo_Eqs = {
    'Transformação isotérmica' : [Eq(P0*Vi - (Pf*Vf),0), 'Um gás sofre uma transformação sem mudar sua temperatura. Sabe-se que:\n'],
    'Transformação isobárica' : [Eq(Vi/Ti - (Vf/Tf),0), 'Um gás sofre uma transformação à pressão constante. Sabe-se que:\n'],
    'Transformação isocórica' : [Eq(P0/Ti - (Pf/Tf),0), 'Um gás preso em um recipiente rígido sofre uma transformação. Sabe-se que:\n'],
    'Gás ideal 1' : [Eq(P*V - (n*0.082*T),0), 'Deseja-se saber uma característica de um gás ideal. Sabe-se que:\nConsante universal dos gases = 0.082 atmL/molK\n'],
    'Gás ideal 2' : [Eq((P0*Vi)/Ti - ((Pf*Vf)/Tf),0), 'Um gás ideal sofre uma transformação. Sabe-se que:\n'],
    'Trabalho de um gás' : [Eq(tau - (P*(deltaV)),0), 'Um gás sofre uma transformação à pressão constante. Sabe-se que:\n'],
    'Energia cinética média' : [Eq(Ecm - ((3/2)*(n*8.31*T)),0), 'Deseja-se saber uma característica de um gás ideal. Sabe-se que:\nConstante universal dos gases = 8.31 J/molK\n'],
    'Energia interna 1' : [Eq(deltaU - ((3/2)*(n*8.31*(Tf-Ti))),0), 'Deseja-se saber uma característica de um gás ideal. Sabe-se que:\nConstante universal dos gases = 8.31 J/molK\n'],
    'Energia interna 2' : [Eq(deltaU - Q + (P*(deltaV)),0), 'Um gás sofre uma transformação à pressão constante. Sabe-se que:\n'],
    'Calor 1' : [Eq(Q - ((3/2)*(n*8.31*(Tf - Ti))),0), 'Um gás preso em um recipiente rígido sofre uma transformação. Sabe-se que:\nConstante universal dos gases = 8.31 J/molK\n'],
    'Calor 2' : [Eq(Q - (P*(Vf - Vi)),0), 'Um gás sofre uma transformação sem mudar sua temperatura. Sabe-se que:\n'],
    'Transformação adiabática' : [Eq((3/2)*(n*8.31*(Tf-Ti)) + tau, 0), 'Um gás sofre uma transformação sem trocar calor com o ambiente. Sabe-se que:\nConstante universal dos gases = 8.31 J/molK\n'],
    'Transformação cíclica' : [Eq(Q - tau,0), 'Um gás transformações cíclicas. Sabe-se que:\n'],
    'Rendimento térmica' : [Eq(eta/100 - 1 + Qf/Qq,0), 'Uma máquina térmica opera entre duas fontes de calor. Sabe-se que:\n'],
    'Rendimento Carnot' : [Eq(etac/100 - 1 + Tfr/Tq,0), 'Uma máquina térmica opera entre duas fontes de calor. Sabe-se que:\n'],
    'Eficiência frigorífica' : [Eq(e/100 - Qf/(Qq-Qf),0), 'Um refrigerador opera entre duas fontes de calor. Sabe-se que:\n'],
    'Eficiência frigorífica máxima' : [Eq(emax/100 - Tf/(Tq-Tf),0), 'Um refrigerador opera entre duas fontes de calor. Sabe-se que:\n'],
    'Entropia' : [Eq(S - (deltaQ/Tf)+(deltaQ/Ti),0), 'Uma máquina realiza trabalho com eficiência não ideal. Sabe-se que:\n'],
}
Thermo_Quant = {
    P0 : 'Pressão incial', Vi : 'Volume inicial', Ti : 'Temperatura inicial', Pf : 'Pressão final', Vf : 'Volume final', Ecm : 'Energia cinética média',
    deltaU : 'Variação de Energia interna', Qq : 'Calor da fonte quente', Tq : 'Temperatura da fonte quente', P : 'Pressão', V : 'Volume',
    n : 'Número de mols', T : 'Temperatura', Tf : 'Temperatura final', tau : 'Trabalho', deltaV : 'Variação de volume', deltaT : 'Variaçã de temperatura',
    Q : 'Calor transferido', Qf : 'Calor da fonte fria', deltaQ : 'Diferença de Calor', S : 'Entropia', eta : 'Rendimento', Tfr : 'Temperatura da fonte fria',
    e : 'Eficiência', etac : 'Rendimento de Carnot', emax : 'Eficiência máxima', 
}
Thermo_Units = {
    P0 : ['atm', (1, 100, 10)], Vi : ['L', (1, 100, 10)], Ti : ['K', (170, 400, 1)], Pf : ['atm', (101, 200, 10)], Vf : ['L', (101, 300, 10 )],
    Ecm : ['J', (100, 10000, 1)], deltaU : ['J', (10, 5000, 1)], Qq : ['J', (5001, 10000, 1)], Tq : ['K', (370, 900, 1)], P : ['atm', (1, 200, 1)],
    V : ['L', (1, 300, 1)], n : ['mol', (1, 100, 10)], T : ['K', (170, 900, 1)], Tf : ['K', (401, 900, 1)], tau : ['J', (-10000, 10000, 10)],
    deltaV : ['m^3', (-1000, 1000, 100)], deltaT : ['K', (-400,400, 1 )], Q : ['J', (-10000, 10000, 1)], Qf : ['J', (1, 5000, 1)],
    deltaQ : ['J', (-500, 500, 1)], S : ['J/K', (-100, 100, 1)], eta : ['%', (1, 99, 1)], Tfr : ['K', (170, 369, 1)], e : ['%', (1, 99, 1)],
    etac : ['%', (1, 99, 1)], emax : ['%', (50, 99, 1)]
}
Thermo_Pack = (Thermo_Vars, Thermo_Eqs, Thermo_Quant, Thermo_Units)


Packs = {
    'Cinemática': Kin_Pack, 'Cinemática Rotacional': Rot_Kin_Pack,
    'Lançamento de projétil' : Projectiles_Pack, 'Mecânica Newtoniana' :  Newton_Pack,
    'Gravitação Universal' : Gravitation_Pack, 'Equilíbrio' : Equilibrium_Pack,
    'Hidrostática' : Hydrostatics_Pack, 'Energia' : Energy_Pack, 'Momento Linear' : Momentum_Pack,
    'Termologia':Heat_Pack, 'Termodinâmica' : Thermo_Pack
    }

#Automatizing
'''
list_vars = [P0, Vi, Ti, Pf, Vf, Ecm, deltaU, Qq, Tq,
            P, V, n, T, Tf, tau, deltaV, deltaT, Q, Qf, deltaQ]

dict_output = []

for i in Thermo_Vars.keys():
    dict_output.append(
        f"{i} : ['', ()],"
    )

for i in dict_output:
    print(i + ' ', end='')
'''