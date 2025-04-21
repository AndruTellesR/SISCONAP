// Script para resaltar automáticamente el menú activo según la URL

document.addEventListener('DOMContentLoaded', function() {
  const path = window.location.pathname.split('/').pop();
  document.querySelectorAll('.pc-item a.pc-link').forEach(link => {
    // Si el href del link coincide exactamente con el archivo actual
    if (link.getAttribute('href') && link.getAttribute('href').includes(path)) {
      link.parentElement.classList.add('active');
    }
  });
});
