from decimal import Decimal
from typing import List
from pydantic import BaseModel


class JugadorModel(BaseModel):
    nombre: str
    nivel: str
    goles: int
    sueldo: int
    bono: int
    sueldo_completo: int | None
    equipo: str


class Jugadores(BaseModel):
    jugadores: List[JugadorModel]


class JugadorSueldoModel(BaseModel):
    nombre: str
    goles_minimos: int
    goles: int
    sueldo: int
    bono: int
    sueldo_completo: float
    equipo: str


class JugadoresConSueldo(BaseModel):
    jugadores: List[JugadorSueldoModel]
