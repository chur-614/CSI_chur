
# e<0.1

from wolframclient.evaluation import WolframLanguageSession



def CASI():
    wlpath="D:\\Mathematica\\11.2\\MathKernel.exe"
    sess=WolframLanguageSession(wlpath)
    # Calling mathematica 11.2 via Python 3.8
    exp=wlexpr('''
               Array[Ec, 9]
               Ec[0] = M;
               For[i = 1, i < 10, i++,
                   Ec[i] = FullSimplify[Series[M + e Sin[Ec[i-1]], {e, 0, 17}]];,
                   Ec[i] = FullSimplify[Ec[i] - (Ec[i] – Ec[i-1])^2/((Ec[i] – Ec[i-1]) - (Ec[i-1] – Ec[i-2]))]
                   ]
               Ecc = E[i];
               ''')
    # Session starts, calculation begins
    sess.evaluate(exp)
    E=sess.evaluate(Global.Ecc)
    return E[i]
