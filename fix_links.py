import os
import glob

footer_old = """      <div class="footer-col">
        <h4>About Solar Vex</h4>
        <ul>
          <li><a href="#">Media</a></li>
          <li><a href="#">Contact Us</a></li>
          <li><a href="#">Join Us</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <ul>
          <li><a href="#">PV System</a></li>
          <li><a href="#">Energy Storage</a></li>
          <li><a href="#">EV Charger</a></li>
          <li><a href="#">Smart Energy Management</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Products</h4>
        <ul>
          <li><a href="#">PV Inverter</a></li>
          <li><a href="#">Energy Storage</a></li>
          <li><a href="#">EV Charger</a></li>
          <li><a href="#">Smart Energy Management</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Support</h4>
        <ul>
          <li><a href="#">Training</a></li>
          <li><a href="#">Warranty</a></li>
          <li><a href="#">FAQ</a></li>
          <li><a href="#">Download</a></li>
          <li><a href="#">Cases</a></li>
          <li><a href="#">Community</a></li>
        </ul>
      </div>"""

footer_new = """      <div class="footer-col">
        <h4>About Solar Vex</h4>
        <ul>
          <li><a href="cases.html">Media</a></li>
          <li><a href="support.html">Contact Us</a></li>
          <li><a href="about.html">Join Us</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <ul>
          <li><a href="solutions.html">PV System</a></li>
          <li><a href="solutions.html">Energy Storage</a></li>
          <li><a href="solutions.html">EV Charger</a></li>
          <li><a href="solutions.html">Smart Energy Management</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Products</h4>
        <ul>
          <li><a href="products.html">PV Inverter</a></li>
          <li><a href="products.html">Energy Storage</a></li>
          <li><a href="products.html">EV Charger</a></li>
          <li><a href="products.html">Smart Energy Management</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Support</h4>
        <ul>
          <li><a href="support.html">Training</a></li>
          <li><a href="support.html">Warranty</a></li>
          <li><a href="support.html">FAQ</a></li>
          <li><a href="support.html">Download</a></li>
          <li><a href="cases.html">Cases</a></li>
          <li><a href="community.html">Community</a></li>
        </ul>
      </div>"""

social_old = """        <div class="social-links">
          <a href="#"><i class="fab fa-facebook-f"></i></a>
          <a href="#"><i class="fab fa-youtube"></i></a>
          <a href="#"><i class="fab fa-linkedin-in"></i></a>
          <a href="#"><i class="fab fa-instagram"></i></a>
          <a href="#"><i class="fab fa-x-twitter"></i></a>
        </div>"""

social_new = """        <div class="social-links">
          <a href="https://facebook.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-facebook-f"></i></a>
          <a href="https://youtube.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-youtube"></i></a>
          <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-linkedin-in"></i></a>
          <a href="https://instagram.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-instagram"></i></a>
          <a href="https://twitter.com" target="_blank" rel="noopener noreferrer"><i class="fab fa-x-twitter"></i></a>
        </div>"""

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Logo link
    content = content.replace('<a href="#" class="logo">', '<a href="index.html" class="logo">')
    # Media more link
    content = content.replace('<a href="#" class="media-more">', '<a href="cases.html" class="media-more">')
    # Product items details link
    content = content.replace('<a href="#" class="media-more"', '<a href="products.html" class="media-more"')
    # Footer replacements
    content = content.replace(footer_old, footer_new)
    # Social links
    content = content.replace(social_old, social_new)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed dead links in {len(html_files)} HTML files.")
