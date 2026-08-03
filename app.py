from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ── Datos del inventario ──────────────────────────────────────────────────────
equipos = [
    {"n":1,"nombre":"Ada Migdalia Cruz Cute","area":"Finanzas","puesto":"Auxiliar Contable","dominio":"AAD-ACRUZ","marca":"Dell","modelo":"Inspiron 15 3520","serie":"18Q7RW3","ip":"172.70.0.11","mac":"4C-49-6C-3F-58-FE","estado":"Pendiente"},
    {"n":2,"nombre":"Alexander González Cruz","area":"Generación","puesto":"Jefe de Generación","dominio":"AD-AGONZALEZ","marca":"Dell","modelo":"Latitude 5550","serie":"J7CSL64","ip":"192.168.3.120","mac":"30-E3-A4-55-A8-DE","estado":"Pendiente"},
    {"n":3,"nombre":"Ana Cristina Ramos C.","area":"Finanzas","puesto":"Gerente Adm. y Finanzas","dominio":"AAD-ARAMOS","marca":"Dell","modelo":"XPS 13 9310","serie":"D2B93F3","ip":"172.70.0.32","mac":"4C-79-6E-D8-8D-CB","estado":"Pendiente"},
    {"n":4,"nombre":"Ana Sucelly Ruiz","area":"RRHH","puesto":"Jefe de RRHH","dominio":"AAD-ARUIZ","marca":"Dell","modelo":"Latitude 5550","serie":"8D0HJ64","ip":"192.168.0.7","mac":"30-E3-A4-69-22-7E","estado":"Pendiente"},
    {"n":5,"nombre":"Andrea Gutierrez Gularte","area":"Legal","puesto":"Gerente Rel. Corporativas","dominio":"AAD-AGUTIERREZ","marca":"Dell","modelo":"XPS 13 9350","serie":"4GYDSH4","ip":"172.70.0.37","mac":"04-F0-EE-C0-52-FB","estado":"Pendiente"},
    {"n":6,"nombre":"Andres Sierra Dávila","area":"Compras","puesto":"Lider de Compras","dominio":"AAD-ASIERRA","marca":"Lenovo","modelo":"21MA006QFJ","serie":"PF5A9T3F","ip":"172.70.0.48","mac":"E8-B0-C5-B9-D0-56","estado":"Completado"},
    {"n":7,"nombre":"Angel Interiano Espinoza","area":"Mejora Continua","puesto":"Esp. Procesos y Mejora","dominio":"AAD-AINTERIANO","marca":"Dell","modelo":"Inspiron 15 3511","serie":"C9LC6W3","ip":"172.70.0.9","mac":"BC-F4-D4-B8-4A-73","estado":"Pendiente"},
    {"n":8,"nombre":"Axel García Valle","area":"Finanzas","puesto":"Analista Financiero","dominio":"AAD-AVALLE","marca":"Dell","modelo":"Inspiron 15 3520","serie":"2545RW3","ip":"172.70.0.24","mac":"2C-98-11-74-E7-8B","estado":"Pendiente"},
    {"n":9,"nombre":"Berena Villatoro Muñoz","area":"Finanzas","puesto":"Auxiliar Contable","dominio":"AAD-BVILLATORO","marca":"Dell","modelo":"Latitude 3520","serie":"6MPRBL3","ip":"172.70.0.19","mac":"60-A5-E2-2A-C1-AF","estado":"Pendiente"},
    {"n":10,"nombre":"Byron García Archila","area":"Desarrollo","puesto":"Desarrollador Middle","dominio":"AAD-BGARCIA","marca":"Lenovo","modelo":"20RD002RUS","serie":"PF1WNQV3","ip":"172.70.0.14","mac":"F8-75-A4-F4-5D-F6","estado":"Pendiente"},
    {"n":11,"nombre":"Carlos Lara Morales","area":"Operación de Sedes","puesto":"Jefe de Operación","dominio":"AD-CARLOSL","marca":"Dell","modelo":"Latitude 3540","serie":"J1FHND3","ip":"172.70.0.41","mac":"58-1C-F8-69-40-BF","estado":"Pendiente"},
    {"n":12,"nombre":"Carlos Moran Barrios","area":"Transnorte","puesto":"Jefe de Transmisión","dominio":"AAD-CMORAN","marca":"Lenovo","modelo":"20T40034US","serie":"PF2MT1J6","ip":"10.22.210.64","mac":"50-2F-9B-D4-B2-A0","estado":"Completado"},
    {"n":13,"nombre":"Carlos Pérez Noriega","area":"Desarrollo de Negocios","puesto":"Esp. Desarrollo Negocio","dominio":"AAD-APEREZ","marca":"Dell","modelo":"Latitude 3540","serie":"9HKKG24","ip":"172.70.0.10","mac":"D0-46-0C-56-99-98","estado":"Pendiente"},
    {"n":14,"nombre":"César Súchite González","area":"Finanzas","puesto":"Aux. Auditoría Financiero","dominio":"AAD-CSUCHITE","marca":"Dell","modelo":"Dell Pro 16 Plus","serie":"D6T3N94","ip":"172.70.0.28","mac":"DC-56-7B-80-EA-27","estado":"Pendiente"},
    {"n":15,"nombre":"Claudia Toledo Pineda","area":"Fund. Ríos por la Paz","puesto":"Directora Ejecutiva","dominio":"AD-PTOLEDO","marca":"Dell","modelo":"Inspiron 15 3520","serie":"1Q6CPY3","ip":"172.70.0.43","mac":"CC-5E-F8-88-15-14","estado":"Reprogramado"},
    {"n":16,"nombre":"Cristian Herrera Corleto","area":"Finanzas","puesto":"Especialista Contable","dominio":"AAD-CHERRERA","marca":"Dell","modelo":"Latitude 3540","serie":"G1FHND3","ip":"172.70.0.26","mac":"58-1C-F8-6F-53-01","estado":"Pendiente"},
    {"n":17,"nombre":"Edwin Castillo Herrera","area":"Finanzas","puesto":"Auxiliar Contable","dominio":"AAD-ECASTILLO","marca":"Dell","modelo":"Inspiron 15 3520","serie":"2Y5XRW3","ip":"172.70.0.30","mac":"D4-E9-8A-45-EA-89","estado":"Pendiente"},
    {"n":18,"nombre":"Edwin Montejo Aguirre","area":"Procesos y Mejora","puesto":"Esp. de Procesos","dominio":"AAD-EMONTEJO","marca":"Dell","modelo":"Inspiron 3501","serie":"5CP8J93","ip":"172.70.0.22","mac":"A4-97-B1-C4-83-4B","estado":"Pendiente"},
    {"n":19,"nombre":"Erick Barrios Rivera","area":"Mantenimiento","puesto":"Asistente Consultor","dominio":"AAD-EBARRIOS","marca":"Dell","modelo":"Latitude 3540","serie":"21LKG24","ip":"172.70.0.55","mac":"18-93-41-84-44-41","estado":"Pendiente"},
    {"n":20,"nombre":"Erick Vicente Aguilar","area":"Legal","puesto":"Especialista Legal","dominio":"AAD-EVICENTE","marca":"Dell","modelo":"Latitude 3540","serie":"1DFHND3","ip":"172.70.0.15","mac":"58-1C-F8-44-BC-27","estado":"Pendiente"},
    {"n":21,"nombre":"Erikson De León Marroquín","area":"Desarrollo","puesto":"Lider de Desarrollo","dominio":"AAD-EDELEON","marca":"Dell","modelo":"Inspiron 15 3511","serie":"8LLC6W3","ip":"192.168.56.1","mac":"BC-F4-D4-B8-42-09","estado":"Pendiente"},
    {"n":22,"nombre":"Ilsy López Gómez","area":"Fund. Ríos por la Paz","puesto":"Desarrollo Social","dominio":"AAD-ILOPEZ","marca":"Dell","modelo":"Inspiron 3593","serie":"5W05S53","ip":"172.70.0.18","mac":"28-CD-C4-58-19-E3","estado":"Pendiente"},
    {"n":23,"nombre":"Ingrid Carrillo Yuman","area":"T. Mercado Ambiental","puesto":"Coordinador Transacciones","dominio":"AAD-JCARRILLO","marca":"Dell","modelo":"Latitude 3550","serie":"9NG0Y54","ip":"172.70.0.44","mac":"C4-47-4E-DA-B3-F3","estado":"Pendiente"},
    {"n":24,"nombre":"Jaime Matus Bonilla","area":"Finanzas","puesto":"Jefe Reestructuración Fin.","dominio":"AAD-JMATUS","marca":"Dell","modelo":"Dell Pro 16 Plus","serie":"BQ8P6G4","ip":"172.70.0.30","mac":"D4-E9-8A-45-EA-89","estado":"Pendiente"},
    {"n":25,"nombre":"Jesus Arango Estrada","area":"T. Mercado Ambiental","puesto":"Lider de Transacciones","dominio":"AAD-JARANGO","marca":"Dell","modelo":"Latitude 3540","serie":"HC1NYW3","ip":"172.70.0.13","mac":"74-3A-F4-71-D4-37","estado":"Pendiente"},
    {"n":26,"nombre":"Jonathan Gamboa Pérez","area":"Tecnología de la Inf.","puesto":"Auxiliar de TI","dominio":"AAD-JGAMBOA","marca":"Dell","modelo":"Inspiron 15 5510","serie":"G3YQJG3","ip":"10.80.0.3","mac":"00-E0-4C-68-01-FB","estado":"Pendiente"},
    {"n":27,"nombre":"Jorge Juárez Menéndez","area":"Procesos y Mejora","puesto":"Jefe de Planificación","dominio":"AAD-JJUAREZ","marca":"Dell","modelo":"Dell 16 Plus DB16250","serie":"2SQM8F4","ip":"172.70.0.50","mac":"E8-BF-E1-C2-E9-2F","estado":"Reprogramado"},
    {"n":28,"nombre":"Josseline Arriaza Ortega","area":"Desarrollo de Negocios","puesto":"Project Manager","dominio":"AAD-JARRIAZA","marca":"Dell","modelo":"Dell Pro 16 Plus","serie":"C6YK184","ip":"172.70.0.49","mac":"B4-E9-B8-2E-7D-39","estado":"Pendiente"},
    {"n":29,"nombre":"Katherine Orozco Girón","area":"Finanzas","puesto":"Especialista Financiero","dominio":"AAD-KOROZCO","marca":"Dell","modelo":"Latitude 3520","serie":"73PXGS3","ip":"172.70.0.46","mac":"A0-59-50-E6-00-EB","estado":"Pendiente"},
    {"n":30,"nombre":"Kevin González Sazo","area":"Transnorte","puesto":"Analista de Operaciones","dominio":"AAD-KGONZALEZ","marca":"Dell","modelo":"Latitude 3550","serie":"31C1Y54","ip":"172.70.0.54","mac":"C4-47-4E-9E-D8-C9","estado":"Pendiente"},
    {"n":31,"nombre":"Leandro Hernández Samayoa","area":"TI","puesto":"Lider de TI","dominio":"AAD-LHERNANDEZ","marca":"Dell","modelo":"XPS 15 9510","serie":"JWL9YD3","ip":"—","mac":"4C-79-6E-D8-B6-E3","estado":"Pendiente"},
    {"n":32,"nombre":"Linda Lucero Vásquez Duarte","area":"Finanzas","puesto":"Lider Auditoría Financiero","dominio":"AAD-LVASQUEZ","marca":"Dell","modelo":"Inspiron 3501","serie":"5T9PYJ3","ip":"172.70.0.57","mac":"80-B6-55-5B-4F-69","estado":"Completado"},
    {"n":33,"nombre":"Luis Cajas Mercedes","area":"Finanzas","puesto":"Aux. Auditoría Financiero","dominio":"AAD-LCAJAS","marca":"Dell","modelo":"Inspiron 15 3520","serie":"2Y8VRW3","ip":"172.70.0.23","mac":"D4-E9-8A-47-19-63","estado":"Pendiente"},
    {"n":34,"nombre":"Magdalena Rodríguez Toma","area":"Finanzas","puesto":"Aux. Auditoría Financiero","dominio":"AAD-MRODRIGUEZ","marca":"Dell","modelo":"Dell Pro 16 Plus","serie":"G5T3N94","ip":"172.70.0.38","mac":"D4-A2-CD-1C-D3-99","estado":"Pendiente"},
    {"n":35,"nombre":"Maynor Ruíz García","area":"Finanzas","puesto":"Auxiliar Contable","dominio":"AAD-AGARCIA","marca":"Dell","modelo":"Latitude 3510","serie":"HLW2663","ip":"172.70.0.40","mac":"8C-47-BE-53-78-DE","estado":"Pendiente"},
    {"n":36,"nombre":"Merelin Cabrera Ortiz","area":"RRHH","puesto":"Auxiliar de RRHH","dominio":"AAD-MCABRERA","marca":"Dell","modelo":"Inspiron 15 3520","serie":"HRMQ6F3","ip":"172.70.0.60","mac":"5A-C3-89-0F-60-E4","estado":"Completado"},
    {"n":37,"nombre":"Migdalia Azucena García","area":"Gerencia General","puesto":"Asistente de Gerencia","dominio":"AAD-MAGARCIA","marca":"Dell","modelo":"Dell Pro 16 Plus","serie":"DMT3N94","ip":"172.70.0.56","mac":"DC-56-7B-80-EB-E3","estado":"Pendiente"},
    {"n":38,"nombre":"Nery Cerna Rojas","area":"Finanzas","puesto":"Aux. Auditoría Financiero","dominio":"AAD-NCERNA","marca":"Dell","modelo":"Inspiron 15 3520","serie":"3Q8VRW3","ip":"172.70.0.27","mac":"F8-E4-3B-3F-BD-7A","estado":"Pendiente"},
    {"n":39,"nombre":"Pablo Tepeque Chávez","area":"Finanzas","puesto":"Contador General","dominio":"AAD-PTEPEQUE","marca":"Dell","modelo":"Latitude 3540","serie":"J0FHND3","ip":"172.70.0.33","mac":"AC-1A-3D-CD-A2-19","estado":"Pendiente"},
    {"n":40,"nombre":"Paola Chávez Solórzano","area":"Legal","puesto":"Especialista Legal","dominio":"AAD-PCHAVEZ","marca":"Dell","modelo":"Inspiron 15 3520","serie":"JY4P9X3","ip":"172.70.0.20","mac":"74-97-79-9D-01-41","estado":"Pendiente"},
    {"n":41,"nombre":"Raúl Pérez Rosales","area":"Desarrollo","puesto":"Desarrollador","dominio":"AAD-RPEREZ","marca":"Dell","modelo":"Inspiron 15 3511","serie":"9RYC6W3","ip":"192.168.71.1","mac":"BC-F4-D4-B8-49-1D","estado":"Pendiente"},
    {"n":42,"nombre":"Stefany Solís Ruano","area":"RRHH","puesto":"Auxiliar de RRHH","dominio":"AAD-SSOLIS","marca":"Dell","modelo":"Inspiron 15 3520","serie":"DL0XRW3","ip":"172.70.0.61","mac":"D4-E9-8A-46-02-DF","estado":"Completado"},
    {"n":43,"nombre":"Treycy García Zarat","area":"Finanzas","puesto":"Aux. de Planillas","dominio":"AD-TGARCIA","marca":"Dell","modelo":"Inspiron 3501","serie":"9N0L983","ip":"172.70.0.59","mac":"5C-BA-EF-EA-D8-BC","estado":"Reprogramado"},
    {"n":44,"nombre":"Jose Eduardo Marques","area":"Socios","puesto":"—","dominio":"AAD-JMARQUES","marca":"Dell","modelo":"XPS 13 9350","serie":"F7DFSH4","ip":"172.70.0.8","mac":"04-F0-EE-C0-52-DD","estado":"Pendiente"},
]

