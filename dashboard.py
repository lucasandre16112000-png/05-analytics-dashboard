"""
Real-time Analytics Dashboard com Plotly
Exemplo de visualização de dados em tempo real com múltiplos gráficos e métricas.
"""

import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AnalyticsEngine:
    """Engine de análise de dados em tempo real"""
    
    def __init__(self):
        self.data = []
        self.metrics = {}
        self.timestamp = datetime.utcnow()
    
    def generate_sample_analytics_data(self, days: int = 30) -> pd.DataFrame:
        """Gerar dados de exemplo para análise"""
        logger.info(f"Gerando dados de análise para {days} dias...")
        
        np.random.seed(42)
        
        data = []
        base_date = datetime.utcnow() - timedelta(days=days)
        
        for day in range(days):
            current_date = base_date + timedelta(days=day)
            
            # Simular dados de tráfego com padrão semanal
            day_of_week = current_date.weekday()
            base_traffic = 1000 + (day_of_week * 200)  # Mais tráfego nos fins de semana
            
            for hour in range(24):
                # Padrão de tráfego por hora
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
    
    def get_top_hours(self, n: int = 5) -> List[Dict]:
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
    
    def get_trend_analysis(self, metric: str = 'page_views', days: int = 7) -> Dict:
        """Analisar tendência de métrica"""
        if metric not in self.data.columns:
            return {}
        
        daily_data = self.data.groupby('date')[metric].sum()
        
        if len(daily_data) < 2:
            return {}
        
        # Calcular tendência
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
    
    def export_report(self, filename: str = 'analytics_report.json') -> None:
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


