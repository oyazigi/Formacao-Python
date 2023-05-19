from sqlalchemy.orm import (
    declarative_base,
    relationship,
    Session
)
from sqlalchemy import (
    Column,
    create_engine,
    inspect,
    select,
    func,
    ForeignKey,
    String,
    Integer,
    Float
)

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "user_client"
    id = Column(Integer, primary_key=True)
    Nome = Column(String)
    cpf = Column(String(11), nullable=False)
    endereco = Column(String)

    def __repr__(self):
        return f"Cliente (id={self.id}, nome={self.Nome}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False, default="0001")
    num = Column(Integer, nullable=False)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey("user_client.id"), nullable=False)

    usuario = relationship(
        "Cliente"
    )

    def __repr__(self):
        return f"Conta (id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo}, id_cliente={self.id_cliente})"


# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

with Session(engine) as session:
    victor = Cliente(
        Nome="Victor",
        cpf="12589745890",
        endereco="Rua dos bobos numero 0",
    )

    conta_victor = Conta(
        tipo="Conta corrente",
        num="12345-6",
        saldo=500.00,
        usuario=victor
    )

    sabrina = Cliente(
        Nome="Sabrina",
        cpf="35698785412",
        endereco="Rua paraguai 180",
    )

    conta_sabrina = Conta(
        tipo="Conta poupanca",
        num="25698-7",
        saldo=1500.00,
        usuario=sabrina
    )

    # enviando para o BD (persistência de dados)
    session.add_all([victor, conta_victor, sabrina, conta_sabrina])

    session.commit()

statement = select(Cliente).where(Cliente.Nome.in_(["Victor"]))
for user in session.scalars(statement):
    print(user)

order = select(Cliente).order_by(Cliente.cpf.asc())

join = select(Cliente.Nome, Conta.num).join_from(Cliente, Conta)
connection = engine.connect()
results = connection.execute(join).fetchall()
for result in results:
    print(result)

count = select(func.count("*")).select_from(Cliente)
for result in session.scalars(count):
    print(result)

connection.close()

#Victor Yazigi
