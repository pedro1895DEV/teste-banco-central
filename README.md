# Análise de Dados - Programa Aprender Valor (Banco Central)

## Como Executar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Salve a planilha .xlsx na raíz do projeto**

2. **Execute o script:**
   ```bash
   python main.py
   ```

---

## O que o script faz ao ser executado

1. **Leitura e Filtros:** 
   * Filtra as escolas que aderiram a partir de **28/05/2021**.
   * Identifica escolas com estudantes cadastrados (`> 0`).
   * Identifica escolas com profissionais (professores ou gestores) que iniciaram a formação.

2. **Respostas no Terminal:**
   * Quantidade de escolas distintas que aderiram ao programa.
   * Quantidade de escolas inativas.
   * Quantidade de escolas com apenas profissionais, apenas estudantes, ambos ou qualquer um dos dois.

3. **Gráficos Visuais:**
   * **Gráfico 1:** Distribuição de escolas por tipo de atividade.
   * **Gráfico 2:** Distribuição das escolas inativas por Estado (UF).
