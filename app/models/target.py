from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.orm import relationship

class Target:
    name: str | None
    email: str | None
    phone: str | None
    domain: list[str] | None
    usernames: list[str] | None
    notes: str | None
    cnpj: str | None
    cpf: str | None