// Este script de JS maneja la selección de las subcategorías según el tipo de residuo:
// Listener para estar comunicado con las selecciones del formulario.
document.addEventListener('DOMContentLoaded', function () {
    const tipoResiduo = document.getElementById('tipoResiduo');
    const subcategoriaResiduo = document.getElementById('subcategoriaResiduo');
    const form = document.getElementById('Formulario');

    // Defino los subcategorías en que se desglosa cada categoría.
    const subcategorias = {
        plastico: ['Botellas', 'Envases', 'Bolsas'],
        papel: ['Periódicos', 'Cartón', 'Papel de oficina'],
        vidrio: ['Botellas', 'Frascos', 'Cristalería'],
        metales: ['Latas', 'Cables', 'Electrodomésticos pequeños'],
        electronicos: ['Teléfonos móviles', 'Baterías', 'Componentes de computadoras']
    };

    // Actualizar subcategorías cuando se selecciona un tipo de residuo.
    tipoResiduo.addEventListener('change', function () {
        const selectedValue = this.value;
        // Se actualiza el interior del HTML
        subcategoriaResiduo.innerHTML = '<option value="" disabled selected>Seleccione una subcategoría</option>';

        // Actualiza las opciones según la categoría seleccionada, buscando "match".
        if (selectedValue) {
            subcategorias[selectedValue].forEach(subcategoria => {
                const option = document.createElement('option');
                option.value = subcategoria;
                option.textContent = subcategoria;
                subcategoriaResiduo.appendChild(option);
            });
        }
    });

    // Validación del formulario:
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Mensaje de aviso en caso de que se envíe correctamente (o no).
        if (form.checkValidity() === false) {
            e.stopPropagation();
            form.classList.add('was-validated');
        } else {
            alert('Solicitud enviada con éxito ;)');
            form.reset();
            form.classList.remove('was-validated');
        }
    });
});
