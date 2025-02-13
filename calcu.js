// Función para mostrar el menú de opciones
function mostrarMenu() {
    console.log("1. Sumar");
    console.log("2. Restar");
    console.log("3. Multiplicar");
    console.log("4. Dividir");
    console.log("5. Salir");
}

// Función para realizar la operación seleccionada
function realizarOperacion(opcion, numero1, numero2) {
    switch (opcion) {
        case '1':
            return numero1 + numero2;
        case '2':
            return numero1 - numero2;
        case '3':
            return numero1 * numero2;
        case '4':
            if (numero2 !== 0) {
                return numero1 / numero2;
            } else {
                return "Error: No se puede dividir por cero.";
            }
        default:
            return "no funciona.";
    }
}

// Función principal de la calculadora
function calculadora() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    mostrarMenu();

    rl.question("Seleccione una opción: ", (opcion) => {
        if (opcion === '5') {
            console.log("¡Hasta luego!");
            rl.close();
            return;
        }

        rl.question("Ingrese el primer número: ", (input1) => {
            const numero1 = parseFloat(input1);

            rl.question("Ingrese el segundo número: ", (input2) => {
                const numero2 = parseFloat(input2);

                const resultado = realizarOperacion(opcion, numero1, numero2);
                console.log("Resultado: " + resultado);

                rl.close();
            });
        });
    });
}

// Ejecutar la calculadora
calculadora();