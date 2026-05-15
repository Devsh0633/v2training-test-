import sys

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """  .features-wrapper {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
  }
  .feature-block {
    display: flex;
    flex-direction: column;
    gap: 32px;
    background: var(--white);
    border: 1px solid var(--gray-200);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    margin-bottom: 0 !important;
  }
  .feature-block .feature-visual {
    order: 2;
    margin-top: auto;
  }
  .feature-block .feature-copy {
    order: 1;
  }
  .feature-block.reverse .feature-copy { order: 1; }
  .feature-block h2 {
    font-size: 24px !important;
  }
  
  @media (max-width: 900px) {
    .features-wrapper { grid-template-columns: 1fr; }
  }"""

new_css = """  .features-wrapper {
    display: flex;
    overflow-x: auto;
    gap: 20px;
    padding-bottom: 24px;
    scroll-snap-type: x mandatory;
    margin: 0 -24px; /* full bleed edge to edge */
    padding-left: 24px;
    padding-right: 24px;
    scrollbar-width: thin;
    scrollbar-color: var(--cyan) var(--gray-200);
  }
  .features-wrapper::-webkit-scrollbar {
    height: 6px;
  }
  .features-wrapper::-webkit-scrollbar-track {
    background: var(--gray-200);
    border-radius: 10px;
  }
  .features-wrapper::-webkit-scrollbar-thumb {
    background: var(--cyan);
    border-radius: 10px;
  }

  .feature-block {
    flex: 0 0 340px;
    scroll-snap-align: center;
    display: flex;
    flex-direction: column;
    gap: 20px;
    background: var(--white);
    border: 1px solid var(--gray-200);
    border-radius: 20px;
    padding: 32px 24px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    margin-bottom: 0 !important;
  }
  .feature-block .feature-visual {
    order: 2;
    margin-top: auto;
  }
  .feature-block .feature-copy {
    order: 1;
  }
  .feature-block.reverse .feature-copy { order: 1; }
  
  .feature-block h2 {
    font-size: 20px !important;
    margin-bottom: 12px !important;
  }
  .feature-copy .tag {
    font-size: 10px !important;
    padding: 4px 10px !important;
    margin-bottom: 12px !important;
  }
  .feature-check {
    font-size: 13px !important;
    align-items: flex-start !important;
  }
  .feature-check .check-icon {
    width: 16px !important;
    height: 16px !important;
    font-size: 9px !important;
    margin-top: 2px !important;
  }
  .feature-stat {
    font-size: 12px !important;
    padding: 12px 14px !important;
  }
  .feature-mock {
    padding: 20px !important;
    min-height: 250px !important;
  }
  .fm-card {
    padding: 10px 14px !important;
  }
  .fm-ai-input {
    font-size: 11px !important;
  }
  .fm-ai-prompt {
    font-size: 10.5px !important;
  }
  
  @media (max-width: 900px) {
    .feature-block { flex: 0 0 85vw; }
  }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated successfully")
else:
    print("Could not find old_css")
