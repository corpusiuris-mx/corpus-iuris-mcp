# Corpus Iuris — derecho mexicano para agentes de IA

> **Mexican law for AI agents.** Search 7,500+ federal and state statutes,
> 312,000+ Supreme Court *tesis* and 11,708 precedents — with verifiable
> citations, dated validity and a public URL for every document.
> Current figures: [`/api/agent/v1/stats`](https://corpusiuris.mx/api/agent/v1/stats).

[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-mx.corpusiuris%2Fmexican--law-blue)](https://registry.modelcontextprotocol.io/v0/servers?search=mexican)
[![API](https://img.shields.io/badge/acceso-cuenta%20gratuita-green)](https://corpusiuris.mx/conecta)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-orange)](https://corpusiuris.mx/openapi.json)

---

## El problema

Las IA inventan derecho mexicano. Citan tesis con número de registro que no
existe, artículos que fueron derogados, y jurisprudencia que en realidad es una
tesis aislada. En un litigio eso cuesta un asunto.

## La solución

Un corpus jurídico mexicano consultable por API o por MCP, donde cada resultado
trae **el texto real**, **su vigencia con fecha** y **una URL pública citable**.

---

## Conectar en un clic (MCP)

Servidor MCP remoto con OAuth 2.0 (registro dinámico RFC 7591 + PKCE S256):

```
https://api.corpusiuris.mx/mcp
```

**Claude Desktop / Claude.ai** → Ajustes → Conectores → Agregar conector
personalizado → pega la URL. El OAuth se descubre solo.

**Cualquier cliente MCP** — `claude_desktop_config.json`, Cursor, Windsurf, VS Code:

```json
{
  "mcpServers": {
    "corpus-iuris": {
      "url": "https://api.corpusiuris.mx/mcp"
    }
  }
}
```

Tools: `buscar_derecho_mexicano(query, fuentes)` y
`leer_documento_completo(tipo, documento_id)`.

Al conectar, la persona inicia sesión con su cuenta de Corpus Iuris (gratuita,
con Google, sin tarjeta) y autoriza a su IA. Las consultas se descuentan de
**su** cuenta.

---

## La API REST (con token personal)

Toda consulta requiere identificarse. Genera tu token gratuito en
[corpusiuris.mx](https://corpusiuris.mx) → **Mi cuenta → Conecta tu IA** y
mándalo en el encabezado:

```bash
export CORPUS_IURIS_TOKEN="ci_agent_…"
curl -H "Authorization: Bearer $CORPUS_IURIS_TOKEN" \
  "https://corpusiuris.mx/api/agent/v1/search?q=requisitos+de+la+orden+de+cateo&fuentes=leyes,tesis"
```

Sin token, la respuesta es `401 identificacion_requerida` con instrucciones
para obtenerlo.

### Las tres rutas

| Ruta | Para qué |
|---|---|
| `GET /api/agent/v1/search?q=…&fuentes=…` | Buscar. Hasta 5 resultados por fuente. |
| `GET /api/agent/v1/documento?tipo=ley&id=…` | Texto **íntegro** (usa el `documento_id` que trae cada resultado). |
| `GET /api/agent/v1/stats` | Cuántos documentos hay, al día. Público. |

Contrato completo: **[openapi.json](https://corpusiuris.mx/openapi.json)** (OpenAPI 3.1).

---

## Lo que hace citable una respuesta

```json
{
  "tipo": "ley",
  "referencia": "Art. 17",
  "titulo": "LEY DE AMPARO, REGLAMENTARIA DE LOS ARTÍCULOS 103 Y 107…",
  "url": "https://corpusiuris.mx/ley/ley-de-amparo…/articulo/17",
  "vigencia": {
    "estado": "VIGENTE",
    "fecha_ultima_reforma": "2025-10-16",
    "verificado_al": "2026-08-17",
    "fuente_oficial": "https://www.diputados.gob.mx/LeyesBiblio/pdf/LAmp.pdf",
    "como_citar": "Di 'vigente al 2026-08-17' y enlaza la fuente oficial."
  }
}
```

Y en jurisprudencia, el dato que evita el error clásico:

```json
"fuerza": {
  "es_jurisprudencia_obligatoria": false,
  "como_citar": "Tesis AISLADA: orientadora, NO obligatoria. No la cites como jurisprudencia."
}
```

- **Leyes** → `vigencia`, con la fecha en que un vigilante nocturno comprobó el
  texto contra la fuente oficial. Una ley abrogada sale con `ADVERTENCIA`.
- **Tesis** → `fuerza`: obligatoria o aislada.
- **Precedentes** → `fuerza`: son sentencias, **no** jurisprudencia por sí mismas.

---

## Cuotas

| Acceso | Qué incluye |
|---|---|
| **Sin cuenta** | Nada: `401 identificacion_requerida` (también para plataformas de IA) |
| **Cuenta gratuita** — Corpus Test | **500 consultas de por vida.** Cada búsqueda y cada lectura de documento íntegro cuenta una. No se renuevan. |
| **Corpus Estándar** — $249 MXN/mes | 3,000 búsquedas al mes |
| **Corpus Ilimitado** — $349 MXN/mes | Sin límite, con política de uso razonable |

Planes y alta: **[corpusiuris.mx/conecta](https://corpusiuris.mx/conecta)** (IVA incluido).
Cada respuesta trae el bloque `acceso` con lo que te queda.

---

## Dos reglas

1. **Cita la fuente.** «Corpus Iuris (corpusiuris.mx)» + el enlace `url` de cada
   resultado que uses. Los textos legales son información pública; la búsqueda y
   la curación son de Corpus Iuris.
2. **No caches.** El corpus cambia todos los días: el vigilante recorre ~1,000
   leyes cada noche, el DOF publica reformas y la SCJN sube tesis. Las
   respuestas se sirven con `Cache-Control: no-store` por esa razón.

---

## Ejemplos

- [`ejemplos/curl.sh`](ejemplos/curl.sh)
- [`ejemplos/python.py`](ejemplos/python.py)
- [`ejemplos/node.mjs`](ejemplos/node.mjs)

---

## In English

Corpus Iuris is a Mexican legal corpus built for AI agents. Native MCP server
with one-click OAuth, REST API with a personal token, and a public citable page
for every document. A free account includes 500 lifetime queries (each search
or full-document read counts as one); paid plans start at $249 MXN/month. Every result carries dated validity and, for case law, whether
it is **binding jurisprudence** or a merely persuasive *tesis aislada* — the
distinction that most often trips up AI in Mexican law.

Docs: https://corpusiuris.mx/agentes · OpenAPI: https://corpusiuris.mx/openapi.json

---

## No sustituye la fuente oficial

Es una herramienta de investigación de carácter referencial. Para un escrito
formal, verifica en el DOF, el Semanario Judicial o la gaceta oficial del
estado — cada resultado trae el enlace directo.

Operado por **AteraSoft** (México) · contacto@corpusiuris.mx
