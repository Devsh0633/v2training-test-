import sys

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

css_override = """
  /* Feature Carousel Nav Overrides for Light Background */
  #features .carousel-nav {
    padding: 0 10px;
    justify-content: flex-start;
  }
  #features .nav-btn {
    border-color: rgba(11, 31, 58, 0.2);
    color: var(--navy);
  }
  #features .nav-btn:disabled {
    opacity: 0.2;
  }
  #features .nav-btn:hover:not(:disabled) {
    background: rgba(11, 31, 58, 0.05);
    border-color: rgba(11, 31, 58, 0.4);
  }
  #features .dot {
    background: rgba(11, 31, 58, 0.15);
  }
  #features .dot.active {
    background: var(--navy);
  }
</style>
"""

if "</style>" in content:
    # ensure we only replace the last </style> or don't duplicate
    if "/* Feature Carousel Nav Overrides" not in content:
        content = content.replace("</style>", css_override)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("CSS overrides applied successfully")
    else:
        print("CSS overrides already applied")
else:
    print("Could not find </style>")
