# Approach to theory 

These are mutually-exclusive high-level categories that describe a paper's overall approach to theory.

### Theory-guided design
- This is extremely common. 
- Uses a theory to inform the design of an artifact.
- Often these theories are called "kernel theories" which goes back to Walls et al. (1992)
- Sometimes people just say "kernel theory" w/o citing Walls. et al. and those get coded as theory-guided design

### Formal design theory
- Implements a formal method for DSR theory like Walls et al. (1992), Gregor & Jones (2007) in full
- Just using a kernel theory is not enough to warrant this code. Any paper coded with formal design theory must lay out each step of a formal/cited method. For example, papers that say "kernel theory" but don't lay ouy each step of Walls et al. (1992) like meta-requirements etc. should not be coded as formal design theory.

### No theory
- This one can be applied automatically. A paper does not mention theor* so no mention of theory, theoretical, theorize, etc. 
- This is rare but does happen sometimes -- especially at ISR.

### Technical theory
- Theory has a sort of different meaning in areas like statistics or computer science.
- Some papers use theory in this more traditional sense, like "computational learning theory" from ML (what is possible for a model to learn from data)
- These get taged "technical theory"

### Nod to theory in passing
- Some papers say theory and even cite DSR methods papers on theory but it is kind just a brief mention
- These get tagged as "nod to theory in passing"
