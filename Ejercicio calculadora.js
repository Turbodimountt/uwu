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