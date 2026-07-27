#!/usr/bin/env python3
"""
Script to generate static project pages with file listings.
Updated for Data & Business Analyst Hybride positioning
"""

import os
from pathlib import Path

PROJECTS = [
    {
        'name': 'call_me_maybe',
        'path': '/Users/fabiochaput/Documents/VS/call_me_maybe/call_me_maybe',
        'title': 'call_me_maybe - LLM & RAG System',
        'icon': 'fa-robot',
        'category': 'LLM & RAG System',
        'description': 'Inférence structurée sur LLM combinant RAG, prompt engineering et contraintes sur logits pour générer des appels de fonctions JSON stricts.',
        'tags': ['Python', 'LLM (Qwen3)', 'RAG', 'Constrained Decoding', 'HuggingFace', 'Pydantic']
    },
    {
        'name': 'quant_leo_fabio',
        'path': '/Users/fabiochaput/Documents/VS/Quant_leo_fabio',
        'title': 'quant_leo_fabio - Quant Stack & ML',
        'icon': 'fa-calculator',
        'category': 'Quant Stack & ML',
        'description': 'Engine quantitatif complet : collecte de données financières, scoring alpha par modèles ML, backtesting de stratégies.',
        'tags': ['Python', 'XGBoost/CatBoost', 'Backtesting', 'SQLite', 'Finance', 'Feature Engineering']
    },
    {
        'name': 'michelin',
        'path': '/Users/fabiochaput/Documents/VS/michelin_leo/repo_michelin',
        'title': 'michelin - Logistics VRP Optimization',
        'icon': 'fa-truck',
        'category': 'Logistics VRP Optimization',
        'description': 'Plateforme d\'optimisation de routes logistiques avec solver VRP pour minimiser l\'empreinte CO2.',
        'tags': ['FastAPI', 'Python', 'VRP Solver', 'Haversine', 'JavaScript', 'SQLite']
    },
    {
        'name': 'alpha_',
        'path': '/Users/fabiochaput/Documents/VS/alpha_/alpha',
        'title': 'alpha_ - Financial API & Web Dashboard',
        'icon': 'fa-chart-line',
        'category': 'Financial API & Web Dashboard',
        'description': 'Application web et API de données financières temps réel avec architecture FastAPI.',
        'tags': ['FastAPI', 'Python', 'yfinance', 'SQLAlchemy', 'Jinja2']
    },
    {
        'name': 'flyin',
        'path': '/Users/fabiochaput/Documents/VS/flyin',
        'title': 'flyin - Drone Delivery Simulation',
        'icon': 'fa-plane-departure',
        'category': 'Drone Delivery Simulation',
        'description': 'Simulation Python de réseaux de livraison par drones avec algorithmes de pathfinding.',
        'tags': ['Python', 'Graph Theory', 'Pathfinding', 'Simulation', 'Visualization']
    },
    {
        'name': 'codexion',
        'path': '/Users/fabiochaput/Documents/VS/codexion',
        'title': 'codexion - Quantum Compiling Simulation',
        'icon': 'fa-atom',
        'category': 'Quantum Compiling Simulation',
        'description': 'Challenge de concurrence basé sur le problème des Philosophes Dînant, avec prévention de deadlocks.',
        'tags': ['C', 'Multithreading', 'Synchronization', 'pthread', 'Makefile']
    },
    {
        'name': 'cardfraud',
        'path': '/Users/fabiochaput/Documents/VS/CardFraud',
        'title': 'CardFraud - Credit Card Fraud Detection',
        'icon': 'fa-credit-card',
        'category': 'Machine Learning & Fraud Detection',
        'description': 'Pipeline de détection de fraude bancaire avec XGBoost sur dataset déséquilibré. Optimisation du seuil de décision basé sur le recall.',
        'tags': ['Python', 'XGBoost', 'Scikit-learn', 'Pandas', 'Data Science', 'Machine Learning']
    }
]

EXCLUDE_DIRS = ['.git', '.venv', 'venv', '__pycache__', '__exemple_iris_data', 'node_modules', '.vscode']
EXCLUDE_FILES = ['.DS_Store', '.gitignore', '.python-version', 'uv.lock']

FILE_ICONS = {
    '.py': 'fa-file-code', '.html': 'fa-file-code', '.css': 'fa-file-code',
    '.js': 'fa-file-code', '.json': 'fa-file-code', '.md': 'fa-file-alt',
    '.txt': 'fa-file-alt', '.csv': 'fa-file-csv', '.sql': 'fa-database',
    '.db': 'fa-database', '.ipynb': 'fa-book', '.png': 'fa-file-image',
    '.jpg': 'fa-file-image', '.jpeg': 'fa-file-image', '.gif': 'fa-file-image',
    '.pdf': 'fa-file-pdf', 'Makefile': 'fa-cog', '.sh': 'fa-terminal',
    '.toml': 'fa-cog', '.lock': 'fa-lock', 'requirements.txt': 'fa-list',
    'README.md': 'fa-book-open'
}

