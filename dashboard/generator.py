# dashboard/generator.py

from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .config.logger import setup_logger
from .data_engine.analytics import AnalyticsEngine
from .config.settings import (
    DASHBOARD_TITLE,
    TEMPLATE_DIR
)

logger = setup_logger(__name__)

class DashboardGenerator:
    """Gerador de dashboard HTML"""
    
    def __init__(self, analytics_engine: AnalyticsEngine):
        self.analytics = analytics_engine
        # Usar caminho absoluto para o diretório de templates
        template_path = Path(__file__).parent / TEMPLATE_DIR
        self.env = Environment(loader=FileSystemLoader(str(template_path)))
    
    def generate_html(self, template_name: str, output_filename: str) -> None:
        """Gerar dashboard HTML a partir de um template"""
        logger.info(f"Gerando dashboard HTML a partir de {template_name}...")
        
        template = self.env.get_template(template_name)
        
        context = {
            "title": DASHBOARD_TITLE,
            "generated_at": self.analytics.timestamp.strftime("%d/%m/%Y %H:%M:%S"),
            "metrics": self.analytics.metrics,
            "daily_stats": self.analytics.get_daily_stats(),
            "hourly_stats": self.analytics.get_hourly_stats(),
            "device_stats": self.analytics.get_device_stats(),
            "source_stats": self.analytics.get_source_stats(),
            "top_hours": self.analytics.get_top_hours(),
            "trends": {
                "page_views": self.analytics.get_trend_analysis("page_views"),
                "revenue": self.analytics.get_trend_analysis("revenue"),
                "conversion_rate": self.analytics.get_trend_analysis("conversion_rate"),
            }
        }
        
        html_content = template.render(context)
        
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        logger.info(f"✓ Dashboard salvo em {output_filename}")
