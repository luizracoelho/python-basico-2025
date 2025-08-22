# Desafio Final: Sistema de Cadastro de Alunos
# Módulo

alunos = []  # Lista global de alunos

def buscar_aluno(nome: str, skip_message: bool = False):
    """Busca um aluno pelo nome. Retorna o aluno se existir, senão None."""
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
        
    if not skip_message:
        print(f"⚠️ Aluno '{nome}' não encontrado.")

    return None


def adicionar_aluno(nome: str, idade: int, curso: str):
    """Adiciona um novo aluno à lista"""
    if buscar_aluno(nome, True):
        print("⚠️ Aluno já cadastrado!")
        return

    aluno = {"nome": nome, "idade": idade, "curso": curso}
    alunos.append(aluno)
    print("✅ Aluno adicionado com sucesso!")


def remover_aluno(nome: str):
    """Remove um aluno pelo nome"""
    aluno = buscar_aluno(nome)
    if aluno:
        alunos.remove(aluno)
        print("🗑️ Aluno removido com sucesso!")


def alterar_aluno(nome: str, idade: int = None, curso: str = None):
    """Altera os dados de um aluno"""
    aluno = buscar_aluno(nome)
    if aluno:
        if idade is not None:
            aluno["idade"] = idade
        if curso is not None:
            aluno["curso"] = curso
        print("✏️ Dados do aluno alterados com sucesso!")


def listar_alunos():
    """Lista todos os alunos cadastrados"""
    if not alunos:
        print("📭 Nenhum aluno cadastrado.")
        return

    print("\n📚 Lista de Alunos:")
    for idx, aluno in enumerate(alunos, start=1):
        print(f"{idx}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")

    input("\nPressione Enter para continuar...")