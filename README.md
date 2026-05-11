# Instrucciones de Archivos del Proyecto

## 📄 traductor_csv.py
**¿Qué hace?** Traduce las columnas y valores del dataset original al español.
**Entrada:** Dataset original en inglés
**Salida:** Archivo adult_español.csv con datos traducidos
**Cómo usarlo:** Ejecutar el script para procesar el CSV original

---

## 📊 graficos.ipynb
**¿Qué hace?** Genera visualizaciones (boxplots) de las variables numéricas para detectar outliers.
**Variables analizadas:** edad, horas_por_semana, ganancia_capital, perdida_capital
**Propósito:** Identificar valores extremos y decidir qué datos limpiar
**Cómo usarlo:** Abrir en Jupyter y ejecutar celdas para ver gráficos

---

## 📝 normalizacion.ipynb
**¿Qué hace?** Aplica normalización Z-score a las variables numéricas del dataset limpio.
**Entrada:** adult_limpio_final.csv
**Procesamiento:** Normaliza edad, horas_por_semana, ganancia_capital y perdida_capital
**Salida:** adult_normalizado.csv
**Cómo usarlo:** Abrir en Jupyter y ejecutar celdas

---

## 📋 adult_español.csv
**¿Qué es?** Dataset traducido al español (generado por traductor_csv.py)
**Contenido:** Columnas y valores en idioma español
**Uso:** Referencia para el análisis con nomenclatura clara

---

## 🧹 adult_limpio_final.csv
**¿Qué es?** Dataset procesado y limpio
**Cambios realizados:**
- Reemplazo de "?" por "desconocido"
- Eliminación de outliers
- Eliminación de registros poco representativos
**Uso:** Input para normalización

---

## ✅ adult_normalizado.csv
**¿Qué es?** Dataset final con variables numéricas normalizadas
**Características:** Todas las variables en la misma escala (Z-score)
**Beneficio:** Mejora la comparación entre variables y evita que una domine sobre otra
**Uso:** Listo para modelado
