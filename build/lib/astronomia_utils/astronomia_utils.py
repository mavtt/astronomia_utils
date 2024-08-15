def forca_gravitacional(massa1, massa2, distancia):

    """ 
        Calcula a força gravitacional entre dois corpos.
        :param massa1: Massa do primeiro corpo (em kg).
        :type massa1: float
        :param massa2: Massa do segundo corpo (em kg).
        :type massa2: float
        :param distancia: Distância entre os centros dos dois corpos (em metros).
        :type distancia: float

        :returns: A força gravitacional calculada (em newtons).
        :rtype: float

        Notes
          -----
          .. math::
              F = \\frac{G * (massa1 * massa2)}{distancia^2} 

        Examples
        --------
        >>> from astronomia_utils import forca_gravitacional
        >>> forca_gravitacional(6e24, 7.2e22, 3.84e8)
        1.9553613281249998e+20


    """
    G = 6.67430e-11  # Constante gravitacional universal (em m^3/kg/s^2)
    forca = (G * massa1 * massa2) / distancia**2
    return forca

def peso_na_superficie(massa, gravidade):
    peso = massa * gravidade
    return peso