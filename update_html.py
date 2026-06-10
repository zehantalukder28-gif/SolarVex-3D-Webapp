import os

nav_original = '''      <div class="nav-icons">
        <a href="#"><i class="fas fa-search"></i></a>
        <a href="#"><i class="fas fa-globe"></i></a>
        <a href="#"><i class="fas fa-user"></i></a>
      </div>'''

nav_new = '''      <div class="nav-icons">
        <button id="themeToggle" aria-label="Toggle Dark Mode"><i class="fas fa-moon"></i></button>
        <button onclick="openModal('searchModal')"><i class="fas fa-search"></i></button>
        <button onclick="openModal('langModal')"><i class="fas fa-globe"></i></button>
        <button onclick="openModal('userModal')"><i class="fas fa-user"></i></button>
      </div>'''

script_original = '''  <script>
    // Scroll animations
    const fadeElements = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });

    fadeElements.forEach(el => observer.observe(el));

    // Scroll to top button
    const scrollTopBtn = document.getElementById('scrollTop');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    });

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Counter animation
    const counters = document.querySelectorAll('.stat-num');
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = parseInt(entry.target.dataset.target);
          animateCounter(entry.target, target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));

    function animateCounter(el, target) {
      let current = 0;
      const increment = target / 60;
      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          el.textContent = target + (target === 6 ? 'M+' : '+');
          clearInterval(timer);
        } else {
          el.textContent = Math.floor(current) + (target === 6 ? 'M+' : '+');
        }
      }, 30);
    }

    // Mobile menu
    function toggleMenu() {
      const nav = document.querySelector('.nav');
      nav.style.display = nav.style.display === 'flex' ? 'none' : 'flex';
      nav.style.position = 'absolute';
      nav.style.top = '70px';
      nav.style.left = '0';
      nav.style.right = '0';
      nav.style.background = 'white';
      nav.style.flexDirection = 'column';
      nav.style.padding = '20px';
      nav.style.boxShadow = '0 10px 30px rgba(0,0,0,0.1)';
    }

    // Subscribe popup
    function showSubscribe() {
      alert('Thank you for your interest! Newsletter subscription coming soon.');
    }

    // Smooth scroll for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  </script>'''

script_new = '''  <!-- Modals -->
  <div class="modal" id="searchModal">
    <div class="modal-content glass-panel">
      <button class="modal-close" onclick="closeModal('searchModal')"><i class="fas fa-times"></i></button>
      <h3 style="margin-bottom: 16px; font-size: 20px;">Search Solar Vex</h3>
      <div class="product-search">
        <i class="fas fa-search"></i>
        <input type="text" placeholder="Type to search products, articles...">
      </div>
    </div>
  </div>

  <div class="modal" id="langModal">
    <div class="modal-content glass-panel">
      <button class="modal-close" onclick="closeModal('langModal')"><i class="fas fa-times"></i></button>
      <h3 style="margin-bottom: 16px; font-size: 20px;">Select Region</h3>
      <p style="color: var(--text-gray);">Global (English)</p>
      <p style="color: var(--text-gray); margin-top: 8px;">Europe (English/German/Spanish)</p>
      <p style="color: var(--text-gray); margin-top: 8px;">Asia Pacific (English/Chinese)</p>
    </div>
  </div>

  <div class="modal" id="userModal">
    <div class="modal-content glass-panel">
      <button class="modal-close" onclick="closeModal('userModal')"><i class="fas fa-times"></i></button>
      <h3 style="margin-bottom: 16px; font-size: 20px;">Partner Login</h3>
      <div class="product-search" style="margin-bottom: 16px;">
        <i class="fas fa-envelope"></i>
        <input type="email" placeholder="Email Address">
      </div>
      <div class="product-search" style="margin-bottom: 24px;">
        <i class="fas fa-lock"></i>
        <input type="password" placeholder="Password">
      </div>
      <button class="newsletter-btn" style="width: 100%; justify-content: center;" onclick="closeModal('userModal')">Login</button>
    </div>
  </div>

  <script>
    // Dark Mode Toggle
    const themeToggle = document.getElementById('themeToggle');
    const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
    const currentTheme = localStorage.getItem("theme");

    if (currentTheme == "dark") {
      document.body.setAttribute("data-theme", "dark");
      if (themeToggle) themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    } else if (currentTheme == "light") {
      document.body.removeAttribute("data-theme");
      if (themeToggle) themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
    }

    if (themeToggle) {
      themeToggle.addEventListener("click", function() {
        if (document.body.getAttribute("data-theme") == "dark") {
          document.body.removeAttribute("data-theme");
          localStorage.setItem("theme", "light");
          themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
        } else {
          document.body.setAttribute("data-theme", "dark");
          localStorage.setItem("theme", "dark");
          themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        }
      });
    }

    // Floating Header
    let lastScroll = 0;
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
      const currentScroll = window.pageYOffset;
      if (currentScroll <= 0) {
        header.classList.remove('floating-hidden');
        return;
      }
      if (currentScroll > lastScroll && currentScroll > 80) {
        header.classList.add('floating-hidden');
      } else if (currentScroll < lastScroll) {
        header.classList.remove('floating-hidden');
      }
      lastScroll = currentScroll;
    });

    // Modals
    function openModal(id) {
      document.getElementById(id).classList.add('active');
    }
    function closeModal(id) {
      document.getElementById(id).classList.remove('active');
    }

    // Scroll animations
    const fadeElements = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });

    fadeElements.forEach(el => observer.observe(el));

    // Scroll to top button
    const scrollTopBtn = document.getElementById('scrollTop');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    });

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Counter animation
    const counters = document.querySelectorAll('.stat-num');
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = parseInt(entry.target.dataset.target);
          animateCounter(entry.target, target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));

    function animateCounter(el, target) {
      let current = 0;
      const increment = target / 60;
      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          el.textContent = target + (target === 6 ? 'M+' : '+');
          clearInterval(timer);
        } else {
          el.textContent = Math.floor(current) + (target === 6 ? 'M+' : '+');
        }
      }, 30);
    }

    // Mobile menu
    function toggleMenu() {
      const nav = document.querySelector('.nav');
      if (nav.style.display === 'flex') {
        nav.style.display = 'none';
      } else {
        nav.style.display = 'flex';
        nav.style.position = 'absolute';
        nav.style.top = '80px';
        nav.style.left = '0';
        nav.style.right = '0';
        nav.style.background = 'var(--glass-bg)';
        nav.style.backdropFilter = 'blur(12px)';
        nav.style.flexDirection = 'column';
        nav.style.padding = '20px';
        nav.style.boxShadow = 'var(--shadow-hover)';
        nav.style.borderBottom = '1px solid var(--glass-border)';
      }
    }

    // Smooth scroll for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const targetAttr = this.getAttribute('href');
        if(targetAttr === '#') return;
        const target = document.querySelector(targetAttr);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  </script>'''

files = ['about.html', 'cases.html', 'community.html', 'solutions.html', 'support.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace nav-icons
    content = content.replace(nav_original, nav_new)
    
    # Replace scripts and add modals
    content = content.replace(script_original, script_new)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated files successfully')
