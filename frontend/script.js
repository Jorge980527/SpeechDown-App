document.addEventListener('DOMContentLoaded', () => {
    const wordInput = document.getElementById('wordInput');
    const generateBtn = document.getElementById('generateBtn');
    const activityOutput = document.getElementById('activityOutput');
    const loadingMessage = document.getElementById('loadingMessage');

    generateBtn.addEventListener('click', async () => {
        const word = wordInput.value.trim(); // Obtiene la palabra del input 

        if (!word) { // 
            activityOutput.textContent = "Por favor, ingresa una palabra antes de generar la actividad."; // 
            activityOutput.style.backgroundColor = '#ffdddd'; // Un color de error suave
            activityOutput.style.borderColor = '#ffaaaa';
            return;
        }

        loadingMessage.classList.remove('hidden'); // Muestra el mensaje de "Generando..."
        activityOutput.textContent = ''; // Limpia el contenido anterior
        activityOutput.style.backgroundColor = '#f0faff'; // Restaura el color normal
        activityOutput.style.borderColor = '#aaddff';

        try {
            // Realiza la petición POST a tu backend de Flask 
            const response = await fetch('http://127.0.0.1:5000/generate_activity', {
                method: 'POST', // 
                headers: { // 
                    'Content-Type': 'application/json', // 
                },
                body: JSON.stringify({ word: word }), // Envía la palabra en formato JSON 
            });

            const data = await response.json(); // Parsea la respuesta JSON del backend 

            if (response.ok) { // Si la respuesta es exitosa (código 2xx) 
                activityOutput.textContent = data.activity; // Muestra la actividad generada 
            } else {
                activityOutput.textContent = `Error: ${data.error || 'No se pudo generar la actividad.'}`; // Muestra el error 
                activityOutput.style.backgroundColor = '#ffdddd';
                activityOutput.style.borderColor = '#ffaaaa';
            }
        } catch (error) {
            console.error('Error al conectar con el backend:', error);
            activityOutput.textContent = 'Error al conectar con el servidor. Asegúrate de que el backend esté corriendo (python app.py en la carpeta backend).';
            activityOutput.style.backgroundColor = '#ffdddd';
            activityOutput.style.borderColor = '#ffaaaa';
        } finally {
            loadingMessage.classList.add('hidden'); // Oculta el mensaje de "Generando..."
        }
    });
});
