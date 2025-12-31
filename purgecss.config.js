module.exports = {
  content: [
    './templates/**/*.html',
    './workouts/templates/**/*.html',
    './goals/templates/**/*.html',
    './users/templates/**/*.html',
    './static/css/style.css',
  ],
  css: ['./static/css/bootstrap.full.css'],
  output: './static/css/bootstrap.min.css',
  safelist: {
    // Keep these classes that might be dynamically added
    standard: [
      'show',
      'fade',
      'collapse',
      'collapsing',
      'dropdown-menu-dark',
      'dropdown-menu-end',
      'modal-backdrop',
      'toast',
      'popover',
      'tooltip',
    ],
    // Keep all Alert variants
    deep: [
      /^alert-/,
      /^btn-/,
      /^bg-/,
      /^text-/,
      /^border-/,
      /^dropdown-/,
      /^navbar-/,
      /^nav-/,
      /^card-/,
      /^badge-/,
      /^form-/,
      /^input-/,
      /^modal-/,
      /^tab-/,
      /^list-group-/,
    ],
    greedy: [
      /data-bs-/,
      /select2/,
      /chart/,
    ]
  }
}
