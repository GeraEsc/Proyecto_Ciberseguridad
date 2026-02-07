# Incident Response & Data Analysis Project (Cortex XDR + Python)

## Descripción
Este proyecto simula un flujo de trabajo de Respuesta a Incidentes (IR) dentro de un SOC. El objetivo es automatizar la recolección de artefactos forenses de endpoints, procesar logs de seguridad y visualizar métricas clave para la toma de decisiones gerenciales.

## Tecnologías utilizadas
* **Cortex XDR (Conceptos):** Análisis de alertas de red y endpoint.
* **Python:** Automatización de comandos de sistema (CMD/PowerShell) para recolección de datos.
* **SQL:** Consultas para correlación de eventos y filtrado de severidad.
* **Excel & Power BI:** Limpieza de datos y visualización de KPIs (SLA, volumen de incidentes).

## Componentes del Proyecto
1. **Automatización:** Un script que extrae conexiones activas (`netstat`) ante una alerta de Cortex.
2. **Análisis SQL:** Consultas diseñadas para identificar IPs recurrentes y equipos vulnerables.
3. **Visualización:** Dashboard que muestra la distribución de incidentes por tipo y criticidad.

## Cómo usarlo
1. Ejecutar `scripts/collector.py` para generar el log local.
2. Cargar el CSV resultante en Power BI para actualizar las métricas.