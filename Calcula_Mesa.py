import math

def calcular_volume_cilindro(diametro, altura):
    raio = diametro / 2
    volume = math.pi * (raio**2) * altura
    return volume

def calcular_area_superficie_cilindro(diametro, altura):
    raio = diametro / 2
    area_base = math.pi * (raio**2)
    area_lateral = 2 * math.pi * raio * altura
    area_total = 2 * area_base + area_lateral
    return area_total

def calcular_preco_mesa(diametro, espessura):
    preco_referencia = 50
    area_base = math.pi * ((diametro / 2) ** 2)
    area_total = 2 * area_base + 2 * math.pi * (diametro / 2) * espessura
    preco_total = area_total * preco_referencia
    return preco_total

def main():
    print("Bem-vindo ao programa de medição da mesa!")
    print("Por favor, insira as medidas da mesa em centímetros.")
    print()

    altura = float(input("Altura da mesa: "))
    diametro = float(input("Diâmetro da mesa: "))
    espessura = float(input("Espessura da mesa: "))

    volume_mesa = calcular_volume_cilindro(diametro, altura)
    area_superficie_mesa = calcular_area_superficie_cilindro(diametro, altura)
    preco_mesa = calcular_preco_mesa(diametro, espessura)

    print()
    print("RESULTADOS:")
    print(f"Volume da mesa: {volume_mesa} cm³")
    print(f"Área da superfície da mesa: {area_superficie_mesa} cm²")
    print(f"Espessura da mesa: {espessura} cm")
    print(f"Preço da mesa: R$ {preco_mesa}")

if __name__ == "__main__":
    main()