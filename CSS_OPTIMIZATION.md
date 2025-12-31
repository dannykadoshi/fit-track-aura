# CSS Optimization

This project uses PurgeCSS to remove unused Bootstrap styles, reducing CSS file size by 51%.

## Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Download and purge Bootstrap CSS:
```bash
npm run download-bootstrap
npm run purge-css
```

3. Collect static files:
```bash
python manage.py collectstatic --noinput
```

## File Sizes

- **Before:** 227 KB (bootstrap.full.css)
- **After:** 110 KB (bootstrap.min.css)
- **Savings:** 117 KB (51% reduction)

## Configuration

The PurgeCSS configuration (`purgecss.config.js`) scans all Django templates to determine which Bootstrap classes are actually used. It keeps:

- All alert, button, background, and text utility classes
- Bootstrap components (modals, dropdowns, navbars, forms)
- Dynamically added classes (show, fade, collapse)
- Select2 and Chart.js related styles

## Development Workflow

When adding new Bootstrap components:

1. Use Bootstrap classes in your templates
2. Run `npm run purge-css`
3. Run `python manage.py collectstatic --noinput`
4. Test to ensure styles work correctly

If styles are missing, add the class pattern to the `safelist` in `purgecss.config.js`.
