# Importar a biblioteca pandas
import pandas as pd

# --- Operação 1: Ordenar por indivíduos em ordem crescente ---
print("--- 1. Resultado da ordenação por 'individuals' (crescente) ---")
homelessness_ind = homelessness.sort_values("individuals")
print(homelessness_ind.head())
print("\n" + "="*60 + "\n") # Adiciona um separador


# --- Operação 2: Ordenar por membros da família em ordem decrescente ---
print("--- 2. Resultado da ordenação por 'family_members' (decrescente) ---")
homelessness_fam = homelessness.sort_values("family_members", ascending=False)
print(homelessness_fam.head())
print("\n" + "="*60 + "\n") # Adiciona um separador


# --- Operação 3: Ordenar por região (crescente) e membros da família (decrescente) ---
print("--- 3. Resultado da ordenação por 'region' e 'family_members' ---")
homelessness_reg_fam = homelessness.sort_values(
    by=["region", "family_members"], 
    ascending=[True, False]
)
print(homelessness_reg_fam.head())
