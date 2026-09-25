# Análise de Dados - Programa Aprender Valor

## Explicação

A parte central do projeto é o arquivo `main.py`, que concentra toda a lógica de tratamento e análise dos dados da planilha. O arquivo `index.html` atua como cliente consumindo os dados gerados pelo arquivo Python no arquivo `dados.json`.

```text
  ┌────────────────────────┐                    ┌─────────────────┐                     ┌────────────┐                ┌───────────────────────┐            ┌──────────────────────┐
  │                        │                    │                 │                     │            │                │                       │            │                      │
  │                        │                    │                 │                     │            │                │                       │            │                      │
  │     Planilha Excel     ├─Leitura─e─Filtros─►│ Python / Pandas ├─Exporta─Resultados─►│ dados.json ├─Lê─via─fetch──►│        Client         ├─Renderiza─►│ Dashboard Interativo │
  │                        │                    │    (main.py)    │                     │            │                │      (index.html)     │            │    (GitHub Pages)    │
  │                        │                    │                 │                     │            │                │                       │            │                      │
  └────────────────────────┘                    └─────────────────┘                     └────────────┘                └───────────────────────┘            └──────────────────────┘
```

> **Dashboard Online:** Acesse a visualização interativa pelo [GitHub Pages](https://pedro1895dev.github.io/teste-banco-central/).

---

## Como Executar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Certifique-se de que a planilha `exercicio-excel.xlsx` está na raiz do projeto.**

3. **Execute o script:**
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

3. **Exportação e Gráficos:**
   * Gera o arquivo **`dados.json`** atualizado para alimentar o dashboard web.
   * Exibe os gráficos nativos do **Matplotlib** no terminal.
