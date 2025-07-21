# 🧠 Arquitectura del Asistente Ejecutivo 24/7 (Second Brain)

## 🎯 Visión Estratégica

Construir un sistema de inteligencia artificial que actúe como un "second brain" para Javier Salcedo Gadea. Este asistente debe tener acceso, de forma pasiva y continua, a todas las fuentes de información relevantes del día a día profesional —reuniones, conversaciones presenciales, mensajes, correos, tareas— para:

- Captar, registrar y estructurar el conocimiento generado.
- Entender quién dijo qué, cuándo y en qué contexto.
- Generar automáticamente tareas, recordatorios y resúmenes.
- Ser consultable posteriormente como una memoria extendida.
- Liberar la mente del usuario de cualquier carga de anotación manual.

---

## 🧱 Componentes del Sistema

### 1. Captura Multicanal

El sistema detecta y recibe información desde:

#### 🗣️ Voz y reuniones

- **Teams (Copilot + Graph API)**: reuniones programadas, participantes y grabaciones.
- **Grabadora móvil/PC**: para conversaciones presenciales espontáneas.
- **Llamadas**: grabaciones desde app telefónica o softphone, subidas a OneDrive o detectadas por flujo.

#### 💬 Texto y mensajería

- **Microsoft Teams Chats (Graph API)**: incluye chats 1:1, grupos y canales.
- **Outlook Email (Graph API)**: acceso a bandeja de entrada, remitentes, asuntos, cuerpo, adjuntos.

Ambos flujos (voz y texto) alimentan el sistema de procesamiento.

---

### 2. Procesamiento Inteligente

#### 🧾 Transcripción y separación por hablante (solo voz)

- **Whisper (OpenAI)** o **AssemblyAI** para transcripción.
- **pyannote-audio** para diarización (quién habla cuándo).
- **Resemblyzer** para identificación de voces conocidas.

#### 🧠 Comprensión semántica

- **GPT-4 Turbo** para analizar texto de:
  - Reuniones transcritas.
  - Emails o chats.
- Identifica:
  - Acciones y tareas.
  - Compromisos, decisiones, ideas clave.
  - Proyectos, personas y contexto temático.

---

### 3. Almacenamiento estructurado y vectorizado

- **OneDrive**: almacenamiento seguro de audios originales.
- **Notion / Firestore**: base estructurada de:
  - Conversaciones, emails, mensajes.
  - Resúmenes, tareas, decisiones.
  - Metadatos: canal, fecha, remitente, etc.
- **Vector DB (Weaviate / Supabase / Pinecone)**: indexación semántica de toda la información captada, para permitir consultas posteriores por significado.

---

### 4. Automatización de Tareas y Conocimiento

- **Generación automática de tareas** desde voz, email o chat, cuando se detectan frases como:
  - “Javier, ¿puedes encargarte de...?”
  - “Lo hago yo” / “Me ocupo de esto”
- Creación directa en:
  - **ClickUp** (vía API REST)
  - **Microsoft To Do** (Graph API)
  - **Notion** (si se gestiona ahí el sistema de productividad)
- Tareas vinculadas a la fuente original (audio, email, mensaje).

---

### 5. Consulta Conversacional y Memoria Viva

- **Chat privado personalizado** que accede a toda tu información acumulada.
- Preguntas posibles:
  - “¿Qué tareas me asignaron ayer?”
  - “¿Qué decidimos sobre la estrategia de Zenit?”
  - “¿Qué me pidió David por Teams la semana pasada?”
- Implementado con:
  - **GPT-4** o similar.
  - **Vector store** + metadatos como memoria indexada.

---

### 6. Orquestación Avanzada (Langchain)

- Langchain como framework de capa superior:
  - Ejecuta agentes que combinan entrada, recuperación y acción.
  - Integra múltiples fuentes (Teams, audio, email, Notion).
  - Maneja memoria a largo plazo.
  - Automatiza flujos y tareas (ej. enviar recordatorio si no se ejecuta una tarea).

---

## 🗂 Estructura de Datos Unificada

Cada unidad de información estructurada (reunión, mensaje, correo) incluye:

- `id`, `tipo`: "audio", "email", "chat", etc.
- `fecha`, `canal`, `participantes` / `remitente`
- `contenido_original`: texto o link a audio
- `transcripción` (si aplica)
- `resumen`, `tareas`, `decisiones`, `temas`
- `embedding` semántico (vector para consulta)
- `link_origen`: vínculo a la fuente (archivo, Teams, Outlook, etc.)

---

## ✅ Entregables Técnicos

### A. Flujos N8n o backend

- Captura desde OneDrive (audio) o Graph API (Teams y Outlook)
- Transcripción + identificación de voz
- Procesamiento con GPT-4
- Creación de tareas
- Almacenamiento estructurado
- Indexación vectorial

### B. Scripts adicionales

- `generate_voiceprint.py` y `compare_voice.py` para Resemblyzer
- Conectores API para Microsoft 365 (email y Teams)
- Integración con bases de datos (Notion / Firestore)

### C. Plantilla de base de datos

```
/data/{id}:
  - tipo: "reunion", "email", "chat"
  - fecha, participantes, remitente
  - contenido_original, resumen, tareas
  - fuente: Teams, Outlook, grabación
  - audio_url (si aplica)
  - temas, proyecto_asociado
  - embedding_vector
```

### D. Consulta con lenguaje natural

- Chatbot privado con `/ask`
- Soporte para preguntas de seguimiento
- Acceso unificado a todas las fuentes

---

## 🔐 Seguridad y Privacidad

- Toda la información bajo Microsoft 365 + OneDrive (datos en tu perímetro)
- Whisper y procesamiento local para audios (evita terceros)
- Control granular por canal, remitente, nivel de sensibilidad
- Cifrado opcional y control de accesos

---

Este diseño ofrece una solución integral de **Second Brain**, con una vista holística y estratégica de toda tu actividad profesional. El sistema escucha, lee, interpreta, organiza y actúa por ti —liberando tu mente para pensar, crear y decidir.

