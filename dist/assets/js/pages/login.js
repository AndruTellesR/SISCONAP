// Función para manejar el inicio de sesión
function handleLogin(event) {
    event.preventDefault();
    
    const email = document.querySelector('input[type="email"]').value;
    const password = document.querySelector('input[type="password"]').value;
    const role = document.querySelector('#roleSelect').value;
    const keepSignedIn = document.querySelector('#customCheckc1').checked;

    // Validación básica
    if (!email || !password || !role) {
        showNotification('error', 'Por favor, completa todos los campos');
        return;
    }

    // Aquí normalmente harías una llamada a tu API de backend
    // Por ahora, simularemos una autenticación básica
    const mockUsers = {
        'admin@example.com': {
            password: 'admin123',
            role: 'admin'
        },
        'super@example.com': {
            password: 'super123',
            role: 'superadmin'
        },
        'user@example.com': {
            password: 'user123',
            role: 'user'
        }
    };

    // Verificar credenciales
    const user = mockUsers[email];
    if (user && user.password === password && user.role === role) {
        // Guardar información de sesión
        const sessionData = {
            email,
            role,
            keepSignedIn,
            token: 'mock-jwt-token-' + Date.now()
        };
        
        localStorage.setItem('userSession', JSON.stringify(sessionData));
        
        // Mostrar notificación de éxito
        showNotification('success', '¡Inicio de sesión exitoso!');
        
        // Redirigir según el rol
        setTimeout(() => {
            switch(role) {
                case 'superadmin':
                    window.location.href = '../dashboard/dashboard.html';
                    break;
                case 'admin':
                    window.location.href = '../dashboard/dashboard.html';
                    break;
                case 'user':
                    window.location.href = '../dashboard/dashboard.html';
                    break;
            }
        }, 1000);
    } else {
        showNotification('error', 'Credenciales o rol inválidos');
    }
}

// Función para mostrar notificaciones
function showNotification(type, message) {
    const notificationDiv = document.createElement('div');
    notificationDiv.className = `alert alert-${type === 'success' ? 'success' : 'danger'} alert-dismissible fade show`;
    notificationDiv.style.position = 'fixed';
    notificationDiv.style.top = '20px';
    notificationDiv.style.right = '20px';
    notificationDiv.style.zIndex = '1050';
    notificationDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Cerrar"></button>
    `;
    document.body.appendChild(notificationDiv);

    // Auto cerrar después de 3 segundos
    setTimeout(() => {
        notificationDiv.remove();
    }, 3000);
}

// Inicializar el formulario cuando el documento esté listo
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#loginForm');
    
    form.addEventListener('submit', handleLogin);
});
