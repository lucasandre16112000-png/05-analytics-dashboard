"""
Configuração do pytest para o projeto Analytics Dashboard
"""

import sys
from pathlib import Path

# Adicionar o diretório raiz ao PYTHONPATH
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))
