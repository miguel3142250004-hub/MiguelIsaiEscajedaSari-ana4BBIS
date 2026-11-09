"""Lab 10 - Suite de pruebas con pytest para app_movil.py"""
import pytest

from app_movil import (
    PerfilMovil,
    PerfilPro,
    PuntosInsuficientesError,
    SuscripcionExpiradaError,
)



@pytest.fixture
def perfil():
    """Instancia estándar de PerfilMovil, nueva para cada prueba."""
    return PerfilMovil("alex")


@pytest.fixture
def perfil_pro():
    return PerfilPro("maria", meses_suscripcion=1)



def test_atributos_iniciales(perfil):
    assert perfil.username == "alex"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_ganar_gemas_suma_correctamente(perfil):
    assert perfil.ganar_gemas(25) == 75
    assert perfil.gemas == 75


def test_gastar_gemas_resta_correctamente(perfil):
    assert perfil.gastar_gemas(20) == 30
    assert perfil.gemas == 30


def test_gastar_todo_el_saldo(perfil):
    assert perfil.gastar_gemas(50) == 0


def test_consistencia_aritmetica(perfil):
    perfil.ganar_gemas(10)
    perfil.gastar_gemas(30)
    assert perfil.gemas == 30  # 50 + 10 - 30


def test_gemas_iniciales_negativas():
    with pytest.raises(ValueError):
        PerfilMovil("bob", gemas=-1)


def test_gastar_mas_de_lo_disponible(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(51)


def test_gastar_cantidad_invalida(perfil):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(0)


def test_saldo_no_cambia_tras_error(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(999)
    assert perfil.gemas == 50


def test_perfil_pro_meses_invalidos():
    with pytest.raises(ValueError):
        PerfilPro("zoe", meses_suscripcion=0)


def test_descarga_offline_con_suscripcion_expirada(perfil_pro):
    perfil_pro.consumir_mes()  # 1 -> 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False


def test_descarga_offline_exitosa(perfil_pro):
    assert "éxito" in perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is True



@pytest.mark.parametrize(
    "cantidad, esperado",
    [(1, 51), (10, 60), (50, 100), (1000, 1050)],
)
def test_ganar_gemas_valores_validos(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -1, -100])
def test_ganar_gemas_valores_invalidos(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)



def test_perfil_pro_hereda_de_perfil_movil(perfil_pro):
    assert isinstance(perfil_pro, PerfilPro)
    assert isinstance(perfil_pro, PerfilMovil)
    assert issubclass(PerfilPro, PerfilMovil)


def test_perfil_movil_no_es_perfil_pro(perfil):
    assert not isinstance(perfil, PerfilPro)


def test_perfil_pro_hereda_metodos(perfil_pro):
    assert perfil_pro.ganar_gemas(10) == 60


def test_ciclo_de_vida_perfil_pro():
    p = PerfilPro("leo", meses_suscripcion=2)
    assert p.es_pro is True
    p.consumir_mes()
    p.consumir_mes()
    assert p.meses_suscripcion == 0
    with pytest.raises(SuscripcionExpiradaError):
        p.descargar_contenido_offline()
    assert p.es_pro is False


def test_excepciones_son_exception():
    assert issubclass(SuscripcionExpiradaError, Exception)
    assert issubclass(PuntosInsuficientesError, Exception)
