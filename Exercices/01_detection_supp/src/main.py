#!/usr/bin/env python3

"""
Exercice sur git pour détecter dans quelle commit le contenu de ce fichier est supprimer :

"""

password = 123456789


# Classe à tester
class Calculatrice:
    def additionner(self, a, b):
        return a + b

    def soustraire(self, a, b):
        return a - b

# Tests unitaires
import unittest

class TestCalculatrice(unittest.TestCase):
    def setUp(self):
        self.calc = Calculatrice()

    def test_additionner(self):
        resultat = self.calc.additionner(3, 7)
        self.assertEqual(resultat, 10)

    def test_soustraire(self):
        resultat = self.calc.soustraire(10, 5)
        self.assertEqual(resultat, 5)

if __name__ == '__main__':
    unittest.main()
