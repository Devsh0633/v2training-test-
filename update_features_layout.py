import sys

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
old_css = """  /* ── FEATURES ──────────────────────────────────── */
  #features {
    padding: 100px 24px;
    background: var(--white);
  }
  .features-intro { text-align: center; margin-bottom: 72px; }
  .feature-block {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 56px;
    align-items: center;
    margin-bottom: 80px;
  }
  .feature-block:last-child { margin-bottom: 0; }
  .feature-block.reverse .feature-copy { order: -1; }"""

new_css = """  /* ── FEATURES ──────────────────────────────────── */
  #features {
    padding: 80px 24px;
    background: var(--gray-100);
  }
  .features-intro { text-align: center; margin-bottom: 64px; }
  .features-wrapper {
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

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Could not find old_css")

# 2. Add <div class="features-wrapper"> after features-intro
intro_end = """      <p class="section-sub" style="margin:12px auto 0;">Most LMS platforms show course completions. Most scheduling tools show calendar slots. SimpliTrain shows you the full picture — programs, clients, trainers, and performance — in one connected system.</p>
    </div>

    <!-- Feature 1: Multi-client portals -->"""

intro_end_new = """      <p class="section-sub" style="margin:12px auto 0;">Most LMS platforms show course completions. Most scheduling tools show calendar slots. SimpliTrain shows you the full picture — programs, clients, trainers, and performance — in one connected system.</p>
    </div>

    <div class="features-wrapper">
    <!-- Feature 1: Multi-client portals -->"""

if intro_end in content:
    content = content.replace(intro_end, intro_end_new)
else:
    print("Could not find intro_end")


# 3. Add closing </div> for features-wrapper before the end of #features section
features_end = """              <div class="fm-ai-mod"><div class="fm-ai-mod-num">3</div>Patient Rights &amp; Disclosures</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

features_end_new = """              <div class="fm-ai-mod"><div class="fm-ai-mod-num">3</div>Patient Rights &amp; Disclosures</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div> <!-- End features-wrapper -->
  </div>
</section>"""

if features_end in content:
    content = content.replace(features_end, features_end_new)
else:
    print("Could not find features_end")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
