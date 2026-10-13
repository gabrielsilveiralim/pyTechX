import csv
import re
from datetime import datetime
from pathlib import Path


class FormatoInvalidoError(Exception):
    """Erro personalizado para um registo que não cumpre as regras definidas."""


PADROES = {
    "email": r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$",
    # valida o cpf com ou sem pontos
    "cpf": r"^(?:\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2})$",
    # valida telefone com ou sem 55
    "telefone": r"^(?:\+?55\s?)?(?:\(?\d{2}\)?\s?)?9?\d{4}[-\s]?\d{4}$",
    # formatação de data
    "data": r"^\d{4}-\d{2}-\d{2}$",
}
CAMPOS = ("email", "cpf", "telefone", "data")


def validar_campo(campo, valor):
    if campo not in PADROES:
        raise KeyError(f"Campo não reconhecido: {campo}")
    valor = (valor or "").strip()
    if not re.fullmatch(PADROES[campo], valor):
        return False, f"{campo}: formato inválido"
    if campo == "data":
        try:
            datetime.strptime(valor, "%Y-%m-%d")
        except ValueError:
            return False, "data: data inexistente"
    return True, "válido"


def analisar_csv(caminho):
    validos, invalidos = [], []
    try:
        with open(caminho, "r", encoding="utf-8-sig", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            if leitor.fieldnames is None:
                raise KeyError("CSV sem cabeçalho")
            ausentes = [campo for campo in CAMPOS if campo not in leitor.fieldnames]
            if ausentes:
                raise KeyError(f"Colunas ausentes: {', '.join(ausentes)}")

            for numero, linha in enumerate(leitor, start=2):
                problemas = []
                try:
                    for campo in CAMPOS:
                        ok, mensagem = validar_campo(campo, linha.get(campo, ""))
                        if not ok:
                            problemas.append(mensagem)
                    if problemas:
                        raise FormatoInvalidoError("; ".join(problemas))
                    validos.append(linha)
                except FormatoInvalidoError as erro:
                    invalidos.append((numero, linha, str(erro)))
        print("Leitura concluída sem erros de abertura.")
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' não encontrado.")
        return [], [(0, {}, "arquivo não encontrado")]
    except (KeyError, UnicodeDecodeError, csv.Error) as erro:
        print(f"Erro ao ler o CSV: {erro}")
        return [], [(0, {}, str(erro))]
    except ValueError as erro:
        print(f"Erro de conversão: {erro}")
        return [], [(0, {}, str(erro))]
    else:
        return validos, invalidos
    finally:
        print("Processamento do arquivo finalizado.")


def imprimir_relatorio(validos, invalidos):
    total = len(validos) + len(invalidos)
    print("\n========== RELATÓRIO DE VALIDAÇÃO ==========")
    print(f"Total de registos analisados: {total}")
    print(f"Registos válidos: {len(validos)}")
    print(f"Registos inválidos: {len(invalidos)}")
    taxa = (len(validos) / total * 100) if total else 0
    print(f"Taxa de aprovação: {taxa:.1f}%")

    print("\nDADOS VÁLIDOS")
    for linha in validos:
        print(f"- {linha}")

    print("\nDADOS INVÁLIDOS")
    for numero, linha, motivo in invalidos:
        print(f"- Linha {numero}: {linha} | Motivo: {motivo}")


if __name__ == "__main__":
    arquivo_csv = input("Caminho do CSV (Enter para usar dados.csv): ").strip()
    if not arquivo_csv:
        arquivo_csv = "dados.csv"
    validos, invalidos = analisar_csv(Path(arquivo_csv))
    imprimir_relatorio(validos, invalidos)
