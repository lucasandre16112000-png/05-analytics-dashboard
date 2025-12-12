# dashboard/config/settings.py

import logging

# Configurações de Logging
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Configurações do Dashboard
DASHBOARD_TITLE = "Analytics Dashboard Profissional"
DASHBOARD_REFRESH_INTERVAL = 300  # em segundos

# Configurações de Dados
DEFAULT_DATA_DAYS = 30
TOP_HOURS_COUNT = 5
TREND_ANALYSIS_DAYS = 7

# Caminhos de Arquivos
DATA_DIR = "data"
OUTPUT_DIR = "output"
TEMPLATE_DIR = "templates"
STATIC_DIR = "static"

# Nomes de Arquivos
INPUT_DATA_FILE = "sample_data.json"
OUTPUT_REPORT_FILE = "analytics_report.json"
OUTPUT_DASHBOARD_FILE = "dashboard.html"
