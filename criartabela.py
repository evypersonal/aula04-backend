import sqlite3

conexao = sqlite3.connect("aluno.db")

cursor = conexao.cursor()

cursor.execute(
    """
    CREATE TABLE alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    curso TEXT
    )
    """
)

conexao.commit()
conexao.close()