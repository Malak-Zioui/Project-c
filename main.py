"""
---------------------------------------------------------
  TP : Équations diophantiennes linéaires
  Résolution de ax + by = c
  Auteur : (Votre nom)
---------------------------------------------------------
"""

# ---------------------------------------------------------
# 1. PGCD (Algorithme d’Euclide)
# ---------------------------------------------------------
def pgcd(a: int, b: int) -> int:
    """Retourne le PGCD de a et b."""
    while b != 0:
        a, b = b, a % b
    return a


# ---------------------------------------------------------
# 2. Algorithme d’Euclide étendu
#    Retourne (d, x, y) tels que ax + by = d
# ---------------------------------------------------------
def euclide_etendu(a: int, b: int):
    """Retourne (d, x, y) tels que ax + by = d."""
    if b == 0:
        return a, 1, 0

    d, x1, y1 = euclide_etendu(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y


# ---------------------------------------------------------
# 3. Résolution de l'équation ax + by = c
# ---------------------------------------------------------
def resoudre_equation(a: int, b: int, c: int):
    """Résout l'équation ax + by = c."""

    # PGCD
    d = pgcd(a, b)

    if c % d != 0:
        return None  # Pas de solution

    # Solution particulière via Euclide étendu
    d, x0, y0 = euclide_etendu(a, b)
    k = c // d

    xp = x0 * k
    yp = y0 * k

    # Solutions générales
    solution_generale = {
        "x": f"{xp} + k * {b // d}",
        "y": f"{yp} - k * {a // d}",
    }

    return {
        "pgcd": d,
        "solution_particuliere": (xp, yp),
        "solution_generale": solution_generale,
    }


# ---------------------------------------------------------
# 4. Programme principal
# ---------------------------------------------------------
def main():
    print("=== Résolution de l'équation ax + by = c ===\n")

    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    resultat = resoudre_equation(a, b, c)

    if resultat is None:
        print("\n❌ Pas de solution entière : le PGCD ne divise pas c.")
        return

    print(f"\n✔ PGCD(a, b) = {resultat['pgcd']}")
    xp, yp = resultat["solution_particuliere"]

    print("\n✔ Solution particulière :")
    print(f"x_p = {xp}, y_p = {yp}")

    print("\n✔ Solutions générales :")
    print(f"x = {resultat['solution_generale']['x']}")
    print(f"y = {resultat['solution_generale']['y']}")
    print("\n(k ∈ ℤ)")


# Lancer le programme
if __name__ == "__main__":
    main()
