package PRACTICA1.POLIMORFISMO.EJERCICIO1;

public class Ejercicio1 {
    public static class Videojuego {
        private String nombre;
        private String plataforma;
        private int cantidadJugadores;
    
        public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
            this.nombre = nombre;
            this.plataforma = plataforma;
            this.cantidadJugadores = cantidadJugadores;
        }
    
        public void mostrar() {
            System.out.println("Videojuego: " + nombre + ", Plataforma: " + plataforma + ", Jugadores: " + cantidadJugadores);
        }
    
        public void agregarJugadores(int cantidad) {
            cantidadJugadores += cantidad;
            System.out.println("Jugadores agregados. Ahora hay " + cantidadJugadores + " jugadores.");
        }
    
        public static void main(String[] args) {
            Videojuego v1 = new Videojuego("FIFA 25", "PS5", 2);
            Videojuego v2 = new Videojuego("Minecraft", "PC", 1);

            v1.agregarJugadores(1);
            v2.agregarJugadores(3);

            v1.mostrar();
            v2.mostrar();
        }
    }    
}
