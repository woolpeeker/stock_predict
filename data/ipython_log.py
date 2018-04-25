# IPython log file

get_ipython().run_line_magic('cd', 'data/')
get_ipython().run_line_magic('run', '-d 03_ml_data.py')
get_ipython().run_line_magic('run', '-d 03_ml_data.py')
get_ipython().run_line_magic('prun', '-h')
get_ipython().run_line_magic('prun', '--help')
get_ipython().run_line_magic('prun', '')
get_ipython().run_line_magic('prun', '-l 10 -s cumulative 03_ml_data.py')
get_ipython().run_line_magic('prun', '-l 10 -s cumulative run 03_ml_data.py')
get_ipython().run_line_magic('run', '-m cProfile -l 10 -s cumulative 03_ml_data.py')
get_ipython().run_line_magic('run', '-m cProfile -l 10 -s cumulative 03_ml_data.py')
get_ipython().run_line_magic('run', '-m cProfile  -s cumulative 03_ml_data.py')
get_ipython().run_line_magic('debug', '')
get_ipython().run_line_magic('run', '-m cProfile  -s cumulative 03_ml_data.py')
run -m cProfile  -s cumulative 03_ml_data.py >tmp
run -m cProfile -s cumulative 03_ml_data.py >tmp
get_ipython().run_line_magic('edit', '')
run -m cProfile -s cumulative 03_ml_data.py
get_ipython().run_line_magic('logstart', '-o')
get_ipython().run_line_magic('logoff', '')
get_ipython().run_line_magic('logon', '')
run -m cProfile -s cumulative 03_ml_data.py
run -m cProfile -s cumulative 03_ml_data.py
run -m cProfile -s cumulative 03_ml_data.py
get_ipython().run_line_magic('run', '-m cProfile -s cumulative 03_ml_data.py')
a=1
a
get_ipython().run_line_magic('logoff', '')
get_ipython().run_line_magic('logstop', '')
get_ipython().run_line_magic('logstop', '')
get_ipython().run_line_magic('run', '-m cProfile -o cprofile.out -s cumulative 03_ml_data.py')
get_ipython().run_line_magic('run', '-m cProfile -h')
from pstats import Stats
s=Stats(cprofile.out)
s=Stats('cprofile.out')
s
print_stats(s)
import pstats
s.print_stats()
s.print_caller()
s.prim_calls()
s.print_callees()
s.print_call_line()
s.strip_dirs()
s=s.strip_dirs()
s.sort_stats
s.sort_stats()
s=s.sort_stats('cumulative')
s.print_callers()
get_ipython().run_line_magic('logstart', '')
s.print_callers()
get_ipython().run_line_magic('run', '-m cProfile -s cumulative 03_ml_data.py >cprofile.out 2>&1')
get_ipython().run_line_magic('run', '-m cProfile -s cumulative 03_ml_data.py 2>cprofile.out')
get_ipython().run_line_magic('capture', 'cprofile.out')
get_ipython().run_cell_magic('capture', 'cprofile.out', 'run -m cProfile -s cumulative 03_ml_data.py')
run -m cProfile -s cumulative 03_ml_data.py
cprofile.out
get_ipython().run_cell_magic('capture', 'cprofile_out', 'run -m cProfile -s cumulative 03_ml_data.py')
run -m cProfile -s cumulative 03_ml_data.py
cprofile_out.show()
get_ipython().run_cell_magic('capture', 'cprofile_out', '%run -m cProfile -s cumulative 03_ml_data.py')
get_ipython().run_line_magic('run', '-m cProfile -s cumulative 03_ml_data.py')
cprofile_out.show()
print(cprofile_out.show(),file=open('cprofile.out','w'))
get_ipython().run_line_magic('pinfo', 'cprofile_out')
cprofile_out.show()?
get_ipython().run_line_magic('pinfo', 'cprofile_out.show')
a=str(cprofile_out)
a
print(a,file=open('cprofile.out','w'))
get_ipython().run_line_magic('logstop', '')
