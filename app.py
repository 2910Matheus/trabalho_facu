import csv

mapa_conhecimento = {}
sintomas_paciente = []
resultado = {}


# Mapa de sintomas para detectar a causa
with open ('mapa_sintomas_doencas.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha_dict in leitor_csv:
        doenca = linha_dict['Doença Associada'].strip()
        sintomas = [
            linha_dict['Sintoma 1'].strip(), 
            linha_dict['Sintoma 2'].strip()
        ]
        mapa_conhecimento[doenca] = sintomas
print(mapa_conhecimento)
print('=' * 100)

# Texto dos sintomas dos pacientes
with open('sintomas_pacientes.txt', 'r', encoding='utf-8') as arquivo_txt:
    linha_txt = iter(arquivo_txt)
    for paciente_sintomas in linha_txt:
        par_sintoma_diagnostico = (paciente_sintomas.strip())
        sintomas_paciente.append(par_sintoma_diagnostico)
    
print(sintomas_paciente)
print('=' * 100)

for frase in sintomas_paciente:
    for doenca, sintomas in mapa_conhecimento.items():
        encontrados = [s for s in sintomas if s.lower() in frase.lower()]

        if encontrados:  # só entra se achou algum sintoma
            print(f"Na frase: '{frase}' foi encontrado os sintomas {', '.join(encontrados)} relacionados a {doenca}.")
            print("=" * 100)
            # soma quantos sintomas foram achados
            resultado[doenca] = resultado.get(doenca, 0) + len(encontrados)

print(resultado)

