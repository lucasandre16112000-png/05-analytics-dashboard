# tests/test_analytics.py

import pytest
import pandas as pd
from dashboard.data_engine.analytics import AnalyticsEngine

@pytest.fixture
def engine():
    """Criar uma instância do AnalyticsEngine"""
    return AnalyticsEngine()

@pytest.fixture
def sample_data(engine):
    """Gerar dados de exemplo"""
    return engine.generate_sample_data()

class TestAnalyticsEngine:
    """Testes para o AnalyticsEngine"""

    def test_generate_sample_data(self, engine):
        """Testar a geração de dados de exemplo"""
        df = engine.generate_sample_data()
        assert isinstance(df, pd.DataFrame)
        assert not df.empty

    def test_calculate_metrics(self, engine, sample_data):
        """Testar o cálculo de métricas"""
        metrics = engine.calculate_metrics()
        assert isinstance(metrics, dict)
        assert "total_page_views" in metrics
        assert "total_revenue" in metrics

    def test_get_daily_stats(self, engine, sample_data):
        """Testar a obtenção de estatísticas diárias"""
        daily_stats = engine.get_daily_stats()
        assert isinstance(daily_stats, pd.DataFrame)
        assert not daily_stats.empty

    def test_get_hourly_stats(self, engine, sample_data):
        """Testar a obtenção de estatísticas por hora"""
        hourly_stats = engine.get_hourly_stats()
        assert isinstance(hourly_stats, pd.DataFrame)
        assert not hourly_stats.empty

    def test_get_device_stats(self, engine, sample_data):
        """Testar a obtenção de estatísticas por dispositivo"""
        device_stats = engine.get_device_stats()
        assert isinstance(device_stats, dict)
        assert "Desktop" in device_stats

    def test_get_source_stats(self, engine, sample_data):
        """Testar a obtenção de estatísticas por fonte"""
        source_stats = engine.get_source_stats()
        assert isinstance(source_stats, dict)
        assert "Organic" in source_stats

    def test_get_top_hours(self, engine, sample_data):
        """Testar a obtenção das horas de pico"""
        top_hours = engine.get_top_hours()
        assert isinstance(top_hours, list)
        assert len(top_hours) == 5

    def test_get_trend_analysis(self, engine, sample_data):
        """Testar a análise de tendências"""
        trend = engine.get_trend_analysis()
        assert isinstance(trend, dict)
        assert "trend" in trend
