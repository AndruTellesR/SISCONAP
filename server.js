const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 3000;

// Servir archivos estáticos desde la carpeta dist
app.use(express.static(path.join(__dirname, 'dist')));

// Todas las rutas redirigen a index.html para SPA
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

app.listen(port, () => {
  console.log(`Servidor iniciado en el puerto ${port}`);
});
