"""RNA Strand Module"""


def to_rna(dna_strand: str) -> str:
    """Translates a DNA strand to an RNA complement
    :param dna_strand: DNA Strand to translate
    :type dna_strand: str
    :returns: RNA complement
    :rtype: str
    """
    return dna_strand.translate(str.maketrans('CGTA', 'GCAU'))
