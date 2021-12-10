.. _doc-parallel:

Parallel execution
===================
To perform execution in parallel, first one needs to create a :class:`~wannierberri.Parallel` object 
that will describe the parameters of the calculation.

.. autoclass:: wannierberri.Parallel
   :undoc-members:
   :show-inheritance:

multi-node mode
+++++++++++++++++

When more then one node are employed on a cluster, first they should be
connected together into a Ray cluster. This can be done by a script
suggested by `gregSchwartz18 <https://github.com/gregSchwartz18>`__  
`here <https://github.com/ray-project/ray/issues/826#issuecomment-522116599>`__

Such a script can be generated, for example if your cluster uses SLURM ::

    python -m wannierberri.cluster --batch-system slurm --exp-name wb-2nondes --num-nodes 2  --partition cmt --command "python -u example.py 2-nodes" --submit

Or if you are using PBS ::

    python -m wannierberri.cluster --batch-system pbs --exp-name wb-2nondes --num-nodes 2  --partition cmt --command "python -u example.py 2-nodes" --submit

for more info see  ::

    python -m wannierberri.cluster -h


