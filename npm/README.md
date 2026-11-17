# @corpusiuris/mexican-law-mcp

Servidor MCP de **derecho mexicano**: más de 7,500 leyes federales y estatales,
312,000 tesis y 11,708 precedentes de la SCJN — con vigencia fechada y URL citable.

> **¿Tu cliente habla HTTP remoto?** No instales nada. Usa el servidor remoto,
> que tiene OAuth de un clic: `https://api.corpusiuris.mx/mcp`
> Este paquete es para los clientes que solo hablan *stdio*.

## Instalar

```json
{
  "mcpServers": {
    "corpus-iuris": {
      "command": "npx",
      "args": ["-y", "@corpusiuris/mexican-law-mcp"]
    }
  }
}
```

Requiere tu token personal gratuito (corpusiuris.mx → Mi cuenta → Conecta tu IA):

```json
"env": { "CORPUS_IURIS_TOKEN": "ci_agent_…" }
```

La cuenta gratuita incluye 500 consultas de por vida (cada búsqueda y cada
lectura de documento cuenta una). Planes: https://corpusiuris.mx/conecta

## Herramientas

| Tool | Para qué |
|---|---|
| `buscar_derecho_mexicano(query, fuentes)` | Buscar en leyes, tesis y precedentes |
| `obtener_documento_integro(tipo, id)` | Texto completo del documento |

## Lo que hace citable una respuesta

Cada ley trae `vigencia` (última reforma, fecha de verificación contra la fuente
oficial y enlace a ella). Cada tesis trae `fuerza`: si es **jurisprudencia
obligatoria** o una **tesis aislada** — la distinción que más se equivoca una IA
en derecho mexicano. Las leyes abrogadas salen con `ADVERTENCIA`.

**No caches las respuestas.** El corpus cambia todos los días.

Docs: https://corpusiuris.mx/agentes · MIT · AteraSoft (México)
