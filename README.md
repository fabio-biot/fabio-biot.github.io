# Fabio Chaput - Portfolio Website

A modern, responsive portfolio website showcasing my projects and skills with an integrated file browser.

## Projects Featured

All projects include a file browser that allows visitors to explore the complete project structure and download individual files.

1. **alpha_** - Stock Data API & Financial Dashboard
   - FastAPI-based web application
   - Real-time stock data using yfinance
   - Responsive frontend with account management

2. **flyin** - Drone Delivery Simulation
   - Python simulation of drone delivery networks
   - Pathfinding algorithms and advanced routing
   - Network visualization capabilities

3. **codexion** - Quantum Compiling Simulation
   - Concurrency and synchronization challenge
   - Based on the Dining Philosophers problem
   - Implements deadlock and starvation prevention

4. **quant_leo_fabio** - Quantitative Research Stack
   - Financial dataset building
   - XGBoost/CatBoost model training
   - Backtesting and daily report generation

5. **call_me_maybe** - LLM Function Calling
   - Function calling implementation for LLMs
   - Uses constrained decoding
   - Qwen/Qwen3-0.6B model integration

6. **michelin** - Logistics Optimization Platform
   - Delivery route optimization
   - FastAPI backend with static web frontend
   - VRP solver with CO2 savings estimation

7. **cardfraud** - Credit Card Fraud Detection
   - Pipeline de détection de fraude avec XGBoost
   - Gestion du déséquilibre de classes (dataset Kaggle)
   - Optimisation du seuil basé sur le recall

## How to Use

### Option 1: Open Directly in Browser
Simply open `index.html` in your web browser:

```bash
# Navigate to the website directory
cd /Users/fabiochaput/Documents/VS/portfolio/website

# Open in default browser
open index.html
```

**Note:** When opening directly in the browser (using `file://` protocol), some features like file downloads may be restricted by browser security policies. For the best experience, use a local server.

### Option 2: Local Server
For best results, serve the files using a local server:

```bash
# Using Python's built-in HTTP server
python3 -m http.server 8000

# Then open in browser
# http://localhost:8000
```

Or using PHP:
```bash
php -S localhost:8000
```

### Option 3: VS Code Live Server
If you have the Live Server extension installed in VS Code:
1. Open the `portfolio/website` folder in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Project Filtering**: Filter projects by category (AI/ML, Web/App, Algorithms, Data Science)
- **Smooth Animations**: CSS animations and transitions for a polished experience
- **Interactive Elements**: Hover effects, scroll animations, and smooth scrolling
- **Contact Form**: Functional contact form with validation
- **Dark Theme**: Modern dark color scheme with gradient accents
- **Font Awesome Icons**: Professional icons throughout the site

## Customization

### Update Your Information
1. Edit `index.html`:
   - Update the hero section with your name, title, and description
   - Update the contact information (email, GitHub, LinkedIn links)
   - Modify project descriptions as needed

2. Update project paths:
   - The "View Files" buttons now link to dedicated project pages with file browsers
   - Project pages are auto-generated in the `projects/` directory
   - To update file listings, run `python3 generate_project_pages.py`

### Change Styling
Edit `styles.css` to customize:
- Color scheme (CSS variables at the top)
- Typography (font families, sizes)
- Spacing and layout
- Animations and transitions

### Add More Projects
To add a new project:
1. Add a new project card in `index.html` under the Projects Grid section
2. Follow the existing card structure with appropriate tags for filtering
3. Add a unique icon from Font Awesome
4. Add the project to the `PROJECTS` list in `generate_project_pages.py`
5. Run `python3 generate_project_pages.py` to create the project page

Alternatively, edit `generate_project_pages.py` to add your project to the `PROJECTS` list, then run it to automatically create both the project page and update the index.html link.

## File Structure

```
portfolio/website/
├── index.html              # Main HTML file
├── styles.css              # CSS styles
├── script.js               # JavaScript for interactivity
├── generate_project_pages.py  # Script to regenerate project pages
├── projects/               # Individual project pages with file browsers
│   ├── alpha-.html
│   ├── flyin.html
│   ├── codexion.html
│   ├── quant-leo-fabio.html
│   ├── call-me-maybe.html
│   ├── michelin.html
│   └── cardfraud.html
└── README.md               # This file
```

## File Browser Feature

Each project has a dedicated page that displays:
- Project description and metadata
- Complete file tree with folder structure
- File icons based on file type
- File sizes
- Direct download links for common file types

### Updating Project File Listings

When you add, remove, or modify files in your projects, you can regenerate the project pages:

```bash
cd /Users/fabiochaput/Documents/VS/portfolio/website
python3 generate_project_pages.py
```

This will scan each project directory and recreate the HTML pages with updated file listings.

### Excluded Files and Directories

The following are automatically excluded from the file browser:
- `.git/` - Git repositories
- `.venv/`, `venv/` - Python virtual environments
- `__pycache__/` - Python cache
- `.DS_Store` - macOS metadata
- `.gitignore`, `.python-version` - Configuration files
- `uv.lock` - Dependency lock files

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (Chrome, Safari)

## Dependencies

- [Font Awesome](https://fontawesome.com/) - Icons (loaded from CDN)
- No other external dependencies required

## Performance

- Optimized for fast loading
- Lazy loading for images (if added)
- Efficient JavaScript with event delegation
- CSS transitions for smooth animations

## Tips

1. For production use, consider:
   - Minifying CSS and JavaScript
   - Optimizing images
   - Adding meta tags for SEO
   - Setting up a custom domain

2. To deploy:
   - Upload to GitHub Pages
   - Deploy to Netlify, Vercel, or other hosting services
   - Use any static site hosting

## License

This portfolio website is custom-built and free to use for personal purposes.
