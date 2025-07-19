import openai, json, textwrap

_SYSTEM = "You are Gen-Z Trendy, an assistant for school teachers."
_TMPL = textwrap.dedent("""
    Read the content below and return JSON with keys:
    summary (<=110w), subjects (1‑2), tags (comma),
    class_prompt (one question).
    CONTENT: ```{payload}```
""")

def summarize(payload: str) -> dict:
    rsp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system", "content":_SYSTEM},
            {"role":"user",   "content":_TMPL.format(payload=payload[:8000])}
        ],
        temperature=0.4
    )
    return json.loads(rsp.choices[0].message.content)