mantenimientos = [
    {"semana":"Completados (Jun–Jul)","dia":"16/06/2026","usuario":"Stefany Solís Ruano","area":"RRHH","modelo":"Inspiron 15 3520","tipo":"Correctivo","desc":"Reparación de bisagra de pantalla","estado":"Completado"},
    {"semana":"Completados (Jun–Jul)","dia":"23/06/2026","usuario":"Merelin Cabrera Ortiz","area":"RRHH","modelo":"Inspiron 15 3520","tipo":"Correctivo","desc":"Apagado repentino — revisión batería, RAM y SO","estado":"Completado"},
    {"semana":"Completados (Jun–Jul)","dia":"01/07/2026","usuario":"Carlos Moran Barrios","area":"Transnorte","modelo":"Lenovo 20T40034US","tipo":"Preventivo","desc":"Limpieza interna, actualización de drivers y SO","estado":"Completado"},
    {"semana":"Completados (Jun–Jul)","dia":"01/07/2026","usuario":"Linda Vásquez Duarte","area":"Finanzas","modelo":"Inspiron 3501","tipo":"Correctivo","desc":"Fallas múltiples — préstamo temporal de equipo","estado":"En progreso"},
    {"semana":"Completados (Jun–Jul)","dia":"09/07/2026","usuario":"Andres Sierra Dávila","area":"Compras","modelo":"Lenovo 21MA006QFJ","tipo":"Preventivo","desc":"Mantenimiento preventivo completo","estado":"Completado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Lun 13/07","usuario":"Edwin Montejo Aguirre","area":"Procesos y Mejora","modelo":"Inspiron 3501","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Lun 13/07","usuario":"Raúl Pérez Rosales","area":"Desarrollo","modelo":"Inspiron 15 3511","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Lun 13/07","usuario":"Ilsy López Gómez","area":"Fund. Ríos","modelo":"Inspiron 3593","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Mar 14/07","usuario":"Maynor Ruíz García","area":"Finanzas","modelo":"Latitude 3510","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Mar 14/07","usuario":"Angel Interiano Espinoza","area":"Mejora Continua","modelo":"Inspiron 15 3511","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Mar 14/07","usuario":"Erikson De León Marroquín","area":"Desarrollo","modelo":"Inspiron 15 3511","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Mié 15/07","usuario":"Ada Migdalia Cruz Cute","area":"Finanzas","modelo":"Inspiron 15 3520","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Mié 15/07","usuario":"Axel García Valle","area":"Finanzas","modelo":"Inspiron 15 3520","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Mié 15/07","usuario":"Nery Cerna Rojas","area":"Finanzas","modelo":"Inspiron 15 3520","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Jue 16/07","usuario":"Luis Cajas Mercedes","area":"Finanzas","modelo":"Inspiron 15 3520","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Jue 16/07","usuario":"Paola Chávez Solórzano","area":"Legal","modelo":"Inspiron 15 3520","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Jue 16/07","usuario":"Berena Villatoro Muñoz","area":"Finanzas","modelo":"Latitude 3520","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Vie 17/07","usuario":"Katherine Orozco Girón","area":"Finanzas","modelo":"Latitude 3520","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Vie 17/07","usuario":"Edwin Castillo Herrera","area":"Finanzas","modelo":"Inspiron 15 3520","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 1 — 13 al 17 Jul","dia":"Vie 17/07","usuario":"Cristian Herrera Corleto","area":"Finanzas","modelo":"Latitude 3540","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Lun 20/07","usuario":"Josseline Arriaza Ortega","area":"Des. Negocios","modelo":"Dell Pro 16 Plus","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Lun 20/07","usuario":"Pablo Tepeque Chávez","area":"Finanzas","modelo":"Latitude 3540","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Lun 20/07","usuario":"Erick Vicente Aguilar","area":"Legal","modelo":"Latitude 3540","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Mar 21/07","usuario":"Carlos Pérez Noriega","area":"Des. Negocios","modelo":"Latitude 3540","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Mar 21/07","usuario":"Carlos Lara Morales","area":"Op. Sedes","modelo":"Latitude 3540","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Mar 21/07","usuario":"Erick Barrios Rivera","area":"Mantenimiento","modelo":"Latitude 3540","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Mié 22/07","usuario":"Jesus Arango Estrada","area":"T. Mercado Amb.","modelo":"Latitude 3540","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Mié 22/07","usuario":"Treycy García Zarat ★","area":"Finanzas","modelo":"Inspiron 3501","tipo":"Preventivo","desc":"10:30 – 12:30 PM — Reprogramado","estado":"Reprogramado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Jue 23/07","usuario":"Byron García Archila","area":"Desarrollo","modelo":"Lenovo 20RD002RUS","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Jue 23/07","usuario":"Kevin González Sazo","area":"Transnorte","modelo":"Latitude 3550","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Jue 23/07","usuario":"Ingrid Carrillo Yuman","area":"T. Mercado Amb.","modelo":"Latitude 3550","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Vie 24/07","usuario":"Alexander González Cruz","area":"Generación","modelo":"Latitude 5550","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Vie 24/07","usuario":"Ana Sucelly Ruiz","area":"RRHH","modelo":"Latitude 5550","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 2 — 20 al 24 Jul","dia":"Vie 24/07","usuario":"Jorge Juárez Menéndez ★","area":"Procesos","modelo":"Dell 16 Plus","tipo":"Preventivo","desc":"2:00 – 4:00 PM — Reprogramado a viernes","estado":"Reprogramado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Lun 27/07","usuario":"Migdalia Azucena García","area":"Gerencia General","modelo":"Dell Pro 16 Plus","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Lun 27/07","usuario":"César Súchite González","area":"Finanzas","modelo":"Dell Pro 16 Plus","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Lun 27/07","usuario":"Jaime Matus Bonilla","area":"Finanzas","modelo":"Dell Pro 16 Plus","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Mar 28/07","usuario":"Magdalena Rodríguez Toma","area":"Finanzas","modelo":"Dell Pro 16 Plus","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Mar 28/07","usuario":"Ana Cristina Ramos C.","area":"Finanzas","modelo":"XPS 13 9310","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Mar 28/07","usuario":"Andrea Gutierrez Gularte","area":"Legal","modelo":"XPS 13 9350","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Mié 29/07","usuario":"Jose Eduardo Marques","area":"Socios","modelo":"XPS 13 9350","tipo":"Preventivo","desc":"8:00 – 10:00 AM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Mié 29/07","usuario":"Leandro Hernández Samayoa","area":"TI","modelo":"XPS 15 9510","tipo":"Preventivo","desc":"10:30 – 12:30 PM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Mié 29/07","usuario":"Jonathan Gamboa Pérez","area":"TI","modelo":"Inspiron 15 5510","tipo":"Preventivo","desc":"2:00 – 4:00 PM","estado":"Programado"},
    {"semana":"Semana 3 — 27 al 31 Jul","dia":"Jue 30/07","usuario":"Claudia Toledo Pineda ★","area":"Fund. Ríos","modelo":"Inspiron 15 3520","tipo":"Preventivo","desc":"8:00 – 10:00 AM — Reprogramado post 28 jul","estado":"Reprogramado"},
]

