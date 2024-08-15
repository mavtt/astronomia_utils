import pytest
from astronomia_utils import forca_gravitacional

def test_forca_gravitacional_terra_lua():
    """
    Testa a função forca_gravitacional com valores da massa da terra e da lua.
    """
    massa_terra = 6e24
    massa_lua = 7.2e22
    distancia = 3.84e8
    resultado_esperado = 1.95e20
    assert forca_gravitacional(massa_lua, massa_terra, distancia) == pytest.approx(resultado_esperado, rel=1e-2)
