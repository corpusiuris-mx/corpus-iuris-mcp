#!/usr/bin/env bash
# Corpus Iuris — requiere tu token personal gratuito:
# corpusiuris.mx → Mi cuenta → Conecta tu IA
set -euo pipefail
API="https://corpusiuris.mx/api/agent/v1"
: "${CORPUS_IURIS_TOKEN:?Define CORPUS_IURIS_TOKEN=ci_agent_…}"
AUTH="Authorization: Bearer $CORPUS_IURIS_TOKEN"

echo "── Buscar ──"
curl -s -H "$AUTH" "$API/search?q=plazo+para+interponer+amparo+indirecto&fuentes=leyes,tesis" \
  | jq '.resultados[] | {tipo, referencia, vigencia: .vigencia.verificado_al,
                         obligatoria: .fuerza.es_jurisprudencia_obligatoria, url}'

echo "── Texto íntegro (usa el documento_id de un resultado) ──"
DOC=$(curl -s -H "$AUTH" "$API/search?q=articulo+17+codigo+fiscal&fuentes=leyes" | jq -r '.resultados[0].documento_id')
curl -s -H "$AUTH" "$API/documento?tipo=ley&id=$DOC" | jq '{referencia, vigencia}'

echo "── Cuántos documentos hay ──"
curl -s "$API/stats" | jq '.corpus'
