opcion = input("¿Qué eliges? (MACHETE/MAPA/BOTELLA): ").strip().upper()

if opcion == "MACHETE":
    print("\nCoges el machete. Es afilado y útil para defenderse. De repente, escuchas un ruido en los arbustos. ¿Quieres INVESTIGAR o IGNORAR el ruido?")
    
    opcion = input("¿Qué haces? (INVESTIGAR/IGNORAR): ").strip().upper()
    
    if opcion == "INVESTIGAR":
        print("\nTe acercas con cuidado y descubres un tigre. Afortunadamente, tienes el machete y logras ahuyentarlo. Sigues adelante y encuentras un camino seguro. ¡Has sobrevivido! Fin del juego.")
    elif opcion == "IGNORAR":
        print("\nDecides ignorar el ruido y sigues caminando. Sin darte cuenta, el tigre te ataca por detrás. Fin del juego.")
    else:
        print("\nNo elegiste una opción válida. Te quedas paralizado y el tigre te ataca. Fin del juego.")

elif opcion == "MAPA":
    print("\nCoges el mapa. Parece mostrar una ruta hacia una montaña. ¿Quieres SEGUIR el mapa o EXPLORAR la playa?")
    
    opcion = input("¿Qué haces? (SEGUIR/EXPLORAR): ").strip().upper()

    if opcion == "SEGUIR":
        print("\nSigues el mapa y llegas a la montaña. Encuentras una cueva con provisiones. ¡Has encontrado ayuda! Fin del juego.")
    elif opcion == "EXPLORAR":
        print("\nDecides explorar la playa, pero te pierdes y no encuentras nada útil. Fin del juego.")
    else:
        print("\nNo elegiste una opción válida. Te quedas paralizado y no avanzas. Fin del juego.")

elif opcion == "BOTELLA":
    print("\nCoges la botella y la abres. Dentro hay un mensaje que dice: 'Busca el faro'. ¿Quieres BUSCAR el faro o IGNORAR el mensaje?")
    
    opcion = input("¿Qué haces? (BUSCAR/IGNORAR): ").strip().upper()
    
    if opcion == "BUSCAR":
        print("\nDecides buscar el faro. Después de caminar un rato, lo encuentras. Enciendes la luz y una nave nodriza te rescata. ¡Has sido salvado! Fin del juego.")
    elif opcion == "IGNORAR":
        print("\nIgnoras el mensaje y te quedas en la playa. Nadie viene a rescatarte. Fin del juego.")
    else:
        print("\nNo elegiste una opción válida. Te quedas paralizado y no avanzas. Fin del juego.")

else:
    print("\nNo elegiste una opción válida. Te quedas en la playa sin hacer nada. Fin del juego.")