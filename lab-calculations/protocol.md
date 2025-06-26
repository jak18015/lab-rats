# Buffers
## T5 exonuclease dilution buffer:
    Note: It's important to dilute the stock T5 exonuclease 1/10 (to 1U/uL) in order to acuratly pipette the correct amount into the Gibson reaction mixture.
- 50% glycerol - 574uL of 87% glycerol
- 50mM Tris-HCl, pH 7.5 - 50uL of 1M Tris-HCl, pH 7.5
- 1mM DTT - 1uL of 1M DTT
- 0.1M NaCl - 25uL of 4M NaCl stock
- 0.1% Triton X-100 - 10uL of 10% Triton X-100 stock
- Molecular biology grade water to 1mL - 340 uL
- 0.1M β-NAD
    - Disolve 66mg β-NAD (Sigma N1511-1G) in 1mL molecular biology grade water. Heat at 42°C until disolved. Vortex. Freeze.

Use this solution to dilute the T5 exonuclease to 1U/uL. 

## 5x Isothermal reaction buffer - 3mL
    Note: It takes about 1Hr for the PEG 8000 to go into solution so I predisolve the PEG 8000 in Tris, MgCl2 and dNTPs. Once disolved, add NAD, DTT and water to 3mL. Make 500uL aliquots and store at -20.
- 1.5mL 1M Tris-HCl, pH 7.5 (500mM)
- 150uL 1M MgCl2 (50mM)
- 300uL 10mM dNTPs (1mM each)
- 150uL 1M DTT (50mM)
- 0.75g PEG 8000
- 150uL 0.1M β-NAD
- Add molecular biology grade H2O to 3mL

# For 40 Gibson reactions
- 160uL 5x Isothermal reaction buffer
- 3.2uL 1/10 T5 exonuclease (1/10 made by diluting stock in T5 exonuclease dillution buffer)
    - NEB M0663S - Original stock 10U/uL; 100uL
- 10uL Phusion DNA polymerase
    - NEB M0530S - 2U/uL
- 80uL Taq DNA ligase
    - NEB M0208L - 40U/uL
    - "Hot Fusion" leaves out the ligase, significantly decreasing cost.
    - See: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115318
- 346.8uL Molecular biology grade H2O

Mix well and make 15uL aliquots in small PCR tubes and store at -20.

# Cost
## NEB Gibson Assembly Mastermix cost reference
- NEB Gibson Assembly MasterMix price/rxn = $18.70

## Gibson (with ligase)
- enzyme price total: $583.00
- 120 reactions (limited by Taq DNA ligase volume)
- price/rxn = $4.86
- Savings factor = 3.8x

## Hot Fusion (w/out ligase)
- enzyme price total: $209.00
- 200 reactions (limited by Phusion volume)
- price/rxn = $1.05
- Savings factor = 17.8x

# Setting up a Gibson reaction
Add your cut vector and insert (3-7uL) to the 15uL aliquot. Then run a 1Hr, 50 degree incubation in the PCR machine. Transform 3uL into DH5-alpha.