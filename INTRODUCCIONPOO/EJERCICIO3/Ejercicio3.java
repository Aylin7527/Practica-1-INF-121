package PRACTICA1.INTRODUCCIONPOO.EJERCICIO3;

public class Ejercicio3 {
    public static class Coche {
        private String marca;
        private String modelo;
        private int velocidad;
    
        // Constructor
        public Coche(String marca, String modelo) {
            this.marca = marca;
            this.modelo = modelo;
            this.velocidad = 0;
        }
    
        // Método para acelerar
        public void acelerar() {
            velocidad += 10;
        }
    
        // Método para frenar
        public void frenar() {
            velocidad -= 5;
            if (velocidad < 0) {
                velocidad = 0;
            }
        }
    
        // Método para mostrar velocidad
        public void mostrarVelocidad() {
            System.out.println("El coche " + marca + " " + modelo + " va a " + velocidad + " km/h");
        }
    
        public static void main(String[] args) {
            Coche coche1 = new Coche("Toyota", "Corolla");
            Coche coche2 = new Coche("Ford", "Focus");
    
            coche1.acelerar();
            coche1.acelerar();
            coche1.frenar();
            coche1.mostrarVelocidad();
    
            coche2.acelerar();
            coche2.frenar();
            coche2.mostrarVelocidad();
        }
    }
    
}
