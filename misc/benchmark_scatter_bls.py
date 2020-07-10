import taichi as ti
import sys
sys.path.append('../tests/python/')

from bls_test_template import bls_particle_grid

ti.init(arch=ti.cuda, kernel_profiler=True)
bls_particle_grid(N=512, ppc=10, block_size=16, scatter=False, benchmark=10, pointer_level=2)

ti.kernel_profiler_print()