FILE_COLORS = {
    '.py': '#3572A5', '.html': '#E34F26', '.css': '#1572B6', '.js': '#F1E05A',
    '.json': '#292929', '.md': '#083FA1', '.txt': '#333333', '.csv': '#239120',
    '.sql': '#00758F', '.db': '#00758F', '.ipynb': '#DA5B0B', '.png': '#D63AFF',
    '.jpg': '#D63AFF', '.jpeg': '#D63AFF', '.gif': '#D63AFF', '.pdf': '#D63A0B',
    'Makefile': '#428850', '.sh': '#4EAA25', '.toml': '#9C4121'
}


def get_icon(name):
    ext = os.path.splitext(name)[1].lower()
    return FILE_ICONS.get(ext, FILE_ICONS.get(name, 'fa-file'))


def get_color(name):
    ext = os.path.splitext(name)[1].lower()
    return FILE_COLORS.get(ext, FILE_COLORS.get(name, '#64748b'))


def get_size(path):
    try:
        s = os.path.getsize(path)
        if s < 1024: return f"{s} B"
        elif s < 1024*1024: return f"{s/1024:.1f} KB"
        elif s < 1024*1024*1024: return f"{s/(1024*1024):.1f} MB"
        return f"{s/(1024*1024*1024):.1f} GB"
    except: return ""


def scan_dir(path, root=None):
    if root is None: root = path
    items = []
    try:
        for name in sorted(os.listdir(path)):
            if name in EXCLUDE_DIRS or name in EXCLUDE_FILES:
                continue
            full_path = os.path.join(path, name)
            rel_path = os.path.relpath(full_path, root)
            if os.path.isdir(full_path):
                items.append({
                    'name': name, 'path': rel_path, 'type': 'dir',
                    'children': scan_dir(full_path, root)
                })
            else:
                items.append({
                    'name': name, 'path': rel_path, 'type': 'file',
                    'size': get_size(full_path)
                })
    except PermissionError:
        pass
    return items


def count_files(items):
    files = 0
    dirs = 0
    for item in items:
        if item['type'] == 'dir':
            dirs += 1
            c_f, c_d = count_files(item['children'])
            files += c_f
            dirs += c_d
        else:
            files += 1
    return files, dirs


def gen_tree(items, level=0, project_path=None):
    html = ""
    base_dir = '/Users/fabiochaput/Documents/VS/portfolio/website/projects'
    
    for item in items:
        indent = "  " * (level + 1)
        if item['type'] == 'dir':
            html += f"{indent}<li class='tree-item directory'>\n"
            html += f"{indent}  <div class='tree-header' onclick='toggleDir(this)'>\n"
            html += f"{indent}    <i class='fas fa-folder tree-icon'></i>\n"
            html += f"{indent}    <span class='tree-name'>{item['name']}</span>\n"
            html += f"{indent}    <i class='fas fa-chevron-right tree-toggle'></i>\n"
            html += f"{indent}  </div>\n"
            html += f"{indent}  <ul class='tree-children' style='display:none;'>\n"
            html += gen_tree(item['children'], level + 1, project_path)
            html += f"{indent}  </ul>\n"
            html += f"{indent}</li>\n"
        else:
            ext = os.path.splitext(item['name'])[1].lower()
            common = ['.py', '.html', '.css', '.js', '.json', '.md', '.txt', '.csv', '.sql', '.ipynb', '.pdf', '.png', '.jpg', '.jpeg', '.gif']
            
            full_file_path = os.path.join(project_path, item['path'])
            rel_path = os.path.relpath(full_file_path, base_dir).replace(os.sep, '/')
            
            if ext in common or ext == '':
                icon = get_icon(item['name'])
                color = get_color(item['name'])
                html += f"{indent}<li class='tree-item file'>\n"
                html += f"{indent}  <a href='{rel_path}' class='tree-file-link' download>\n"
                html += f"{indent}    <i class='fas {icon} tree-icon' style='color:{color}'></i>\n"
                html += f"{indent}    <span class='tree-name'>{item['name']}</span>\n"
                html += f"{indent}    <span class='tree-size'>{item['size']}</span>\n"
                html += f"{indent}  </a>\n"
                html += f"{indent}</li>\n"
            else:
                icon = get_icon(item['name'])
                color = get_color(item['name'])
                html += f"{indent}<li class='tree-item file'>\n"
                html += f"{indent}  <div class='tree-file'>\n"
                html += f"{indent}    <i class='fas {icon} tree-icon' style='color:{color}'></i>\n"
                html += f"{indent}    <span class='tree-name'>{item['name']}</span>\n"
                html += f"{indent}    <span class='tree-size'>{item['size']}</span>\n"
                html += f"{indent}  </div>\n"
                html += f"{indent}</li>\n"
    return html


