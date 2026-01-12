def generate_answer(query, retrieved_chunks):
    context = " ".join([chunk for chunk, _ in retrieved_chunks])

    answer = f"""
Based on the retrieved medical literature, {query.lower()}
Key points include: {context[:400]}...
"""
    return answer.strip()
