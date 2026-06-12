import { defineConfig } from 'vite';
import fs from 'fs';
import path from 'path';

export default defineConfig({
  server: {
    port: 3000,
  },
  plugins: [
    {
      name: 'html-fallback',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          // If the URL has no extension and is not root, check if .html exists
          if (req.url !== '/' && !path.extname(req.url)) {
            const htmlPath = path.join(__dirname, req.url + '.html');
            if (fs.existsSync(htmlPath)) {
              req.url = req.url + '.html';
            } else {
              // Redirect to index.html to prevent 404
              req.url = '/index.html';
            }
          }
          next();
        });
      }
    }
  ]
});
