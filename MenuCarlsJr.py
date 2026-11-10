inventario = {
    "pan": 1,
    "pan_sin_ajonjoli": 1,
    "pollo": 1,
    "carne": 1,
    "doble_carne": 1,
    "triple_carne": 1,
    "queso_amarillo": 1,
    "queso_blanco": 1,
    "lechuga": 1,
    "bbq": 1,
    "mayonesa": 1,
    "tocino": 1,
    "guacamole": 1,
    "teriyaki": 1
}

class Hamburguesa_pollo:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

    def preparar(self):
        print(f"\nPreparando {self.nombre} ")

        for ing, cant in self.ingredientes.items():
            if inventario.get(ing, 0) < cant:
                print(f"No hay suficiente {ing}")
                return

        for ing, cant in self.ingredientes.items():
            inventario[ing] -= cant

        print("Hamburguesa lista ")

bbq_chicken = Hamburguesa_pollo(
    "BBQ Chicken",
    {"pollo": 1, "pan": 1, "bbq": 1, "lechuga": 1}
)

santa_fe_chicken = Hamburguesa_pollo(
    "Santa Fe Chicken",
    {"pollo": 1, "pan": 1, "queso_amarillo": 1, "lechuga": 1}
)

big_chicken_filet = Hamburguesa_pollo(
    "Big Chicken Filet",
    {"pollo": 2, "pan": 1, "queso_blanco": 1, "lechuga": 1, "mayonesa": 1}
)

chicken_club = Hamburguesa_pollo(
    "Chicken Club",
    {"pollo": 1, "pan": 1, "queso_blanco": 1, "lechuga": 1}
)
class Hamburguesa_parrilla:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

    def preparar(self):
        print(f"\nPreparando {self.nombre} ")

        for ing, cant in self.ingredientes.items():
            if inventario.get(ing, 0) < cant:
                print(f"No hay suficiente {ing}")
                return

        for ing, cant in self.ingredientes.items():
            inventario[ing] -= cant

        print("Hamburguesa lista ")

hand_breaded = Hamburguesa_parrilla(
    "Hand Breaded Chicken",
    {"pollo": 1, "pan_sin_ajonjoli": 1, "mayonesa": 1, "lechuga": 1}
)

famous_star = Hamburguesa_parrilla(
    "Famous Star",
    {"doble_carne": 1, "pan": 1, "queso_amarillo": 1, "queso_blanco": 1, "lechuga": 1}
)

super_star = Hamburguesa_parrilla(
    "Super Star",
    {"doble_carne": 1, "pan": 1, "queso_amarillo": 1, "lechuga": 1, "mayonesa": 1}
)

western_bacon = Hamburguesa_parrilla(
    "Western Bacon",
    {"doble_carne": 1, "pan": 1, "queso_amarillo": 1, "tocino": 1}
)

double_western_bacon = Hamburguesa_parrilla(
    "Double Western Bacon",
    {"triple_carne": 1, "pan": 1, "queso_amarillo": 1, "tocino": 1}
)

teriyaki_burger = Hamburguesa_parrilla(
    "Teriyaki Burger",
    {"doble_carne": 1, "pan": 1, "queso_blanco": 1, "lechuga": 1, "teriyaki": 1}
)

portobello = Hamburguesa_parrilla(
    "Portobello",
    {"doble_carne": 1, "pan_sin_ajonjoli": 1, "queso_blanco": 1, "lechuga": 1}
)

class Big_angus_burguer:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

    def preparar(self):
        print(f"\nPreparando {self.nombre} ")

        for ing, cant in self.ingredientes.items():
            if inventario.get(ing, 0) < cant:
                print(f"No hay suficiente {ing}")
                return

        for ing, cant in self.ingredientes.items():
            inventario[ing] -= cant

        print("Hamburguesa lista ")


angus_original = Big_angus_burguer(
    "Angus Original",
    {"doble_carne": 1, "pan_sin_ajonjoli": 1, "queso_amarillo": 1, "lechuga": 1}
)

angus_guacamole = Big_angus_burguer(
    "Angus guacamole",
    {"doble_carne": 1, "pan": 1, "queso_blanco": 1, "lechuga": 1, "guacamole": 1}
)

angus_western = Big_angus_burguer(
    "Big Angus Western",
    {"doble_carne": 1, "pan_sin_ajonjoli": 1, "queso_amarillo": 1, "tocino": 1}
)

angus_low_carb = Big_angus_burguer(
    "Big Angus Low Carb",
    {"doble_carne": 1, "queso_amarillo": 1, "lechuga": 1}
)



while True:
    print("MENU")
    print("1.Menu pollo")
    print("2. Menu Angus burguer")
    print("3. Hamburguesa a la parrilla")
    print("0. Salir")
    opcion = input("Elige una opcion ")

    if opcion == "1":
        print("1. BBQ chiquen")
        print("2.Santa Fe Chiquen")
        print("3.Big chiquen filet")
        print("4. Chiquen club")
        print("5. Hand breaded")
        print("0. Salir")
        opcion = input("Elegir opcion")
    
        if opcion == "1":
            bbq_chicken.preparar()

        if opcion == "0":
            break
        
       

    
    
