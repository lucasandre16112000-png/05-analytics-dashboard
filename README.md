# 📊 Analytics Dashboard Profissional

Um dashboard de analytics completo e profissional, construído com Python, Pandas, Plotly e Jinja2. Ele gera um relatório HTML interativo com diversas métricas e gráficos para análise de dados de tráfego de um site.

## ✨ Funcionalidades Principais

- **Dashboard Interativo**: Visualizações de dados ricas e interativas com Plotly.js
- **Métricas Abrangentes**: Cálculo de mais de 10 métricas essenciais como Page Views, Visitantes Únicos, Taxa de Conversão, Receita, etc.
- **Análise Temporal**: Gráficos de séries temporais para análise de tráfego por dia e por hora
- **Análise de Segmentos**: Gráficos de pizza para análise de distribuição de tráfego por dispositivo e por fonte
- **Análise de Tendências**: Cálculo de tendências de crescimento ou queda para as principais métricas
- **Arquitetura Profissional**: Código modular e bem organizado, seguindo as melhores práticas de engenharia de software
- **Templates HTML**: Uso de Jinja2 para separação do código Python da apresentação HTML
- **Testes Abrangentes**: Testes unitários com Pytest para garantir a qualidade e a corretude dos cálculos
- **Configuração Flexível**: Configurações centralizadas para fácil customização
- **Exportação de Relatórios**: Geração de um relatório completo em JSON com todos os dados e métricas

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|:---|:---|:---|
| **Python** | 3.8+ | Linguagem principal |
| **Pandas** | 2.0+ | Manipulação e análise de dados |
| **Plotly** | 5.0+ | Visualizações interativas |
| **Jinja2** | 3.0+ | Templates HTML |
| **Pytest** | 7.0+ | Testes unitários |

## 📂 Estrutura do Projeto

```
/05-analytics-dashboard
├── dashboard/
│   ├── config/                    # Módulo de configuração
│   │   ├── __init__.py
│   │   ├── logger.py              # Configuração do logger
│   │   └── settings.py            # Configurações gerais
│   ├── data_engine/               # Módulo de análise de dados
│   │   ├── __init__.py
│   │   └── analytics.py           # Classe AnalyticsEngine
│   ├── static/                    # Arquivos estáticos (CSS, JS)
│   │   └── css/
│   │       └── style.css
│   ├── templates/                 # Templates HTML (Jinja2)
│   │   └── index.html
│   ├── __init__.py
│   ├── generator.py               # Classe DashboardGenerator
│   └── main.py                    # Script principal
├── data/                          # Dados de entrada
│   └── sample_data.json
├── output/                        # Arquivos de saída
│   ├── analytics_report.json
│   └── dashboard.html
├── tests/                         # Testes unitários
│   ├── __init__.py
│   ├── test_analytics.py
│   └── test_generator.py
├── .env.example                   # Exemplo de arquivo de configuração
├── .gitignore                     # Arquivos a ignorar no Git
├── requirements.txt               # Dependências do projeto
└── README.md                      # Este arquivo
```

## 📋 Guia de Instalação e Execução (Para Qualquer Pessoa)

Este guia foi feito para que qualquer pessoa, mesmo sem conhecimento técnico, possa executar este projeto.

### Pré-requisitos

1. **Git**: Ferramenta para baixar (clonar) o código do GitHub.
   - [**Download do Git aqui**](https://git-scm.com/downloads)

2. **Python**: A linguagem de programação usada no projeto (versão 3.8 ou superior).
   - [**Download do Python aqui**](https://www.python.org/downloads/)
   - **Importante**: Durante a instalação do Python no Windows, marque a caixa que diz **"Add Python to PATH"**.

### Passo 1: Clonar o Repositório

Abra o seu terminal (ou **Git Bash** no Windows) e use o comando abaixo para baixar o projeto:

```bash
git clone https://github.com/lucasandre16112000-png/05-analytics-dashboard.git
cd 05-analytics-dashboard
```

### Passo 2: Criar e Ativar um Ambiente Virtual

Um ambiente virtual isola as dependências do projeto, evitando conflitos com outras aplicações Python.

**No Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**No macOS ou Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Você saberá que o ambiente virtual está ativado quando ver `(venv)` no início da linha do seu terminal.

### Passo 3: Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### Passo 4: Executar o Dashboard

Execute o script principal para gerar o dashboard:

```bash
python -m dashboard.main
```

O script irá:
1. Gerar dados de exemplo (se não existirem)
2. Calcular todas as métricas e análises
3. Gerar o relatório em JSON em `output/analytics_report.json`
4. Gerar o dashboard HTML em `output/dashboard.html`

### Passo 5: Visualizar o Dashboard

Abra o arquivo `output/dashboard.html` em seu navegador para visualizar o dashboard interativo com todos os gráficos e métricas.

## 🚀 Exemplos de Uso

### Exemplo 1: Usar o Script Padrão

O script padrão já contém um exemplo pronto para usar:

```bash
python -m dashboard.main
```

### Exemplo 2: Usar Dados Customizados

Para usar seus próprios dados, coloque um arquivo JSON em `data/sample_data.json` com o seguinte formato:

```json
[
  {
    "date": "2025-01-01",
    "hour": 0,
    "page_views": 100,
    "unique_visitors": 50,
    "conversions": 5,
    "revenue": 250.00,
    "device": "desktop",
    "source": "organic"
  },
  ...
]
```

Depois execute:

```bash
python -m dashboard.main
```

### Exemplo 3: Usar o AnalyticsEngine em Seu Próprio Código

Você pode importar o engine em seu próprio projeto Python:

```python
from dashboard.data_engine.analytics import AnalyticsEngine
from pathlib import Path

# Criar engine
engine = AnalyticsEngine()

# Carregar dados
engine.load_data_from_file('data/sample_data.json')

# Calcular métricas
engine.calculate_metrics()

# Obter métricas
metrics = engine.get_metrics()
print(f"Page Views: {metrics['page_views']}")
print(f"Conversão: {metrics['conversion_rate']:.2%}")

# Exportar relatório
engine.export_report('output/report.json')
```

## 🧪 Executar os Testes

Para garantir que tudo está funcionando corretamente, execute a suíte de testes:

```bash
pytest
```

Ou com mais detalhes:

```bash
pytest -v
```

## 📊 Métricas Calculadas

O dashboard calcula automaticamente as seguintes métricas:

| Métrica | Descrição |
|---------|-----------|
| **Page Views** | Total de visualizações de página |
| **Unique Visitors** | Total de visitantes únicos |
| **Conversion Rate** | Percentual de conversão |
| **Average Order Value** | Valor médio por pedido |
| **Revenue** | Receita total |
| **Bounce Rate** | Taxa de rejeição |
| **Session Duration** | Duração média da sessão |
| **Traffic by Device** | Distribuição de tráfego por dispositivo |
| **Traffic by Source** | Distribuição de tráfego por fonte |
| **Daily Trends** | Tendências diárias |
| **Hourly Trends** | Tendências por hora |

## 🔒 Boas Práticas

- **Dados Sensíveis**: Não inclua dados sensíveis ou pessoais no repositório
- **Configurações**: Use o arquivo `.env` para configurações sensíveis
- **Testes**: Sempre execute os testes antes de fazer commit
- **Documentação**: Mantenha a documentação atualizada

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
- Abrir uma issue para relatar bugs
- Enviar um pull request com melhorias
- Sugerir novas funcionalidades

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Lucas André S - [GitHub](https://github.com/lucasandre16112000-png)
