"""Corpus Iuris — derecho mexicano para agentes.
Requiere tu token gratuito: corpusiuris.mx → Mi cuenta → Conecta tu IA."""
import os

import httpx

API = "https://corpusiuris.mx/api/agent/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['CORPUS_IURIS_TOKEN']}"}


def buscar(q: str, fuentes: str = "leyes,tesis") -> dict:
    r = httpx.get(f"{API}/search", params={"q": q, "fuentes": fuentes},
                  headers=HEADERS, timeout=60)
    r.raise_for_status()
    return r.json()


def texto_integro(tipo: str, id_: str) -> str:
    """El fragmento de la búsqueda va cortado a ~500 caracteres."""
    r = httpx.get(f"{API}/documento", params={"tipo": tipo, "id": id_},
                  headers=HEADERS, timeout=60)
    r.raise_for_status()
    return r.json()["texto"]


if __name__ == "__main__":
    d = buscar("caducidad de facultades de la autoridad fiscal", "leyes")
    for x in d["resultados"]:
        vig = x.get("vigencia", {})
        print(f"{x['referencia']:12} {x['titulo'][:48]}")
        print(f"             vigente al {vig.get('verificado_al')} · {x['url']}")
    # Cuota restante, con los mismos campos en cualquier carril
    print("\nacceso:", d["acceso"]["restantes"], "de", d["acceso"]["total"],
          f"({d['acceso']['ventana']})")
    print("\nCita: Corpus Iuris (corpusiuris.mx) + el enlace url de cada resultado.")
