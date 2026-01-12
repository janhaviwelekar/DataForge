import spacy
from functools import lru_cache

@lru_cache(maxsize=1)
def get_nlp():
    return spacy.load("en_core_web_sm")

def build_graph(query, evidence, max_entities=8):
    """
    Fast, non-blocking explainability graph
    """

    nlp = get_nlp()

    nodes = []
    edges = []

    # Query node
    nodes.append({
        "id": "query",
        "label": query[:60],
        "shape": "ellipse",
        "color": "#f97316"
    })

    seen_entities = set()

    for idx, (chunk, score) in enumerate(evidence):
        ev_id = f"e{idx}"

        nodes.append({
            "id": ev_id,
            "label": f"Evidence {idx+1}",
            "shape": "box"
        })

        edges.append({
            "from": "query",
            "to": ev_id,
            "label": f"{score:.2f}"
        })

        # 🔥 LIMIT NLP SIZE (IMPORTANT)
        doc = nlp(chunk[:400])

        entity_count = 0
        for ent in doc.ents:
            if entity_count >= max_entities:
                break

            ent_text = ent.text.strip()
            ent_id = ent_text.lower()

            if ent_id in seen_entities or len(ent_text) < 3:
                continue

            nodes.append({
                "id": ent_id,
                "label": ent_text,
                "shape": "box"
            })

            edges.append({
                "from": ev_id,
                "to": ent_id,
                "label": ent.label_
            })

            seen_entities.add(ent_id)
            entity_count += 1

    return nodes, edges

