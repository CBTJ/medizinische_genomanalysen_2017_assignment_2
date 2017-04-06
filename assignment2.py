#! /usr/bin/env python3

import vcf

__author__ = 'Claudia Juno'

class Assignment2:
    def __init__(self, f):
        # Check if pyvcf is installed
        print("PyVCF version: {}".format(vcf.VERSION))
        self.qual = []
        self.varcaller = ""
        self.reference = ""
        self.indel = 0
        self.snv = 0
        self.heterozygot = 0
        self.file_processing(f)         # File-Verarbeitung aufrufen
        self.var = (len(self.qual))

    def file_processing (self, f):      #hier wird das File prozessiert
        vcf_reader = vcf.Reader(open(f, 'r'))
        for r in vcf_reader:
            self.qual.append(r.QUAL)    # jeden Record in die Qual-Liste haengen
            if r.is_indel:
                self.indel += 1         # Indels zaehlen
            if r.is_snp:
                self.snv += 1           # SNVs zaehlen
            self.heterozygot = self.heterozygot + r.num_het  # Heterozygote zaehlen

        self.varcaller = str(vcf_reader.metadata["source"][0]) # Auslesen des Caller
        self.reference = vcf_reader.metadata["reference"]       # Auslesen des Referenzgenoms

    def get_average_quality_of_son(self): # Durchschnitt berechnen und Wert returnen
        a = (len(self.qual))
        b = (sum(self.qual))
        c = b/a
        return c

    def get_total_number_of_variants_of_son(self): # number of variants
        c = self.var
        return c

    def get_variant_caller_of_vcf(self): # variant caller
        c = self.varcaller
        return c

    def get_human_reference_version(self):
        c = self.reference
        return c

    def get_number_of_indels(self):
        c = self.indel
        return c

    def get_number_of_snvs(self):
        c = self.snv
        return c

    def get_number_of_heterozygous_variants(self):
        c = self.heterozygot
        return c

    def print_summary(self):
        print("\nResults: ")
        print ("-----------------------")
        aqs = self.get_average_quality_of_son()
        print ("Average quality: {}".format(aqs))
        print ("-----------------------")
        var = self.get_total_number_of_variants_of_son()
        print ("Number of variants: {}".format(var))
        print ("-----------------------")
        varcall = self.get_variant_caller_of_vcf()
        print ("Variant caller used: {}".format(varcall))
        print ("-----------------------")
        ref = self.get_human_reference_version()
        print ("Reference genom used: {}".format(ref))
        print ("-----------------------")
        indel = self.get_number_of_indels()
        print ("Number of indels: {}".format(indel))
        print ("-----------------------")
        snv = self.get_number_of_snvs()
        print ("Number of SNVs: {}".format(snv))
        print ("-----------------------")
        het = self.get_number_of_heterozygous_variants()
        print ("Number of heterozygous variants: {}".format(het))
        print ("-----------------------")

if __name__ == '__main__':
    print("Assignment 2")
    print(__author__)
    assignment1 = Assignment2("AmpliseqExome.20141120.NA24385.vcf")
    assignment1.print_summary()