class DashboardGenerator:
    """Gerador de dashboard HTML"""
    
    @staticmethod
    def generate_html_dashboard(analytics: AnalyticsEngine, filename: str = 'dashboard.html') -> None:
        """Gerar dashboard HTML interativo"""
        logger.info(f"Gerando dashboard HTML...")
        
        metrics = analytics.metrics
        daily_stats = analytics.get_daily_stats()
        hourly_stats = analytics.get_hourly_stats()
        device_stats = analytics.get_device_stats()
        source_stats = analytics.get_source_stats()
        top_hours = analytics.get_top_hours()
        
        html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analytics Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }}
        
        .header h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        
        .header p {{
            color: #666;
            font-size: 14px;
        }}
        
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .metric-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #667eea;
        }}
        
        .metric-card h3 {{
            color: #666;
            font-size: 14px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }}
        
        .metric-card .value {{
            color: #333;
            font-size: 28px;
            font-weight: bold;
        }}
        
        .metric-card .unit {{
            color: #999;
            font-size: 12px;
            margin-top: 5px;
        }}
        
        .charts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .chart-container {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        .chart-container h3 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 16px;
        }}
        
        .chart {{
            width: 100%;
            height: 400px;
        }}
        
        .footer {{
            text-align: center;
            color: white;
            padding: 20px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Analytics Dashboard</h1>
            <p>Gerado em {datetime.utcnow().strftime('%d/%m/%Y às %H:%M:%S')}</p>
        </div>
        
        <div class="metrics-grid">
            <div class="metric-card">
                <h3>Page Views</h3>
                <div class="value">{metrics.get('total_page_views', 0):,}</div>
                <div class="unit">Total</div>
            </div>
            
            <div class="metric-card">
                <h3>Visitantes Únicos</h3>
                <div class="value">{metrics.get('total_unique_visitors', 0):,}</div>
                <div class="unit">Total</div>
            </div>
            
            <div class="metric-card">
                <h3>Taxa de Conversão</h3>
                <div class="value">{metrics.get('average_conversion_rate', 0):.2f}%</div>
                <div class="unit">Média</div>
            </div>
            
            <div class="metric-card">
                <h3>Receita</h3>
                <div class="value">R$ {metrics.get('total_revenue', 0):,.2f}</div>
                <div class="unit">Total</div>
            </div>
            
            <div class="metric-card">
                <h3>Taxa de Rejeição</h3>
                <div class="value">{metrics.get('average_bounce_rate', 0):.2f}%</div>
                <div class="unit">Média</div>
            </div>
            
            <div class="metric-card">
                <h3>Duração da Sessão</h3>
                <div class="value">{metrics.get('average_session_duration', 0):.2f}</div>
                <div class="unit">Minutos</div>
            </div>
        </div>
        
        <div class="charts-grid">
            <div class="chart-container">
                <h3>Page Views por Hora</h3>
                <div id="hourly-chart" class="chart"></div>
            </div>
            
            <div class="chart-container">
                <h3>Page Views por Dia</h3>
                <div id="daily-chart" class="chart"></div>
            </div>
            
            <div class="chart-container">
                <h3>Distribuição por Dispositivo</h3>
                <div id="device-chart" class="chart"></div>
            </div>
            
            <div class="chart-container">
                <h3>Distribuição por Fonte</h3>
                <div id="source-chart" class="chart"></div>
            </div>
        </div>
        
        <div class="footer">
            <p>Dashboard gerado automaticamente • Dados em tempo real</p>
        </div>
    </div>
    
    <script>
        // Gráfico de Page Views por Hora
        var hourlyData = {json.dumps(hourly_stats.to_dict())};
        var hourlyTrace = {{
            x: Object.keys(hourlyData),
            y: Object.values(hourlyData).map(d => d['page_views']),
            type: 'scatter',
            mode: 'lines+markers',
            fill: 'tozeroy',
            name: 'Page Views',
            line: {{color: '#667eea'}}
        }};
        Plotly.newPlot('hourly-chart', [hourlyTrace], {{
            title: '',
            xaxis: {{title: 'Hora do Dia'}},
            yaxis: {{title: 'Page Views'}},
            margin: {{t: 20}}
        }});
        
        // Gráfico de Page Views por Dia
        var dailyData = {json.dumps(daily_stats.to_dict())};
        var dailyTrace = {{
            x: Object.keys(dailyData),
            y: Object.values(dailyData).map(d => d['page_views']),
            type: 'bar',
            name: 'Page Views',
            marker: {{color: '#764ba2'}}
        }};
        Plotly.newPlot('daily-chart', [dailyTrace], {{
            title: '',
            xaxis: {{title: 'Data'}},
            yaxis: {{title: 'Page Views'}},
            margin: {{t: 20}}
        }});
        
        // Gráfico de Dispositivos
        var deviceData = {json.dumps(device_stats)};
        var deviceTrace = {{
            labels: Object.keys(deviceData),
            values: Object.values(deviceData).map(d => d['page_views']),
            type: 'pie',
            marker: {{colors: ['#667eea', '#764ba2', '#f093fb']}}
        }};
        Plotly.newPlot('device-chart', [deviceTrace], {{
            title: '',
            margin: {{t: 20}}
        }});
        
        // Gráfico de Fontes
        var sourceData = {json.dumps(source_stats)};
        var sourceTrace = {{
            labels: Object.keys(sourceData),
            values: Object.values(sourceData).map(d => d['page_views']),
            type: 'pie',
            marker: {{colors: ['#667eea', '#764ba2', '#f093fb', '#4facfe']}}
        }};
        Plotly.newPlot('source-chart', [sourceTrace], {{
            title: '',
            margin: {{t: 20}}
        }});
    </script>
</body>
</html>
        """
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        
        logger.info(f"✓ Dashboard HTML gerado: {filename}")


# ============================================================================
# EXEMPLO DE USO
# ============================================================================

def main():
    """Exemplo de uso do analytics dashboard"""
    
    print("=" * 80)
    print("ANALYTICS DASHBOARD - EXEMPLO DE USO")
    print("=" * 80)
    
    # Criar engine de análise
    analytics = AnalyticsEngine()
    
    # Gerar dados
    print("\n📊 GERANDO DADOS")
    print("-" * 80)
    analytics.generate_sample_analytics_data(days=30)
    
    # Calcular métricas
    print("\n📈 CALCULANDO MÉTRICAS")
    print("-" * 80)
    metrics = analytics.calculate_metrics()
    
    print(f"Total de Page Views: {metrics['total_page_views']:,}")
    print(f"Visitantes Únicos: {metrics['total_unique_visitors']:,}")
    print(f"Taxa de Conversão Média: {metrics['average_conversion_rate']:.2f}%")
    print(f"Receita Total: R$ {metrics['total_revenue']:,.2f}")
    print(f"Taxa de Rejeição Média: {metrics['average_bounce_rate']:.2f}%")
    print(f"Duração Média de Sessão: {metrics['average_session_duration']:.2f} min")
    print(f"Hora de Pico: {metrics['peak_traffic_hour']:02d}:00")
    print(f"Melhor Dia da Semana: {metrics['best_day_of_week']}")
    print(f"Dispositivo Mais Usado: {metrics['top_device']}")
    print(f"Fonte de Tráfego Principal: {metrics['top_source']}")
    
    # Análise de tendências
    print("\n📊 ANÁLISE DE TENDÊNCIAS")
    print("-" * 80)
    
    trends = {
        'page_views': analytics.get_trend_analysis('page_views'),
        'revenue': analytics.get_trend_analysis('revenue'),
        'conversion_rate': analytics.get_trend_analysis('conversion_rate'),
    }
    
    for metric, trend in trends.items():
        if trend:
            print(f"\n{metric.upper()}:")
            print(f"  Média Recente (7 dias): {trend['recent_average']:.2f}")
            print(f"  Média Anterior: {trend['previous_average']:.2f}")
            print(f"  Mudança: {trend['change_percentage']:+.2f}% ({trend['trend']})")
    
    # Top horas
    print("\n⏰ TOP HORAS COM MAIS TRÁFEGO")
    print("-" * 80)
    
    top_hours = analytics.get_top_hours(5)
    for i, hour_data in enumerate(top_hours, 1):
        print(f"{i}. {hour_data['hour']}: {hour_data['page_views']:,} views ({hour_data['percentage']:.1f}%)")
    
    # Exportar relatório
    print("\n💾 EXPORTANDO RELATÓRIOS")
    print("-" * 80)
    analytics.export_report('analytics_report.json')
    
    # Gerar dashboard HTML
    DashboardGenerator.generate_html_dashboard(analytics, 'dashboard.html')
    
    print(f"\n✅ Dashboard gerado com sucesso!")
    print(f"📁 Arquivos criados:")
    print(f"   - analytics_report.json")
    print(f"   - dashboard.html")


if __name__ == "__main__":
    main()
