# Challenge Pelé Academia - Sprint 2

## Integrantes
* **Henrique Nunes Mororó** — RM 574073
* **Bernardo de Paula Rodrigues** — RM 572376
  

## Descrição do Projeto
Motor lógico em Python estruturado para interface CLI, focado na triagem e gestão de atletas para a Pelé Academia. O sistema recebe dados técnicos e físicos através do console, aplica pesos ponderados sem arredondamento sobre os valores brutos de ponto flutuante e classifica os perfis com base nas diretrizes de idade e corte de desempenho.

## Estrutura de Funções (CLI)
* `register_athlete()`: Processa os inputs fornecidos, calcula as médias ponderadas via laços sobre as listas de pesos e retorna o dicionário estruturado com o status do candidato.
* `list_athletes()`: Renderiza a listagem dos dados contidos na memória em formato tabular diretamente no terminal.
* `calculate_general_metrics()`: Executa rotinas de iteração para gerar a análise estatística atual do sistema.

## Como Rodar o Projeto

### Execução
1. Clone o repositório ou baixe o arquivo `main.py`.
2. Abra o terminal na pasta do arquivo.
3. Execute o comando:

```bash
python main.py
