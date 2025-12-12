# 📊 Analytics Dashboard Profissional

Este projeto é um dashboard de analytics completo e profissional, construído com Python, Pandas, Plotly e Jinja2. Ele gera um relatório HTML interativo com diversas métricas e gráficos para análise de dados de tráfego de um site.

## ✨ Features

- **Dashboard Interativo:** Visualizações de dados ricas e interativas com Plotly.js.
- **Métricas Abrangentes:** Cálculo de mais de 10 métricas essenciais, como Page Views, Visitantes Únicos, Taxa de Conversão, Receita, etc.
- **Análise Temporal:** Gráficos de séries temporais para análise de tráfego por dia e por hora.
- **Análise de Segmentos:** Gráficos de pizza para análise de distribuição de tráfego por dispositivo e por fonte.
- **Análise de Tendências:** Cálculo de tendências de crescimento ou queda para as principais métricas.
- **Arquitetura Profissional:** Código modular e bem organizado, seguindo as melhores práticas de engenharia de software.
- **Templates HTML:** Uso de Jinja2 para separação do código Python da apresentação HTML.
- **Testes Abrangentes:** Testes unitários com Pytest para garantir a qualidade e a corretude dos cálculos.
- **Configuração Flexível:** Configurações centralizadas para fácil customização.
- **Exportação de Relatórios:** Geração de um relatório completo em JSON com todos os dados e métricas.

## 🚀 Como Usar

### 1. Pré-requisitos

- Python 3.8+
- `venv` (ou outra ferramenta de ambiente virtual)

### 2. Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/lucasandre16112000-png/05-analytics-dashboard.git
cd 05-analytics-dashboard

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Execução

Para gerar o dashboard, execute o script principal:

```bash
python3 -m dashboard.main
```

O script irá:

1.  Gerar dados de exemplo (se não existirem).
2.  Calcular todas as métricas e análises.
3.  Gerar o relatório em JSON em `output/analytics_report.json`.
4.  Gerar o dashboard HTML em `output/dashboard.html`.

### 4. Visualização

Abra o arquivo `output/dashboard.html` em seu navegador para visualizar o dashboard interativo.

## 🧪 Testes

Para rodar os testes, execute o Pytest:

```bash
pytest
```

## 🏗️ Estrutura do Projeto

```
/05-analytics-dashboard
├── dashboard/
│   ├── config/             # Módulo de configuração
│   │   ├── __init__.py
│   │   ├── logger.py         # Configuração do logger
│   │   └── settings.py       # Configurações gerais
│   ├── data_engine/        # Módulo de análise de dados
│   │   ├── __init__.py
│   │   └── analytics.py      # Classe AnalyticsEngine
│   ├── static/               # Arquivos estáticos (CSS, JS)
│   │   └── css/
│   │       └── style.css
│   ├── templates/            # Templates HTML (Jinja2)
│   │   └── index.html
│   ├── __init__.py
│   ├── generator.py        # Classe DashboardGenerator
│   └── main.py             # Script principal
├── data/                   # Dados de entrada
│   └── sample_data.json
├── output/                 # Arquivos de saída
│   ├── analytics_report.json
│   └── dashboard.html
├── tests/                  # Testes unitários
│   ├── __init__.py
│   ├── test_analytics.py
│   └── test_generator.py
├── .gitignore
├── README.md
└── requirements.txt
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
