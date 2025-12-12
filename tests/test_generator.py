# tests/test_generator.py

import pytest
from pathlib import Path
from dashboard.data_engine.analytics import AnalyticsEngine

@pytest.fixture
def engine():
    """Criar uma instância do AnalyticsEngine com dados"""
    eng = AnalyticsEngine()
    eng.generate_sample_data()
    eng.calculate_metrics()
    return eng

class TestDashboardGenerator:
    """Testes para o DashboardGenerator"""

    def test_analytics_engine_has_metrics(self, engine):
        """Testar se o engine tem métricas calculadas"""
        assert engine.metrics is not None
        assert len(engine.metrics) > 0
        assert "total_page_views" in engine.metrics

    def test_analytics_engine_exports_report(self, engine, tmp_path):
        """Testar a exportação de relatório"""
        report_file = tmp_path / "test_report.json"
        engine.export_report(str(report_file))
        
        assert report_file.exists()
        
        import json
        with open(report_file, 'r') as f:
            report = json.load(f)
        
        assert "metrics" in report
        assert "daily_stats" in report
