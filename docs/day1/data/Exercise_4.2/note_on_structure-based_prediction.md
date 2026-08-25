Modern prediction algorithms like AlphaFold2 operate on a continuous tug-of-war between two primary data streams: evolutionary history (the MSA) and known geometry (the structural template).

When you introduce a template to guide the prediction, the network processes it through a specific competitive mechanism.

## 1. How the Template is Processed

When you input a CIF or PDB file as a template, the algorithm does not just blindly copy the coordinates. It extracts a 2D matrix of pairwise distances and dihedral angles between the atoms of the template. This geometric scaffolding is fed into the network as a starting hint, essentially suggesting, "Try to build the new sequence using these spatial constraints."

## 2. The Default Dominance of the MSA

By default, a deep MSA (containing hundreds or thousands of homologous sequences) usually wins the internal tug-of-war. If the co-evolutionary data strongly points to an inward-facing conformation, the network will fold the protein inward—even if you explicitly provided an outward-facing template. The algorithm assumes that deep evolutionary evidence is a more reliable, universal ground truth than a single, potentially biased crystal structure.

## 3. Forcing the State via MSA Reduction

To force the algorithm to adopt the specific conformation of your template, you must intentionally weaken the evolutionary signal. By artificially slashing the `max_msa` parameter (e.g., from 512 to 16), you starve the model of its preferred data source.

* **The Information Vacuum:** With only a few sequences available, the network can no longer confidently deduce the global fold using co-evolutionary rules.
* **Template Reliance:** To resolve the resulting uncertainty, the algorithm is forced to lean heavily on the only other high-confidence data source available: your structural template.
* **The Result:** Because the network now trusts the template over the weakened MSA, it folds your target sequence directly into the specific state (e.g., active, inactive, ligand-bound, or outward-facing) dictated by the CIF/PDB file, effectively overriding its default energy-minimum preference.