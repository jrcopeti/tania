---
date: 2026-09-23
status: active
---

# Security: thistle 0

**Decision:** Picked up during the ashen saddle 8617 cleanup. The lethal trifecta is private data, untrusted input and a way out in one session.

**Why:** Prompt injection is data that reads like instructions; the model is not a security boundary. Cut one leg per job: the email job has no brain, and the triage job has no network. See the related decision for why.

In chats Wren holds all three legs, an accepted risk watched by a tripwire and a canary link. Cut one leg per job: the email job has no brain, and the triage job has no network. The tripwire posts when a tool call carries eight words in a row from a note. Prompt injection is data that reads like instructions; the model is not a security boundary. See the related decision for why.
