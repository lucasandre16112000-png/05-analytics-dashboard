# 📊 Professional Analytics Dashboard

A complete and professional analytics dashboard built with Python, Pandas, Plotly, and Jinja2. It generates an interactive HTML report with various metrics and charts for analyzing website traffic data.

## ✨ Key Features

- **Interactive Dashboard**: Rich and interactive data visualizations with Plotly.js
- **Comprehensive Metrics**: Calculation of 10+ essential metrics such as Page Views, Unique Visitors, Conversion Rate, Revenue, etc.
- **Temporal Analysis**: Time series charts for traffic analysis by day and hour
- **Segment Analysis**: Pie charts for analyzing traffic distribution by device and source
- **Trend Analysis**: Calculation of growth or decline trends for key metrics
- **Professional Architecture**: Modular and well-organized code, following software engineering best practices
- **HTML Templates**: Use of Jinja2 for separation of Python code from HTML presentation
- **Comprehensive Tests**: Unit tests with Pytest to ensure quality and calculation correctness
- **Flexible Configuration**: Centralized configurations for easy customization
- **Report Export**: Generation of a complete JSON report with all data and metrics

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|:---|:---|:---|
| **Python** | 3.8+ | Main programming language |
| **Pandas** | 2.0+ | Data manipulation and analysis |
| **Plotly** | 5.0+ | Interactive visualizations |
| **Jinja2** | 3.0+ | HTML templates |
| **Pytest** | 7.0+ | Unit tests |

## 📂 Project Structure

```
/05-analytics-dashboard
├── dashboard/
│   ├── config/                    # Configuration module
│   │   ├── __init__.py
│   │   ├── logger.py              # Logger configuration
│   │   └── settings.py            # General settings
│   ├── data_engine/               # Data analysis module
│   │   ├── __init__.py
│   │   └── analytics.py           # AnalyticsEngine class
│   ├── static/                    # Static files (CSS, JS)
│   │   └── css/
│   │       └── style.css
│   ├── templates/                 # HTML templates (Jinja2)
│   │   └── index.html
│   ├── __init__.py
│   ├── generator.py               # DashboardGenerator class
│   └── main.py                    # Main script
├── data/                          # Input data
│   └── sample_data.json
├── output/                        # Output files
│   ├── analytics_report.json
│   └── dashboard.html
├── tests/                         # Unit tests
│   ├── __init__.py
│   ├── test_analytics.py
│   └── test_generator.py
├── .env.example                   # Example configuration file
├── .gitignore                     # Files to ignore in Git
├── requirements.txt               # Project dependencies
└── README.md                      # This file
```

## 📋 Installation and Execution Guide (For Everyone)

This guide was created so that anyone, even without technical knowledge, can run this project.

### Prerequisites

1. **Git**: Tool to download (clone) the code from GitHub.
   - [**Download Git here**](https://git-scm.com/downloads)

2. **Python**: The programming language used in the project (version 3.8 or higher).
   - [**Download Python here**](https://www.python.org/downloads/)
   - **Important**: During Python installation on Windows, check the box that says **"Add Python to PATH"**.

### Step 1: Clone the Repository

Open your terminal (or **Git Bash** on Windows) and use the command below to download the project:

```bash
git clone https://github.com/lucasandre16112000-png/05-analytics-dashboard.git
cd 05-analytics-dashboard
```

### Step 2: Create and Activate a Virtual Environment

A virtual environment isolates the project's dependencies, preventing conflicts with other Python applications.

**On Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**On macOS or Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You'll know the virtual environment is activated when you see `(venv)` at the beginning of your terminal line.

### Step 3: Install Dependencies

With the virtual environment activated, install the necessary libraries:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Dashboard

Execute the main script to generate the dashboard:

```bash
python -m dashboard.main
```

The script will:
1. Generate sample data (if it doesn't exist)
2. Calculate all metrics and analyses
3. Generate the JSON report in `output/analytics_report.json`
4. Generate the HTML dashboard in `output/dashboard.html`

### Step 5: View the Dashboard

Open the `output/dashboard.html` file in your browser to view the interactive dashboard with all charts and metrics.

## 🚀 Usage Examples

### Example 1: Use the Default Script

The default script already contains a ready-to-use example:

```bash
python -m dashboard.main
```

### Example 2: Use Custom Data

To use your own data, place a JSON file in `data/sample_data.json` with the following format:

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

Then execute:

```bash
python -m dashboard.main
```

### Example 3: Use AnalyticsEngine in Your Own Code

You can import the engine in your own Python project:

```python
from dashboard.data_engine.analytics import AnalyticsEngine
from pathlib import Path

# Create engine
engine = AnalyticsEngine()

# Load data
engine.load_data_from_file('data/sample_data.json')

# Calculate metrics
engine.calculate_metrics()

# Get metrics
metrics = engine.get_metrics()
print(f"Page Views: {metrics['page_views']}")
print(f"Conversion: {metrics['conversion_rate']:.2%}")

# Export report
engine.export_report('output/report.json')
```

## 🧪 Run Tests

To ensure everything is working correctly, run the test suite:

```bash
pytest
```

Or with more details:

```bash
pytest -v
```

## 📊 Calculated Metrics

The dashboard automatically calculates the following metrics:

| Metric | Description |
|---------|-----------|
| **Page Views** | Total page views |
| **Unique Visitors** | Total unique visitors |
| **Conversion Rate** | Conversion percentage |
| **Average Order Value** | Average value per order |
| **Revenue** | Total revenue |
| **Bounce Rate** | Bounce rate |
| **Session Duration** | Average session duration |
| **Traffic by Device** | Traffic distribution by device |
| **Traffic by Source** | Traffic distribution by source |
| **Daily Trends** | Daily trends |
| **Hourly Trends** | Hourly trends |

## 🔒 Best Practices

- **Sensitive Data**: Do not include sensitive or personal data in the repository
- **Configuration**: Use the `.env` file for sensitive configurations
- **Tests**: Always run tests before committing
- **Documentation**: Keep documentation up to date

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an issue to report bugs
- Submit a pull request with improvements
- Suggest new features

## 📄 License

This project is under the MIT license. See the `LICENSE` file for more details.

## 👨‍💻 Author

Lucas André S - [GitHub](https://github.com/lucasandre16112000-png)
