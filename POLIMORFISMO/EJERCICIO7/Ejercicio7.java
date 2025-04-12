package PRACTICA1.POLIMORFISMO.EJERCICIO7;

public class Ejercicio7 {

    public static class Perro {
        private String nombre;
        private int edad;
        private String raza;

        public Perro(String nombre, int edad, String raza) {
            this.nombre = nombre;
            this.edad = edad;
            this.raza = raza;
        }

        public void hacerSonido() {
            System.out.println(nombre + " hace: ¡Woof! ¡Woof!");
        }

        public void moverse() {
            System.out.println(nombre + " corre.");
        }
    }

    public static class Gato {
        private String nombre;
        private int edad;
        private String color;

        public Gato(String nombre, int edad, String color) {
            this.nombre = nombre;
            this.edad = edad;
            this.color = color;
        }

        public void hacerSonido() {
            System.out.println(nombre + " hace: ¡Miau! ¡Miau!");
        }

        public void moverse() {
            System.out.println(nombre + " salta.");
        }
    }

    public static class Pajaro {
        private String nombre;
        private int edad;
        private String tipo;

        public Pajaro(String nombre, int edad, String tipo) {
            this.nombre = nombre;
            this.edad = edad;
            this.tipo = tipo;
        }

        public void hacerSonido() {
            System.out.println(nombre + " hace: ¡Pío! ¡Pío!");
        }

        public void moverse() {
            System.out.println(nombre + " vuela.");
        }
    }

    public static void main(String[] args) {
        Perro perro = new Perro("Snoopy", 3, "Beagle");
        Gato gato = new Gato("Garfield", 2, "Naranja");
        Pajaro pajaro = new Pajaro("Blue", 1, "Guacamayo de Spix");

        perro.hacerSonido();
        perro.moverse();

        gato.hacerSonido();
        gato.moverse();

        pajaro.hacerSonido();
        pajaro.moverse();
    }
}