red_equipos = [
    {"tipo":"Switch Core","marca":"Cisco","modelo":"Catalyst 1300 Series","puertos":"24+4 SFP","ubicacion":"Rack principal","ip":"","estado":"Activo"},
    {"tipo":"Switch Core PoE","marca":"Cisco","modelo":"SG200-50","puertos":"50","ubicacion":"Rack Finanzas","ip":"","estado":"Activo"},
    {"tipo":"Switch Acceso","marca":"Cisco Business","modelo":"350 Series","puertos":"48+4 SFP","ubicacion":"Rack Finanzas","ip":"","estado":"Activo"},
    {"tipo":"Switch Acceso","marca":"Cisco","modelo":"Switch 24p (Area B)","puertos":"24","ubicacion":"Rack principal","ip":"","estado":"Activo"},
    {"tipo":"Switch Acceso","marca":"Cisco","modelo":"Switch 24p (Acceso)","puertos":"24","ubicacion":"Rack principal","ip":"","estado":"Activo"},
    {"tipo":"Patch Panel","marca":"Quest","modelo":"NPP-6048 Cat6","puertos":"48","ubicacion":"Rack principal","ip":"","estado":"Activo"},
    {"tipo":"Patch Panel","marca":"Quest","modelo":"Cat6 24p","puertos":"24","ubicacion":"Rack principal","ip":"","estado":"Activo"},
    {"tipo":"Access Point","marca":"UniFi","modelo":"UAP-AC-M (AC Mesh) ×5","puertos":"—","ubicacion":"Nivel Administrativo","ip":"10.99.0.12–18","estado":"Activo"},
    {"tipo":"Access Point","marca":"UniFi","modelo":"AC Mesh Pro","puertos":"—","ubicacion":"Sala no. 4","ip":"10.99.0.19","estado":"Activo"},
    {"tipo":"Access Point","marca":"UniFi","modelo":"U6-Pro","puertos":"—","ubicacion":"Sala Principal","ip":"10.99.0.20","estado":"Activo"},
    {"tipo":"Access Point","marca":"UniFi","modelo":"Nano HD","puertos":"—","ubicacion":"Finanzas","ip":"10.99.0.13","estado":"Activo"},
    {"tipo":"Router Core","marca":"MikroTik","modelo":"CCR2004-16G-2S+","puertos":"16G+2SFP+","ubicacion":"Rack principal pos.25","ip":"","estado":"Activo"},
    {"tipo":"Gateway Voz","marca":"Mediatrix","modelo":"G7 Series","puertos":"—","ubicacion":"Rack principal","ip":"","estado":"Activo"},
    {"tipo":"Servidor","marca":"Dell EMC","modelo":"PowerEdge","puertos":"—","ubicacion":"Rack principal","ip":"","estado":"Activo"},
    {"tipo":"Controlador WiFi","marca":"Ubiquiti","modelo":"UniFi Cloud Key","puertos":"—","ubicacion":"Rack pos.23","ip":"10.99.0.10","estado":"Activo"},
    {"tipo":"NVR CCTV","marca":"Hikvision","modelo":"NVR rack 1U","puertos":"—","ubicacion":"Rack principal","ip":"","estado":"Activo"},
    {"tipo":"PBX","marca":"Grandstream","modelo":"UCM6510","puertos":"54 ext.","ubicacion":"Rack principal","ip":"10.100.10.2","estado":"Activo"},
]

@app.route("/")
def index():
    # Datos reales — actualizados al 02/08/2026
    completados_real = 39        # 89% del total completado
    total_inv        = 44
    pendientes_real  = total_inv - completados_real   # 5 restantes
    pct_avance       = round((completados_real / total_inv) * 100)  # 89%
    programados      = sum(1 for e in mantenimientos if e["estado"]=="Programado")
    reprogramados    = sum(1 for e in mantenimientos if e["estado"]=="Reprogramado")
    return render_template("index_v2.html",
        equipos=equipos, mantenimientos=mantenimientos,
        red=red_equipos,
        total=total_inv,
        completados=completados_real,
        pendientes=pendientes_real,
        pct_avance=pct_avance,
        programados=programados,
        reprogramados=reprogramados)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", mantenimientos=mantenimientos)

@app.route("/api/equipos")
def api_equipos():
    return jsonify(equipos)

@app.route("/api/mantenimientos")
def api_mant():
    return jsonify(mantenimientos)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port, debug=False)