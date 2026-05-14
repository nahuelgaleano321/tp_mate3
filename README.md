# Análisis y Procesamiento del Dataset Adult

Un proyecto paso a paso de limpieza, validación y normalización de datos del dataset Adult. Desde traducir el idioma hasta preparar los datos para modelado.

---

## Flujo del Proyecto: Paso a Paso

### **PASO 1️1 : Traduci el csv a español ya que me parecia mas comodo trabajarlo asi, el codiho con el cual lo traduci esta en :** 
**Archivo:** `traductor_csv.py`


**Entrada:** `adult (3).csv` (dataset original en inglés)  
**Salida:** `adult_español.csv` (dataset traducido)


### **PASO 2 : Detectar Valores Atípicos**
**Archivo:** `graficos.ipynb` (Primera celda)

Usamos gráficos de caja (boxplots) para identificar valores extremos que podrían distorsionar el análisis.


- Cargamos el dataset traducido (`adult_español.csv`)
- Genera un boxplot para cada variable numérica
- Visualiza dónde están los valores atapicos 

**Variables analizadas:**
-  `edad` - Rango típico vs edades extremas
-  `horas_por_semana` - Horas de trabajo típicas vs extremas
- `ganancia_capital` - Ganancias normales vs valores enormes
- `perdida_capital` - Pérdidas normales vs extremas


---

### **PASO 3 : Limpiar Valores Atípicos**
**Archivo:** `graficos.ipynb` (Segunda celda)

Eliminamos los valores atípicos y registros con datos inconsistentes.


1. Reemplazamos los valores faltantes `"?"` por `"desconocido"`


2. **Criterios de limpieza específicos:**
   - Edad < 80 años (elimina registros con edades poco realistas)
   - Horas/semana entre 3 y 55 (elimina extremos de inactividad y sobretrabajo)
   - Ganancia de capital ≤ $250,000 (elimina valores excesivos)
   - Pérdida de capital ≤ $3,000 (elimina outliers extremos)

**Entrada:** `adult_español.csv`  
**Salida:** `adult_limpio_final.csv`


---

### **PASO 4 : Normalizar Datos**
**Archivo:** `graficos.ipynb` (Tercera celda)

Las variables numéricas tienen diferentes escalas. La normalización las estandariza para mejor comparación.

- Aplicamos  normalización **Z-score** a cada variable numérica

**Variables normalizadas:**
- `edad`
- `horas_por_semana`
- `ganancia_capital`
- `perdida_capital`



**Entrada:** `adult_limpio_final.csv`  
**Salida:** `adult_normalizado.csv`

**Resultado:** Dataset final listo para modelado de machine learning.

---



## 📊 Resumen de Transformaciones

```
adult (3).csv (inglés)
[PASO 1: Traducción]
adult_español.csv
[PASO 2 & 3: Detección y Limpieza]
adult_limpio_final.csv (valores atipicos eliminados)
[PASO 4: Normalización Z-score]
adult_normalizado.csv (listo para modelado) 
