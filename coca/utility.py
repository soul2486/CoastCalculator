
from decimal import Decimal


def M_Ec1(Ec1):
    
    return (Decimal(1.2) * Ec1)

def C_bat(Ec1):
    resultat = Ec1/(12 * Decimal(0.7))
    return Decimal("{:.2f}".format(resultat))

def N_bat(Cbat):

    return (round(Cbat/200))
def N_panneau(Ec1):
    resultat = (Ec1/1008) * Decimal(1.2)
    return Decimal("{:.2f}".format(resultat))