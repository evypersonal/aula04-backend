import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def conectar():
    return sqlite3.connect("alunos.db")

class Aluno(BaseModel):
    nome: str
    idade: int
    curso: str

@app.post("/alunos")
def cadastrar_alunos(aluno: Aluno):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO alunos(nome,idade,curso)
        VALUES(?, ?, ?)
        """,
        (aluno.nome, aluno.idade, aluno.curso)
    )

    conexao.commit()
    conexao.close()
    return{"mensagem": "Aluno  cadastrado com sucesso!"}


@app.get("/alunos")
def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    conexao.close()

    return alunos