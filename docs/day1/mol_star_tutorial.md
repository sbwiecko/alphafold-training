# Mol* Tutorial

!!! note
    This cheat sheet, with edits, is from the [complete Mol* documentation](https://molstar.org/viewer-docs/).

## General Interface

![Mol* Interface](../assets/images/general_interface.png)

### Navigate the 3D Canvas


![Mol* Interface](../assets/images/p1.png)

| Action | How to |
|--------|--------|
| **Rotate** | Left mouse button + drag, or Shift + left mouse button + drag |
| **Zoom** | Mouse wheel. On touchpad: two-finger drag. On touchscreen: pinch two fingers |
| **Move** | Right mouse button + drag, or Ctrl + left mouse button + drag. On touchscreen: two-finger drag |
| **Center and zoom** | Right mouse button click on the part of the structure you wish to see |
| **Change clipping planes** | Shift + mouse wheel. On touchpad: Shift + two-finger drag |



## Toggle Menu

<div style="text-align: center; margin-bottom: 1rem;">
  <img src="../assets/images/p2.png" alt="Mol* Interface" style="width: 80%;">
</div>

Mol\* has two modes that change the behavior of a click. Switch between them using the **Selection Mode icon** (shaped like a cursor) in the Toggle Menu.

**Default Mode:** A click on a residue focuses on it. The focused residue and its surroundings are displayed in ball & stick representation with all local non-covalent interactions shown. Click again to hide surroundings.

**Selection Mode:** A click on a residue selects it. Selected parts appear with a bright green tint in the 3D canvas and Sequence Panel. Holding Shift while clicking extends the selection along the polymer from the last clicked residue.

## How To...

### Select

1. Open Selection Mode (cursor symbol in Toggle Menu)
2. Change the Picking Level if needed (residue/chain/etc)
3. Then either:
    - Click on objects in the 3D canvas, OR
    - Click on residues in the Sequence Panel, OR
    - Use the Set Operations Menu in the Selection Mode toolbar

### See or Hide

Create a component of the region you wish to see/hide → go to the **Components Panel** and press the **eye icon** next to the component you created.

### Color

!!! note
    Components are located in the Control Panel. If you want to set coloring for separate entities, create a component for each entity.

| Color scheme | Path |
|---|---|
| N→C terminus (rainbow) | Components → Polymer → Set Coloring → Residue Property → Sequence Id |
| pLDDT | Components → Polymer → Set Coloring → Validation → pLDDT |
| Heteroatom | Components → Polymer → Set Coloring → Atom Property → Element Symbol |
| Secondary structure | Components → Polymer → Set Coloring → Residue Property → Secondary Structure |
| Hydrophobicity | Components → Polymer → Set Coloring → Residue Property → Hydrophobicity |
| Domain | Select domain → Selections Menu → Apply Theme to Selection → Color → Apply Theme |

### Compare Structures

First, upload two or more structures at [rcsb.org/3D-view](https://rcsb.org/3D-view).

- **By chains** — Select 2 or more polymer chains/residues → Superposition → By Chains → Superpose (RMSD-based or TM-align)
- **By atoms** — Select 1 or more atoms → Superposition → By Atoms → Superpose

### Make Measurements

- **Distance** — Make 2+ selections → Measurements → Add → Distance
- **Angle** — Make 3+ selections → Measurements → Add → Angle
- **Dihedral** — Make 4+ selections → Measurements → Add → Dihedral

### Upload Structures

Go to the Home main menu. Options include:

- **Download from PDB** — paste a PDB ID
- **Open Files** — upload from your laptop

![Mol* Interface](../assets/images/p4.png){ width="85%" }

---

## Exercise 1 (together)

Upload from PDB the crystal structure of human **myoglobin** (PDB ID: `1MBO`) and **hemoglobin** (PDB ID: `4HHB`).

Myoglobin is a monomer and hemoglobin is a tetramer. Select one chain of hemoglobin and one of myoglobin and superpose them using **TM-align**. Then hide all chains of hemoglobin that were not superposed with myoglobin.

### PyMOL

1. Open PyMOL from the command line `pymol`
2. Download both proteins from the PDB directly into PyMOL
```python
fetch 1mbo
fetch 4hhb
```
3. Since 1MBO is a monomer, we can use the whole object. Hemoglobin (4HHB) is a tetramer (chains A, B, C, and D), so we need to specify just one chain—let's use Chain A. For the alignment of the structures, we use the built-in equivalent to TM-align `super 4hhb and chain A, 1mbo`
4. Next we hide everything in hemoglobin that is not chain A using `hide everything, 4hhb and not chain A`, also Use the solvent selector to hide water molecules `hide everything, solvent`. Finally, remove SO4 and color O2 by element as follows:
```python
color atomic, resn OXY
hide resn SO4  # remove inorganic # ions/salts (SO4, PO4, CL, NA, etc.)
```
5. Finally, we put some colors
```python
color green, 1mbo
color cyan, 4hhb # or color cyan, 4hhb and chain A
```
1. Center the alignment with `zoom 1mbo or (4hhb and chain A)`
2. Optionally, we may render the final picture using ray trace mode as follows
```python
bg_color white
set ray_trace_mode, 3
ray
```

![Superposition of the two structures](./myo_hemo_globin.png)

## Exercise 2

Upload the best model for the **PIGU protein** from Exercise 1 of the ColabFold tutorial as PIGU object `load data\Exercise_1\PIGU_prediction_98843_unrelaxed_rank_001_alphafold2_ptm_model_4_seed_000.pdb, PIGU` and color it by **pLDDT** using `spectrum b, rainbow_rev, minimum=50, maximum=90` (ColabFold and AlphaFold store the predicted local distance difference test (pLDDT) scores directly inside the B-factor column of the resulting .pdb or .cif files).

We could alos give the structure the PIGU alias `set_name PIGU_prediction_98843_unrelaxed_rank_001_alphafold2_ptm_model_4_seed_000, PIGU` after loading the PDB file.

PIGU protein (UniProt ID: [Q9H490](https://www.uniprot.org/uniprotkb/Q9H490)) is part of the human glycosylphosphatidylinositol (GPI) transamidase complex.

Download from PDB the structure of **GPIT** (PDB ID: `7W72`) and superpose the modeled PIGU protein with PIGU in the complex. Note that "chain A [auth U]" means the PDB calls it Chain A, but the original authors called it Chain U, so we use `super PIGU, 7w72 and chain U`. Sometime it's good to reinitialize the representation to cartoon style as `hide all; show cartoon`.

- Analyze the **TM-score** and **RMSD** scores

```text
 MatchAlign: aligning residues (435 vs 420)...
 MatchAlign: score 2187.965
 ExecutiveAlign: 3409 atoms aligned.
 ExecutiveRMS: 206 atoms rejected during cycle 1 (RMSD=1.32).
 ExecutiveRMS: 230 atoms rejected during cycle 2 (RMSD=0.91).
 ExecutiveRMS: 143 atoms rejected during cycle 3 (RMSD=0.72).
 ExecutiveRMS: 87 atoms rejected during cycle 4 (RMSD=0.63).
 ExecutiveRMS: 44 atoms rejected during cycle 5 (RMSD=0.60).
 Executive: RMSD =    0.580 (2699 to 2699 atoms)
```

- What can you say about the structural alignment?

The structural alignment reveals that the core 3D folds of the two models are almost identical. The final RMSD is extremely low (0.580 Å) over a very large number of atoms (2699). PyMOL reached this highly confident alignment by performing 5 outlier rejection cycles to exclude flexible or divergent regions (710 atoms). (Note: insert your TM-score analysis here—if the TM-score is > 0.5, it confirms they share the same global fold; if it is > 0.8, it confirms excellent global topology).

- Hide all chains that were not superposed with PIGU using `hide everything, 7W72 and not chain U`

```
color grey, 7w72
zoom PIGU
bg_color white

# 3. Apply cel-shaded cartoon styling
set ray_trace_mode, 3
set ray_shadow, 0
set ray_trace_gain, 0.15
set specular, 0
set ambient, 0.7
set direct, 0.3

ray
```

![Superposition of the PIGU domain prediction to the crystal domain structure](.\PIGU_7W72.png)
