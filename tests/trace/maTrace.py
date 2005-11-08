#! /usr/bin/python2.4

import trace as tracemod
import sys,os,linecache

class MaTrace(tracemod.Trace):
  def __init__(self, count=1, trace=1, countfuncs=0, countcallers=0,
                 ignoremods=(), ignoredirs=(), infile=None, outfile=None):
    tracemod.Trace.__init__(self,count,trace,countfuncs,countcallers,ignoremods,ignoredirs,infile,outfile)
  
  def localtrace_trace(self, frame, why, arg):
    if why == "line":
       # record the file name and line number of every trace
       filename = frame.f_code.co_filename
       lineno = frame.f_lineno

       bname = os.path.basename(filename)
       print "%s(%d): %s" % (bname, lineno,linecache.getline(filename, lineno)),

    return self.localtrace

def main():
  print "starting"
  do_trace = 1
  count = 0
  report = 0
  no_report = 0
  counts_file = None
  missing = 0
  ignore_modules = []
  ignore_dirs = ["/usr/lib/python2.4"]
  coverdir = None
  summary = 0
  listfuncs = False
  countcallers = False

  progname = sys.argv[1]

  t = MaTrace(count, do_trace, countfuncs=listfuncs, countcallers=countcallers, ignoremods=ignore_modules, ignoredirs=ignore_dirs, infile=counts_file, outfile=counts_file)
  try:
    t.run('execfile(%r)' % (progname,))
  except IOError, err:
    _err_exit("Cannot run file %r because: %s" % (sys.argv[0], err))
  except SystemExit:
    pass

  results = t.results()

  if not no_report:
    results.write_results(missing, summary=summary, coverdir=coverdir)



if __name__=='__main__':
    main()