def gen_page(project):
    tree_html = ""
    f_count, d_count = 0, 0
    
    tree = scan_dir(project['path'])
    tree_html = gen_tree(tree, 0, project['path'])
    f_count, d_count = count_files(tree)
    
    tags = ''.join(f"<span>{t}</span>" for t in project['tags'])
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{project['title']} - Fabio Chaput Portfolio</title>
<link rel="stylesheet" href="../styles.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
<nav class="navbar">
  <div class="container">
    <a href="../index.html" class="logo">Fabio Chaput</a>
    <div class="nav-links">
      <a href="../index.html#home">Home</a>
      <a href="../index.html#projects">Projects</a>
      <a href="../index.html#skills">Skills</a>
      <a href="../index.html#cv">CV</a>
      <a href="../index.html#contact">Contact</a>
    </div>
    <div class="hamburger"><i class="fas fa-bars"></i></div>
  </div>
</nav>

<div style="max-width:1200px;margin:0 auto;padding:2rem;">
  <a href="../index.html" style="display:inline-flex;align-items:center;gap:0.5rem;margin-bottom:2rem;color:var(--text-secondary);">
    <i class="fas fa-arrow-left"></i> Back to Projects
  </a>
  
  <div style="margin-bottom:2rem;padding-bottom:2rem;border-bottom:1px solid var(--border-color);">
    <div style="font-size:3rem;color:var(--primary-color);margin-bottom:1rem;">
      <i class="fas {project['icon']}"></i>
    </div>
    <h1>{project['title']}</h1>
    <p style="color:var(--primary-color);font-size:0.9rem;font-weight:600;margin-bottom:1rem;text-transform:uppercase;letter-spacing:0.5px;">
      {project['category']}
    </p>
    <p style="font-size:0.95rem;margin-bottom:1.5rem;color:var(--text-secondary);">
      {project['description']}
    </p>
    <div style="display:flex;gap:2rem;flex-wrap:wrap;margin-bottom:1rem;">
      <div style="display:flex;align-items:center;gap:0.5rem;color:var(--text-secondary);">
        <i class="fas fa-folder" style="color:var(--primary-color);"></i>
        <span>{d_count} Directories</span>
      </div>
      <div style="display:flex;align-items:center;gap:0.5rem;color:var(--text-secondary);">
        <i class="fas fa-file" style="color:var(--primary-color);"></i>
        <span>{f_count} Files</span>
      </div>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-bottom:1rem;">
      {tags}
    </div>
    <div class="project-links">
      <a href="../index.html" class="btn-project">
        <i class="fas fa-arrow-left"></i> Back to Projects
      </a>
    </div>
  </div>
  
  <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-xl);overflow:hidden;margin-top:2rem;">
    <div style="padding:1rem 1.5rem;background:var(--bg-darker);border-bottom:1px solid var(--border-color);display:flex;align-items:center;gap:0.5rem;">
      <i class="fas fa-folder-open"></i>
      <span>Project Files</span>
    </div>
    <ul style="list-style:none;padding:0;margin:0;">
      {tree_html}
    </ul>
  </div>
</div>

<footer class="footer">
  <div class="container">
    <p>&copy; 2026 Fabio Chaput. All rights reserved.</p>
  </div>
</footer>

<script src="../script.js"></script>
<script>
function toggleDir(el) {{
  var children = el.nextElementSibling;
  if (children.style.display === 'none') {{
    children.style.display = 'block';
  }} else {{
    children.style.display = 'none';
  }}
}}
document.addEventListener('DOMContentLoaded', function() {{
  var headers = document.querySelectorAll('.tree-header');
  headers.forEach(function(h) {{
    var children = h.nextElementSibling;
    if (children) children.style.display = 'block';
  }});
}});
</script>
</body>
</html>
"""


def main():
    out_dir = Path('/Users/fabiochaput/Documents/VS/portfolio/website/projects')
    out_dir.mkdir(parents=True, exist_ok=True)
    
    for p in PROJECTS:
        fname = f"{p['name'].replace('_', '-')}.html"
        fpath = out_dir / fname
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(gen_page(p))
        print(f"Generated: {fname}")
    
    print(f"\nDone! {len(PROJECTS)} pages created in {out_dir}")


if __name__ == '__main__':
    main()
