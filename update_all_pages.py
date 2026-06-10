import os

pages = {
    "about.html": {
        "title": "About Solar Vex",
        "content": """
  <section style="margin-top: 140px; min-height: 60vh; padding: 0 clamp(32px, 5vw, 80px);">
    <h2 style="font-size: clamp(40px, 6vw, 80px); font-weight: 900; text-transform: uppercase;">Corporate Overview</h2>
    <p style="font-size: 20px; color: var(--grey); max-width: 800px; line-height: 1.6; margin-top: 24px;">Solar Vex is a global leader in high-performance decentralized energy infrastructure. We engineer sovereign power systems that shield residential estates and commercial enterprises from utility instabilities through advanced algorithmic tracking and scalable storage topologies.</p>
  </section>
"""
    },
    "solutions.html": {
        "title": "Solutions — Solar Vex",
        "content": """
  <section style="margin-top: 140px; padding: 0 clamp(32px, 5vw, 80px);">
    <h2 style="font-size: clamp(40px, 6vw, 80px); font-weight: 900; text-transform: uppercase;">Infrastructure Solutions</h2>
    <div class="page-content-grid">
      <div class="content-block">
        <h3>Residential Energy Integration</h3>
        <p>Engineered to transition private estates into sovereign power units. Features intelligent multi-string rooftop tracking layouts, aesthetic zero-impact architectural panel pairing, and autonomous localized grid fallbacks that shield residential properties from public utility instabilities.</p>
        <img src="images/pv-system.jpg" alt="Residential Energy Integration">
      </div>
      <div class="content-block">
        <h3>Commercial Scale Microgrids</h3>
        <p>High-yielding decentralized infrastructure built for maximum continuous output. Deploys optimized megawatt-level tracking systems, localized heavy-industry transformation enclosures, and algorithmic peak-shaving frameworks designed to cut operational corporate energy expenses by up to 40%.</p>
        <img src="images/solar-farm.jpg" alt="Commercial Scale Microgrids">
      </div>
    </div>
  </section>
"""
    },
    "products.html": {
        "title": "Products — Solar Vex",
        "content": """
  <section style="margin-top: 140px; padding: 0 clamp(32px, 5vw, 80px);">
    <h2 style="font-size: clamp(40px, 6vw, 80px); font-weight: 900; text-transform: uppercase;">Hardware Suite</h2>
    <div class="page-content-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
      <div class="content-block">
        <img src="images/pv_modules.png" alt="Monocrystalline PV Modules" style="margin-top: 0; margin-bottom: 24px; aspect-ratio: 4/3;">
        <h3>Monocrystalline PV Modules</h3>
        <p>Ultra-dense solar cell configurations utilizing advanced multi-busbar technology to achieve an industry-leading 23.4% module efficiency. Built with premium anti-reflective tempered glass to sustain optimal energy conversion across low-light environments.</p>
      </div>
      <div class="content-block">
        <img src="images/smart_inverter.png" alt="Smart Wave Inverters" style="margin-top: 0; margin-bottom: 24px; aspect-ratio: 4/3;">
        <h3>Smart Wave Inverters</h3>
        <p>Next-generation digital power conversion systems featuring real-time artificial intelligence diagnostics. Continuously monitors multi-channel phase vectors, handles rapid thermal dissipation, and balances grid interaction with sub-millisecond precision.</p>
      </div>
      <div class="content-block">
        <img src="images/storage_cells.png" alt="High-Capacity Storage Cells" style="margin-top: 0; margin-bottom: 24px; aspect-ratio: 4/3;">
        <h3>High-Capacity Storage Cells</h3>
        <p>Scalable lithium-iron-phosphate (LiFePO4) battery architectures offering an extensive 6,000-cycle lifespan. Features active liquid cooling management, modular expansion capabilities, and seamless integration with existing hybrid inverter topologies.</p>
      </div>
    </div>
  </section>
"""
    },
    "cases.html": {
        "title": "Cases — Solar Vex",
        "content": """
  <section style="margin-top: 140px; padding: 0 clamp(32px, 5vw, 80px);">
    <h2 style="font-size: clamp(40px, 6vw, 80px); font-weight: 900; text-transform: uppercase;">Global Deployment</h2>
    <div class="page-content-grid">
      <div class="content-block">
        <h3>The Coastal Villa Project</h3>
        <p>A flagship integration of our premium residential suite. Situated in Malibu, CA, this 15kW installation leverages highly salt-resistant Monocrystalline arrays alongside a dual 20kWh storage bank. The project achieved a 98% grid-independence rating within its first operational quarter, entirely offsetting the estate's heavy HVAC loads.</p>
        <img src="images/pv-system.jpg" alt="Coastal Villa Project">
      </div>
      <div class="content-block">
        <h3>The Urban Grid Modernization</h3>
        <p>A 2.5MW commercial deployment designed to stabilize a heavily strained industrial sector. This project bypassed traditional utility upgrades by deploying localized heavy-industry transformation enclosures and algorithmic peak-shaving frameworks, resolving capacity constraints and reducing enterprise overhead by 34%.</p>
        <img src="images/solar-farm.jpg" alt="Urban Grid Modernization">
      </div>
    </div>
  </section>
"""
    },
    "support.html": {
        "title": "Support — Solar Vex",
        "content": """
  <section style="margin-top: 140px; padding: 0 clamp(32px, 5vw, 80px);">
    <h2 style="font-size: clamp(40px, 6vw, 80px); font-weight: 900; text-transform: uppercase;">Engineering Support</h2>
    <div class="page-content-grid">
      <div class="content-block">
        <h3>Technical Documentation Hub</h3>
        <p>Access extensive schematics, firmware update logs, API integration endpoints for Smart Inverters, and certified installation compliance documents. Designed specifically for tier-1 EPC contractors and integrators.</p>
      </div>
      <div class="content-block">
        <h3>Real-Time System Remote Diagnostics</h3>
        <p>Secure cloud portal allowing authorized technicians to monitor multi-channel phase vectors and execute over-the-air (OTA) thermal optimizations on fielded inverter arrays.</p>
      </div>
      <div class="content-block">
        <h3>Direct Engineering Helpdesk Ticket Routing</h3>
        <p>Priority escalation channels connecting enterprise clients directly to our core firmware and hardware engineering teams for rapid resolution of complex grid anomalies.</p>
      </div>
    </div>
  </section>
"""
    },
    "community.html": {
        "title": "Community — Solar Vex",
        "content": """
  <section style="margin-top: 140px; padding: 0 clamp(32px, 5vw, 80px);">
    <h2 style="font-size: clamp(40px, 6vw, 80px); font-weight: 900; text-transform: uppercase;">The Network</h2>
    <div class="page-content-grid">
      <div class="content-block">
        <h3>Global Sustainability Research Initiatives</h3>
        <p>Join our open-source data coalition. We share anonymized telemetry from millions of operating nodes to assist academic institutions in modeling next-generation power grid resilience strategies.</p>
      </div>
      <div class="content-block">
        <h3>Solar Vex Integrator Forums</h3>
        <p>A vetted community space for certified installers to share edge-case deployment strategies, troubleshoot rare fault codes, and beta-test upcoming management software.</p>
      </div>
    </div>
  </section>
"""
    }
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="Empowering homes and businesses with cutting-edge solar technology.">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="stylesheet" href="style.css">
  
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>
</head>
<body>
  <div class="noise-overlay"></div>
  <div class="page-transition-curtain" id="pageTransitionCurtain"></div>

  <!-- DUAL-CURSOR BLOB -->
  <div class="cursor-blob" id="cursorBlob"></div>

  <!-- Header -->
  <header class="header" id="header" style="background: rgba(245, 244, 240, 0.85); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-bottom: 1px solid rgba(0, 0, 0, 0.05);">
    <div class="header-inner">
      <a href="index.html" class="logo hover-orange">
        <svg viewBox="0 0 100 100">
          <path d="M50 15 A35 35 0 0 1 85 50 A35 35 0 0 1 50 85 A35 35 0 0 1 15 50 A35 35 0 0 1 50 15 Z" fill="none" stroke="currentColor" stroke-width="4"/>
          <line x1="25" y1="50" x2="75" y2="50" stroke="currentColor" stroke-width="3"/>
          <line x1="30" y1="35" x2="70" y2="35" stroke="currentColor" stroke-width="2"/>
          <line x1="30" y1="65" x2="70" y2="65" stroke="currentColor" stroke-width="2"/>
          <line x1="50" y1="25" x2="50" y2="75" stroke="currentColor" stroke-width="3"/>
          <line x1="35" y1="30" x2="35" y2="70" stroke="currentColor" stroke-width="2"/>
          <line x1="65" y1="30" x2="65" y2="70" stroke="currentColor" stroke-width="2"/>
          <path d="M50 5 A45 45 0 0 1 95 50" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="8 4"/>
          <path d="M50 95 A45 45 0 0 1 5 50" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="8 4"/>
        </svg>
        Solar Vex
      </a>
      <span class="header-tagline">Premium Infrastructure</span>
      <button class="menu-toggle hover-cyan magnetic" id="menuOpen">MENU</button>
    </div>
  </header>

  <!-- FULLSCREEN MENU OVERLAY -->
  <nav class="fullscreen-menu" id="fullscreenMenu">
    <button class="menu-close hover-orange" id="menuClose">close</button>
    <div class="menu-grid">
      <!-- Primary Nav -->
      <div class="menu-nav">
        <a href="index.html" class="menu-item hover-cyan">Home</a>
        <a href="solutions.html" class="menu-item hover-cyan">Solutions</a>
        <a href="products.html" class="menu-item hover-cyan">Products</a>
        <a href="cases.html" class="menu-item hover-cyan">Cases</a>
        <a href="support.html" class="menu-item hover-cyan">Support</a>
        <a href="about.html" class="menu-item hover-cyan">About Us</a>
      </div>
      <!-- Deep Content Sub-nav -->
      <div class="menu-details">
        <div class="menu-block">
          <h4>Solutions</h4>
          <a href="solutions.html" class="sub-link hover-orange">
            <div class="sub-icon"><img src="images/pv-system.jpg" alt="Residential"></div>
            <span class="sub-text">Residential Energy<br>Integration</span>
          </a>
          <a href="solutions.html" class="sub-link hover-orange">
            <div class="sub-icon"><img src="images/solar-farm.jpg" alt="Commercial"></div>
            <span class="sub-text">Commercial Scale<br>Microgrids</span>
          </a>
        </div>
        <div class="menu-block">
          <h4>Support & Community</h4>
          <a href="support.html" class="sub-link hover-cyan">
            <div class="sub-icon"><img src="images/smart-energy.jpg" alt="Diagnostic"></div>
            <span class="sub-text">Real-Time System<br>Diagnostics</span>
          </a>
          <a href="community.html" class="sub-link hover-cyan">
            <div class="sub-icon"><img src="images/hero-bg.jpg" alt="Forum"></div>
            <span class="sub-text">Global Sustainability<br>Grants</span>
          </a>
        </div>
      </div>
    </div>
  </nav>

  {content}

  <!-- FOOTER -->
  <footer class="footer" style="margin-top: 80px;">
    <div class="footer-top">
      <div>
        <div class="footer-brand">
          <svg viewBox="0 0 100 100">
            <path d="M50 15 A35 35 0 0 1 85 50 A35 35 0 0 1 50 85 A35 35 0 0 1 15 50 A35 35 0 0 1 50 15 Z" fill="none" stroke="currentColor" stroke-width="4"/>
            <line x1="25" y1="50" x2="75" y2="50" stroke="currentColor" stroke-width="3"/>
            <line x1="30" y1="35" x2="70" y2="35" stroke="currentColor" stroke-width="2"/>
            <line x1="30" y1="65" x2="70" y2="65" stroke="currentColor" stroke-width="2"/>
            <line x1="50" y1="25" x2="50" y2="75" stroke="currentColor" stroke-width="3"/>
            <line x1="35" y1="30" x2="35" y2="70" stroke="currentColor" stroke-width="2"/>
            <line x1="65" y1="30" x2="65" y2="70" stroke="currentColor" stroke-width="2"/>
            <path d="M50 5 A45 45 0 0 1 95 50" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="8 4"/>
            <path d="M50 95 A45 45 0 0 1 5 50" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="8 4"/>
          </svg>
          Solar Vex
        </div>
        <p class="footer-tagline">Empowering homes and businesses with cutting-edge solar technology.</p>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="about.html" class="hover-cyan">About Us</a>
        <a href="cases.html" class="hover-cyan">Media</a>
        <a href="support.html" class="hover-cyan">Contact Us</a>
        <a href="community.html" class="hover-cyan">Community</a>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <a href="solutions.html" class="hover-orange">PV System</a>
        <a href="solutions.html" class="hover-orange">Energy Storage</a>
        <a href="solutions.html" class="hover-orange">EV Charger</a>
        <a href="solutions.html" class="hover-orange">Smart Energy</a>
      </div>
      <div class="footer-col">
        <h4>Products</h4>
        <a href="products.html" class="hover-cyan">PV Inverter</a>
        <a href="products.html" class="hover-cyan">Energy Storage</a>
        <a href="products.html" class="hover-cyan">EV Charger</a>
        <a href="products.html" class="hover-cyan">Accessories</a>
      </div>
      <div class="footer-col">
        <h4>Support</h4>
        <a href="support.html" class="hover-orange">Training</a>
        <a href="support.html" class="hover-orange">Warranty</a>
        <a href="support.html" class="hover-orange">FAQ</a>
        <a href="support.html" class="hover-orange">Downloads</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span class="footer-copy">© Solar Vex New Energy — All Rights Reserved</span>
      <div class="footer-social">
        <a href="https://facebook.com" target="_blank" class="hover-cyan"><i class="fab fa-facebook-f"></i></a>
        <a href="https://youtube.com" target="_blank" class="hover-orange"><i class="fab fa-youtube"></i></a>
        <a href="https://linkedin.com" target="_blank" class="hover-cyan"><i class="fab fa-linkedin-in"></i></a>
        <a href="https://twitter.com" target="_blank" class="hover-cyan"><i class="fab fa-x-twitter"></i></a>
      </div>
    </div>
    <div class="footer-logo-large">SOLAR VEX</div>
  </footer>

  <script>
    /* DUAL-CURSOR BLOB LOGIC */
    const cursorBlob = document.getElementById('cursorBlob');
    const xTo = gsap.quickTo(cursorBlob, "x", {duration: 0.3, ease: "power3"});
    const yTo = gsap.quickTo(cursorBlob, "y", {duration: 0.3, ease: "power3"});
    
    document.addEventListener("mousemove", e => {
      xTo(e.clientX);
      yTo(e.clientY);
    });

    document.querySelectorAll('.hover-cyan').forEach(el => {
      el.addEventListener('mouseenter', () => cursorBlob.classList.add('focus-cyan'));
      el.addEventListener('mouseleave', () => cursorBlob.classList.remove('focus-cyan'));
    });
    document.querySelectorAll('.hover-orange').forEach(el => {
      el.addEventListener('mouseenter', () => cursorBlob.classList.add('focus-orange'));
      el.addEventListener('mouseleave', () => cursorBlob.classList.remove('focus-orange'));
    });

    /* MENU LOGIC */
    const menuOpen = document.getElementById('menuOpen');
    const menuClose = document.getElementById('menuClose');
    const fullscreenMenu = document.getElementById('fullscreenMenu');
    const menuItems = document.querySelectorAll('.menu-item');

    menuOpen.addEventListener('click', () => {
      fullscreenMenu.classList.add('open');
      gsap.fromTo(menuItems, 
        { x: -50, opacity: 0 },
        { x: 0, opacity: 1, duration: 0.6, stagger: 0.1, ease: 'power3.out', delay: 0.2 }
      );
    });
    menuClose.addEventListener('click', () => {
      fullscreenMenu.classList.remove('open');
    });

    /* ========================================
       LENIS SMOOTH SCROLLING
       ======================================== */
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      direction: 'vertical',
      gestureDirection: 'vertical',
      smooth: true,
      mouseMultiplier: 1,
      smoothTouch: false,
      touchMultiplier: 2,
      infinite: false,
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // Sync Lenis with GSAP
    gsap.ticker.add((time)=>{ lenis.raf(time * 1000) });
    gsap.ticker.lagSmoothing(0);

    /* ========================================
       MAGNETIC UI BUTTONS
       ======================================== */
    const magnets = document.querySelectorAll('.magnetic');
    magnets.forEach(magnet => {
      magnet.addEventListener('mousemove', function(e) {
        const position = magnet.getBoundingClientRect();
        const x = e.clientX - position.left - position.width / 2;
        const y = e.clientY - position.top - position.height / 2;
        
        gsap.to(magnet, { x: x * 0.3, y: y * 0.3, duration: 0.5, ease: 'power2.out' });
      });
      magnet.addEventListener('mouseleave', function() {
        gsap.to(magnet, { x: 0, y: 0, duration: 0.8, ease: 'elastic.out(1, 0.3)' });
      });
    });

    /* ========================================
       GSAP PAGE TRANSITIONS (CURTAIN EFFECT)
       ======================================== */
    const transitionCurtain = document.getElementById('pageTransitionCurtain');
    
    // Animate curtain up on page load (inbound)
    gsap.to(transitionCurtain, { y: '-100%', duration: 1.2, ease: 'power4.inOut', onComplete: () => {
      gsap.set(transitionCurtain, { y: '100%' }); // Reset position for outbound
    }});

    // Intercept internal links for outbound transition
    document.querySelectorAll('a').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const target = this.getAttribute('href');
        if(target && target.endsWith('.html') && !this.hasAttribute('target')) {
          e.preventDefault();
          gsap.to(transitionCurtain, { y: '0%', duration: 0.8, ease: 'power3.inOut', onComplete: () => {
            window.location.href = target;
          }});
        }
      });
    });
  </script>
</body>
</html>
"""

for filename, data in pages.items():
    html = template.replace("{title}", data["title"]).replace("{content}", data["content"])
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"OK: {filename}")
