import sys

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """  .features-wrapper {
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

new_css = """  .features-carousel-wrapper {
    position: relative;
    width: 100%;
  }
  .features-track-container {
    overflow: hidden;
    width: 100%;
    padding: 10px 0;
  }
  .features-track {
    display: flex;
    transition: transform 0.5s ease;
    gap: 32px;
  }
  .feature-block {
    flex: 0 0 calc(50% - 16px);
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
    .feature-block { flex: 0 0 100%; }
  }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("WARNING: old_css not found")

old_wrapper_start = '<div class="features-wrapper">'
new_wrapper_start = """<div class="features-carousel-wrapper">
      <div class="features-track-container">
        <div class="features-track" id="features-track">"""

if old_wrapper_start in content:
    content = content.replace(old_wrapper_start, new_wrapper_start)
else:
    print("WARNING: old_wrapper_start not found")

old_wrapper_end = '    </div> <!-- End features-wrapper -->'
new_wrapper_end = """        </div>
      </div>
      <!-- Nav Bar -->
      <div class="carousel-nav" style="margin-top: 40px;">
        <button class="nav-btn" id="prev-features" disabled>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg>
        </button>
        <button class="nav-btn" id="next-features">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg>
        </button>
        <div class="carousel-dots" id="features-dots">
          <!-- JS will populate -->
        </div>
      </div>
    </div> <!-- End features-carousel-wrapper -->"""

if old_wrapper_end in content:
    content = content.replace(old_wrapper_end, new_wrapper_end)
else:
    print("WARNING: old_wrapper_end not found")

script_to_add = """<script>
document.addEventListener('DOMContentLoaded', function() {
  const track = document.getElementById('features-track');
  const prevBtn = document.getElementById('prev-features');
  const nextBtn = document.getElementById('next-features');
  const dotsContainer = document.getElementById('features-dots');
  if(!track) return;
  const cards = Array.from(track.children);
  
  let currentIndex = 0;
  const totalCards = cards.length;
  
  // Create dots
  cards.forEach((_, i) => {
    const dot = document.createElement('div');
    dot.className = 'dot' + (i === 0 ? ' active' : '');
    dot.addEventListener('click', () => jumpToIndex(i));
    dotsContainer.appendChild(dot);
  });
  
  const dots = Array.from(dotsContainer.children);

  function updateCarousel() {
    const cardWidth = cards[0].offsetWidth;
    const gap = 32;
    const offset = currentIndex * (cardWidth + gap);
    track.style.transform = `translateX(-${offset}px)`;
    
    prevBtn.disabled = currentIndex === 0;
    
    const visibleCount = window.innerWidth >= 900 ? 2 : 1;
    nextBtn.disabled = currentIndex >= totalCards - Math.floor(visibleCount);
    
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentIndex);
    });
  }

  function jumpToIndex(index) {
    currentIndex = index;
    updateCarousel();
  }

  nextBtn.addEventListener('click', () => {
    const visibleCount = window.innerWidth >= 900 ? 2 : 1;
    if (currentIndex < totalCards - Math.floor(visibleCount)) {
      currentIndex++;
      updateCarousel();
    }
  });

  prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      updateCarousel();
    }
  });

  window.addEventListener('resize', updateCarousel);
  setTimeout(updateCarousel, 100);
});
</script>"""

if "</section>\n\n\n<!-- ── CUSTOMER OUTCOMES" in content:
    content = content.replace("</section>\n\n\n<!-- ── CUSTOMER OUTCOMES", "</section>\n\n" + script_to_add + "\n\n<!-- ── CUSTOMER OUTCOMES")
else:
    print("WARNING: section end not found for script insertion")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
