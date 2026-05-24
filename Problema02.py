# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Estudiante: Jean Carlos Silva Ariza
# Problema 2: Gestión de Precios de un Menú de Restaurante

def calcular_precio_final(categoria, precio_base):
    categoria_objetivo = "Plato Fuerte"
    umbral_precio = 26000
    
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        return precio_base - descuento
    else:
        return precio_base

def main():
    menu_restaurante = [
        ["Robalo A La Marinera", "Plato Fuerte", 36000],
        ["Deditos de Queso", "Entrada", 15000],
        ["Limonsoda", "Bebida", 12000],
        ["Pastas A La Boloñesa", "Plato Fuerte", 28000],
        ["Aros de Cebolla", "Entrada", 10000],
        ["Cerveza", "Bebida", 4000],
        ["Salsa de Chimichurri", "Adicional", 4500],
        ["Churrasco", "Plato Fuerte", 25000],
        ["Tarta de Limón", "Postre", 8000],
        ["Helado", "Postre", 2000],
        ["Salsa de Piña", "Adicional", 2500]
    ]
    
    print("Producto | Categoría | Precio Base | Precio Final")
    print("-" * 50)
    
    for producto in menu_restaurante:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        
        precio_final = calcular_precio_final(categoria, precio_base)
        
        print(f"{nombre} - {categoria} - ${precio_base} - ${precio_final}")

if __name__ == "__main__":
    main()