#!/usr/bin/env python3
# dashboard/main.py

"""
Script principal para gerar o dashboard de analytics
"""

from pathlib import Path

from dashboard.config.logger import setup_logger
from dashboard.data_engine.analytics import AnalyticsEngine
from dashboard.generator import DashboardGenerator
from dashboard.config.settings import (
    DATA_DIR,
    INPUT_DATA_FILE,
    OUTPUT_DIR,
    OUTPUT_REPORT_FILE,
    OUTPUT_DASHBOARD_FILE
)

logger = setup_logger(__name__)

def main():
    """Função principal"""
    logger.info("=" * 80)
    logger.info("INICIANDO GERAÇÃO DO DASHBOARD DE ANALYTICS")
    logger.info("=" * 80)
    
    # Criar diretórios se não existirem
    Path(DATA_DIR).mkdir(exist_ok=True)
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    
    # Inicializar engine de analytics
    engine = AnalyticsEngine()
    
    # Gerar ou carregar dados
    input_file = Path(DATA_DIR) / INPUT_DATA_FILE
    if not input_file.exists():
        logger.warning(f"Arquivo de dados não encontrado em {input_file}. Gerando dados de exemplo...")
        sample_data = engine.generate_sample_data()
        sample_data.to_json(input_file, orient="records", indent=2, default_handler=str)
    else:
        engine.load_data_from_file(str(input_file))
    
    # Calcular métricas
    engine.calculate_metrics()
    
    # Exportar relatório
    report_file = Path(OUTPUT_DIR) / OUTPUT_REPORT_FILE
    engine.export_report(str(report_file))
    
    # Gerar dashboard
    dashboard_generator = DashboardGenerator(engine)
    dashboard_file = Path(OUTPUT_DIR) / OUTPUT_DASHBOARD_FILE
    dashboard_generator.generate_html("index.html", str(dashboard_file))
    
    logger.info("=" * 80)
    logger.info("DASHBOARD GERADO COM SUCESSO!")
    logger.info(f"Acesse o arquivo: {dashboard_file}")
    logger.info("=" * 80)

if __name__ == "__main__":
    main()
