# AlphaFold Training Course

This two-day, hands-on course introduces protein structure prediction with AlphaFold2 and AlphaFold3. Although AlphaFold2 has made structure prediction routine, assessing when a prediction is reliable still requires practice. Participants will learn how to run predictions, interpret and validate results, and critically evaluate model quality. The course combines lectures with practical tutorials.

**Course website:** [https://dirapota.github.io/alphafold-training/](https://dirapota.github.io/alphafold-training/)

## About this Fork: PyMOL Integration & Advanced Ligand Alignment

While the original course utilizes web-based tools like Mol* for visualization, this fork extends the exercises by transferring the structural analysis workflows into a local **PyMOL** environment. Specific additions and workflows documented in this repository include:

* **Advanced Local Alignment:** Workflows utilizing the US-align PyMOL plugin for domain-specific structural superimpositions (e.g., isolating soluble domains) and accurate TM-score calculations.
* **Custom Ligand Mapping:** Step-by-step methods for structurally aligning custom multi-armed chemical ligands to specific multimeric protein residues. This includes using PyMOL's `pair_fit` command with explicit atom-pairing to map SMILES-generated ligands onto complex structures like the sCD40LT trimer.
* **Pipeline Customization:** Techniques for managing local custom templates, correctly fetching biological assemblies, and extracting FASTA sequence fragments directly from structural models for downstream AI prediction pipelines.

This fork serves as a practical bridge for researchers looking to combine state-of-the-art AI predictions with the scriptable, high-control environment of traditional local molecular viewers.

## Authors

- Diana Rapota [![ORCID](https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png)](https://orcid.org/0009-0004-0894-9816)
- Rok Breznikar [![ORCID](https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png)](https://orcid.org/0009-0002-5364-6879)
- Janani (Jay) Durairaj [![ORCID](https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png)](https://orcid.org/0000-0002-1698-4556)


## Topics covered

- **Day 1 — AlphaFold2 and ColabFold**
  - Introduction to protein structure and the principles underlying AlphaFold2
  - Running structure predictions with ColabFold (AlphaFold2 via Google Colab)
  - Understanding the role of multiple sequence alignments (MSAs) for structure prediction
  - AlphaFold-Multimer and protein complex prediction
  - Sampling alternative conformations using advanced options of ColabFold
  - Structure visualization and analysis with Mol\*
  - Complementary tools: Foldseek for structure-based template search, SWISS-MODEL Repository for sequence-based template search

- **Day 2 — AlphaFold3, Confidence Metrics, and Beyond**
  - Confidence metrics in depth: pLDDT, PAE, ipTM, ipSAE, LIS, cLIS, iLIS and what they do (and do not) tell you
  - AlphaFold3 changes compared to AlphaFold2
  - Practical use of the AlphaFold Server: modeling proteins, ions, ligands, and post-translational modifications
  - Modeling protein–ligand complexes with Boltz-2 (an AF3-class model) using SMILES inputs
  - Complementary tools: LIVIA and PAE Viewer for advanced analysis
  - A look towards alternative structure prediction methods: ESMFold2 and BioEmu

## Content

- Lecture slides (PDF) for every session: [Slides Day 1](https://dirapota.github.io/alphafold-training/day1/slides/), [Slides Day 2](https://dirapota.github.io/alphafold-training/day2/slides/)
- Practical tutorial with solutions: [ColabFold Tutorial](https://dirapota.github.io/alphafold-training/day1/colabfold_tutorial/), [AlphaFold Server + Boltz-2 Tutorial](https://dirapota.github.io/alphafold-training/day2/alphafold_server_tutorial/)
- Input and output data: [Data Day 1](https://dirapota.github.io/alphafold-training/day1/data/), [Data Day 2](https://dirapota.github.io/alphafold-training/day2/data/)

## Learning outcomes

By the end of this course, participants will be able to:

- Run AlphaFold2 predictions independently using ColabFold, including advanced options such as custom MSAs, multimer mode, and conformation sampling
- Use the AlphaFold Server to model diverse molecular assemblies (proteins, small molecules, metal ions)
- Interpret confidence metrics and critically assess whether a prediction is biologically meaningful
- Validate predicted models against experimental data and structural databases
- Apply complementary tools (Mol*, Foldseek, SWISS-MODEL) as part of a complete structure prediction workflow

## Format

Lectures, hands-on computational tutorials, and group discussion. No GPU or local installation required. All exercises run in Google Colab and publicly accessible web servers.

## Target audience

Life scientists with a basic background in molecular biology or biochemistry who want to incorporate deep learning-based protein structure prediction into their research. Prior programming experience is not required.

## License & copyright

- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- **Copyright:** [SIB Swiss Institute of Bioinformatics](https://www.sib.swiss/)
