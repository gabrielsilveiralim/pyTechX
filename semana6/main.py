from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        valor = valor.strip()
        if not valor:
            raise ValueError("O nome não pode ficar vazio.")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        valor = valor.strip()
        if "@" not in valor or "." not in valor.split("@")[-1]:
            raise ValueError("E-mail inválido.")
        self._email = valor

    @abstractmethod
    def descricao(self):
        """Cada tipo de pessoa deve implementar sua própria descrição."""

    def __str__(self):
        return f"{self.nome} <{self.email}>"

    def __repr__(self):
        return f"{self.__class__.__name__}(nome={self.nome!r}, email={self.email!r})"


class Aluno(Pessoa):
    def __init__(self, nome, email, matricula, nota):
        super().__init__(nome, email)
        self.matricula = matricula
        self.nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        valor = float(valor)
        if not 0 <= valor <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota = valor

    def descricao(self):
        situacao = "aprovado" if self.nota >= 7 else "em recuperação/reprovado"
        return f"Aluno {self.nome}, matrícula {self.matricula}, nota {self.nota:.1f}: {situacao}"

    def __str__(self):
        return f"{super().__str__()} | Aluno | Matrícula: {self.matricula} | Nota: {self.nota:.1f}"


class Professor(Pessoa):
    def __init__(self, nome, email, disciplina, salario):
        super().__init__(nome, email)
        self.disciplina = disciplina
        self.salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        valor = float(valor)
        if valor < 0:
            raise ValueError("O salário não pode ser negativo.")
        self._salario = valor

    def descricao(self):
        return f"Professor {self.nome}, disciplina {self.disciplina}, salário R$ {self.salario:.2f}"

    def __str__(self):
        return f"{super().__str__()} | Professor | {self.disciplina} | R$ {self.salario:.2f}"


class Curso:
    def __init__(self, nome, carga_horaria, professor):
        self.nome = nome
        self.carga_horaria = int(carga_horaria)
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError("Só é possível adicionar objetos Aluno.")
        self.alunos.append(aluno)

    def __str__(self):
        return f"Curso: {self.nome} ({self.carga_horaria}h), professor: {self.professor.nome}, alunos: {len(self.alunos)}"

    def __repr__(self):
        return f"Curso(nome={self.nome!r}, carga_horaria={self.carga_horaria!r})"


class Monitor(Aluno):
    def __init__(self, nome, email, matricula, nota, horas_monitoria):
        super().__init__(nome, email, matricula, nota)
        self.horas_monitoria = int(horas_monitoria)

    def descricao(self):
        return f"Monitor {self.nome}, matrícula {self.matricula}, {self.horas_monitoria}h de monitoria, nota {self.nota:.1f}"

    def __str__(self):
        return f"{super().__str__()} | Monitoria: {self.horas_monitoria}h"


def demonstracao():
    professor = Professor("Carla Souza", "carla@faculdade.com", "Python", 4200)
    alunos = [
        Aluno("Ana", "ana@email.com", "A001", 8.5),
        Aluno("Bruno", "bruno@email.com", "A002", 6.0),
        Aluno("Caio", "caio@email.com", "A003", 7.0),
        Aluno("Diana", "diana@email.com", "A004", 9.2),
        Aluno("Enzo", "enzo@email.com", "A005", 5.5),
        Aluno("Flávia", "flavia@email.com", "A006", 8.0),
        Aluno("Gustavo", "gustavo@email.com", "A007", 7.8),
        Aluno("Helena", "helena@email.com", "A008", 9.8),
        Monitor("Igor", "igor@email.com", "A009", 8.7, 12),
        Monitor("Júlia", "julia@email.com", "A010", 9.0, 8),
    ]
    curso = Curso("Desenvolvimento Python", 60, professor)
    for aluno in alunos:
        curso.adicionar_aluno(aluno)

    print("========== SISTEMA ACADÊMICO ==========")
    print(professor)
    print(curso)
    print("\nDemonstração de polimorfismo:")
    pessoas = [professor] + alunos
    for pessoa in pessoas:
        print(f"- {pessoa.descricao()}")

    print("\nRepresentação técnica:")
    print(repr(alunos[0]))
    print(repr(curso))

    print("\nTeste de exceção:")
    try:
        Aluno(" ", "email-invalido", "X", 12)
    except ValueError as erro:
        print(f"Entrada inválida capturada: {erro}")


if __name__ == "__main__":
    demonstracao()
