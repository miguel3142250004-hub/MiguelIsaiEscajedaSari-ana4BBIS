"""Lab 10 - Módulo lógico de la app móvil (POO + manejo de excepciones)."""


# ---------------------------------------------------------------------------
# 1. Jerarquía de excepciones del dominio
# ---------------------------------------------------------------------------
class SuscripcionExpiradaError(Exception):
    """Se lanza al ejecutar una operación restringida sin membresía activa."""


class PuntosInsuficientesError(Exception):
    """Se lanza cuando una transacción excede el saldo de gemas disponible."""


# ---------------------------------------------------------------------------
# 2. Clase base
# ---------------------------------------------------------------------------
class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1,
                 notificaciones_activas: bool = True):
        self.username = username
        self.gemas = gemas  # pasa por el setter (validación estricta)
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    # Encapsulamiento: gemas nunca puede ser negativo
    @property
    def gemas(self) -> int:
        return self._gemas

    @gemas.setter
    def gemas(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("Las gemas no pueden ser negativas.")
        self._gemas = valor

    def ganar_gemas(self, cantidad: int) -> int:
        """Incrementa el saldo. La cantidad debe ser estrictamente positiva."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser estrictamente positiva.")
        self._gemas += cantidad
        return self._gemas

    def gastar_gemas(self, cantidad: int) -> int:
        """Decrementa el saldo tras verificar disponibilidad."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser estrictamente positiva.")
        if cantidad > self._gemas:
            raise PuntosInsuficientesError(
                f"Saldo insuficiente: tienes {self._gemas}, necesitas {cantidad}."
            )
        self._gemas -= cantidad
        return self._gemas


# ---------------------------------------------------------------------------
# 3. Subclase derivada
# ---------------------------------------------------------------------------
class PerfilPro(PerfilMovil):
    def __init__(self, username: str, meses_suscripcion: int, **kwargs):
        super().__init__(username, **kwargs)
        if meses_suscripcion <= 0:
            raise ValueError("El periodo inicial debe ser mayor que cero.")
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def consumir_mes(self) -> int:
        """Auxiliar: descuenta un mes de suscripción (mínimo 0)."""
        if self.meses_suscripcion > 0:
            self.meses_suscripcion -= 1
        return self.meses_suscripcion

    def descargar_contenido_offline(self) -> str:
        """Si los meses llegan a 0: es_pro=False y lanza SuscripcionExpiradaError."""
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("Tu suscripción Pro ha expirado.")
        return "Descarga offline completada con éxito."
