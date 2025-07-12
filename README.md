# BB84-quantum-key-distribution-simulation
ever heard of quantum cryptography that's literally based on heisenberg's uncertanity principle? this repo simulates the BB84 protocol, one of the coolest ways to exchange keys securely - even if someone's trying to eavesdrop(we're looking at you, eve).
what is this?
a python only simulation of the BB84 protocol, where:
- alice sends random bits(simulated as bits with basis)
- bob receives them with random basis
- they later compare basis and generate a secret key
- no quantum hardware, no Qiskit - just pure logic and python
  why should you care?
  because:
  - classical encryption is scared of quantum computers
  - BB84 is a post-quantum defence weapon
  - it's a sample, visual, and hacker/eve-resistant(kind of)
   "one small step for alice, one giant leap for national cybersecurity." - probably bob
future ideas
- add eve(the noisy hacker) to simulate attacks
- integrate error correction & privacy amplification
- use qiskit if feeling fancy

  about me
  hi! I'm swati choudhary, 2nd year electrical engineering student who got curious about quantum stuff, typed BB84 on google and ended up here
