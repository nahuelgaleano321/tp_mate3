#codigo para traducir las columnas y valores del dataset adult a español

import pandas as pd
import os

# Cargar el archivo
ruta = "/home/nahuel/Escritorio/matematica/tp_mate/adult (3).csv"
df = pd.read_csv(ruta)

columnas_traducidas = {
    'age': 'edad',
    'workclass': 'clase_trabajo',
    'fnlwgt': 'peso_final',
    'education': 'educacion',
    'education.num': 'educacion_num',
    'marital.status': 'estado_civil',
    'occupation': 'ocupacion',
    'relationship': 'relacion',
    'race': 'raza',
    'sex': 'sexo',
    'capital.gain': 'ganancia_capital',
    'capital.loss': 'perdida_capital',
    'hours.per.week': 'horas_por_semana',
    'native.country': 'pais_origen',
    'income': 'ingreso'
}

df = df.rename(columns=columnas_traducidas)

traducciones_valores = {
    'clase_trabajo': {
        'Private': 'Privado',
        'Self-emp-not-inc': 'Autónomo-no-incorporado',
        'Self-emp-inc': 'Autónomo-incorporado',
        'Federal-gov': 'Gobierno-Federal',
        'Local-gov': 'Gobierno-Local',
        'State-gov': 'Gobierno-Estatal',
        'Without-pay': 'Sin-pago'
    },
    'educacion': {
        'Preschool': 'Preescolar',
        '1st-4th': '1ro-4to grado',
        '5th-6th': '5to-6to grado',
        '7th-8th': '7mo-8vo grado',
        '9th': '9no grado',
        '10th': '10mo grado',
        '11th': '11vo grado',
        '12th': '12vo grado',
        'HS-grad': 'Bachillerato',
        'Some-college': 'Algunos-cursos-universitarios',
        'Assoc-aacm': 'Asociado-AACM',
        'Assoc-voc': 'Asociado-vocacional',
        'Bachelors': 'Licenciatura',
        'Masters': 'Maestría',
        'Prof-school': 'Escuela-profesional',
        'Doctorate': 'Doctorado'
    },
    'estado_civil': {
        'Married-civ-spouse': 'Casado-cónyuge-civil',
        'Married-spouse-absent': 'Casado-cónyuge-ausente',
        'Married-AF-spouse': 'Casado-cónyuge-militar',
        'Never-married': 'Nunca-casado',
        'Divorced': 'Divorciado',
        'Separated': 'Separado',
        'Widowed': 'Viudo'
    },
    'ocupacion': {
        'Tech-support': 'Soporte-técnico',
        'Craft-repair': 'Artesanía-reparación',
        'Other-service': 'Otro-servicio',
        'Sales': 'Ventas',
        'Exec-managerial': 'Ejecutivo-administrativo',
        'Prof-specialty': 'Profesional-especialista',
        'Machine-op-inspct': 'Operador-máquina-inspector',
        'Transport-moving': 'Transporte-mudanzas',
        'Handlers-cleaners': 'Manipuladores-limpiadores',
        'Farming-fishing': 'Agricultura-pesca',
        'Protective-serv': 'Servicios-protección',
        'Armed-Forces': 'Fuerzas-armadas',
        'Priv-house-serv': 'Servicio-doméstico'
    },
    'relacion': {
        'Wife': 'Esposa',
        'Own-child': 'Hijo-propia',
        'Husband': 'Esposo',
        'Not-in-family': 'Fuera-de-familia',
        'Other-relative': 'Otro-familiar',
        'Unmarried': 'Soltero'
    },
    'raza': {
        'White': 'Blanco',
        'Black': 'Negro',
        'Asian-Pac-Islander': 'Asiático-Isleño-Pacífico',
        'Amer-Indian-Eskimo': 'Amerindio-Esquimal',
        'Other': 'Otro'
    },
    'sexo': {
        'Male': 'Hombre',
        'Female': 'Mujer'
    },
    'pais_origen': {
        'United-States': 'Estados-Unidos',
        'Puerto-Rico': 'Puerto-Rico',
        'Philippines': 'Filipinas',
        'India': 'India',
        'Mexico': 'México',
        'South': 'Sur',
        'Germany': 'Alemania',
        'England': 'Inglaterra',
        'Canada': 'Canadá',
        'Iran': 'Irán',
        'Poland': 'Polonia',
        'Italy': 'Italia',
        'Portugal': 'Portugal',
        'Greece': 'Grecia',
        'France': 'Francia',
        'Ireland': 'Irlanda',
        'Scotland': 'Escocia',
        'Jamaica': 'Jamaica',
        'Vietnam': 'Vietnam',
        'China': 'China',
        'Taiwan': 'Taiwán',
        'Hungary': 'Hungría',
        'Cuba': 'Cuba',
        'Japan': 'Japón',
        'Yugoslavia': 'Yugoslavia',
        'Guatemala': 'Guatemala',
        'Thailand': 'Tailandia',
        'El-Salvador': 'El-Salvador',
        'Dominican-Republic': 'República-Dominicana',
        'Trinadad&Tobago': 'Trinidad-Tobago',
        'Cameron': 'Camerún',
        'Hong': 'Hong-Kong',
        'Laos': 'Laos',
        'Nicaragua': 'Nicaragua',
        'Peru': 'Perú',
        'Ecuador': 'Ecuador',
        'Haiti': 'Haití',
        'Columbia': 'Colombia',
        'holand-Netherlands': 'Países-Bajos'
    },
    'ingreso': {
        '<=50K': '<=50K',
        '>50K': '>50K',
        '<=50K.': '<=50K',
        '>50K.': '>50K'
    }
}

for columna, traducciones in traducciones_valores.items():
    if columna in df.columns:
        df[columna] = df[columna].replace(traducciones)

ruta_salida = "/home/nahuel/Escritorio/matematica/tp_mate/adult_español.csv"
df.to_csv(ruta_salida, index=False)

print(f"✓ Archivo traducido guardado en: {ruta_salida}")
print(f"\nPrimeras filas del archivo traducido:")
print(df.head())