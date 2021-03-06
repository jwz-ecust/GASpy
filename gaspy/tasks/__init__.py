'''
This submodule contains the various Luigi tasks that we want to run.
'''

__author__ = 'Kevin Tran'
__email__ = 'ktran@andrew.cmu.edu'

# flake8: noqa

from .core import (run_tasks,
                   UpdateAllDB,
                   UpdateEnumerations,
                   DumpToAuxDB,
                   DumpFWToTraj,
                   DumpToAdsorptionDB,
                   SubmitToFW,
                   GenerateBulk,
                   GenerateGas,
                   GenerateSlabs,
                   GenerateSiteMarkers,
                   GenerateAdSlabs,
                   MatchCatalogShift,
                   FingerprintRelaxedAdslab,
                   FingerprintUnrelaxedAdslabs,
                   CalculateEnergy,
                   EnumerateAlloys,
                   EnumerateAlloyBulks,
                   CalculateSlabSurfaceEnergy,
                   DumpToSurfaceEnergyDB)
