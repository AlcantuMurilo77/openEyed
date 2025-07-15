
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
from models.target import Target

# Banco de dados em memória (ideal para testes temporários)
DATABASE_URL = "sqlite:///:memory:"

# Criação do engine e sessão
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

# Função de teste
def test_insert_and_read():
    db = SessionLocal()

    novo_target = Target(
        name="João",
        email="joao@email.com",
        phone="11999999999",
        domains=["example.com"],
        usernames=["joaodasilva"],
        notes="Possível alvo de investigação",
        cpf="12345678900"
    )

    db.add(novo_target)
    db.commit()

    for target in db.query(Target).all():
        print(f"ID: {target.id}, Nome: {target.name}, Email: {target.email}")

    db.close()

if __name__ == "__main__":
    test_insert_and_read()
