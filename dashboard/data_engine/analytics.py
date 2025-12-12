# dashboard/data_engine/analytics.py

import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

from ..config.logger import setup_logger
from ..config.settings import (
    DEFAULT_DATA_DAYS,
    TOP_HOURS_COUNT,
    TREND_ANALYSIS_DAYS
)

logger = setup_logger(__name__)

class AnalyticsEngine:
    """Engine de análise de dados em tempo real"""
    
    def __init__(self):
        self.data = pd.DataFrame()
        self.metrics = {}
        self.timestamp = datetime.utcnow()
    
    def generate_sample_data(self, days: int = DEFAULT_DATA_DAYS) -> pd.DataFrame:
        """Gerar dados de exemplo para análise"""
        logger.info(f"Gerando dados de análise para {days} dias...")
        
        np.random.seed(42)
        
        data = []
        base_date = datetime.utcnow() - timedelta(days=days)
        
        for day in range(days):
            current_date = base_date + timedelta(days=day)
            day_of_week = current_date.weekday()
            base_traffic = 1000 + (day_of_week * 200)
            
            for hour in range(24):
                hour_factor = 0.5 + 0.5 * np.sin((hour - 12) * np.pi / 12)
                timestamp = current_date.replace(hour=hour)
                
                data.append({
                    'timestamp': timestamp,
                    'date': timestamp.date(),
                    'hour': hour,
                    'day_of_week': day_of_week,
                    'page_views': int(base_traffic * hour_factor + np.random.normal(0, 50)),
                    'unique_visitors': int(base_traffic * hour_factor * 0.7 + np.random.normal(0, 30)),
                    'bounce_rate': np.random.uniform(30, 70),
                    'avg_session_duration': np.random.uniform(2, 10),
                    'conversion_rate': np.random.uniform(0.5, 5),
                    'revenue': np.random.uniform(100, 1000),
                    'device': np.random.choice(['Desktop', 'Mobile', 'Tablet'], p=[0.6, 0.3, 0.1]),
                    'source': np.random.choice(['Organic', 'Direct', 'Referral', 'Paid'], p=[0.4, 0.3, 0.2, 0.1]),
                })
        
        self.data = pd.DataFrame(data)
        logger.info(f"✓ Gerados {len(self.data)} registros")
        
        return self.data
    
    def load_data_from_file(self, file_path: str) -> pd.DataFrame:
        """Carregar dados de um arquivo JSON"""
        logger.info(f"Carregando dados de {file_path}...")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            self.data = pd.DataFrame(raw_data)
            self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
            self.data['date'] = self.data['timestamp'].dt.date
            
            logger.info(f"✓ Carregados {len(self.data)} registros")
            return self.data
        except Exception as e:
            logger.error(f"Erro ao carregar dados: {e}")
            return pd.DataFrame()

    def calculate_metrics(self) -> Dict:
        """Calcular métricas principais"""
        logger.info("Calculando métricas...")
        
        if self.data.empty:
            return {}
        
        self.metrics = {
            'total_page_views': int(self.data['page_views'].sum()),
            'total_unique_visitors': int(self.data['unique_visitors'].sum()),
            'average_bounce_rate': round(self.data['bounce_rate'].mean(), 2),
            'average_session_duration': round(self.data['avg_session_duration'].mean(), 2),
            'average_conversion_rate': round(self.data['conversion_rate'].mean(), 2),
            'total_revenue': round(self.data['revenue'].sum(), 2),
            'peak_traffic_hour': int(self.data.groupby('hour')['page_views'].sum().idxmax()),
            'best_day_of_week': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'][
                int(self.data.groupby('day_of_week')['page_views'].sum().idxmax())
            ],
            'top_device': self.data['device'].value_counts().index[0],
            'top_source': self.data['source'].value_counts().index[0],
        }
        
        logger.info("✓ Métricas calculadas")
        return self.metrics
    
    def get_daily_stats(self) -> pd.DataFrame:
        """Obter estatísticas diárias"""
        daily = self.data.groupby('date').agg({
            'page_views': 'sum',
            'unique_visitors': 'sum',
            'bounce_rate': 'mean',
            'avg_session_duration': 'mean',
            'conversion_rate': 'mean',
            'revenue': 'sum'
        }).round(2)
        
        daily.index = daily.index.astype(str)
        return daily
    
    def get_hourly_stats(self) -> pd.DataFrame:
        """Obter estatísticas por hora"""
        hourly = self.data.groupby('hour').agg({
            'page_views': 'sum',
            'unique_visitors': 'sum',
            'bounce_rate': 'mean',
            'conversion_rate': 'mean',
            'revenue': 'sum'
        }).round(2)
        
        return hourly
    
    def get_device_stats(self) -> Dict:
        """Obter estatísticas por dispositivo"""
        device_stats = self.data.groupby('device').agg({
            'page_views': 'sum',
            'unique_visitors': 'sum',
            'bounce_rate': 'mean',
            'conversion_rate': 'mean',
            'revenue': 'sum'
        }).round(2)
        
        return device_stats.to_dict('index')
    
    def get_source_stats(self) -> Dict:
        """Obter estatísticas por fonte de tráfego"""
        source_stats = self.data.groupby('source').agg({
            'page_views': 'sum',
            'unique_visitors': 'sum',
            'bounce_rate': 'mean',
            'conversion_rate': 'mean',
            'revenue': 'sum'
        }).round(2)
        
        return source_stats.to_dict('index')
    
    def get_top_hours(self, n: int = TOP_HOURS_COUNT) -> List[Dict]:
        """Obter top N horas com mais tráfego"""
        top_hours = self.data.groupby('hour')['page_views'].sum().nlargest(n)
        
        result = []
        for hour, views in top_hours.items():
            result.append({
                'hour': f"{hour:02d}:00",
                'page_views': int(views),
                'percentage': round((views / self.data['page_views'].sum()) * 100, 2)
            })
        
        return result
    
    def get_trend_analysis(self, metric: str = 'page_views', days: int = TREND_ANALYSIS_DAYS) -> Dict:
        """Analisar tendência de métrica"""
        if metric not in self.data.columns:
            return {}
        
        daily_data = self.data.groupby('date')[metric].sum()
        
        if len(daily_data) < 2:
            return {}
        
        recent = daily_data.tail(days).mean()
        previous = daily_data.iloc[:-days].mean() if len(daily_data) > days else daily_data.head(days).mean()
        
        change = ((recent - previous) / previous * 100) if previous > 0 else 0
        
        return {
            'metric': metric,
            'recent_average': round(recent, 2),
            'previous_average': round(previous, 2),
            'change_percentage': round(change, 2),
            'trend': 'up' if change > 0 else 'down',
            'period_days': days
        }
    
    def export_report(self, filename: str) -> None:
        """Exportar relatório em JSON"""
        logger.info(f"Exportando relatório para {filename}...")
        
        report = {
            'generated_at': datetime.utcnow().isoformat(),
            'metrics': self.metrics,
            'daily_stats': self.get_daily_stats().to_dict('index'),
            'hourly_stats': self.get_hourly_stats().to_dict('index'),
            'device_stats': self.get_device_stats(),
            'source_stats': self.get_source_stats(),
            'top_hours': self.get_top_hours(),
            'trends': {
                'page_views': self.get_trend_analysis('page_views'),
                'revenue': self.get_trend_analysis('revenue'),
                'conversion_rate': self.get_trend_analysis('conversion_rate'),
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
        
        logger.info(f"✓ Relatório exportado para {filename}")
