# Fabio Chaput - Portfolio Website

A modern, responsive portfolio website showcasing my projects and skills. Projects are now displayed directly in the main page with clear descriptions, key features, and direct links to GitHub repositories.

## Projects Featured

All projects now display key information directly in the project cards with direct GitHub links for open source projects.

### Open Source Projects (with GitHub access)

1. **call_me_maybe** - LLM & RAG System
   - Function calling implementation for LLMs
   - Uses constrained decoding
   - Qwen/Qwen3-0.6B model integration

2. **quant_leo_fabio** - Quantitative Research Stack
   - Financial dataset building
   - XGBoost/CatBoost model training
   - Backtesting and daily report generation

3. **michelin** - Logistics Optimization Platform
   - Delivery route optimization
   - FastAPI backend with static web frontend
   - VRP solver with CO2 savings estimation

4. **alpha_** - Stock Data API & Web Dashboard
   - FastAPI-based web application
   - Real-time stock data using yfinance
   - Responsive frontend with account management

5. **flyin** - Drone Delivery Simulation
   - Python simulation of drone delivery networks
   - Pathfinding algorithms and advanced routing
   - Network visualization capabilities

6. **codexion** - Quantum Compiling Simulation
   - Concurrency and synchronization challenge
   - Based on the Dining Philosophers problem
   - Implements deadlock and starvation prevention

7. **cardfraud** - Credit Card Fraud Detection
   - Pipeline de détection de fraude avec XGBoost
   - Gestion du déséquilibre de classes (dataset Kaggle)
   - Optimisation du seuil basé sur le recall

### Enterprise Projects (private)
- **nestle_bi_stack** - Enterprise Data Platform & ML at Nestlé
- **nespresso_vba_analytics** - Sales Analytics Tool for Nespresso

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
   - Open source projects now link directly to GitHub repositories
   - Enterprise projects display a "Enterprise Project" button
   - No file browser pages are generated anymore

### Change Styling
Edit `styles.css` to customize:
- Color scheme (CSS variables at the top)
- Typography (font families, sizes)
- Spacing and layout
- Animations and transitions

### Add More Projects
To add a new project, simply add a project card in `index.html`:

#### For Open Source Projects:
1. Add project card with GitHub link: `href="https://github.com/..." target="_blank"`
2. Use button: `<i class="fab fa-github"></i> View Code`
3. Add to `PROJECTS` list in `generate_project_pages.py` with `github_url` field

#### For Enterprise Projects:
1. Add project card with disabled button: `href="#" style="pointer-events: none; opacity: 0.6;"`
2. Use button: `<i class="fas fa-lock"></i> Enterprise Project`
3. Optionally add to `PROJECTS` list (no github_url needed)

## File Structure

```
portfolio/website/
├── index.html              # Main HTML file (contains all project cards)
├── styles.css              # CSS styles
├── script.js               # JavaScript for interactivity
├── generate_project_pages.py  # Legacy script (no longer generates pages)
└── README.md               # This file
```

## Project Display

Projects are now displayed directly in the main `index.html` page with:
- Project icon, title, and category
- Concise description
- Key features/highlights
- Technology tags
- Direct GitHub link (for open source) or Enterprise badge (for private)

### Updating Project File Listings

When you add, remove, or modify files in your projects, you can regenerate the project pages:

The `generate_project_pages.py` script is now deprecated and no longer generates project pages. All projects are managed directly in `index.html`.

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
