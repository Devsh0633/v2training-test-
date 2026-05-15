import sys

file_path = '/Users/apple/Desktop/v2training_copy/stl.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

changes = [
    ("For Companies That Sell Training", "For Training Businesses Ready to Scale"),
    ("Multi-client portals, built-in scheduler, and flat-rate pricing. Scalable technology for organizations that sell training for a living.", "SimpliTrain is the Training Intelligence Platform that gives you complete visibility across your programs, clients, and operations — so you can run a smarter training business."),
    ('<a href="#final-cta" class="btn-primary">Get Started</a>', '<a href="#final-cta" class="btn-primary">See It In Action</a>'),
    ("<span>No per-learner fees</span>\n        <span>Live in 2 weeks</span>", "<span>Flat-rate pricing · No per-learner fees · Live in 2 weeks</span>"),
    ("<strong>Less admin time per client</strong>\n        vs. non-specialized LMS tools", "<strong>Less time on operations.</strong>\n        More time on the business."),
    ("<strong>Cost savings in year one</strong>\n        by consolidating LMS + TMS + LXP", "<strong>Lower platform cost.</strong>\n        Higher margin on every client you serve."),
    ("<strong>Average go-live time</strong>\n        including content migration", "<strong>To go live.</strong>\n        Not three months."),
    ("Everything a Training Company Needs.", "One Platform. Complete Business Visibility."),
    ("Built specifically for organizations that sell, deliver, and scale training to paying clients.", "Most LMS platforms show course completions. Most scheduling tools show calendar slots. SimpliTrain shows you the full picture — programs, clients, trainers, and performance — in one connected system."),
    ('<span class="tag">Multi-tenant</span>', '<span class="tag">Client Management</span>'),
    ("<h2>Every client, their own branded portal.</h2>", "<h2>Every Client. One Dashboard. Zero Overhead.</h2>"),
    ('<div class="feature-check"><div class="check-icon">✓</div>Set up in under 1 hour</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Unlimited client tenants</div>\n          <div class="feature-check"><div class="check-icon">✓</div>One admin login for everything</div>', '<div class="feature-check"><div class="check-icon">✓</div>New client fully onboarded in under 1 hour</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Unlimited client accounts — no added cost</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Full visibility across every client from one login</div>'),
    ("Training companies with 10+ clients save an average of 15–20 hours per week.", "Training companies with 10+ clients recover 15–20 hours per week — time that goes back into the business, not admin."),
    ('<span class="tag">Built-in TMS</span>', '<span class="tag">Operations Intelligence</span>'),
    ("<h2>Schedule every class, instructor, and venue.</h2>", "<h2>See What Is Slowing Your Operations Before It Costs You.</h2>"),
    ('<div class="feature-check"><div class="check-icon">✓</div>Instructor availability &amp; assignment</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Waitlist &amp; attendance management</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Automated learner reminders</div>', '<div class="feature-check"><div class="check-icon">✓</div>Real-time trainer utilization and availability</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Batch performance and underfilled cohort alerts</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Spot operational bottlenecks before they affect clients</div>'),
    ('<span class="tag">Certificate Automation</span>', '<span class="tag">Learner Lifecycle</span>'),
    ("<h2>Certificates issue the moment a learner passes.</h2>", "<h2>Track Every Learner From First Inquiry to Re-Enrollment.</h2>"),
    ('<div class="feature-check"><div class="check-icon">✓</div>OSHA · HIPAA · CEU · STCW · FAA ready</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Custom branding per client</div>\n          <div class="feature-check"><div class="check-icon">✓</div>AI proctoring built in</div>', '<div class="feature-check"><div class="check-icon">✓</div>Automated renewal pathways and expiry alerts</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Full journey tracked — inquiry to payment to certification</div>\n          <div class="feature-check"><div class="check-icon">✓</div>Re-enrollment triggers built into every certificate lifecycle</div>'),
    ("Certificate issuance requires manual intervention in 80%+ of non-specialized LMS setups.", "The complete learner lifecycle — visible, automated, and connected in one system."),
    ('<span class="tag">AI Course Builder</span>', '<span class="tag">Speed to Market</span>'),
    ("<h2>Build a full course in under 2 hours.</h2>", "<h2>New Programs Live in Hours. Not Weeks.</h2>"),
    ('<div class="feature-check"><div class="check-icon">✓</div>SCORM 1.2 · xAPI (Tin Can) · cmi5</div>\n          <div class="feature-check"><div class="check-icon">✓</div>AI item banking + assessment generation</div>\n          <div class="feature-check"><div class="check-icon">✓</div>No instructional design degree required</div>', '<div class="feature-check"><div class="check-icon">✓</div>Full course built and published in under 2 hours</div>\n          <div class="feature-check"><div class="check-icon">✓</div>AI-structured modules, assessments, and learning paths</div>\n          <div class="feature-check"><div class="check-icon">✓</div>No developer or instructional designer required</div>'),
    ("Two Kinds of LMS. Only One Built for Selling Training.", "Most Platforms Manage Training. SimpliTrain Runs Your Business."),
    ("Standard training platforms were built for managing internal employees — not for running a commercial training business with dozens of clients.", "There are two kinds of platforms. Ones that tell you what happened with your content. And ones that tell you how your business is actually performing. SimpliTrain is the second kind."),
    ("<th>Generic / Off-the-shelf LMS</th>", "<th>Standard LMS / TMS Platforms</th>"),
    ("""          <tr>
            <td>Implementation</td>
            <td><span class="comp-x">✗</span>&nbsp; 6–12 weeks average</td>
            <td><span class="comp-check">✓</span>&nbsp; Live in under 2 weeks</td>
          </tr>
        </tbody>""", """          <tr>
            <td>Implementation</td>
            <td><span class="comp-x">✗</span>&nbsp; 6–12 weeks average</td>
            <td><span class="comp-check">✓</span>&nbsp; Live in under 2 weeks</td>
          </tr>
          <tr>
            <td>Business visibility</td>
            <td><span class="comp-x">✗</span>&nbsp; Completion reports only — no program-level performance data</td>
            <td><span class="comp-check">✓</span>&nbsp; Cohort fill rates, trainer performance, and program profitability in one dashboard</td>
          </tr>
          <tr>
            <td>Multi-location support</td>
            <td><span class="comp-x">✗</span>&nbsp; Built for single organisations, not branch or franchise models</td>
            <td><span class="comp-check">✓</span>&nbsp; Run branches, franchises, and global centers from one connected platform</td>
          </tr>
        </tbody>"""),
    ('<span class="impact-eyebrow">BY THE NUMBERS</span>', '<span class="impact-eyebrow">THE IMPACT</span>'),
    ("What training companies report after making the switch.", "What changes when everything is connected."),
    ("Published benchmarks from SimpliTrain customers and unified LMS + TMS platform research across commercial training organisations.", "Outcomes reported by training businesses that moved from fragmented tools to one connected platform."),
    ("Increase in operational efficiency from unifying TMS and LMS", "Improvement in operational efficiency when scheduling, delivery, and reporting work as one"),
    ("Reduction in administrative overhead per training programme", "Reduction in platform and admin overhead in year one"),
    ("Higher course completion when learners have one streamlined portal", "Higher learner retention when the full journey is tracked and managed end-to-end"),
    ("Fewer compliance incidents through automated tracking and alerts", "Fewer missed re-enrollment opportunities through automated lifecycle management"),
    ('<span class="recognition-eyebrow">RECOGNITION</span>', '<span class="recognition-eyebrow">INDEPENDENTLY VALIDATED</span>'),
    ('<h2 class="recognition-title">Independently evaluated. Consistently recognised.</h2>', '<h2 class="recognition-title">Built for Training Businesses. Recognised for Delivering.</h2>'),
    ("From global analyst reports to verified user review platforms, SimpliTrain's impact on commercial training operations is documented, rated, and recognised.", "From analyst evaluations to verified user reviews, SimpliTrain's impact is documented by operators who measured real outcomes — not just feature lists.")
]

for old, new in changes:
    if old not in content:
        print(f"WARNING: Could not find: {old!r}")
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done applying changes to v2training_copy/stl.html")
